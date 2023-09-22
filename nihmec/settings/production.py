from .base import *
import environ
from django.core.management.utils import get_random_secret_key
import dj_database_url

ALLOWED_HOSTS = ["nihmec-production.up.railway.app", "nihmec.com"]
DEBUG = env('DEBUG')
EMAIL_HOST_USER = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')


PAYSTACK_SECRET_KEY = env('PAYSTACK_SECRET_KEY')
try:
    from .local import *
except ImportError:
    pass

