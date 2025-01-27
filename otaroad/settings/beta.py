from .base import *
from .util import get_secure_data
import socket

SERVER_RELEASE_ADDR = 'otaroad-oracle-cloud.wahoo-in.ts.net'
CONTAINER_INTERNAL_IP = socket.gethostbyname(socket.gethostname())
TAILSCALE_IP = '100.109.210.96'

ALLOWED_HOSTS = ['127.0.0.1', CONTAINER_INTERNAL_IP,
                 SERVER_RELEASE_ADDR, 'beta.otaroad.party',
                 TAILSCALE_IP
                 ]

# Debug Options
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
db_data = get_secure_data('.secure/db-beta.json')

if db_data['default'] == '':
    raise ImproperlyConfigured(
        'Please input db-beta.json in .secure/')

DATABASES = db_data

# Application definition
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# 허용할 Origin 추가
CORS_ALLOWED_ORIGINS = [
    'https://dev.subculture-map-frontend.pages.dev',
    'http://127.0.0.1:3000',
    f'http://{CONTAINER_INTERNAL_IP}:7500',
    'https://beta.otaroad.party',
    f'https://{SERVER_RELEASE_ADDR}:7500',
    'http://127.0.0.1:7500',
    f'https://{CONTAINER_INTERNAL_IP}:7500'

]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 신뢰할 수 있는 ORIGIN 추가
CSRF_TRUSTED_ORIGINS = [
    f'https://{SERVER_RELEASE_ADDR}/v1/shop/',
    'https://beta.otaroad.party',
    f'https://{SERVER_RELEASE_ADDR}/swagger',
    f'https://{SERVER_RELEASE_ADDR}/redoc',
    f'https://{SERVER_RELEASE_ADDR}/otaroad-admin/',
    f'https://{SERVER_RELEASE_ADDR}/django-admin/',
    'http://127.0.0.1:3000',
    f'http://{CONTAINER_INTERNAL_IP}:7500/otaroad-admin/',
    f'http://{CONTAINER_INTERNAL_IP}:7500/django-admin/',
    f'http://{CONTAINER_INTERNAL_IP}/swagger',
    f'http://{CONTAINER_INTERNAL_IP}/redoc',
    'http://127.0.0.1:7500',
    f'http://{TAILSCALE_IP}:7500/otaroad-admin/',
    f'http://{TAILSCALE_IP}:7500/django-admin/',
    f'http://{TAILSCALE_IP}/swagger',
    f'http://{TAILSCALE_IP}/redoc',
]
