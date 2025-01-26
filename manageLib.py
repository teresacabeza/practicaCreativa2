import logging, subprocess, os
from subprocess import call

GRUP_NUM = 16 # Variable de entorno con el número de grupo. No se si la tengo que definir aquí, en el script principal o en un json aparte.
GRUP_NOM = 'g16'

log = logging.getLogger('manage-p2.py')


# 1. DESPLIEGUE DE LA APLICACIÓN EN MÁQUINA VIRTUAL PESADA
def mv_pesada (puerto):
  log.debug("mv_pesada ")
  subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
  subprocess.run(['find', './', '-type', 'f', '-exec', 'sed', '-i', f's/Simple Bookstore App/GRUPO: {GRUP_NUM}/g', '{}', '+'])
  os.chdir('practica_creativa2/bookinfo/src/productpage')
  subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
  subprocess.call(['python3', 'productpage_monolith.py', f'{puerto}'])

# 2. DESPLIEGUE DE LA APLICACIÓN MONOLÍTICA USANDO DOCKER
## 2.1. Despliegue de la aplicación mediante Docker
def mv_docker ():
  log.debug("mv_docker ")

  subprocess.call(['sudo', 'docker', 'build', '-t', f'product-page/{GRUP_NOM}', '.'])
  subprocess.call(['sudo', 'docker', 'run', '--name', f'product-page-{GRUP_NOM}', '-p', '5080:5080', '-e', f'GROUP_NUM={GRUP_NUM}', '-d', f'product-page/{GRUP_NOM}'])

## 2.2. Eliminar todas las imágenes y contenedores Docker
def docker_destroy():
  subprocess.call(['sudo docker stop $(sudo docker ps -aq)'], shell=True)
  subprocess.call(['sudo docker rm $(sudo docker ps -aq)'], shell=True)
  subprocess.call(['sudo docker rmi --force $(sudo docker images -q)'], shell=True)


# 3. DESPLIEGUE DE LA APLICACIÓN USANDO DOCKER-COMPOSE
 def mv_docker_compose ():

call(['sudo', 'apt-get', 'install', '-y', 'docker.io'])
call(['sudo', 'apt-get', 'install', '-y', 'docker-compose'])

#Instalaciones en la máquina virtual
call(['sudo', 'apt-get', 'upgrate'])
call(['sudo', 'apt-get', 'install', '-y', 'python3-pip']) 
call(['sudo', 'apt-get', 'install', '-y','git'])
call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
call(['sudo', 'apt-get', 'update'])


#Ejecutar el comando que dice el enunciado en la ruta src/reviews:				
os.chdir('practica_creativa2/bookinfo/src/reviews')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
os.chdir(os.path.expanduser("~"))
os.chdir('practicaCreativa2/apartado3')
#print("Directorio actual")
#subprocess.run(['pwd'])
#print("Archivos en el directorio actual")
#subprocess.run(['ls', '-l'])


#Situarnos en la carpeta donde se encuentra docker-compose.yaml e iniciar los servicios definidos en ese archivo
#os.chdir('practica_creativa2/bookinfo/src')
call(['sudo', 'docker-compose', 'build'])
call(['sudo', 'docker-compose', 'up', '-d'])
  
#   # Clonar repositorio de la app
#   # subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git', './bloque3'])
#   subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
#   subprocess.call(['sudo', 'apt', 'install', '-y', 'docker-compose'])
  
#   os.chdir('/home/rrjorge8/PraCreativa2/bloque3/bookinfo/src/reviews')
#   current_dir = os.getcwd()
#   subprocess.call(['sudo', 'docker', 'run', '--rm', '-u', 'root', '-v', f'{current_dir}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
#   # subprocess.call(['sudo', 'docker', 'run', '--rm', '-u', 'root', '-v', '"$(pwd)":/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
  
#   # Cambiar al directorio raíz
#   os.chdir('/home/rrjorge8/PraCreativa2/bloque3')
#   # Crear el contenido del fichero docker-compose.yaml
#   log.debug("CONSTRUIR DOCKER_COMPOSE")
#   contenido_docker_compose = f"""
#       version: '3.3'
#       services:
#         productpage:
#           build:
#             context: . 
#             dockerfile: Dockerfile
#           image: "product-page/{GRUP_NOM}:latest"
#           container_name: product-page-{GRUP_NOM}
#           ports:
#             - '9080:9080'
#           environment:
#             - GROUP_NUMBER=16
#           volumes:
#             - productpage-vol:/home/rrjorge8/PraCreativa2/volumes/productpage
#         details:
#           build:
#             context: .
#             dockerfile: Dockerfile
#           image: "details/{GRUP_NOM}:latest"
#           container_name: details-{GRUP_NOM}
#           ports:
#             - '9080'
#           environment:
#             - SERVICE_VERSION=v1
#             - ENABLE_EXTERNAL_BOOK_SERVICE=true
#           volumes:
#             - details-vol:/home/rrjorge8/PraCreativa2/volumes/details
#         reviews:
#           build:
#             context: ./bookinfo/src/reviews/reviews-wlpcfg
#           image: "reviews/{GRUP_NOM}:latest"
#           container_name: reviews-{GRUP_NOM}
#           ports:
#             - '9080'
#           environment:
#             - SERVICE_VERSION=v1
#             - ENABLE_RATINGS=true
#             - STAR_COLOR=red
#           volumes:
#             - reviews-vol:/home/rrjorge8/PraCreativa2/volumes/reviews
#         ratings:
#           build:
#             context: .
#             dockerfile: Dockerfile
#           image: "ratings/{GRUP_NOM}:latest"
#           container_name: ratings-{GRUP_NOM}
#           ports:
#             - '9080'
#           environment:
#             - SERVICE_VERSION=v1
#           volumes:
#             - ratings-vol:/home/rrjorge8/PraCreativa2/volumes/ratings
#       volumes:
#         productpage-vol:
#         details-vol:
#         reviews-vol:
#         ratings-vol:
#       """
#   # Escribir el contenido en el fichero docker-compose.yaml
#   with open('docker-compose.yaml', 'w') as file:
#     file.write(contenido_docker_compose)
  
#   # Version 1 --------------------------------------------------------------------------------------------------------------------
#   # # Crear la imagen de ProductPage
#   # log.debug("CONSTRUIR PRODUCT_PAGE")
#   # subprocess.call(['sudo', 'docker', 'build', '-t', f'product-page/{GRUP_NOM}:latest', './Productpage'])
#   # # subprocess.call(['sudo', 'docker', 'build', '-t', f'product-page/{GRUP_NOM}', './ProductPage'])
#   # # subprocess.call(['sudo', 'docker', 'run', '--name', f'product-page-{GRUP_NOM}', '-p', '9080', '-d', '-it', f'product-page/{GRUP_NOM}:latest'])
#   # subprocess.call(['sudo', 'docker', 'run', '--name', f'product-page-{GRUP_NOM}', '-p', '9080:9080', '-e', f'GROUP_NUM={GRUP_NUM}', '-d', f'product-page/{GRUP_NOM}:latest'])

#   # # Crear la imagen de Details
#   # log.debug("CONSTRUIR DETAILS")
#   # subprocess.call(['sudo', 'docker', 'build', '-t', f'details/{GRUP_NOM}:latest', './Details'])
#   # # subprocess.call(['sudo', 'docker', 'run', '--name', f'details-{GRUP_NOM}', '-p', '9080', '-d', '-it', f'details/{GRUP_NOM}:latest'])
#   # subprocess.call(['sudo', 'docker', 'run', '--name', f'details-{GRUP_NOM}', '-p', '9080:9080', '-e', f'GROUP_NUM={GRUP_NUM}', '-d', f'details/{GRUP_NOM}:latest'])

#   # # Crear la imagen de Ratings
#   # log.debug("CONSTRUIR RATINGS")
#   # subprocess.call(['sudo', 'docker', 'build', '-t', f'ratings/{GRUP_NOM}:latest', './Ratings'])
#   # # subprocess.call(['sudo', 'docker', 'run', '--name', f'ratings-{GRUP_NOM}', '-p', '9080', '-d', '-it', f'ratings/{GRUP_NOM}:latest'])
#   # subprocess.call(['sudo', 'docker', 'run', '--name', f'ratings-{GRUP_NOM}', '-p', '9080:9080', '-e', f'GROUP_NUM={GRUP_NUM}', '-d', f'ratings/{GRUP_NOM}:latest'])

#   # # Crear la imagen de Reviews
#   # log.debug("CONSTRUIR REVIEWS")
#   # os.chdir('practica_creativa2/bookinfo/src/reviews')
#   # subprocess.call(['sudo', 'docker', 'run', '--rm', '-u', 'root', '-v', '/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
#   # subprocess.call(['sudo', 'docker', 'build', '-t', f'reviews/{GRUP_NOM}:latest', './reviews-wlpcfg']) 
#   # # subprocess.call(['sudo', 'docker', 'run', '--name', f'reviews-{GRUP_NOM}', '-p', '9080', '-d', '-it', f'reviews/{GRUP_NOM}:latest'])
#   # subprocess.call(['sudo', 'docker', 'run', '--name', f'reviews-{GRUP_NOM}', '-p', '9080:9080', '-e', f'GROUP_NUM={GRUP_NUM}', '-d', f'reviews/{GRUP_NOM}:latest'])
# # ------------------------------------------------------------------------------------------------------------------------------

  
#   os.chdir('/home/rrjorge8/PraCreativa2/bloque3')
#   subprocess.call(['sudo', 'docker-compose', '-f', 'docker-compose.yaml', 'build'])
#   subprocess.call(['sudo', 'docker-compose', '-f', 'docker-compose.yaml', 'up'])