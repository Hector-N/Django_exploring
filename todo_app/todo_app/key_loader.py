import os

from django.core.exceptions import ImproperlyConfigured


# get security key from usb-stick
with open('/media/osito/JINNLIVEUSB/key/SECRET_KEY', 'r') as fh:
    secret_key = fh.read().strip()

# assign new environment variable
os.environ['SECRET_KEY'] = secret_key

# get key from environment
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(f"Environment variable {var_name} not found.")
