[![Build Status](https://travis-ci.org/ylvaldes/clasesTesting.svg?branch=master)](https://travis-ci.org/ylvaldes/clasesTesting)
[![codecov](https://codecov.io/gh/ylvaldes/clasesTesting/branch/master/graph/badge.svg)](https://codecov.io/gh/ylvaldes/clasesTesting)
[![Coverage Status](https://coveralls.io/repos/github/ylvaldes/clasesTesting/badge.svg)](https://coveralls.io/github/ylvaldes/clasesTesting)
[![Build status](https://ci.appveyor.com/api/projects/status/8npkajpaakxx11sb?svg=true)](https://ci.appveyor.com/project/ylvaldes/clasestesting)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ylvaldes/clasesTesting.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ylvaldes/clasesTesting/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ylvaldes/clasesTesting.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ylvaldes/clasesTesting/context:python)

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=ylvaldes_clasesTesting&metric=alert_status)](https://sonarcloud.io/dashboard?id=ylvaldes_clasesTesting)


1.	Inicialmente debemos configurar en el Scrip estas variables 
#Carpeta Origen de los compilados
origen='D:\gemadesa\IBM\MAXIMO'
#Carpeta Usada para Guardar los Paquetes de Migracion
carpeta_migracion='D:\Migracion'
#Direccion del Codigo
carpeta_codigo='D:\gemadesa\eclipse3.4-java\workspace'

2.	En el archivo clases.txt ponemos el nombre de las clases que integran el paquete sin extensión. 
3.	Al ejecutar el Scrip nos pedirá el número del parisnet y descripción del pasaje (Corto este es para identificar la carpeta)
a.	Se crea la carpeta  YYYYMMDD_#Parisnet_Descripcion
b.	Dentro de la carpeta:
i.	Un txt con los detalles de la actualización (Parsnte, clases actualizada, ruta de las clases)
ii.	La carpeta con las clases compilada y su ruta.
iii.	El zip en el formato solicitado para el pasaje a Testing. 
