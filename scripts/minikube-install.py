#!/usr/bin/env python3

import subprocess
import os

INSTALL_DIR="/usr/local/bin"
APP_NAME="minikube"
OS_TYPE="linux"
ARCH_TYPE="amd64"

UNI_ERR = "\033[0;31m\u2717\033[0m"
UNI_OUT = "\033[92m\u2714\033[0m"

def download_minikube():
    # TODO: look into subprocess/curl functionality. this fails to error when passed with invalid data
    # TODO: look into perms for dir creation
    cmd = [f"curl --create-dirs --output-dir {INSTALL_DIR}/{APP_NAME} -LO https://storage.googleapis.com/minikube/releases/latest/{APP_NAME}-{OS_TYPE}-{ARCH_TYPE}"]
    sp = subprocess.run(cmd, shell=True)

    if sp.returncode == 0:
        print(f"{UNI_OUT} pulled {APP_NAME}-{OS_TYPE}-{ARCH_TYPE} binary")
    else:
        print(f"{UNI_ERR} error pulling binary: {sp.stderr}")
        return sp.stderr

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

    #TODO:Turn binary to executable, move to INSTALL_DIR, verify directory exists, create if not
    #TODO:configure install/curl to specify version/platform
    #print(sp.stderr)
    pass

def check_install():
    print(f"Checking {APP_NAME} installation...")
    cmd = ["minikube version --short"]
    sp = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    #TODO:clean output, verify return code
    if sp.returncode == 0:
        app_version = sp.stdout.strip()
        print(f"{UNI_OUT}  {APP_NAME} verison: {app_version}")
        return sp.stdout.strip()
    else:
        err = sp.stderr.strip()
        print(f"{UNI_ERR}  {err}")
        return err



if __name__ == "__main__":
    #create_install_dir(f"{INSTALL_DIR}/{APP_NAME}")
    download_minikube()
    #install_minikube()
    #check_install()

#check if minikube is up to date/latest version
# specify version?

    #install/update to latest version/specified
    # checkplatform?