import sys
sys.path.insert(0,'../Spotify Projec/Setup')

from Setup import Settings
from Setup import Variables
from Setup.functions import divide
from tqdm import tqdm
import wikipedia
from langdetect import detect
import bson
import time

sp = Settings.sp
collection = Variables.db[Settings.main_collection_name]
checkpoint = Variables.checkpoint 
artists_list = Variables.artists_list
albums_list = Variables.albums_list
albums_per_artist = dict(zip(artists_list[checkpoint:], albums_list[checkpoint:]))

Settings.genius.verbose = False
Settings.genius.remove_section_headers = True
Settings.genius.skip_non_songs = False

tracker = checkpoint + 1

if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente alle lyrics è già presente nel database, sono presenti {} artisti.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per continuare.'.format(collection.estimated_document_count()))
    answer = input('')
    if answer == 'delete':
        definitive = input('Sei sicuro? <y><n>. ')
        if definitive =='y':
            collection.drop()
            checkpoint = 0
            tracker = 1
        else:
            print('collezione non eliminata.')
    else:
        print("Lo scraper ripartirà dall'ultimo artista.")
else:
    divide()
    print('La collezione inerente alle lyrics non è presente nel database.')
   
albums_per_artist = dict(zip(artists_list[checkpoint:], albums_list[checkpoint:]))
for artist in tqdm(artists_list[checkpoint:]): 

    print('\nStarting '+artist  )
    stopper=False
    insert=[]
    Variables.bridge.drop()
    utility = Variables.bridge
    album_n = 0
    size = 0
    
    for uri in albums_per_artist[artist]:
        dati_album = sp.album(uri)
        stuff=[]
        if stopper == True:
            break
        
        
        if dati_album['artists'][0]['name'] == artist and 'live' not in dati_album['name'].lower():
            for i in range(0,len(dati_album['tracks']['items'])):
                song = dati_album['tracks']['items'][i]['name']
                uri = dati_album['tracks']['items'][i]['uri']
                features = sp.audio_features(uri) 
                helper = False
                counter = 0 
                while helper == False:
                    try:
                        counter +=1
                        search = Settings.genius.search_song(song, artist)
                        lyr = search.lyrics
                        rel = search.year
                        lan = detect(lyr)
                        helper = True
                        if len(lyr) > 9000:
                            lyr=''
                    except:
                        counter +=1
                        if counter > 5:
                            lan=''
                            lyr=''
                            rel=''
                            helper=True
                stuff.append({'songname':song, 'language':lan,'uri':uri, 'lyrics':lyr,
                                                          'released':rel,'variables':features})
            insert.append({'name':dati_album['name'], 'tracks':stuff})
            utility.insert_one({'_id':album_n,'name':dati_album['name'], 'tracks':stuff})
            thresh = len(bson.BSON.encode(Variables.bridge.find_one({'_id':album_n})))
            size += thresh
            print('Album: {} _id: {} Size: {} KB'.format(dati_album['name'],album_n,thresh/1000))
            album_n += 1
            if size > 16000000 or album_n == 120:
                print('STOPPED!!!!!')
                stopper = True
                break
    if stopper == True:
        collection.insert_one({'_id':tracker,'Artist':artist,'Albums':insert[:-1]})
        print('{} Total collection size: {} mb'.format(artist,(size-thresh)/1000))
    else:
        collection.insert_one({'_id':tracker,'Artist':artist,'Albums':insert})
        print('{} Total collection size: {} MB'.format(artist, size/1000000))
    tracker += 1

Variables.bridge.drop()
print('Lyrics e variabili ineerenti alle canzoni aggiunte con successo.')