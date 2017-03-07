# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:55:57 2017

@author: chris
"""

import random
import time

def Name():
    print ('Great, the idiot finally decided to show up')
    print ('Whats your name fuckface?')
    name = input ('My name is')
    return name           
        
def Class():
    print ('And what is he supposed to be, said the guy with the weird nose')
    print ('You better shut your mouth ugly nose McGee, i am THE')
    print ('1:Thief   2:Warrior   3:Demon')
    hero = input()
    if (hero==1):
        hero='Thief'
    elif (hero==2):
        hero='Warrior'
    else:
        hero='Demon'
    return hero       
#maybe make a library for those (choose2door, 3 door)
    
def choose2door():
    path=""
    while path!=1 and path!=2:
        path =input('Which door will you choose? (Type 1 or 2): ')
    return path
    if (path==1):
        print('You chose door number 1')
    else:
        print ('You chose door number 2')

def choose3door():
    path=""
    while path!=1 and path!=2 and path!=3:
        path =input('Which door will you choose? (Type 1, 2 or 3): ')
    return path
    if (path==1):
        print ('You chose door number 1')
    elif (path==2):
        print ('You chose door number 2')
    else:
        print ('You chose door number 3')
        
    
def displayIntro(name,hero):
    print (name,', Excellent! Now we can begin with our little....project')
    print ('We have waited for far too long and its our time to shine')
    print ('Our adventure begins')
    print ('Now with the help of the',hero.lower())
  
def initialStats(hero):
  if hero=='Thief':
        HP=100
        MP=50
        Stealth=True #or 1
        DamageDrg=10
        DamageHands=5
  elif hero=='Warrior':
        HP=200
        MP=0
        Stealth= False #or 0
        DamageDrg=25
        DamageHands=50
  elif hero=='Demon':
        HP=300
        MP=100
        Stealth= False #or 0
        DamageDrg=15
        DamageHands=15  
  stats = []  
  stats =[HP,MP,Stealth,DamageDrg,DamageHands]
  return stats

def printStats(stats):
    print ('Your stats are:')
    print ('HealthPoints:',stats[0])
    print ('ManaPoints:',stats[1])
    print ('Stealth:', stats[2])
    print ('DamageDrg:',stats[3])
    print ('DamageHands:',stats[4])
    

  
  
  
  
  
  
  
  
  
#class Character():
#maybe give them the chance to change their character with a while loop
name=Name()
hero=Class()
displayIntro(name,hero)    
stats = initialStats(hero)
print ('You can check your stats whenever you like')
printStats(stats)



     