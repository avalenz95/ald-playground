#!/usr/bin/env python3

import subprocess

#check if minikube is installed

INSTALL_DIR="/usr/local/bin"
APP_NAME="minikube"

def install_minikube():
    cmd = ["curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    #TODO:Configure subprocess to pipe directly to stdout/err?
    #TODO:Turn binary to executable, move to INSTALL_DIR, verify directory exists, create if not
    #TODO:configure install/curl to specify version/platform
    print(res.stderr)

def check_install():
    print(f"Checking {APP_NAME} installation...")
    cmd = ['minikube version --short']
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    #TODO:clean output, verify return code
    if res.returncode == 0:
        app_version = res.stdout.strip()
        print(f"\033[92m\u2713 {APP_NAME} verison: {app_version}")
        return res.stdout.strip()
    else:
        err = res.stderr.strip()
        print(f"\u274C {err}")
        return err



if __name__ == "__main__":
    install_minikube()
    #check_install()

#check if minikube is up to date/latest version
# specify version?

    #install/update to latest version/specified
    # checkplatform?