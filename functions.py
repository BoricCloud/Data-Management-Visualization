def Continenter(row):
    NA = ['Stati Uniti','Canada']

    EUROPE = ['Regno Unito','Italia','Scozia','Inghilterra','Germania','Svezia','Spagna','Francia',
              'Irlanda','Norvegia','Paesi Bassi','Turchia','Belgio','Finlandia','Danimarca',
              'Islanda','Austria', 'Estonia','Grecia','Moldavia','Polonia','Galles','Belgio','Portogallo',
             'Romania','Kosovo','Svizzera','Albania','Solovenia', 'Isola di Man','Irlanda del Nord',
             'Croazia']

    AFRICA = ['Somalia','Uganda','Mauritius','Algeria','multinazionale','RD del Congo','Senegal',
              "Costa d'Avorio",'Egitto','Capo Verde', 'Nigeria', 'Mali','Sud Africa','Marocco']

    CA = ['Guatemala','Haiti','Panama','Cuba','Messico','Isole Vergini britanniche','Porto Rico',
          'Rep. Dominicana','Bermuda','Giamaica']

    SUDA = ['Barbados','Honduras','Cile','Brasile','Giamaica','Colombia','Argentina','Venezuela',
            'Uruguay','Ecuador','Trinidad e Tobago']

    OCEN = ['Australia','Nuova Zelanda','Guam']

    ASIA = ['Filippine','Corea del Sud','Giappone','India','Taiwan','Hong Kong','Iran','Georgia','Malaysia',
        'Libano','Singapore','Mongolia','Cina','Israele','Pakistan','Russia','Kazakistan']
    if row in NA:
        return 'North America'
    elif row in SUDA:
        return 'South America'
    elif row in EUROPE:
        return 'Europe'
    elif row in OCEN:
        return 'Oceania'
    elif row in ASIA:
        return 'Asia'
    elif row in CA:
        return 'Central America'
    else:
        return 'Not Found'
        
        
def Condense(row):
    step = row
    for element in row:
        if isinstance(element[0],int):
            row.remove(element)
    try:
        if len(row)==1:
            row = row[0][0]
        elif row[0][1] == row[1][1]:
            row = '{}-{}'.format(row[0][0],row[1][0])
        elif row[0][1] > row[1][1]:
            row = row[0][0]
        step = row
    except:
        #step = row
        row='various'
    #step = row
    if 'hip' in step:
        step = step.replace('hip','hip hop')
    elif 'hop' in step:
        step = step.replace('hop','hip hop')
        
    if row in ['hip','hop','pop-hip']:
        row = 'hip-hop'
    elif 'rock' in row:
        row = 'rock'
    elif row in ['edm', 'edm-house','disco','techno','house','trance','nightcore','lo-fi','lo','fi',
                 'dance','eurodance']:
        row = 'edm'
    elif 'rap' in row:
        row = 'rap'
    elif row in ['latin','reggaeton', 'samba','latin-pop','latin-reggaeton','pop-latin','pagode-samba',
                'pagode']:
        row = 'latin'
    elif 'indie' in row:
        row = 'indie'
    elif row in ['orchestra','classic','classical']:
        row = 'classical'
    elif row in ['dance-pop','adult-pop']:
        row = 'pop'
    elif row in ['filmi','hollywood','pop-filmi','cartoon','disney','soundtrack']:
        row = 'entertainment'
    elif row in ['calming','sleep','ambient','meditation','relax','chillhop','chillhop-lo',
                 'lullaby','sound']:
        row = 'relax'
    elif row in ['alternative','metal','punk','metalcore']:
        row = 'rock'
        
    if 'tropical' in row or 'bounce' in row or 'room' in row or 'disco' in row or 'dance' in row or 'edm' in row or 'techno' in row or 'house' in row or 'electro' in row:
        row = 'edm'
    elif 'funk' in row:
        row = 'funk'
    elif 'corrido' in row or 'latin' in row or 'flamenco' in row or 'grupera' in row or 'samba' in row or 'banda' in row:
        row = 'latin'
    elif 'jazz' in row or 'blues' in row:
        row = 'blues & jazz'
    elif 'r&b' in row:
        row = 'r&b'
    elif 'chillstep' in row or 'calming' in row or 'instrumental' in row or 'background' in row or 'environmental' in row or 'ambient' in row or 'sleep' in row:
        row = 'relax'
    elif 'otacore' in row or 'hollywood' in row or 'movie' in row or 'show' in row or 'filmi' in row or 'disney' in row or 'broadway' in row:
        row = 'entertainment'
    elif 'folk' in row:
        row = 'folk'
    elif 'mellow' in row or 'metal' in row or 'punk' in row:
        row = 'rock'
    elif 'pop' in row:
        row = 'pop'
    elif 'hip' in row or 'hop' in row:
        row = 'hip-hop'
    elif 'classic' in row or 'piano' in row:
        row='classical'
    elif 'anthem' in row or 'soul' in row:
        row = 'soul'
    elif 'country' in row:
        row = 'country'
    elif 'reggae' in row:
        row = 'reggae'
    elif 'drill' in row or 'urban' in row:
        row = 'rap'
    elif 'adult' in row:
        row = 'country'
    
    return (row,step)