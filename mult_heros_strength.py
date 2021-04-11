import requests
import json
import unittest



class MyTest(unittest.TestCase):

    dict= {'Superman': 100,
           'Luke Skywalker' : 38,
           'Spider-Man': 55
    }

    #Loop through the dictionary 'dict' to veryfy superhero's strength
    for key in dict:
        namev=key
        strengthv= dict[key]
        print(namev + ': ' + str(strengthv))

        url = "https://superhero-search.p.rapidapi.com/api/"
        querystring = {"hero": namev}
        headers = {
            'x-rapidapi-key': "ac8452548dmsha60d04f82d8d5b9p1eeed7jsncabc88b3c32e",
            'x-rapidapi-host': "superhero-search.p.rapidapi.com"
            }

        #Send GET request
        response = requests.request("GET", url, headers=headers, params=querystring)

        #Convert JSON to dictionary
        content=response.content
        info=json.loads(content)

        #GET Hero info

        #Save name
        name=info['name']

        #Accessing hero's strength
        stats= info['powerstats']
        strength= stats['strength']


        # --- Verify information

        tc = unittest.TestCase('__init__')
        #tc.assertEqual(text,textv)

        #Verify name
        tc.assertEqual(name, namev)

        #Verify powerstats
        tc.assertEqual(strength, strengthv)




if __name__ == '__main__':
    unittest.main()
