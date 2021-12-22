import configparser
from os.path import exists
import const

# Configuration file 'config.ini'
config_file_exists = exists(const.CONFIG_FILE_NAME)


def create_config(config):
    if config.sections() != []:
        save_configuration(config)


def delete_configuration():
    return configparser.ConfigParser()


def read_config_file():
    config = configparser.ConfigParser()
    config.read(const.CONFIG_FILE_NAME)
    return config


def set_default_assetto_config(config):
    config["ASSETTOCORSA"] = {
        "name": "Assetto Corsa",
        "path": const.AC_DEFAULT_PATH
    }


def set_default_csp_config(config):
    config["CSP"] = {
        "name": "Custom Shader Patch",
        "metadata_path": const.AC_DEFAULT_PATH + const.CSP_MANIFEST_PATH,
        "version": ""
    }


def set_default_sol_config(config):
    config["SOL"] = {
        "name": "SOL",
        "metadata_path": const.AC_DEFAULT_PATH + const.SOL_MANIFEST_PATH,
        "version": ""
    }


def save_configuration(config):
    try:
        with open(const.CONFIG_FILE_NAME, 'w') as configfile:
            config.write(configfile)
        return True
    except Exception as e:
        print("Could not write configuration file:", e)
        return False
