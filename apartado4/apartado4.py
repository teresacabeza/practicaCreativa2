#!usr/bin/python3
import os

#Descarga las imagenes del repositorio Docker Hub
os.system('sudo docker pull jorgerguezz/details:16')
os.system('sudo docker pull jorgerguezz/productpage:16')
os.system('sudo docker pull jorgerguezz/reviews:16')
os.system('sudo docker pull jorgerguezz/ratings:16')

#Configuracion para usar Docker con Kubernetes
os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y ca-certificates curl gnupg lsb-release')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

#Establece el proyecto de Google Cloud Platform y habilita el servicio de Kubernetes Engine en Google Cloud Platform
os.system('sudo gcloud config set project practicaCreativa2')     
os.system('sudo gcloud services enable container.googleapis.com')


# Crea los pods a partir de los archivos de configuracion .yaml (sino funciona añadir --disk-size=20)
os.system('sudo gcloud container clusters create clusterkubernetes --num-nodes=3 --zone=us-central1-a --no-enable-autoscaling') 


os.system('sudo kubectl apply -f productpage.yaml')
os.system('sudo kubectl apply -f details.yaml')
os.system('sudo kubectl apply -f ratings.yaml')
os.system('sudo kubectl apply -f reviews-service.yaml')

# Se puede elegir la version que queramos 
#os.system('sudo kubectl apply -f reviews-v1-deployment.yaml')
#os.system('sudo kubectl apply -f reviews-v2-deployment.yaml')
os.system('sudo kubectl apply -f reviews-v3-deployment.yaml')

# Lanzamos el servicio
os.system('sudo kubectl expose deployment productpage --type=LoadBalancer --port=9080')