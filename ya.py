import yadisk
import os

remote_clients_file = 'test/client_base.csv'
remote_activations_file = 'test/activations.csv'
local_clients_file = 'resources/client_base.csv'
local_activations_file = 'resources/activations.csv'

yadisk_token = os.environ['YADISK_TOKEN']

class DADisk:
    y=yadisk.YaDisk(yadisk_token)

    def load_clients(self):
        if self.y.check_token():
            self.y.download(remote_clients_file,local_clients_file)
        else:
            print('Failed to load clients due to unresolved token')

    def load_activations(self):
        if self.y.check_token():
            self.y.download(remote_activations_file,local_activations_file)
        else:
            print('Failed to load activation due to unresolved token')

    def save_clients(self):
        if self.y.check_token():
            self.y.upload(local_clients_file, remote_clients_file)
        else:
            print('Failed to save clients due to unresolved token')

    def save_activations(self):
        if self.y.check_token():
            self.y.upload(local_activations_file, remote_activations_file)
        else:
            print('Failed to save activations due to unresolved token')
