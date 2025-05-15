import random
import string

def generate_random_email(length=8):
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    domain = random.choice(['ya.ru', 'gmail.com', 'hotmail.com'])
    return f"{login}@{domain}"

def generate_random_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))