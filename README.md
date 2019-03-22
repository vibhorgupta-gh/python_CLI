## STORE
A CLI tool for managing key-value pairs

Store is a CLI tool built with [Python](https://docs.python.org/3/) for scripting and server and [Redis](https://redis.io/) for data storage used to store, retrieve and watch data stored in the form of key value pairs.

### Installation

- Clone this repository, run
  ```
  git clone https://github.com/VibhorCodecianGupta/python_CLI.git
  ```

- Change directory into project root
  ```
  cd kv/
  ```

- For installing python dependencies, run
  ```
  pip install -r requirements.txt
  ```

- This project can also be run using `virtualenv`,
    ```
    pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install --editable .
    ```

### Setup

 This tool is intended to run as a server/daemon, hence `flask` endpoints are used to call the desired data instead of the CLI tool directly querying `redis`.
 Run the following command to start the server.
   ```
   python3 server.py
   ```

### CLI Usage

Fire up another terminal and you are ready to go! The CLI offers the following commands to play with:


```
store set <key> <value>
```
- This command sets a key value pair in the database with respective values of the arguments.

```
store get <key>
```
- This command retrieves the value of the key passed in the arguments.

```
store watch <key>
```
- This command watched the argument key for any changes. If you use the `store set` command from another terminal on the same key to change its value, the changes will be reflected in this instance of the CLI.


### Testing

- To run tests on CLI functions, run
  ```
  python3 tests/test_cli.py
  ```

- To run tests on server functions, run
  ```
  python3 tests/test_server.py
  ```

- To generate a code coverage reports, run
  ```
  pytest tests/test_cli.py --cov=cli
  pytest tests/test_server.py --cov=server
  ```
### Docker

This project is docker-friendly, and has a `Dockerfile` and a `docker-compose.yml`. To run a docker instance of the application, run
  ```
  docker-compose up
  ```
and continue using the CLI commands as mentioned above.


