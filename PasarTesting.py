#!/usr/bin/env python3
import datetime
import os
import shutil
import fnmatch 
import string
import shutil
import zipfile

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
        shutil.copy2(origen+ lista_path[it][0]+x+'.class', new_dir+ lista_path[it][0]+x+'.class' )
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
    txt=new_dir+'\\detalles.txt'
    g=open(txt,'w')
    g.write(descripcion+' Parisnet: '+parisnet+os.linesep)
    it = 0
    for linea in lista_clases:
        ruta=lista_path[it][0]+linea+'.class\n'
        g.write(ruta.replace('\\','.'))
        it+=1
    g.close()

def svn():
    global lista_clases
    global carpeta_codigo



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

#Leo el fichero con el Nombre de las Clases 
f= open("Clases.txt")
lista_clases=[linea.rstrip('\n') for linea in f]
print(chr(27)+"[1;33m"+"Lista de Clases entradas en el *txt")
print_list(lista_clases)

#Obtengo la lista de los Path dada la lista de clases
lista_path=[obtenerPath(x,origen,'.class') for x in lista_clases]
print("Las Clases entradas en el *txt se encuentran en:")
print_list(lista_path)

#Obtengo la lista de Path de las Clases en el Workspace
lista_workspace=[obtenerPath(x,carpeta_codigo,'.java') for x in lista_clases]
print("Las Clases entradas en el *txt se encuentran en:")
print_list(lista_workspace)

#Creo la Estructura de Carpetas
crearCarpeta(lista_path)
copiaClases(lista_clases)
crearZip()
crearTxtDetalles()
