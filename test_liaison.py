# -*- coding: utf-8 -*-

import serial

def test_liaison():
    ser = serial.Serial('COM7', 9600) #liaison avec le port de l arduino (ici com7)
    
    ser.write('H'.encode())
    
    while 1:
        if(ser.inWaiting() > 0):
        
            #lign = ser.read()
            #etat = lign.decode('ascii') #'utf-8' pour chaine de caractères
            #print(etat, end='')
            
            val2 = ser.read() #lecture du HSB de la valeur envoyee
            val3 = ser.read() #lecture du LSB
            i1 = ord(val2) #conversion byte-> entier
            i2 = ord(val3)
            val = i1 * 256 + i2 #reconstruction de la valeur
            print(val)
            