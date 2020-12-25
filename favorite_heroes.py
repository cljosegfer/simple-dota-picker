patch = '7.28'

favorite_heroes = ['naga-siren',
                   'anti-mage',
                   'terrorblade',
                   'arc-warden',
                   'chaos-knight',
                   'drow-ranger',
                   'ember-spirit',
                   'faceless-void',
                   'gyrocopter',
                   'juggernaut',
                   'lifestealer',
                   'luna',
                   'morphling',
                   'phantom-lancer',
                   'spectre',
                   'sven',
                   'troll-warlord',
                   'wraith-king']

formal_names = ['Naga Siren',
                'Anti-Mage',
                'Terrorblade',
                'Arc Warden',
                'Chaos Knight',
                'Drow Ranger',
                'Ember Spirit',
                'Faceless Void',
                'Gyrocopter',
                'Juggernaut',
                'Lifestealer',
                'Luna',
                'Morphling',
                'Phantom Lancer',
                'Spectre',
                'Sven',
                'Troll Warlord',
                'Wraith King']

adress = []
for hero in favorite_heroes:
    adress.append('https://www.dotabuff.com/heroes/' + 
               hero + '/counters?date=patch_' + patch)
