# REGISTROS DE LO QUE SE HACE PARA LA TESIS
## Version V02 - 24/09/23

## Version de RASA
Utilizo esta versión de rasa:  rasa 3.6.9 
python 3.10 en opensuse compatible con la versión de rasa.

 ## Ambiente
 python3.10 -m venv ./venv
 source ./venv/bin/activate

 Si se quiere purgar los paquetes instalos: pip cache purge

 Instalar rasa: pip install rasa


## Github

Para esta versión el proyecto está en repositorio de github:

https://github.com/JPCet30/tesis


## Ejecución

```shell
rasa shell

```

## Librería para moodle

https://github.com/hexatester/moodlepy



## Apuntes anteriores a 24/09/23 son de la versión 01

Para hacer pruebas públicas: https://ngrok.com/

Para utilizar NGROK tenemos que correr primero ngrok y obtener la url para conectar a telegram bot:

En: /home/juan/Documentos/ASTIAN/DOCUMENTOS/UTN/tesis/ngrok
./ngrok http 5005

obtenemos la URL y la cambiamos en 
/home/juan/Documentos/ASTIAN/DOCUMENTOS/UTN/tesis/asistente/v00/credentials.yml

Luego ejecutamos:

rasa run

rasa run action

### CREACIÓN ASISTENTE CON RASA

- Con esto creo el ambiente en python

python3 -m venv ./venv

source ./venv/bin/activate

/usr/bin/python3 /home/juan/Documentos/tesis/asistente/actions.py

ESTOY USANDO  ASTIAN

(viejo) /home/juan/Nextcloud/Documents/UTN/tesis/asistente

/home/juan/Nextcloud/Documents/UTN/tesis/asistente/v00

source ./venv/bin/activate

rasa test

rasa train // para entrenamiento

rasa shell

Para que funcionen los actions se debe abrir el servidor rasa actions en otra consola:

rasa run actions

## GIT DEL ASISTENTE

Estoy usando bitbucker. El REPO es: https://JPatagonico@bitbucket.org/JPatagonico/asistente.git
Está dentro del proyecto TESISUTN y el nombre del repo es asistente.

Ruta loca: /home/juan/Documentos/ASTIAN/DOCUMENTOS/UTN/tesis/asistente/v01/asistente

se excluyeron de git los archivos tar.gz

## WEBSERVICE MOODLE EN ENSEÑAD!

usuario webservice

clave oM893Ku

token cc38090a1aec58b1e41d3c1824e646a7

USUARIOS MOODLE DE PRUEBA

estudiantes

U estudiante1
C LeroLer0+

URL: https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7

URL: https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=core_user_get_users&moodlewsrestformat=json&courseid=2

REQUEST

- DEVUELVE LISTA DE CURSOS

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=core_course_get_courses&moodlewsrestformat=jsonhttps://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=core_course_get_courses&moodlewsrestformat=json

- DEVUELVE DATOS DE UN CURSO ESPECÍFICO
  
  https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=core_course_get_courses_by_field&field=ids&value=2&moodlewsrestformat=json

- DEVUELVE DATOS DE LOS CURSOS QUE UN USUARIO ESTÁ INSCRIPTO, TENER EN CUENTA EL ID DEL USUARIO

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=core_enrol_get_users_courses&userid=3&moodlewsrestformat=json

## LIB EN PYTHON PARA MOODLE

[moodlepy · PyPI](https://pypi.org/project/moodlepy/)

[GitHub - hexatester/moodlepy: Python client for moodle web service](https://github.com/hexatester/moodlepy)

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=cc38090a1aec58b1e41d3c1824e646a7&wsfunction=report_competency_data_for_report&userid=3&courseid=2&moduleid=16&moodlewsrestformat=json

core_enrol_get_users_courses

core_course_get_courses_by_field&field=ids&value=45

core_enrol_get_users_courses&userid=2

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?username=docente&password=Osp2346147*&wsfunction=core_course_get_courses&moodlewsrestformat=json

https://xn--ensead-zwa.com.ar/lms/login/token.php?username=estudiante1&password=LeroLer0+&service=Moodle_student

CON ESTO SACO EL USER ID POR TOKEN DE USUARIO ESTOY PROBANDO CON EL USUARIO ESTUDIANTE1

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_webservice_get_site_info&moodlewsrestformat=json

GLOSARIO

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=mod_glossary_get_entries_by_search&id=6&query=auto&moodlewsrestformat=json

TRAÍGO LOS CURSOS INSCRIPTOS

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_enrol_get_users_courses&userid=6&moodlewsrestformat=json

TRAIGO LOS ESTADOS DE LOS TRABAJOS POR TOKEN  Y POR CURSO - ID

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=gradereport_user_get_grades_table&userid=6&courseid=2&moodlewsrestformat=json

VER CONTENIDO DE TODO EL CURSO

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_course_get_contents&courseid=2&moodlewsrestformat=json

VER TODOS LOS ÚLTIMOS ACCESOS DE TODOS LOS ESTUDIANTES A LOS DISTINTOS MÓDULOS DE TODOS LOS CURSOS (OJO DEVUELVE MUCHA INFO)

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=block_recentlyaccesseditems_get_recent_items&moodlewsrestformat=json

DEVUELVE LOS EVENTOS DE UN CURSO POR ID DE UN DÍA ESPECÍFICO

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_calendar_get_calendar_day_view&courseid=2&moodlewsrestformat=json&year=2020&day=28&month=12

DEVUELVE LOS EVENTOS DE UN CURSO COURSEID POR MES:

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_calendar_get_calendar_monthly_view&courseid=2&moodlewsrestformat=json&year=2021&month=1

SABER TODAS LOS ESTADOS DE TODOS LOS MÓDULOS DE UN ESTUDIANTE POR CURSO (MUY IMPORTANTE PARA SEGUIMIENTO) [**core_completion_get_activities_completion_status**](https://xn--ensead-zwa.com.ar/lms/admin/webservice/documentation.php# "Clic para expandir o colapsar")

https://xn--ensead-zwa.com.ar/lms/webservice/rest/server.php?wstoken=4431b64009b3deae1dd8ac6d5a214c1a&wsfunction=core_completion_get_activities_completion_status&userid=6&courseid=2&moodlewsrestformat=json

## 

## EJEMPLOS

https://www.analyticsvidhya.com/blog/2019/04/learn-build-chatbot-rasa-nlp-ipl/

https://rasa.com/showcase/moltron/

https://rasa.com/showcase/cbot/

## CONSTRUIR ACTIONS EN RASA

Los siguientes son pasos para realizar actions en Rasa pasando parámetros

1- En nlu.md hay que definir un intent como parámetro de entidad. Por ejemplo:

##intent:search_restaurant

mostrar resto [argentino](hotel)

mostrar resto [chino](hotel)

mostrar resto [italiano](hotel)

2- En domain.yml definir las entities, Por ejemplo:

entities:

- hotel

3- En stories.md definir el intent con su action correspondiente:

## search restorant

* search_restaurant
- action_search_restaurant

4- En actions.py
