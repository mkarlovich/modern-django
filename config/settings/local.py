from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='l#**&*%&-gem2_)pti)u=xbbouddvra_m&%uue3l0so2xumxf2')

DEBUG = env.bool('DJANGO_DEBUG', True)
