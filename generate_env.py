import hvac
import os
import sys

def get_vault_secrets(env):
    client = hvac.Client(url=os.getenv('VAULT_ADDR'), token=os.getenv('VAULT_TOKEN'))
    secrets = client.secrets.kv.v2.read_secret_version(path=f'{env}/config')
    return secrets['data']['data']

def write_env_file(secrets, env):
    with open(f'.env.{env}', 'w') as f:
        for key, value in secrets.items():
            f.write(f'{key}={value}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_env.py <environment>")
        sys.exit(1)

    env = sys.argv[1]
    secrets = get_vault_secrets(env)
    write_env_file(secrets, env)