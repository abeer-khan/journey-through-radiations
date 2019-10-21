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
import time

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
fixedIntro = """
                                                                    Hi, welcome to RadExpo!

                                                                        Travel from province to province to earn money. 

                                                                                Beware! 
                                                                    Survival activities are endangered by harmful radiations. 

                                                                        Earn Money. Have fun. But Survive :)

"""
fixedIntro += "\n" + "-"*200 + "\n\n"
print (fixedIntro)


inp = input()

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
os.system('clear');
print (fixedIntro)
questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'qmark':'( ͡° ͜ʖ ͡°)',
        'message': 'Bienvenue au Quebec! :) What do you wanna work as?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astronaut'],
        'filter': lambda val: val.lower()
    }
]
answers2 = prompt(questions2, style=custom_style_3)

os.system('clear');
print (fixedIntro)
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
os.system('clear');
print (fixedIntro)
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
os.system('clear');
print (fixedIntro)
#pprint(answers4['activities'])

while (True):
    #print('\n\n')
    os.system('clear');
    print (fixedIntro)

    # show plot for relative radiations of each activity
    actRads = [('Eating banana / red meat / carrots', 0.0001825), ('Sleeping next to someone', 5e-08),
               ('Watch TV', 1.000000e-05),
               ('Smoking cigarettes', 0.013), ('Using natural gas at home', 9e-05),
               ('Using soaps / shampoos / other consumer products', 0.011)
               ]
    actRadsBar = Pyasciigraph(float_format='{:,.8f}')
    for line in actRadsBar.graph('Radiations exposure from every activity', actRads):
        print(line)

    #print('\n\n')
    time.sleep(5)
    os.system('clear');
    print (fixedIntro)

    print("""
        The following is the result of your journey.
    """)

    # show plot for total radiations you have accumulated compared to increasing risk of cancer
    totalRadSuffered = [("You've suffered", 0.05), ("Death by cancer :p", 0.1)]
    totalRadSufferedBar = Pyasciigraph(float_format='{:,.2f}')
    for line in totalRadSufferedBar.graph('Do you have health? How much did you suffer? (in Sv)', totalRadSuffered):
        print(line)

    #print('\n\n')
    time.sleep(5)
    os.system('clear');
    print (fixedIntro)

    # show plot for total money you have earned compared to your goal (maybe a number pulled for ideal happiness)
    money = [("You've earned", 25000), ("But you need this much to be happy :(", 50000)]
    moneyBar = Pyasciigraph(float_format='{:,.2f}')
    for line in moneyBar.graph('Are you (monetarily) happy? Do you have wealth? (in CAD)', money):
        print(line)

    time.sleep(5)
    os.system('clear');
    print (fixedIntro)

    print ("                                Would you like to see these again? (y/n)")

    choice = input()
    if choice == "n":
        break
    else:
        continue











