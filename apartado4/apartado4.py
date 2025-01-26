import os
import sys

def build(version):
    os.system('gcloud container clusters get-credentials clusterk --region europe-southwest1 --project norse-block-448119-j1')
    os.system('kubectl apply -f productpage.yaml')
    os.system('kubectl apply -f ratings.yaml')
    os.system('kubectl apply -f details.yaml')
    os.system('kubectl apply -f reviews-svc.yaml')
    os.system(f'kubectl apply -f reviews-{version}-deployment.yaml')

def delete():
    os.system('kubectl delete --all deployments && kubectl delete --all pods && kubectl delete --all services')

param = sys.argv

if len(param) < 2:
    print("Usage: python3 bloque4.py [build|delete] [version]")
    sys.exit(1)

command = param[1]

if command == "build":
    if len(param) < 3:
        print("Please specify a version (e.g., v1, v2, v3)")
        sys.exit(1)
    version = param[2]
    build(version)
elif command == "delete":
    delete()
else:
    print("Unknown command")
