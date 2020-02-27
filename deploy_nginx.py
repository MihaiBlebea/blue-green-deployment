import subprocess


NGINX_PORT = "8089"
NGINX_BLUE_PORT = "8091"
NGINX_GREEN_PORT = "8092"


def build_nginx_img():
    subprocess.call("docker build ./nginx -t nginx_img", shell=True)

def run_nginx_container():
    subprocess.call("docker run -p 8089:8089 -p 8091:8091 -p 8092:8092 --network=isolated_network --name nginx_container -d nginx_img", shell=True)

def stop_nginx_container():
    subprocess.call("docker stop nginx_container", shell=True)

def remove_nginx_container():
    subprocess.call("docker rm nginx_container", shell=True)

def get_conf_file_name(environment: str):
    filen_name = None
    if environment == "BLUE":
        return "python_blue.conf"
    
    if environment == "GREEN":
        return "python_green.conf"

    return None

def symlink(environment: str):
    # validate envirnonment
    file_name = get_conf_file_name(environment)

    if file_name == None:
        raise Exception("Specify a valid environment: BLUE or GREEN")
    
    subprocess.call("docker exec nginx_container ln -s /etc/nginx/sites-available/" + file_name + " /etc/nginx/sites-enabled/" + file_name, shell=True)

def unlink(environment: str):
    # validate envirnonment
    file_name = get_conf_file_name(environment)

    if file_name == None:
        raise Exception("Specify a valid environment: BLUE or GREEN")

    subprocess.call("docker exec nginx_container rm /etc/nginx/sites-enabled/" + file_name, shell=True)

def restart_nginx_service():
    subprocess.call("docker exec nginx_container nginx -s reload", shell=True)