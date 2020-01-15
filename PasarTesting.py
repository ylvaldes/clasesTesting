#!/usr/bin/env python3
"""
------------------------------------------------------------------------------------------------------------ 
@Nombre: Pasar Clases a Testing
@Descripcion: Busca las clases entradas en el .txt y conforma el paquete de clases compiladas para pasar a 
testing en GEMA
@Autor: f286635 Yasmani Ledesma
@email: yasman05@gmail.com
@Fecha_Creado: 2018-12-17
@Version: 1
------------------------------------------------------------------------------------------------------------ 
"""

import datetime
import os
import shutil
import fnmatch 
import zipfile
import os
import subprocess
import sys
import datetime
import string


def crearCarpeta(lista):
    global carpeta_migracion
    global parisnet
    global descripcion
    global new_dir
    new_dir = new_dir+ parisnet+"_"+descripcion
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    for x in lista:
        fichero=new_dir+x[0]
        print(fichero)
        if not os.path.exists(fichero):
            os.makedirs(fichero,0o777)

def obtenerPath(nombreClase,origen,ext):
    path_list = [os.path.join(root, file) for root, _, files in os.walk(origen)
                                          for file in fnmatch.filter(files, nombreClase+ext)]
    #Elimino los nombre de las clases del Path
    it=0
    for i in path_list:
        ruta= i[len(origen):i.rindex("\\")+1]
        path_list[it]=ruta
        it+=1
    return path_list

def print_list(o):
    for x in o:
        print(x)

def copiaClases(lista):
    global origen
    global carpeta_migracion
    global lista_path
    global new_dir
    it=0
    for x in lista:
        shutil.copy(origen+ lista_path[it][0]+x+'.class', new_dir+ lista_path[it][0] )
        it+=1

def crearZip():
    global new_dir
    iniciales=input('Entre sus iniciales:')
    nombre_zip='maximoTEST'+datetime.datetime.now().strftime("%Y%m%d")+iniciales.upper()+'.zip'
    test_zip=zipfile.ZipFile(new_dir+'\\'+nombre_zip,'w')
    for folder, subfolders, files in os.walk(new_dir):
        for file in files:
            if file.endswith('.class'):
                test_zip.write(os.path.join(folder,file),os.path.relpath(os.path.join(folder,file),new_dir),compress_type = zipfile.ZIP_DEFLATED)
    test_zip.close()
def crearTxtDetalles():
    global new_dir
    global descripcion
    
    global parisnet
    global lista_clases
    global lista_path
    global datosSVN
    txt=new_dir+'\\detalles.txt'
    g=open(txt,'w')
    g.write(descripcion+'\nParisnet: '+parisnet+os.linesep+"\n")
    g.write(datosSVN)
    g.write("\n")
    g.write("Clases Modificadas\n")
    for linea in lista_clases:
        g.write(linea+"\n")
    it = 0
    g.write("\n")
    g.write("Ruta de las Clases Modificadas\n")
    for linea in lista_clases:
        ruta=lista_path[it][0]+linea+'.class\n'
        g.write(ruta.replace('\\','.'))
        it+=1
    g.close()

def svn(lista_workspace):
    global lista_clases
    global carpeta_codigo
    it = 0
    rev_list=[]
    for linea in lista_clases:
        ruta=lista_workspace[it][0]+linea+'.java'
        it+=1
        print()
        print(ruta)
        reader= os.popen('svn log -v --limit 1 '+carpeta_codigo+ruta)
        global datosSVN
        for line in reader:
            if len(line.split('|'))== 4:
                print("Versión:    "+ line.split('|')[0])
                datosSVN+="Versión:    "+ line.split('|')[0]+"\n"
            
                autor=line.split('|')[1]

                if "f286635" in autor:
                    autor+=' Yasmani Ledesma Valdes  yledesma@ute.com.uy'
                elif "UT601331" in autor:
                    autor+=' Paulo Maya pMaya@ute.com.uy'
                elif "ut539376" in autor:
                    autor+=' Fernando Balsas FBalsas@ute.com.uy'
                elif "UT601330" in autor:
                    autor+=' Matias Rodriguez Fernandez mrodriguezf@ute.com.uy'
                elif "Z709782" in autor:
                    autor+=' Yendrie Rodriguez Borruel yrodriguezb@ute.com.uy'
                    
                
                print("Autor:    "+ autor+"\n")
                datosSVN+="Autor:    "+ autor+"\n"
                print("Fecha:    "+ line.split('|')[2])
                datosSVN+="Fecha:    "+ line.split('|')[2]+"\n"
                rev_list.append(line.split('|'))
            else:
                 datosSVN+=line
        reader.close()
        #print(datosSVN)



# Carpeta de gemadesa
origen='D:\gemadesa\IBM\MAXIMO'
#Carpeta Usada para Guardar los Paquetes de Migracion
carpeta_migracion='D:\Migracion'
#Direccion del Codigo
carpeta_codigo='D:\gemadesa\eclipse3.4-java\workspace'
#Carpeta con la Fecha
new_dir = os.path.join(carpeta_migracion, datetime.datetime.now().strftime("%Y%m%d_"))   
#Pido y Almaceno el Numero del Parisnet 
parisnet=input('Entre el # del Parisnet:')
#Pido y Almaceno la descripcion
descripcion=input('Entre el nombre de la Carpeta!:')

#Detalles del SVN
datosSVN="Detalles SVN \n"

#Leo el fichero con el Nombre de las Clases 
# Obtiene la direccion del fiche que se ejecuta 
# os.path.dirname(os.path.abspath(__file__))
f= open(os.path.dirname(os.path.abspath(__file__))+"\Clases.txt")
lista_clases=[linea.rstrip('\n') for linea in f]
print()
print("!!!!!!! Lista de Clases entradas en el *txt")
print_list(lista_clases)
print()

#Obtengo la lista de los Path dada la lista de clases
lista_path=[obtenerPath(x,origen,'.class') for x in lista_clases]
print("!!!!!!! Las Clases Compiladas entradas en el *txt se encuentran en:")
print_list(lista_path)
print()

#Obtengo la lista de Path de las Clases en el Workspace
lista_workspace=[obtenerPath(x,carpeta_codigo,'.java') for x in lista_clases]
print("!!!!!!! Las Clases entradas en el *txt se encuentran en:")
print_list(lista_workspace)
print()

#Creo la Estructura de Carpetas
print("!!!!!!! Carpeta creada en:")
crearCarpeta(lista_path)
print()
copiaClases(lista_clases)
crearZip()
svn(lista_workspace)
crearTxtDetalles()

print()
print("Tarea Ejecutada Exitosamente")