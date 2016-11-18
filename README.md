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
[Información del Sensor TI](www.ti.com/sensortag).

Instalación
---------------
Se utiliza la librería bluepy con el contenido que recomienda su autor para generar los fuentes necesarios que permitan comunicar nuestro código python con el dispositivo BLE, en este caso el SensorTag.

Una forma de obtener la librería bluepy es con la instalación de "pip".
Instale "pip" si no lo tiene en su ordenador y las librería que se indica a continuación. 

    $ sudo apt-get install python-pip libglib2.0-dev
    $ sudo pip install bluepy
    
Otra forma, es generando localmente los fuentes necesarios de dicha librería.

    $ sudo apt-get install git
    $ sudo apt-get install build-essential libglib2.0-dev
    $ git clone https://github.com/IanHarvey/bluepy.git
    $ cd bluepy
    $ python setup.py build
    $ python setup.py install
    
Cuando genere los fuentes, vea la imagen siguiente.

![Make Project](https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/make-install.bmp)
 
Copie el directorio generado a este proyecto git, reemplazando en su totalidad el directorio existente con el mismo nombre.
Una vez copiado, ejecute el script btle.py indicando como argumento la MAC del SensorTag.

![Execute btle.py](https://github.com/mfcardenas/test-sl-stagcc2650/blob/master/img/make-install.bmp)

