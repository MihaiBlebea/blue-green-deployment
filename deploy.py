import sys
import subprocess
import requests
import time

import deploy_nginx as nginx
import deploy_python as py


# Get arguments from the command line
def get_environment_from_argv():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return None

def switch_nginx_environments(old: str, new: str):
    nginx.symlink(new)
    nginx.unlink(old)
    time.sleep(2)
    nginx.restart_nginx_service()

def start_blue():
    py.stop_python_blue_container()
    py.remove_python_blue_container()
    py.build_python_img()
    py.run_python_blue_container()

def stop_blue():
    py.stop_python_blue_container()
    py.remove_python_blue_container()

def start_green():
    py.stop_python_green_container()
    py.remove_python_green_container()
    py.build_python_img()
    py.run_python_green_container()

def stop_green():
    py.stop_python_green_container()
    py.remove_python_green_container()


if __name__ == "__main__":

    # Get arguments from the script
    environment = get_environment_from_argv()
    if environment == None:
        print("No environment defined. I will figure it out myself")
        if py.check_container_is_live(py.BLUE_PORT) == True:
            environment = "GREEN"

        elif py.check_container_is_live(py.GREEN_PORT) == True:
            environment = "BLUE"

        else:
            environment = "GREEN"
            

    # Check if nginx is working
    # If not running, then start the container up
    if py.check_container_is_live(nginx.NGINX_PORT) == False:
        nginx.stop_nginx_container()
        nginx.remove_nginx_container()
        nginx.build_nginx_img()
        nginx.run_nginx_container()
    else:
        print("Nginx container is running")

    py.create_network()

    if environment == "BLUE":
        start_blue()

        time.sleep(2)
        if py.check_container_is_live(py.BLUE_PORT) == True:
            print("BLUE container is working")
            switch_nginx_environments("GREEN", "BLUE")
            stop_green()
        else:
            print("BLUE container is NOT working")


    if environment == "GREEN":
        start_green()

        time.sleep(2)
        if py.check_container_is_live(py.GREEN_PORT) == True:
            print("GREEN container is working")
            switch_nginx_environments("BLUE", "GREEN")
            stop_blue()
        else:
            print("GREEN container is NOT working")

