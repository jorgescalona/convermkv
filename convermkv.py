#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

def despedida():
    """Mensaje de ejecucion exitosa"""
    print 'El programa se ejecuto de manera exitosa \n'
    print '@jorgemustaine, https://github.com/jorgescalona'

def renom(arch):
    """esta funcion elimina los espacios en blacos de los nombres de archivos"""
    print arch
    sesp=''.join(arch.split())
    return sesp

def ord_direc():
    """Funcion que ordena el directorio dado y hace la convercion mediante mencoder"""
    indice = 1
    control = 1

    while True:
        if control==1:
            directorio=raw_input('Ingrese la ruta de la carpeta: ')
            if directorio=='':
                directorio=os.getcwd()
                print directorio
            control=2
        try:
            lista=os.listdir(directorio)
            l=sorted(lista)
            for i in l:
            if i[-4:] == ".mkv":
                    org=renom(i)
                    tran=org[0:-3:]
                    nn=''
                    final=tran+'avi'
                    os.rename(i,org)
                    os.system('mencoder %s -ovc xvid -oac mp3lame -oac mp3lame -nosub -lameopts abr:br=192 -xvidencopts pass=2:bitrate=-700000 -o %s' % (org,final))
                    indice=indice+1
            despedida()
            break

        except:
            print 'Ingrese un path valido'
            control=1
            continue

ord_direc()