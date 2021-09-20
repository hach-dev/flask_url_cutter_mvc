import logging
import random
import string
from urllib.parse import urlsplit, urlunsplit, urlparse


def generate_random_name(size=5):
    return ''.join(random.sample(string.ascii_lowercase, size))


def url_validator(value):
    parsed_url = list(urlsplit(value))
    if parsed_url[0] and parsed_url[0] in ('http', 'https'):
        url = value
    elif not parsed_url[0] and not parsed_url[1]:
        url = f'https://{urlunsplit(parsed_url)}'
    else:
        url = urlunsplit(parsed_url)

    validator = urlparse(url)

    return url, all([validator.scheme, validator.netloc])
