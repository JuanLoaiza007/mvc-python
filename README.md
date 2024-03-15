# Personalización del patrón Modelo Vista Controlador en Python

Este repositorio está destinado a alojar una implementación personalizada del patrón Modelo Vista Controlador (MVC) en Python.

La idea es separar la lógica de negocio de la interfaz de usuario, permitiendo así la creación de interfaces directas o indirectas con programas externos como Qt Designer/Qt Creator. Para este ejemplo, se utiliza Qt 5 Designer para generar imágenes ".ui" que luego se transforman a archivos ".py" utilizando el miniprograma "_uitopy.py".

## Contenido

- [Instrucciones](#instrucciones)
- [Uso](#uso)

## Instrucciones

> [!IMPORTANT]
> Debe tener Python instalado en su sistema y tener instalado el modulo PyQt5

Instale el modulo PyQt5:

```
pip install PyQt5
```

Clone este repositorio desde la terminal:


```
git clone https://github.com/JuanLoaiza007/mvc-python.git
```


> **Opcional**
>
> Se recomienda encarecidamente utilizar el módulo **virtualenv** de Python para tener un pequeño sandbox, para instalarlo use el comando:
> ```
> pip install virtualenv
> ```
> A continuación, cree un entorno virtual y actívelo (debe buscar cómo activarlo según su sistema operativo y su IDE), este es el comando para crearlo:
> ```
> virtualenv venv
> ```
> Una vez creado y activado, asegúrese de que al abrir una terminal en la ubicación del proyecto aparezca el prefijo (venv); de esta forma, ya puede instalar los otros módulos sin afectar las versiones que tenga en su ordenador.


Use el siguiente comando para instalar los requisitos:

```
pip install -r requirements.txt
```
Ya estamos listos para empezar a jugar!

## Uso

Se encontrará con una estructura de carpetas igual o similar a esta:

[![imagen.png](https://i.postimg.cc/L4LjyDCB/imagen.png)](https://postimg.cc/bdYGrxjs)

A continuación, explicaré las partes más importantes:

### controllers/

Esta carpeta alberga los controladores del patrón Modelo Vista Controlador (MVC), los controladores actúan como intermediarios entre las vistas y los modelos y se encargan de manejar las interacciones del usuario como clics de botones o entradas de teclado. Los controladores de este ejemplo tienen implementado el cambio de vistas en la misma ventana, es decir, la ventana no se cierra y se vuelve a abrir para mostrar una vista distinta si no que es capaz de repintar la ventana ;)

### models/

La carpeta de modelos contiene la lógica de datos y de negocio de la aplicación, aquí se definen las estructuras de datos y se implementan las operaciones que manipulan estos datos. Los modelos representan la información y el comportamiento del dominio de la aplicación además de almacenar y gestionar los datos, los modelos también pueden realizar cálculos y aplicar reglas de negocio.

### views/

En la carpeta de vistas se encuentran las interfaces de usuario de la aplicación, esta carpeta fue la causante de que yo quisiese crear una version del mvc para python. Resulta que en español no se encuentra mucha información para generar interfaces en Python usando programas si no a punta de código, esto es genial pero no es muy rápido y tengo varios proyectos de la U pa este semestre entonces no aguanta gastar tanto tiempo posicionando cosas.

Como habia mencionado, la ventaja de un mvc es que se pueden crear las interfaces con programas externos, las vistas seran independientes pero a la vez será más ágil implementarlas para que funcionen bien con el código, en esta carpeta hay un archivo muy especial:
- **_uitopy.py:** Es un pequeño programa que hace uso del programa **pyuic5** integrado en **PyQt5**, sirve para transformar las interfaces de Qt Designer (.ui) en interfaces para python (.py) y hasta el momento ha sido genial. El miniprograma _uitopy.py tomará todos los archivos que esten en el mismo nivel de jerarquia que él y si tienen extension .ui los transformará a .py, cada vez que actualice el .ui debe ejecutar el miniprograma o no notará los cambios.

### main.py

En mi main.py se instancia el controlador inicial lo cual es un punto crucial en el funcionamiento de la aplicación, este archivo actúa como el punto de entrada de la aplicación. 

## ¿Que sigue ahora?

Ahora ya puedes jugar con este loco mvc que hice y seguramente crear algo mejor, diviertete y si tienes alguna sugerencia, idea, encontraste un problema o quieres hacer un comentario no dudes en publicarlo ;)