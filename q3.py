# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:22:12 2019

@author: lisa_
"""

#3

file = open("qbdatanew.txt","r")
code = input("Enter a a four digit code: ")
tmp = file.readlines()
c = 1
for i in tmp:
    if i[:4] == code:
        print(i)
        break
    if c == len(tmp):
        print("Not found.")
    c+=1
file.close()
