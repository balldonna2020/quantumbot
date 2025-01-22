import os
import winreg
import logging

# Configure logging
logging.basicConfig(filename='quantumbot.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_registry_key(key_path):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            i = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    subkey_path = os.path.join(key_path, subkey_name)
                    clean_registry_key(subkey_path)
                    i += 1
                except OSError:
                    break

            if i == 0:
                try:
                    winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, key_path)
                    logging.info(f"Deleted empty registry key: {key_path}")
                except OSError as e:
                    logging.error(f"Failed to delete key {key_path}: {e}")

    except FileNotFoundError:
        logging.warning(f"Registry key not found: {key_path}")
    except Exception as e:
        logging.error(f"Error accessing key {key_path}: {e}")

def start_deep_clean():
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        # Add any other registry paths that you want to clean
    ]

    for path in registry_paths:
        logging.info(f"Starting clean for registry path: {path}")
        clean_registry_key(path)

if __name__ == "__main__":
    logging.info("QuantumBot Registry Cleaner started.")
    start_deep_clean()
    logging.info("QuantumBot Registry Cleaner finished.")