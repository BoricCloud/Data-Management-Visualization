import sys
import time
sys.path.insert(0,'../Spotify Projec/ScraperScript')
print('')
print("Benvenuto, con questo script è possibile raccogliere tutte le informazioni inerenti agli artisti. \nSi prega di seguire l'ordine prestabilito nel menu.")
print('')
print("1. Scraping Artisti.")
print("2. Scraping Albums.")
print("3. Scraping Lyrics e variabili canzoni.")
print("4. Scraping Nazionalità")
print("5. Scraping Sesso, Provenienza, Età.")
print("6. Scraping Artisti correlati.")
print("7. Scraping Streams giornalieri")
print("8. Aggregazione")

action = input('Selezionare il numero corrispondente: ')

if action == '1':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperArtists

if action == '2':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperAlbums

if action == '3':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import MainScraper

if action == '4':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperNationality
    
if action == '5':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperSexAgeCity
    
if action == '6':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperRelatedArtists
    
if action == '7':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import ScraperStreams
    
if action == '8':
    print('')
    print('Loading ...')
    time.sleep(2)
    #print('Starting')
    from ScraperScript import Aggregation
       

    print('')
    print('Grazie per aver utilizzato il nostro prodotto, buona giornata.')
