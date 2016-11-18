# Test SensorTag CC2650
Test Data Sensor SimpleLink CC2650 SensorTag

### Requerimientos
##### bluepy
Interface en Python para dispositivos BLE (Bluetooth Low Energy) sobre Linux.
[Ver información de la librería](http://ianharvey.github.io/bluepy-doc/)
[Proyecto Ian Harvey](https://github.com/IanHarvey/bluepy.git)
[Más documentación](http://www.elinux.org/RPi_Bluetooth_LE)

##### Python 2.7 (Recomendada), 3.4 

##### Sensor SimpleLink SensorTag CC2650
[Información del Sensor TI](http://www.ti.com/sensortag).

Probad el Tag
-------------
Desde vuestro móvil o tablet bajaros la app:
https://play.google.com/store/apps/details?id=com.ti.ble.sensortag&hl=es

<img src="https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/img-slst.png" />
<img src="https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/img-connect.png" height="558px" width="620px" />
<img src="https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/img-data-s.png" height="558px" width="620px" />


Quedaros con la MAC del sensor, cuando os conectéis por Bluetooth la podreís ver (Tenerla siempre a mano).

Lectura del sensor
------------------
Haced lo siguiente:

    $ git clone https://github.com/mfcardenas/test-sl-stagcc2650.git
    $ cd  test-sl-stagcc2650/py
    $ python get_acceleration.py 00:00:00:00:00

Esto en principio os debería recuperar datos de vuestro sensor.
 
En los directorios /py y /sh tenéis los script que debéis ejecutar para recuperar datos del tag, solo necesitáis indicar la MAC del mismo. 
Estos script requieren de ciertas "librerías" que se deberían generar en vuestro ordenador pero tal y como está este repositorio no debería ser necesario hacer esa parte porque ya los he generado y les subido aquí.

Si tuvieráis que generar las librerías, os recomiento seguir los pasos que se indican en el apartado siguiente "Generación de librerías".

#### Generación de librerías
-----------------------

Para generar dichas librerías seguid estos pasos:

##### Instalación bluepy
------------------
Se utiliza la librería bluepy para "compilar" o "construir" los script o librerías necesarias que permitirán comunicar nuestro código python con el dispositivo BLE, en este caso el SensorTag.

Bien se puede usar la librería bluepy por defecto, la forma de obtenerla es con "pip".
- Instale "pip" si no lo tiene en su ordenador y la librería de bluepy. 

    $ sudo apt-get install python-pip libglib2.0-dev
    $ sudo pip install bluepy

O utilizar la instalación del propio proyecto del autor:
- instalando localmente los fuentes necesarios para dicha librería.

Si no teneis git:  
    $ sudo apt-get install git

Si no teneis estas dependencias (suelen ser necesarias):
    $ sudo apt-get install build-essential libglib2.0-dev

Clonad el proyecto:
    $ git clone https://github.com/IanHarvey/bluepy.git
    $ cd bluepy
    $ python setup.py build
    $ python setup.py install


##### Creación de script para conectar
--------------------------------------------------
Cuando instales bluepy bien con pip o bien con la misma librerría del autor, debes construir el proyecto con los fuentes para conectar con el sensor (ver la imagen siguiente)

    $ git clone git clone https://github.com/IanHarvey/bluepy.git
    $ cd bluepy/bluepy
    $ make

![Make Project](https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/make-install.bmp)
 
Una vez creado el proyecto con make, ejecute el script "btle.py" que se ha generado pasando como argumento la MAC del sensor.

![Execute btle.py](https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/get-ingo-sensortag.bmp)

Hecho esto volved al apartado "Lectura del sensor".

