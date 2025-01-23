from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

STATIC_URL = 'static/'
ROOT_URLCONF = 'faucet_project.urls'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 0))

# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(',')

# Application definition
INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'faucet_app',

]

# Ethereum Settings
ETHEREUM_NODE_URL =  os.environ.get('ETHEREUM_NODE_URL')
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
FAUCET_AMOUNT = float(os.environ.get('FAUCET_AMOUNT', 0.0001))
RATE_LIMIT_MINUTES = int(os.environ.get('RATE_LIMIT_MINUTES', 1))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
