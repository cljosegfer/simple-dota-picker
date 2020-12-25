patch = '7.28'

favorite_heroes = ['naga-siren', 
                   'anti-mage', 
                   'terrorblade']

formal_names = ['Naga Siren', 
                'Anti-Mage', 
                'Terrorblade']

adress = []
for hero in favorite_heroes:
    adress.append('https://www.dotabuff.com/heroes/' + 
               hero + '/counters?date=patch_' + patch)
