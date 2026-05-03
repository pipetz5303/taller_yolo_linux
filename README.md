# Taller YOLO imagenes distribuciones Linux

Desarrollado por Felipe Castellanos Sánchez, codigo 1030576147

1- Creación del entorno virtual. Vamos a VS Code y en new terminal se corre el script:
Virtual env -p Python 3 env

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/01.png)

2- Se activa con la .\env\Scripts\Activate y despues un pip list para confirmar que no estan todas las librerias sino solo las del entorno virtual

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/02.png)

3- Se intalan las librerias
pip install ultralytics opencv-python matplotlib

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/03.png)
![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/04.png)

4- Se crea el archivo para la aplicación

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/05.png)

Se comprueba que esta funcionando

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/06.png)
![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/07.png)

5- Crear el data set para entrenar el modelo.
Utilizaremos roboflow

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/08.png)
![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/09.png)

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/11.png)

6- Se genera también en Colab de Google

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/12.png)

7-Se instala Roboflow

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/13.png)

8- Se confirma que esta cargada la información

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/14.png)

9- Se carga el modelo YOLO

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/15.png)

10- Se entrena

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/16.png)

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/17.png)

11- Se descarga el archivo best.pt que tiene el mejor modelo entrenado.

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/18.png)

12- Se reemplaza el modelo en archvo que teniamos

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/19.png)

Revisamos su funcionamiento

Arch Linux

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/20.png)

Ubuntu

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/21.png)

Parrot OS

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/22.png)

Kali Linux

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/23.png)

Debian

![img](https://github.com/pipetz5303/taller_yolo_linux/blob/main/24.png)


