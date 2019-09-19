# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:22:12 2019

@author: lisa_
"""

#2

file = open("qbdata.txt","r")
tmp = file.readlines()
deletestu = input("Enter a name: ")
c = 0
NameList = []
for i in tmp:
    for o in range(len(i)):
        if i[o] == "Q":
            NameList.append(i[:o])
nn = deletestu + " "
for i in NameList:
    if i == nn:
        break
    c+=1
    
del tmp[c]
file.close()

index = 0

def zero(str1):
    str1 = str(str1)
    n = 4 - len(str1)
    temp = ""
    temp = temp + "0"*n + str1 +" "
    return temp

file = open("qbdatanew.txt","w")
for e in tmp:
    index+=1
    file.write(str(zero(index)) + e)
file.close()