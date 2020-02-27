import subprocess
import requests


# Define constants
GREEN_PORT = "8081"
BLUE_PORT = "8082"


# Define methods
def create_network():
    subprocess.call("docker network create --driver bridge isolated_network", shell=True)

def build_python_img():
    subprocess.call("docker build . -t python_img", shell=True)

def run_python_green_container():
    subprocess.call("docker run -p 8081:8080 --network=isolated_network --name python_green -d python_img", shell=True)

def run_python_blue_container():
    subprocess.call("docker run -p 8082:8080 --network=isolated_network --name python_blue -d python_img", shell=True)

def stop_python_blue_container():
    subprocess.call("docker stop python_blue", shell=True)

def stop_python_green_container():
    subprocess.call("docker stop python_green", shell=True)

def remove_python_blue_container():
    subprocess.call("docker rm python_blue", shell=True)

def remove_python_green_container():
    subprocess.call("docker rm python_green", shell=True)

def check_container_is_live(port: str):
    try:
        result = requests.get("http://127.0.0.1:" + port)
        if result.status_code == 200:
            return True
        else:
            return False
    except:
        return False
