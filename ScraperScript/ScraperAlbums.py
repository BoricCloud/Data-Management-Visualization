import sys
sys.path.insert(0,'../Spotify Projec/Setup')

from Setup import Settings
from Setup import Variables
from Setup.functions import divide
from tqdm import tqdm

sp = Settings.sp
collection = Variables.db[Settings.albums_collection_name]
check_duplicates = Variables.check_duplicates


if collection.estimated_document_count() != 0:
    divide()
    print('La collezione inerente agli album è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per continuare.')
    answer = input('')
    if answer == 'delete':
        definitive = input('Sei sicuro? <y> <n>.')
        if definitive =='y':
            collection.drop()
            tracker = 0
        else:
            print('collezione non eliminata.')
    else:
        tracker = collection.estimated_document_count() 
else:
    divide()
    print('La collezione inerente agli album non è presente nel database.')
    tracker = 0

for url in tqdm(check_duplicates[tracker:]):
    total_album = []
    results = sp.artist_albums(url)
    albums = results['items']

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    remove_duplicates = []
    for album in albums:
        if album['name'] not in remove_duplicates and 'live' not in album['name'].lower():
            remove_duplicates.append(album['name'])
            total_album.append(album['uri'])
    collection.insert_one({'_id':tracker,'album':total_album})
    tracker += 1
print('Albums aggiunti con successo.')