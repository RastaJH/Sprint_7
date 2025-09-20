import random
import string

def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_unique_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(6)
    return {"login": login, "password": password, "firstName": first_name}