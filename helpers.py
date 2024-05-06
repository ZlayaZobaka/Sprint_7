import string
import random
from data import MagicConstants


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def random_id():
    return random.randint(MagicConstants.MIN_ID, MagicConstants.MAX_ID)

