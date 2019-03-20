import click
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def check_for_update(key, current):
    if r.get(current) == r.get(key):
        return False
    else:
        return True

@click.group()
def main():
    '''
    CLI tool for using a key value store.
    '''
    pass

@main.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """ Sets the argument key value pair """
    r.set(key, value)
    print("\n\nSuccessfully set key: " + key + " with value: " + r.get(key) + "\n\n")

@main.command()
@click.argument('key')
def get(key):
    """ Fetches the argument key value pair """
    if not r.get(key):
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print("\n\nSuccessfully fetched key: " + key + " having value: " + r.get(key) + "\n\n")

@main.command()
@click.argument('key')
def watch(key):
    """ Watches the argument key """
    current = key
    if not r.get(current):
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print("Watching key " + key + " for any changes in value")
        while(True):
            is_updated = check_for_update(key, current)
            if is_updated:
                new_val = r.get(current)
                print("New value of " + str(current) + ": " + str(new_val))
            continue