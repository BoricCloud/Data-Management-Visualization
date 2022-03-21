import sys
sys.path.insert(0,'../Spotify Project/Setup')

import warnings
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from Setup import Settings
from Setup import Variables
from Setup.functions import divide
from tqdm import tqdm
warnings.filterwarnings("ignore")

artists_list = Variables.artists_list
collection = Variables.db[Settings.related_collection_name]
check_duplicates = Variables.check_duplicates
url_related = [i+'/related' for i in check_duplicates]
checkpoint = collection.estimated_document_count()

if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente agli artisti correlati è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per continuare.')
    answer = input('')
    if answer == 'delete':
        definitive = input('Sei sicuro? <y> <n>. ')
        if definitive =='y':
            collection.drop()
            checkpoint=0
        else:
            print('collezione non eliminata.')
    else:
        print("Lo scraper ripartirà dall'ultimo artista.")
else:
    divide()
    print('La collezione non è presente nel database.')

tracker = checkpoint + 1
for url in tqdm(url_related[checkpoint:]):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    test = soup.find_all('div')
    try:
        prova = [element for element in test if 'Related Artists' in element.text][1]
        new = str(prova).split('dir="auto">')
        a = [step.split('</span></div>') for step in new]
        b = [g[0] for g in a]
        related = b[-4:]
        collection.insert_one({'_id':tracker-1, 'Artist':artists_list[tracker-1],'Related':related}) 
    except:
        print(artists_list[tracker-1]+' at index '+ str(tracker-1)+' Not Found!')

    tracker += 1
print('Collezione popolata con successo.')
