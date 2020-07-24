import os


class Config(object):
    BASIC_AUTH_USERNAME = os.environ.get('BAUTH_USER') or 'Raavana'
    BASIC_AUTH_PASSWORD = os.environ.get('BAUTH_PASS') or 'guessme'
    BASIC_AUTH_FORCE = True
