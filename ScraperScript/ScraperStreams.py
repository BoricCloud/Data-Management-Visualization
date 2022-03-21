import sys
sys.path.insert(0,'../Spotify Projec/Setup')

import warnings
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from Setup import Settings
from Setup.functions import Listener
import pandas as pd
from tqdm import tqdm
from Setup import Variables
warnings.filterwarnings("ignore")

collection = Variables.db[Settings.streams_collection_name]
check_duplicates = Variables.check_duplicates
url_about = [url + '/about' for url in check_duplicates]
artists_list = Variables.artists_list
#print(url_about[0])
#print(Listener(0, url_about[0]))

if collection.estimated_document_count() != 0:
    print('La collezione ineerente agli streams è già presente nel database.\nSe si desidera eliminarla digitare <delete> altrimenti un qualsiasi altro tasto per aggiungere dati.')
    answer = input('')
    if answer == 'delete':
        collection.drop()
        for index, element in enumerate(url_about):
            try:
                collection.insert_one(Listener(index, element)[0])
            except:
                collection.insert_one({'_id':index + 1,'Artist': artists_list[index], 'Streams':{pd.to_datetime('today').strftime('%d/%m/%Y'):None}})
                print('Error at index: '+str(index+1)+' Artist: '+ artists_list[index])
            print('Process: '+str(round(((index+1)/len(url_about))*100,2))+'%', end="\r")
        print('DONE!!!')
    else:
        print('La collezione verra aggiornata per oggi: ',pd.to_datetime('today').strftime('%d/%m/%Y'))
        for i in tqdm(range(collection.estimated_document_count())):
            try:
                collection.update({'_id': i+1 },{'$set':{'Streams.'+ pd.to_datetime('today').strftime('%d/%m/%Y'): Listener(i, url_about[i])[1]}})
            except:
                print('\nError at index: '+str(i+1)+' Artist: '+ artists_list[i])
                collection.update({'_id': i+1 },{'$set':{'Streams.'+ pd.to_datetime('today').strftime('%d/%m/%Y'): None}})
else:
    print('Inizializzazione collezione al giorno: ',pd.to_datetime('today').strftime('%d/%m/%Y'))
    for index, element in enumerate(url_about):
        try:
            collection.insert_one(Listener(index, element)[0])
        except:
            collection.insert_one({'_id':index + 1,'Artist': artists_list[index], 'Streams':{pd.to_datetime('today').strftime('%d/%m/%Y'):None}})
            print('Error at index: '+str(index+1)+' Artist: '+ artists_list[index])
        print('Process: '+str(round(((index+1)/len(url_about))*100,2))+'%', end="\r")
    print('DONE!!!')