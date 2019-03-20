import click

storage = {1:2, 3:4}

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
    storage[key] = value
    print("\n\nSuccessfully set key: " + key + " with value: " + storage[key] + "\n\n")

@main.command()
@click.argument('key')
def get(key):
    """ Fetches the argument key value pair """
    key = int(key)
    if not key in storage:
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print(storage[key])

@main.command()
@click.argument('key')
def watch(key):
    """ Watches the argument key """
    key = int(key)
    if not key in storage:
        print("\n\nThis key doesn\'t exist.\nSee store --help for more info on setting keys.\n\n" )
    else:
        print("Watching key " + str(key) + " for any changes in value")
        while(True):
            continue
        pass
