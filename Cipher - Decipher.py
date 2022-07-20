# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:10:53 2022

#This program get a string from the user and print the cipher of the string /n
and print the decipher of that string

@author: Ellie Nia
"""


def cipher(string):      #This function return the cipher of the string
    cipher = ""          #Initialize the string that will contain the cipher message
    for char in string:      
        cipher += chr(ord(char) + ord(string[0]))    #Building the ciphered string
       
    return cipher

def decipher(string):      
    decipher = ""
    key = ord(string[0])//2     #Key is extracted from first ciphered letter, half of ord of first letter
    for char in string:        
        decipher += chr(ord(char) - key)    #Same as ciphering but we subtract the key
       
    return decipher        

   
def main():
   
    userstring = input("Enter a string to be cipher: ")  #Ask user to write the string
    result = cipher(userstring)                          #Call the cipher function
    print ("The cipher code is: ", result)      
    dresult = decipher(result)                  #Call the decipher function
    print ("the decipher code is: ", dresult)
   

main()
