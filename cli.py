import click
import requests
from time import sleep
import pyfiglet

result = pyfiglet.figlet_format('-- Store --')
print(result)

def get_key(key):
    r = requests.get('http://127.0.0.1:3000/get/{}'.format(key))
    r = str(r.content)
    r = r.split('\'')[1]
    return r

def get_key_value(key, value):
    r = requests.get('http://127.0.0.1:3000/set/{}:{}'.format(key, value))
    r = str(r.content)
    r = r.split('\'')[1]
    return r

def check_for_update(key, current):
    key = get_key(str(key))
    current = get_key(str(current))
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
    r = get_key(key)
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
    r = get_key_value(key, value)
    print("\n\nSuccessfully set key: " + key + " with value: " + str(r) + "\n\n")

@cli.command()
@click.argument('key')
def watch(key):
    """ Watches the argument key """
    key = str(key)
    current = key
    current_val = get_key(current)
    if not current_val:
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print("Watching key " + key + " for any changes in value")
        while(True):
            is_updated = check_for_update(key, current)
            if is_updated:
                new_val = get_key(current)
                print("New value of " + str(current) + ": " + str(new_val))
            continue
