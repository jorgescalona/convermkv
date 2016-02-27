#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Copyright (C) <2016>  <@jorgemustaine>
# www.attakatara.wordpress.com
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>



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
