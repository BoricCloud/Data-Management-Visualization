import sys
sys.path.insert(0,'../Spotify Projec/Setup')

import subprocess
import os
import json
import pprint
from Setup import Settings
from Setup import Variables

db = Variables.db

db[Settings.artists_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])

db[Settings.main_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])

db[Settings.natio_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])

db[Settings.SexAgeCity_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])

db[Settings.related_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])

db[Settings.streams_collection_name].aggregate([{
    '$merge': {'into':'Complete','on':'_id'}}])
    
answer = input('Merge completato, vuoi rimuovere le collezioni usate?[y][n] ')
if answer == 'y':
    db[Settings.artists_collection_name].drop()
    db[Settings.natio_collection_name].drop()
    db[Settings.SexAgeCity_collection_name].drop()
    db[Settings.related_collection_name].drop()
    db[Settings.main_collection_name].drop()
    db[Settings.albums_collection_name].drop()
    db[Settings.streams_collection_name].drop()
    print('Done!')
else:
    print('Done!')

answer1 = input('creare un json?[y][n].')
if answer1 =='y':
    answer2 = input('Come si vuole nominare il file: ')
    answer3 = input('Inserire il nome della directory: ')
    subprocess.call("mongoexport --db {} --collection Complete --out {}.json ".format(Settings.cluster_name,answer2), shell = True)
    os.mkdir('{}/{}'.format(Settings.PATH,answer3))
    os.rename('{}/{}.json'.format(Settings.PATH,answer2),'{}/{}/{}.json'.format(Settings.PATH,answer3,answer2))
    print('File creato con successo.')
    