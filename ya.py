import yadisk
import os

remote_clients_file = 'test/client_base.csv'
remote_activations_file = 'test/activations.csv'
# todo check if we can upload/load to/from yadisk without temp file
local_clients_file = 'resources/client_base.csv'
local_activations_file = 'resources/activations.csv'

yadisk_token = os.environ['YADISK_TOKEN']
global y

def __init__() :
    global y
    y = yadisk.YaDisk(yadisk_token)

    if y.check_token():
        print("Yadisk init is successful")
    else:
        print("ERROR: Failed to init yadisk")

def load_clients():
    y.download(remote_clients_file,local_clients_file)

def load_activations():
    y.download(remote_activations_file,local_activations_file)

def save_clients():
    y.upload(local_clients_file, remote_clients_file)

def save_activations():
    y.upload(local_activations_file, remote_activations_file)