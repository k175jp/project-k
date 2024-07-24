import os
from dotenv import dotenv_values

import pathlib

root = pathlib.Path(__file__).parent
env_file = root / '.env'

def create_secret():
    config = dotenv_values(env_file)

    if config is None or config.get('secret') is None:
        with open('.env', 'a') as f:
            f.write(f'secret={os.urandom(24).hex()}')

        print(f"Secret stored at {os.path.abspath('.env')}")

def overwrite_secret():
    config = dotenv_values(env_file)

    with open('.env', 'w') as f:
        for key, value in config.items():
            if key == 'secret':
                value = os.urandom(24).hex()
            f.write(f"{key}={value}")
    print(f"Secret overwrite at {os.path.abspath('.env')}")
