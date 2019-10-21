# -*- coding: utf-8 -*-
"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from __future__ import print_function, unicode_literals
import pygame  # Load the popular external library
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from examples import custom_style_3
from ascii_graph import Pyasciigraph
import os
import time

os.system("clear") #use this for windows. change to os.system("clear") for linux
#os.system("cls") #use this for windows. change to os.system("clear") for linux

pygame.mixer.init()
time.sleep(2)
pygame.mixer.music.load("matrixIntro.mp3")
pygame.mixer.music.play()
#pygame.mixer.music.load('matrixIntro.mp3')
#pygame.mixer.Channel(0).play()
pygame.mixer.music.set_volume(0.2)

time.sleep(25)
                                        #We will also tell you the impact of your 
                                        #journey on your health in the end. 
fixedIntro = """
                                               Welcome traveler, to Journey Through the Radiations!

                                               Explore different cities, and enjoy new experiences. 

                                                                    But beware! 
                                        Every decision you make inflicts on you various level of radiation. 

                                                          Have fun. Hope you survive. :)
"""
fixedIntro += "\n" + "-"*127 + "\n\n"
print (fixedIntro)

#pygame.mixer.music.stop()

inp = input()
fixedIntro = """
                                                    Journey Through the Radiations!
"""
fixedIntro += "\n" + "-"*127 + "\n\n"
os.system("clear")
print (fixedIntro)

questions1 = [

    {
        'type': 'list',
        'name': 'province',
        'qmark': '¯\_(ツ)_/¯',
        'message': 'Which city you want to work in?',
        'choices': ['Vancouver', 'Toronto', 'Montreal', 'Victoria', 'Ottawa', 'Fredericton', 'Charlottetown', 'Whitehorse', 'Edmonton' , 'Halifax'],
        'filter': lambda val: val.lower()
    }
]
answers1 = prompt(questions1, style=custom_style_3)
qcFlag = """
                        .........................................+MMMMMMMMMMMMMMMM+.........................................
                        ...................:dy-..................+MMMMMMMMMMMMMMMM+..................-yd:...................
                        ..................-mMMy..................+MMMMMMMMMMMMMMMM+..................yMMm-..................
                        ................../MMMm-.................+MMMMMMMMMMMMMMMM+.................-mMMM/..................
                        .............../ss:yMM+/ss:..............+MMMMMMMMMMMMMMMM+..............:ss/+MMy:ss/...............
                        ............../MMmN+NhsNNMm-.............+MMMMMMMMMMMMMMMM+.............-mMNNshN+NmMM:..............
                        ...............oo:ydmymo-s/..............+MMMMMMMMMMMMMMMM+............../s-omyddy:oo...............
                        .................:+sMmo+-................+MMMMMMMMMMMMMMMM+................-+omMs+:.................
                        ...................+Nd/..................+MMMMMMMMMMMMMMMM+................../dN+...................
                        ....................:-...................+MMMMMMMMMMMMMMMM+...................-:....................
                        .........................................+MMMMMMMMMMMMMMMM+.........................................
                        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdMMMMMMMMMMMMMMMMdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdMMMMMMMMMMMMMMMMdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
                        .........................................+MMMMMMMMMMMMMMMM+.........................................
                        ....................:-...................+MMMMMMMMMMMMMMMM+...................-:....................
                        ...................oMm:..................+MMMMMMMMMMMMMMMM+..................:mMo...................
                        ..................:MMMd-.................+MMMMMMMMMMMMMMMM+.................-dMMM:..................
                        ..................:NMMh..................+MMMMMMMMMMMMMMMM+..................hMMN:..................
                        ..............-hNms+MN/hNmo..............+MMMMMMMMMMMMMMMM+..............omNh/NM+smNy-..............
                        ..............:NmsdomsdyyMd..............+MMMMMMMMMMMMMMMM+.............-dMyhdsmodsmN:..............
                        ...............-:/hmNdNy-:-..............+MMMMMMMMMMMMMMMM+..............-:-yNdNmh/:-...............
                        ..................-oMm/-.................+MMMMMMMMMMMMMMMM+.................-/mMo-..................
                        ...................-ho-..................+MMMMMMMMMMMMMMMM+..................-oh-...................
                        .........................................+MMMMMMMMMMMMMMMM+.........................................

"""
print (qcFlag)
time.sleep(3)

os.system('clear');
print (fixedIntro)

questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'message': 'Bienvenue au Quebec! :) What do you want to work as?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astronaut'],
        'filter': lambda val: val.lower()
    }
]

answers2 = prompt(questions2, style=custom_style_3)
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
print (dentist)
time.sleep(3)

os.system('clear');
print (fixedIntro)
#pprint(answers2['job'])
mssg = "    Month 1:    Hello Doctor! Let's find you a hobby?"
#mssg = "      Month 1:" + "\n" + " Hello Doctor. Find a new hobby for yourself?"
#print (mssg)
questions3 = [
    {
        'type': 'list',
        'message': mssg,
        'name': 'activities',
        'choices': [
            {
                'name': 'Learn how to cook'
            },
            {
                'name': 'Start smoking'
            },
            {
                'name': 'Read novels'
            }
        ]
    }
]
answers3 = prompt(questions3, style=custom_style_3)
cooking = """
                                            
                                                           .--,--.
                                                           `.  ,.'
                                                            |___|
                                                            :o o:   O
                                                           _`~^~'_  |
                                                         /'   ^   `\=)
                                                       .'  _______ '~|
                                                       `(<=|     |= /'
                                                           |     |
                                                           |_____|
                                                    ~~~~~~~ ===== ~~~~~~~~

"""
print (cooking)
time.sleep(3)

os.system('clear');
print (fixedIntro)
questions4 = [
    {
        'type': 'list',
        'message': """      Month 3:    Good News! You've been offered a position in Bécancour. Would you like to take it?""",
        #'Do you fell Sick? Might you need to undergo one of these scans?',
        'name': 'activities',
        'choices': [
            {
                'name': 'Yes'
            },
            {
                'name': 'No'
            }
        ]
    }
]

answers4 = prompt(questions4, style=custom_style_3)
#pygame.mixer.init()
#pygame.mixer.music.load("getQcDentistJob.mp3")
#pygame.mixer.music.play()
#pygame.mixer.Channel(1).play(pygame.mixer.Sound('getQcDentistJob.mp3'))
fireWorks = """
                                                                                       .''.       
                                                           .''.      .        *''*    :_\/_:     . 
                                                          :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
                                                      .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
                                                     :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
                                                     : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
                                                      '..'  ':::'     * /\ *     .'/.\'.   '
                                                          *            *..*         :
                                                            *
                                                            *
"""
runningToQuebec = """
                                                                  \\\\\\\\
                                                                  \c .(
                                                                   \ _/         ____
                                                                ___/(  /(   .--[[__]]---.
                                                               /--/ \//    ;-----------.|
                                                           __ )/ /\/ \/    |           ||
                                                          `-.\  //\        |           ||
                                                             \//  \        |___________|/
                                                              \/   \
                                                                    \\
                                                                    '--`
"""
print (fireWorks)
print (runningToQuebec)
time.sleep(3)
#pygame.mixer.music.stop()
#pygame.mixer.Channel(1).music.stop()

os.system('clear');
print (fixedIntro)
#pprint(answers4['activities'])

questions5 = [
    {
        'type': 'list',
        'message': """ Month 5: You just learned that a colleague has cancer due to prolonged exposure to radioactivity near your village. What do you want to do?
                """,
        'name': 'activities',
        'choices': [
            {
                'name': 'Pack up and leave the city immediately'
            },
            {
                'name': 'Speak to the ones in charge about a graded approach to solving radioactivity issues'
            },
            {
                'name': "Do nothing"
            }
        ]
    }
]

answers5 = prompt(questions5, style=custom_style_3)
#pygame.mixer.init()
#pygame.mixer.music.load("leaveQc.mp3")
#pygame.mixer.music.play()
manRunning = """







                                      \\\\\\\\
                                      \c .(
                                       \ _/
                                    ___/(  /(
                                   /--/ \\//
                               __ )/ /\/ \/
                              `-.\  //\\
                                 \\//  \\
                                  \/    \\
                                         \\
                                         '--`
"""
radHaz = """
                                 __    _                                   
                            _wr""        "-q__                             
                         _dP                 9m_     
                       _#P                     9#_                         
                      d#@                       9#m                        
                     d##                         ###                       
                    J###                         ###L                      
                    {###K                       J###K                      
                    ]####K      ___aaa___      J####F                      
                __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
             _g##############mZ_         __g##############m_               
           _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
          a###""          ,Z"#####@" '######"\g          ""M##m            
         J#@"             0L  "*##     ##@"  J#              *#K           
         #"               `#    "_gmwgm_~    dF               `#_          
        7F                 "#_   ]#####F   _dK                 JE          
        ]                    *m__ ##### __g@"                   F          
                               "PJ#####LP"                                 
         `                       0######_                      '           
                               _0########_                                   
             .               _d#####^#####m__              ,              
              "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    

"""
for i, j in zip(radHaz.split('\n'), manRunning.split('\n')):
    noSpaces = 30 - len(i)
    print (i + " "*noSpaces + j)
#     print (i + " "*30 + j)
stopped = len(manRunning.split('\n'))
for i in radHaz.split('\n')[stopped:]:
    print (" "*noSpaces + i)
time.sleep(4.2)
#pygame.mixer.music.stop()

os.system('clear');
print (fixedIntro)
questions6 = [
    {
        'type': 'list',
        'message': """      Month 7:    You probably won't find a job for a few months. What will you do with the extra time?""",
        'name': 'activities',
        'choices': [
            {
                'name': 'Learn how to play an instrument'
            },
            {
                'name': 'Watch television for hours'
            },
            {
                'name': 'Search for a new job'
            }
        ]
    }
]
answers6 = prompt(questions6, style=custom_style_3)
tv = """
                                                                   _,-.
                                                                ,-'  _|
                                                                |_,-O__`-._
                                                                |`-._\`.__ `_.
                                                                |`-._`-.\,-'_|  _,-'.
                                                                     `-.|.-' | |`.-'|_
                                                                        |      |_|,-'_`.
                                                                              |-._,-'  |
                                                                              | |    _,'
                                                                              '-|_,-'               
"""
print (tv)
time.sleep(4)

os.system('clear');
print (fixedIntro)
questions7 = [
    {
        'type': 'list',
        'message': """      Month 9:    After 2 months of wallowing in front of a TV, what would you like to do?""",
        'name': 'activities',
        'choices': [
            {
                'name': 'Switch careers'
            },
            {
                'name': 'Switch cities'
            },
            {
                'name': 'Continue to watch TV'
            }
        ]
    }
]

answers7 = prompt(questions7, style=custom_style_3)
os.system('clear');
print (fixedIntro)

questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'message': 'What do you want to work as now?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astronaut'],
        'filter': lambda val: val.lower()
    }
]
answers2 = prompt(questions2, style=custom_style_3)
farmer = """
                                                                       x
                                                             .-. _______|
                                                             |=|/     /  \\
                                                             | |_____|_""_|
                                                       |=|=|=|_|_[X]_|____|
                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
print (farmer)
time.sleep(3)

os.system('clear');
print (fixedIntro)
#print("""
 #        Month 12:
  #      Good news. I can see an improvement in the 
   #     radiation level absorbed by your body!
        
    #    Here are some of the stats for you
        
#)

print("""
        Month 12:
        Good news! Turns out farming doesn't expose you to as much radiation as being a dentist. 
        
        It's been an interesting year. Let's see how your body has fared.
        
        Press Enter to Continue.
    """)
#time.sleep(4)

inp = input()


while (True):
    #print('\n\n')
    os.system('clear');
    print (fixedIntro)
    
    provRads = [('Montreal', 1.6), ("St John's", 1.6), ('Victoria', 1.8), ('Toronto', 1.8), ('Frederiction', 1.8), ('Charlottetown', 1.8),
            ('Whitehorse', 1.9),
            ('Iqaluit', 1.9), ('Edmonton', 2.4), ('Halifax', 2.5), ('Yellowknife', 3.1), ('Regina', 3.5), ('Winnipeg', 4.1)
            ]
    provRadsBar = Pyasciigraph(float_format='{:,.5f}')
    for line in provRadsBar.graph('Background radiations of every province', provRads):
        print(line)
    print('\n\n')

    # show plot for relative radiations of each activity
    inp = input()
    actRads = [('Eating banana / red meat / carrots', 0.1825), ('Sleeping next to someone', 5e-05),
               ('Watch TV', 1.000000e-02),
               ('Smoking cigarettes', 13), ('Using natural gas at home', 9e-02),
               ('Using soaps / shampoos / other consumer products', 11)
               ]
    actRadsBar = Pyasciigraph(float_format='{:,.5f}')
    for line in actRadsBar.graph('Radiations exposure from every activity', actRads):
        print(line)

    #print('\n\n')
    #time.sleep(5)
    inp = input()
    os.system('clear');
    print (fixedIntro)

    print("""
        The following is the result of your journey.
    """)

    # show plot for total radiations you have accumulated compared to increasing risk of cancer
    totalRadSuffered = [("You've suffered", 17.882), ("Increased risk of cancer", 100)]
    totalRadSufferedBar = Pyasciigraph(float_format='{:,.2f}')
    for line in totalRadSufferedBar.graph('Do you have health? How much did you suffer? (in mSv)', totalRadSuffered):
        print(line)

    #print('\n\n')
    #time.sleep(5)
    #inp = input()
    #os.system('clear');
    #print (fixedIntro)

    # show plot for total money you have earned compared to your goal (maybe a number pulled for ideal happiness)
    #money = [("You've earned", 25000), ("But you need this much to be happy :(", 50000)]
    #moneyBar = Pyasciigraph(float_format='{:,.2f}')
    #for line in moneyBar.graph('Are you (monetarily) happy? Do you have wealth? (in CAD)', money):
    #    print(line)

    #time.sleep(5)
    #inp = input()
    #os.system('clear');
    #print (fixedIntro)
   
    inp = input()
    print ("\n\n")
    print ("                                Would you like to see these again? (y/n)")

    choice = input()
    if choice == "n":
        break
    else:
        continue


theend = """
                                                 _____ _                 _                               __  
                                                /__   \ |__   __ _ _ __ | | __   _   _  ___  _   _    _  \ \ 
                                                  / /\/ '_ \ / _` | '_ \| |/ /  | | | |/ _ \| | | |  (_)  | |
                                                 / /  | | | | (_| | | | |   <   | |_| | (_) | |_| |   _   | |
                                                 \/   |_| |_|\__,_|_| |_|_|\_\   \__, |\___/ \__,_|  (_)  | |
                                                                                 |___/                   /_/ 
"""
print (theend)
pygame.mixer.music.fadeout(2000);



