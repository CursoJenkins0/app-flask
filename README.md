# Aplicación Web simple

Este es una simple aplicación web usando [Python Flask](http://flask.pocoo.org/) y [MySQL](https://www.mysql.com/) database. 
Esto se utiliza en la demostración del desarrollo de los Playbooks en Ansible.
  
  A continuación se muestran los pasos necesarios para que esto funcione en un sistema base Linux.
  
  - instalar todas las dependecias requeridas
  - Instalar y configurar un servidor web
  - Comenzar el servidor web
   
## 1. Instalar todas las dependecias requeridas
  
  Python y sus dependecias

    apt-get install -y python3 python-setuptools python-dev build-essential python-pip python-mysqldb

   
## 2. Instalar y configurar el servidor web

Instalar las dependecias de Python Flask

    pip install flask
    pip install flask-mysql

- Copiar app.py o descargarlo desde su repositorio.
- Configurar las credenciales de la base de datos y sus parametros.

## 3. Comenzar el servidor web

    FLASK_APP=app.py flask run --host=0.0.0.0
    
## 4. Testeo

Abrir en tu buscador de preferencia la URL

    http://<IP>:5000                            => Welcome
    http://<IP>:5000/how%20are%20you            => I am good, how about you?
