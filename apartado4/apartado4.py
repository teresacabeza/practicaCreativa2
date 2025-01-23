import os

def iniciar_minikube():
    """
    Inicia Minikube con Docker como controlador.
    """
    print("Iniciando Minikube...")
    os.system('minikube start --driver=docker --disk-size=20g')

def aplicar_archivos_yaml():
    """
    Aplica los archivos YAML necesarios para configurar los servicios y despliegues.
    """
    print("Aplicando archivos YAML...")
    yaml_files = [
        'productpage.yaml',
        'details.yaml',
        'ratings.yaml',
        'reviews-service.yaml',
        'reviews-v3-deployment.yaml'
    ]
    
    for yaml_file in yaml_files:
        print(f"Aplicando {yaml_file}...")
        os.system(f'kubectl apply -f {yaml_file}')

def verificar_pods():
    """
    Verifica el estado de los pods.
    """
    print("Verificando el estado de los pods...")
    os.system('kubectl get pods')

def verificar_servicios():
    """
    Verifica el estado de los servicios.
    """
    print("Verificando el estado de los servicios...")
    os.system('kubectl get services')

def exponer_servicio(service_name):
    """
    Expone un servicio específico usando Minikube.
    """
    print(f"Exponiendo el servicio {service_name}...")
    os.system(f'minikube service {service_name}')

def ejecutar():
    """
    Función principal que ejecuta todos los pasos necesarios.
    """
    try:
        # Paso 1: Iniciar Minikube
        iniciar_minikube()

        # Paso 2: Aplicar los archivos YAML
        aplicar_archivos_yaml()

        # Paso 3: Verificar estado de los pods y servicios
        verificar_pods()
        verificar_servicios()

        # Paso 4: Exponer el servicio principal (productpage)
        exponer_servicio('productpage')

        print("Despliegue completado con éxito.")

    except Exception as e:
        print(f"Error durante el despliegue: {e}")

if __name__ == "__main__":
    ejecutar()
