import pickle
import yaml
import os
import subprocess

def load_model():
    return pickle.load(open("model.pkl", "rb"))

def unsafe_yaml_load(config):
    return yaml.load(config)

def run_command(user_input):
    os.system(user_input)
    subprocess.call(user_input, shell=True)

password = "admin123"
token = "ghp_fakegithubtoken123456789"
