import sys
sys.path.insert(0,'../Spotify Projec/Setup')

import warnings
import wikipedia
import editdistance
from Setup import Settings
from Setup import Variables
from Setup.functions import Respo2, ArtistOrGroup, divide
from tqdm import tqdm
warnings.filterwarnings("ignore")

wikipedia.set_lang('it')
artists_list = Variables.artists_list
collection = Variables.db[Settings.natio_collection_name]
checkpoint = collection.estimated_document_count() 

if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente alla nazionalità degli artisti è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per continuare.')
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
    print('La collezione inerente alle nazionalità degli artisti non è presente nel database.')
   

tracker = checkpoint + 1
for artist in tqdm(artists_list[checkpoint:]):
    try:    
        bridge = [wikipedia.page(element).categories for element in wikipedia.search(artist)[:2]]
    except:
        try:
            bridge = [wikipedia.page(element).categories for element in wikipedia.search(artist)[:5]]
        except:
            print('Ambiguous Error! ',artist)
            collection.insert_one({'_id': tracker, 'Artist':artist})
            continue
    alpha = ArtistOrGroup(bridge)
    if alpha[0]==True:
        try:
            wiki_page = wikipedia.page(wikipedia.search(artist)[alpha[1]])
            wiki_url = wiki_page.url
            popped = wiki_page.title.split('/').pop()
            for_edit = wiki_page.title.replace('(','').replace(')','')
            if editdistance.eval(artist.lower(), popped[:len(artist)].lower()) > 3:
                collection.insert_one({'_id': tracker, 'Artist':artist})
            else:
                result=Respo2(wiki_url)
                if '(' in result:
                    result = result.split('(')[0]
                elif '\xa0' in result:
                    result = result.split('\xa0')
                else:
                    pass
                collection.insert_one({'_id':tracker,'Artist':artist,'nationality':result})
        except:
            collection.insert_one({'_id': tracker, 'Artist':artist})
            print(artist,' not found!')
    else:
        collection.insert_one({'_id': tracker, 'Artist':artist})
    tracker += 1