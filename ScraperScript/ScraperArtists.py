import sys
sys.path.insert(0,'../Spotify Project/Setup')

from Setup import Settings
from Setup import Variables
from Setup.functions import divide
from tqdm import tqdm

sp = Settings.sp
collection = Variables.db[Settings.artists_collection_name]
popularity_tresh = Variables.popularity
tracker = collection.estimated_document_count() + 1

if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente agli artisti è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per aggiungere ulteriori artisti alla collezione.')
    answer = input('')
    if answer == 'delete':
        definitive = input('Sei sicuro? <y> <n>.')
        if definitive =='y':
            collection.drop()
            tracker = 1
        else:
            print('collezione non eliminata.')
    else:
        tracker = collection.estimated_document_count() + 1
else:
    divide()
    print('La collezione inerente agli artisti non è presente nel database.')
    tracker = 1 
   

print('Si vuole eseguire una ricerca personalizzata?\nDigita il nome degli artisti da cercare separandoli con una <,>\nAltrimenti digita <fullsearch> per eseguira la ricerca completa.')
search = input('').split(',')
if search ==['fullsearch']:
    search = Variables.total_search

    
check_duplicates = []
for comb in tqdm(search):

    # Cerca gli artisti in base alle combinazioni di lettere, estrapola 50 artisti per iterazione.
    try:
        artist_search = sp.search(q=comb, type = 'artist', limit = 50)
    except:
    
        # Previene la disconnessione dall'api di spotipy.    
        print('Disconnection prevented!')
    for i, artist in enumerate(artist_search['artists']['items']):
        name = artist['name']
        url = artist['external_urls']['spotify']
        follower = artist['followers']['total']
        genres = artist['genres']
        popularity = int(artist['popularity'])
        
        # Per risolvere il problema di URL duplicate utiliziamo un if in modo da selezionare URL uniche.
        if url not in check_duplicates and popularity >= popularity_tresh:
            collection.insert_one({'_id':tracker, 'Artist':name, 'follower':follower, 
                           'genres':genres, 'popularity':popularity, 'url':url })
            check_duplicates.append(url)
            tracker += 1
print('Artisti aggiunti alla collezione.')