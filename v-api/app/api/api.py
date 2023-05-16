import json

def lees_mensen(geheim: int):
    #with open('v-api/data/mensen.json') as stream:
    with open('data/mensen.json') as stream:   
        mensen = json.load(stream) 
    with open('v-api/data/geheim.json') as stream:
        geheimen = json.load(stream)
    if geheimen[0]['geheim'] == geheim:
        uitkomst = mensen
    else:
        uitkomst = 'geen rechten'

    return uitkomst
    

def zoek_mens(voornaam: str, achternaam:str ):
    #with open('v-api/data/mensen.json') as stream:
    with open('data/mensen.json') as stream:    
        mensen = json.load(stream)
    for mens in mensen:
        if mens['voornaam'] == voornaam and mens['achternaam'] == achternaam:
            uitkomst = mens['geboortedatum']
            break
        else:
            uitkomst = 'niet gevonden'    

    return uitkomst    
    

def nieuw_mens(payload):
    #with open('v-api/data/mensen.json', 'r') as stream:
    with open('data/mensen.json', 'r') as stream:    
        mensen = json.load(stream)
        if mensen:
            #kijk naar het id van de laatste entry in mensen
            last_id = mensen[-1]['id']
            #tel er 1 bij op
            new_id = last_id + 1
        else:
            new_id = 1
        payload['id'] = new_id
        mensen.append(payload)

    #with open('v-api/data/mensen.json', 'w') as stream:
    with open('data/mensen.json', 'w') as stream:    
        json.dump(mensen, stream, indent=4)

    return payload



def toon_gebruikers():
    #with open('v-api/data/gebruikers.json') as stream:
    with open('data/gebruikers.json') as stream:    
        gebruikers = json.load(stream)

    return gebruikers        
 
  

def toon_vrienden(gebruiker_id: int):
    gebruiker_resultaat = []

    #with open('v-api/data/resultaten.json') as stream:
    with open('data/resultaten.json') as stream:    
        resultaten = json.load(stream)

    #with open('v-api/data/gebruikers.json') as stream:
    with open('data/gebruikers.json') as stream:    
        gebruikers = json.load(stream)

    #with open('v-api/data/mensen.json') as stream:
    with open('data/mensen.json') as stream:    
        mensen = json.load(stream)

    for resultaat in resultaten:
        if resultaat['gebruiker_id'] == gebruiker_id:
            for gebruiker in gebruikers:
                if gebruiker['id'] == resultaat['gebruiker_id']:
                    gebruiker_resultaat.append(gebruiker)
                    #break

                    for mens_id in resultaat['mensen']:
                        for mens in mensen:
                            if mens_id == mens['id']:
                                gebruiker_resultaat.append(mens)
                    break
    
    return gebruiker_resultaat
