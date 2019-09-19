# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:22:12 2019

@author: lisa_
"""

#1

file = open("qbdata.txt","r")
char = input("Enter a character: ")
tmp = file.readlines()
file.close()

file = open("qbdata.txt","w")
for i in tmp:
    for o in range(len(i)):
        if i[o] == " ":
            i = i[:o] + char + i[o+1:]
    file.write(i)
file.close()