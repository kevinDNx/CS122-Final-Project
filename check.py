import sys
import requests
import os

def __check_internet__():
    try:
        # Try to send a request to a reliable server
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return True
    except requests.RequestException:
        return False

def __check_dependencies__():
    required_modules = ["requests", "geocoder"]

    missing_modules = []

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        print(f"Missing modules: {', '.join(missing_modules)}")
        install_command = f"pip install {' '.join(missing_modules)}"
        
        try:
            print(f"Installing missing modules using: {install_command}")
            os.system(install_command)
        except Exception as e:
            print(f"Failed to install missing modules: {e}")
            return False

        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                print(f"Failed to install {module}.")
                return False

    return True


def run_check():  
    if (__check_internet__() and __check_dependencies__()):
        print("All checks passed. Running the main part of the script.")
        return True
    return False
