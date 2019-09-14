# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:52:16 2019

@author: dina

list of dictionary objects not good because:
    - place for key name that is same for all dictionaries
    - can change values that is not right 
    
so use collections library to get immutable data structure and put the data 
in a tuple because don't want to delete the values and the objects
"""

import collections


peoples = [{'name': 'dana', 'age':23, 'id':123}, 
          {'name': 'hana', 'age':41, 'id':343}]

print("all peoples list info ")
for people in peoples:
    print (people)
    
peoples[0]['name'] = 'moshe'
print ("\nfirst dictionary info key changed. the dictionary is : ", peoples[0])

#use collection that use tuple instead of dictionary
PeoplesCollection = collections.namedtuple('PeoplesCollection', [
        'name',
        'age',
        'id'
        ])

ela = PeoplesCollection(name ='Ela Stam', age = 45, id = 4545)
if ela.age in range(40, 60):
    print (ela.name, ela.id)

#get immutable data so cann't change key and value info
# put the collections in list so can del objects from the list
#    del we use list 
peoplesL = [PeoplesCollection(name ='Ela Stam', age = 45, id = 4545),
           PeoplesCollection(name ='Efy Stam', age = 13, id = 12345),
           PeoplesCollection(name ='Ted Stam', age = 45, id = 3421)]

print ('\n\ndata')
for people in peoplesL:
    print (people)

#delete object from the list
del peoplesL[1]
print ("\n\n delete second object from the list")
print (peoplesL)

# use collections and tuple because don't want to delete
peoplesT = [PeoplesCollection(name ='Haim Levy', age = 55, id = 123),
           PeoplesCollection(name ='Varda Cohen', age = 13, id = 456),
           PeoplesCollection(name ='Ada Qa', age = 6, id = 789)]

print('\n info tuple')
print (peoplesT)