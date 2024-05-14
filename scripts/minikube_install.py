#!/usr/bin/env python3

import subprocess
import os

#INSTALL_DIR="/usr/local/bin"
INSTALL_DIR="./bin"
APP_NAME="minikube"
OS_TYPE="linux"
ARCH_TYPE="amd64"
VERSION="latest"

UNI_ERR = "\033[0;31m\u2717\033[0m"
UNI_OUT = "\033[92m\u2714\033[0m"

def download_minikube():
    # TODO: look into subprocess/curl functionality. this fails to error when passed with invalid data
    # TODO: address case where bin dir doesn't exist
     
    cmd = [f"sudo curl --output-dir {INSTALL_DIR} -LO https://storage.googleapis.com/minikube/releases/{VERSION}/{APP_NAME}-{OS_TYPE}-{ARCH_TYPE}"]
    sp = subprocess.run(cmd, shell=True)
    print(cmd)
    if sp.returncode == 0:
        print(f"{UNI_OUT} pulled {APP_NAME}-{OS_TYPE}-{ARCH_TYPE} binary")
        return True, sp.stdout
    else:
        print(f"{UNI_ERR} error pulling binary: {sp.stderr}")
        return False, sp.stderr

# def create_install_dir(directory):
#     try:
#         os.makedirs(directory)
#         print(f"{UNI_OUT} directory created at {directory}")
#         return True, None
    
#     except FileExistsError as err:
#         print(f"directory already exists at {directory} procceeding...")
#         return True, err.strerror
    
#     except OSError as err:
#         print(f"{UNI_ERR} failed creating directory at {directory} error: {err.strerror}")
#         return False, err.strerror
    
def install_minikube():
    print(f"Installing {APP_NAME}...")
    cmd = [f"sudo install {INSTALL_DIR}/{APP_NAME}-{OS_TYPE}-{ARCH_TYPE} {INSTALL_DIR}/{APP_NAME}"]
    sp = subprocess.run(cmd, shell=True)

    if sp.returncode == 0:
        print(f"{UNI_OUT} Installed {APP_NAME} to {INSTALL_DIR}")
        return True, sp.stdout
    else:
        print(f"{UNI_ERR} Failed to install: {sp.stderr}")
        return False, sp.stderr

def check_install():
    print(f"Checking {APP_NAME} installation...")
    cmd = [f"{INSTALL_DIR}/{APP_NAME} version --short"]
    sp = subprocess.run(cmd, shell=True, capture_output=True)
    #TODO:clean output, verify return code
    if sp.returncode == 0:
        app_version = sp.stdout.decode()
        print(f"{UNI_OUT} {APP_NAME} version: {app_version}")
        return sp.stdout
    else:
        err = sp.stderr
        print(f"{UNI_ERR}  {err}")
        return err



if __name__ == "__main__":
    #create_install_dir(f"{INSTALL_DIR}/{APP_NAME}")
    #print(download_minikube())
    install_minikube()
    check_install()

#check if minikube is up to date/latest version
# specify version?

    #install/update to latest version/specified
    # checkplatform?