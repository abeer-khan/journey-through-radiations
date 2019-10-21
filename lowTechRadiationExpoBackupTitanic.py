# -*- coding: utf-8 -*-
"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from examples import custom_style_3
from ascii_graph import Pyasciigraph
import os

os.system("clear") #use this for windows. change to os.system("clear") for linux
#os.system("cls") #use this for windows. change to os.system("clear") for linux

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
welcome = "[[cyan]]"

                                        #We will also tell you the impact of your 
                                        #journey on your health in the end. 

print("""
                                        Hi, welcome to RadExpo!
                                        
                                        Travel from province to province to earn money. 
                                        
                                        Beware! Survival activities are endangered by harmful 
                                        radiations. 
                                        
                                        Earn Money. Have fun. But Survive :)
""".center(os.get_terminal_size().columns))

inp = input()
os.system('clear');

questions1 = [

    {
        'type': 'list',
        'name': 'province',
        'qmark': '¯\_(ツ)_/¯',
        'message': 'Which province you want to work at?',
        'choices': ['Alberta', 'British Columbia', 'Manitoba', 'Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador', 'Prince Edward Island' , 'Saskatchewan'],
        'filter': lambda val: val.lower()
    }
]

answers1 = prompt(questions1, style=custom_style_3)

########################################### Fancy stuff when go to Quebec ##############################
import pygame  # Load the popular external library
pygame.mixer.init()
pygame.mixer.music.load("CelineDionTitanicQuebec.mp3")
pygame.mixer.music.play()

print ("                                                            You embark for Quebec! ")
ship1 = """
              |    |    |
             )_)  )_)  )_)
            )___))___))___)\\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^

"""

ship2 = """
                              |    |    |
                             )_)  )_)  )_)
                            )___))___))___)\\
                           )____)____)_____)\\
                         _____|____|____|____\\\__
                ---------\                   /---------
                  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
                    ^^^^      ^^^^     ^^^    ^^
                         ^^^^      ^^^

"""
icebergShip = """
           
                                      |    |    |              ,----....____            
                                     )_)  )_)  )_)             (             ````----....___   
                                    )___))___))___)\              \                            `````
                                   )____)____)_____)\               \                               \        
                                 _____|____|____|____\\__                \                               \       
                        ---------\                   /---------              )`.\  )`.   )`.   )`.   )`.   )`.  \ )`.   
                          ^^^^^ ^^^^^^^^^^^^^^^^^^^^^            -'   `-'   `-'   `-'   `-'   `-'   `-'   `-'
                            ^^^^      ^^^^     ^^^    ^^            
                                 ^^^^      ^^^                  
"""
explode = """

                                                         _.-^^---....,,--       
                                                     _--                  --_  
                                                    <                        >)
                                                    |                         | 
                                                     \._                   _./  
                                                        ```--. . , ; .--'''       
                                                              | |   |             
                                                           .-=||  | |=-.   
                                                           `-=#$%&%$#=-'   
                                                              | ;  :|     
                                                     _____.,-#%&$@%#&#~,._____ 
 """
jk = """
       _   _  __  _
      | | | |/ / | |
      | | | ' /  | |
  _   | | |  <   | |
 | |__| | | . \  |_|
  \____/  |_|\_\ (_)


"""
jk = """
       _   _  __  _            _  _      _____     _ _              _____  _             
      | | | |/ / | |         _| || |_   / ____|   | (_)            |  __ \(_)            
      | | | ' /  | |        |_  __  _| | |     ___| |_ _ __   ___  | |  | |_  ___  _ __  
  _   | | |  <   | |         _| || |_  | |    / _ \ | | '_ \ / _ \ | |  | | |/ _ \| '_ \ 
 | |__| | | . \  |_|        |_  __  _| | |___|  __/ | | | | |  __/ | |__| | | (_) | | | |
  \____/  |_|\_\ (_)          |_||_|    \_____\___|_|_|_| |_|\___| |_____/|_|\___/|_| |_|

                                                                                  """

import time
import os

print (ship1)
time.sleep(1)
#os.system('clear');
print (ship2)
time.sleep(1)
#os.system('clear');
time.sleep(1)
#os.system('clear');
print (icebergShip)
time.sleep(2)
print (explode)
time.sleep(3.3)
print (jk)
time.sleep(3)
pygame.mixer.music.stop()
############################################# end of fancy quebec stuff #########################################

questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'qmark':'( ͡° ͜ʖ ͡°)',
        'message': 'Bienvenue au Quebec! :) What do you wanna work as?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astranaut'],
        'filter': lambda val: val.lower()
    }
]

answers2 = prompt(questions2, style=custom_style_3)
#pprint(answers2['job'])

questions3 = [
    {
        'type': 'checkbox',
        'qmark': '(づ｡◕‿‿◕｡)づ',
        'message': "What do you like to do outside of work? We don't judge.",
        'name': 'activities',
        'choices': [
            {
                'name': 'Have any of these items in your diet: Bananas, Carrots, Red Meat, Potatoes, Brazil Nuts, Lima Beans'
            },
            {
                'name': 'Sleep next to someone'
            },
            {
                'name': 'Watch Television for more than an hour'
            },
            {
                'name': 'Smoke Cigarettes'
            },
            {
                'name': 'Use Natural Gas at home'
            },
            {
                'name': 'Use Consumer Products regularly'
            }
        ]
    }
]

answers3 = prompt(questions3, style=custom_style_3)
#pprint(answers3['activities'])

questions4 = [
    {
        'type': 'checkbox',
        'qmark': '(ง’̀-‘́)ง',
        #'qmark': '(◣_◢ )',
        'message': """I bet you jump around a lot. 
        I bet you need one of the following scans that just so happened to find radiation measurements for. 
        Play along. Please. 
        """,
        #'Do you fell Sick? Might you need to undergo one of these scans?',
        'name': 'activities',
        'choices': [
            {
                'name': 'Arm X-Ray'
            },
            {
                'name': 'Dental X-Ray'
            },
            {
                'name': 'Chest X-Ray'
            },
            {
                'name': 'Head CT Scan'
            },
            {
                'name': 'Chest CT Scan'
            },
            {
                'name': 'Mammogram'
            },
{
                'name': 'Full body CT Scan'
            }
        ]
    }
]

answers4 = prompt(questions4, style=custom_style_3)
#pprint(answers4['activities'])

print("""
    FYI we have listed out different provinces and activities that are exposed to harmful radiations.
    Measurement of radiations are in Sieverts.
""")

provRads = [('QC', 0.0016), ('NL', 0.0016), ('BC', 0.0018), ('ON', 0.0018), ('NB', 0.0018), ('PE', 0.0018),
            ('YT', 0.0019),
            ('NU', 0.0019), ('AB', 0.0024), ('NS', 0.0025), ('NT', 0.0031), ('SK', 0.0035), ('MB', 0.0041)
            ]
provRadsBar = Pyasciigraph(float_format='{:,.5f}')
for line in provRadsBar.graph('Background radiations of every province', provRads):
    print(line)

print('\n\n')

# show plot for relative radiations of each occupation
occRads = [('Farmer', 0.00011), ('Dentist', 0.005), ('Pilot', 0.05), ('Astronaut', 0.5)]
occRadsBar = Pyasciigraph(float_format='{:,.5f}')
for line in occRadsBar.graph('Radiations exposure from every occupation', occRads):
    print(line)

print('\n\n')

# show plot for relative radiations of each activity
actRads = [('Eating banana / red meat / carrots', 0.0001825), ('Sleeping next to someone', 5e-08),
           ('Watch TV', 1.000000e-05),
           ('Smoking cigarettes', 0.013), ('Using natural gas at home', 9e-05),
           ('Using soaps / shampoos / other consumer products', 0.011)
           ]
actRadsBar = Pyasciigraph(float_format='{:,.8f}')
for line in actRadsBar.graph('Radiations exposure from every activity', actRads):
    print(line)

print('\n\n')

print("""
    The following is the result of your journey.
""")

# show plot for total radiations you have accumulated compared to increasing risk of cancer
totalRadSuffered = [("You've suffered", 0.05), ("Death by cancer :p", 0.1)]
totalRadSufferedBar = Pyasciigraph(float_format='{:,.2f}')
for line in totalRadSufferedBar.graph('Do you have health? How much did you suffer? (in Sv)', totalRadSuffered):
    print(line)

print('\n\n')

# show plot for total money you have earned compared to your goal (maybe a number pulled for ideal happiness)
money = [("You've earned", 25000), ("But you need this much to be happy :(", 50000)]
moneyBar = Pyasciigraph(float_format='{:,.2f}')
for line in moneyBar.graph('Are you (monetarily) happy? Do you have wealth? (in CAD)', money):
    print(line)


