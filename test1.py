# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:38:22 2019

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




