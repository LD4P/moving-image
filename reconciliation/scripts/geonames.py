import requests, csv, time, sys, re, codecs, json, string

def query_geonames(name):
    prefix = 'http://api.geonames.org/searchJSON?q='
    suffix = '&maxRows=10&username='
    username = # USERNAME HERE
    translator = str.maketrans('', '', string.punctuation)
    search_url = prefix + name.translate(translator) + suffix + username
    json_string = requests.get(search_url).text
    parsed_json = json.loads(json_string)
    time.sleep(1)
    return parsed_json

def get_countries(countries_string):
    country_list = []
    countries_string = countries_string.replace('\x0b',';').replace('/',';').replace(',',';').replace('|',';')
    for country in countries_string.split(';'):
        if len(country.strip()) > 1:
            country_list += [country.strip()]
    return country_list

def query_geonames_hierarchy(geonameID):
    prefix = 'http://api.geonames.org/hierarchyJSON?geonameId='
    suffix = '&username='
    username = # USERNAME HERE
    search_url = prefix + geonameID + suffix + username
    time.sleep(1)
    return requests.get(search_url)

def select_state(query_results):

    if len(query_results['geonames']) != 0:
        selection = query_results['geonames'][0]
        for result in query_results['geonames']:    
            #print(result['name'])
            if result['fcodeName'] == 'first-order administrative division':
                selection = result 
                #print(selection['name'])
            return [selection['geonameId'], selection['name']]
    else:
        return ['', '']
