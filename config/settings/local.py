from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='^92l&5_l2f-ik5xlav!7*cat904fro-lmdd@0kgz@c*nxua3@p')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)