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
os.system('clear');
print (fixedIntro)
dentist = """
            /-----|
         \-'      |
           Q      |
      )C ~\/\     |
       \\_   \    |
        \_77 |\   |
         |`` \ \  |
        ""\"  ~ ~ ===
"""
pilot = """
           _
         -=\\`\\
     |\\ ____\\_\\__
   -=\\c`""\"""\"" "`)
      `~~~~~/ /~~`
        -==/ /
          '-'
"""
farmer = """
                       x
             .-. _______|
             |=|/     /  \\
             | |_____|_""_|
       |=|=|=|_|_[X]_|____|
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
astro = """
            _..._
          .'     '.      _
         /    .-""-\\   _/ \\
       .-|   /:.   |  |   |
       |  \  |:.   /.-'-./
       | .-'-;:__.'    =/
       .'=  *=|CSA  _.='
      /   _.  |    ;
     ;-.-'|    \\   |
    /   | \\    _\\  _\\
    \\__/'._;.  ==' ==\\
             \\    \\   |
             /    /   /
             /-._/-._/
             \\   `\\  \\
              `-._/._/
"""
questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'qmark':'( ͡° ͜ʖ ͡°)',
        'message': 'Bienvenue au Quebec! :) What do you wanna work as?',
        'choices': ['Dentist'+"\n"+dentist, 'Pilot'+"\n"+pilot, 'Farmer'+"\n"+farmer, 'Astronaut'+"\n"+astro],
        'filter': lambda val: val.lower()
    }
]
answers2 = prompt(questions2, style=custom_style_3)

os.system('clear');
print (fixedIntro)
#pprint(answers2['job'])

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











