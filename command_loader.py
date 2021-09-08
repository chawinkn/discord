import os
from importlib import import_module

def load(client):
    wd = os.getcwd()

    # set up native commands
    folder_path = wd + '/commands'
    error_module = []
    filelist = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    for file in filelist:
        filename = file[:-3]
        print('Loading: ' + filename)
        # import
        command_module = import_module('commands.' + filename)
        command_module.setup(client)