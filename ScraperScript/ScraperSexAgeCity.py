import sys
sys.path.insert(0,'../Spotify Projec/Setup')

import wikipedia
import editdistance
from Setup import Settings
from Setup import Variables
from Setup.functions import GetSex, ArtistOrGroup2, divide
from tqdm import tqdm
import re
import warnings
warnings.filterwarnings("ignore")

wikipedia.set_lang('it')
artists_list = Variables.artists_list
collection = Variables.db[Settings.SexAgeCity_collection_name]
checkpoint = collection.estimated_document_count() 

if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente all Sesso, Citta di provenienza e Età degli artisti è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per continuare.')
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
for artist in tqdm(artists_list[checkpoint:]):
    try:    
        bridge = [wikipedia.page(element).categories for element in wikipedia.search(artist)[:2]]
    except:
        print('Ambiguous Error! ',artist)
    alpha = ArtistOrGroup2(bridge)
    if alpha[0]==True:
        try:
            a = wikipedia.page(wikipedia.search(artist)[alpha[1]])
            for_edit = a.title.replace('(','').replace(')','')
            if editdistance.eval(artist, for_edit) > 9:
                collection.insert_one({'_id': tracker+1, 'Artist':artist})
                continue
            s = a.summary
            m = re.findall('\(.*?\)',s)       
            for element in m:
                if ',' in element:
                    city = element.split(',')[0].replace('(','')
                    break
            try:
                age = 2020 - int(element.split(',')[1].replace(')','').split()[2])
            except:
                age= ''
            if ';' in city:
                city=city.split(';')[1].strip()
            sex = GetSex(s)
            if sex[1]==False:
                collection.insert_one({'_id':tracker+1, 'Artist': artist, 'città': city, 'age': age, 'sex': sex[0]})
            else:
                collection.insert_one({'_id':tracker+1, 'Artist': artist, 'città': city, 'age': 0, 'sex': sex[0]})
        except:
            print('Except')
            collection.insert_one({'_id': tracker+1, 'Artist':artist})
    elif alpha[2]==True:
            collection.insert_one({'_id': tracker+1, 'Artist':artist,'sex':'Group'})
    else:
        collection.insert_one({'_id': tracker+1, 'Artist':artist})
    tracker += 1