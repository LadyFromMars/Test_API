import requests
import json
import unittest

class MyTest(unittest.TestCase):


#----Simple test to verify values -----

    url = "https://superhero-search.p.rapidapi.com/api/"
    querystring = {"hero":"Luke Skywalker"}
    headers = {
        'x-rapidapi-key': "ac8452548dmsha60d04f82d8d5b9p1eeed7jsncabc88b3c32e",
        'x-rapidapi-host': "superhero-search.p.rapidapi.com"
        }

    #Send GET request
    response = requests.request("GET", url, headers=headers, params=querystring)

    #Print the response
    #print(response.text)

    #Convert JSON to dictionary
    content=response.content
    info=json.loads(content)
    print(type(info))

    #GET Hero info

    #---Name---

    #Save name
    name=info['name']

    #---Powerstats

    #Accessing hero's powerstats
    stats= info['powerstats']

    #Saving powerstats
    speed=stats['speed']
    intelligence=stats['intelligence']
    strength= stats['strength']

    #Printing out powerstats
    print('Name: '+ name)
    print('Speed: ' + str(speed))
    print('Intelligence: ' + str(intelligence))
    print('Strength: ' + str(strength))

    #--- Appearance

    #Accessing hero's appearance
    look= info['appearance']

    #Saving appearance
    gender=look['gender']
    race=look['race']
    hairColor=look['hairColor']
    height=look['height'] #Accessing height and saving height in inch
    height_inch= height[0]

    #Printing out appearance
    print('gender: '+ gender)
    print('race: ' + race)
    print('hairColor: ' + hairColor)
    print('Height in inch : ' + str(height_inch))


    # Verify information

    tc = unittest.TestCase('__init__')
    #tc.assertEqual(text,textv)

    #Verify name
    tc.assertEqual(name, 'Luke Skywalker')

    #Verify powerstats
    tc.assertEqual(speed, 42)
    tc.assertEqual(intelligence, 69)
    tc.assertEqual(strength, 38)

    #Verify appearance
    tc.assertEqual(gender, 'Male')
    tc.assertEqual(race, 'Human')
    tc.assertEqual(hairColor, 'Blond')
    tc.assertEqual(height_inch, "5'6")


if __name__ == '__main__':
    unittest.main()
