import click
import requests
from time import sleep

def check_for_update(key, current):
    key = str(key)
    current = str(current)
    key = requests.get('http://127.0.0.1:3000/get/{}'.format(key))
    key = str(key.content)
    key = key.split('\'')[1]
    current = requests.get('http://127.0.0.1:3000/get/{}'.format(current))
    current = str(current.content)
    current = current.split('\'')[1]
    if current == key:
        return False
    else:
        return True

@click.group()
def cli():
    '''
    CLI tool for using a key value store.
    '''
    pass

@cli.command()
@click.argument('key')
def get(key):
    """ Fetches the argument key value pair """
    key = str(key)
    r = requests.get('http://127.0.0.1:3000/get/{}'.format(key))
    r = str(r.content)
    r = r.split('\'')[1]
    if not r:
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print("\n\nSuccessfully fetched key: " + key + " having value: " + str(r) + "\n\n")

@cli.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """ Sets the argument key value pair """
    key = str(key)
    value = str(value)
    r = requests.get('http://127.0.0.1:3000/set/{}:{}'.format(key,value))
    r = str(r.content)
    r = r.split('\'')[1]
    print("\n\nSuccessfully set key: " + key + " with value: " + str(r) + "\n\n")

@cli.command()
@click.argument('key')
def watch(key):
    """ Watches the argument key """
    key = str(key)
    current = key
    current_val = requests.get('http://127.0.0.1:3000/get/{}'.format(current))
    current_val = str(current_val.content)
    if not current_val:
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        current_val = current_val.split('\'')[1]
        print("Watching key " + key + " for any changes in value")
        while(True):
            is_updated = check_for_update(key, current)
            if is_updated:
                new_val = requests.get('http://127.0.0.1:3000/get/{}'.format(current))
                new_val = str(new_val.content)
                new_val = new_val.split('\'')[1]
                print("New value of " + str(current) + ": " + str(new_val))
            continue

