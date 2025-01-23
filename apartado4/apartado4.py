import os
import subprocess

def ejecutar_comando(comando):
    """Ejecuta un comando en la terminal y muestra el resultado."""
    try:
        print(f"Ejecutando: {comando}")
        resultado = subprocess.run(comando, shell=True, check=True, text=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(e)

# 1. Iniciar Minikube
print("Iniciando Minikube...")
ejecutar_comando("minikube start --driver=docker")

# 2. Configurar Minikube para usar imágenes locales
print("Configurando Minikube para usar imágenes locales...")
ejecutar_comando("eval $(minikube docker-env)")

# 3. Construir las imágenes Docker
imagenes = [
    ("productpage", "Dockerfile", "./productpage"),
    ("details", "Dockerfile", "./details"),
    ("reviews", "Dockerfile", "./reviews"),
    ("ratings", "Dockerfile", "./ratings")
]

for nombre, dockerfile, context in imagenes:
    print(f"Construyendo imagen {nombre}...")
    ejecutar_comando(f"docker build -t jorgerguezz/{nombre}:16 -f {context}/{dockerfile} {context}")

# 4. Aplicar archivos YAML
yamls = [
    "productpage.yaml",
    "details.yaml",
    "ratings.yaml",
    "reviews-service.yaml",
    "reviews-v3-deployment.yaml"  # Cambia según tu versión
]

for yaml in yamls:
    print(f"Aplicando {yaml}...")
    ejecutar_comando(f"kubectl apply -f {yaml}")

# 5. Verificar estado de Pods y Servicios
print("Verificando estado de los Pods...")
ejecutar_comando("kubectl get pods")

print("Verificando estado de los Servicios...")
ejecutar_comando("kubectl get services")

# 6. Exponer servicio principal
print("Exponiendo servicio productpage...")
ejecutar_comando("minikube service productpage --url")

print("¡Todo listo! Verifica tu servicio en la URL expuesta por Minikube.")
