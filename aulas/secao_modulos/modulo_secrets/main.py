"""Secrets gera um número verdadeiramente aleatórios"""
import secrets
import string as s

print(secrets.randbelow(100))
print(secrets.choice([1,2,3,4]))

chars = s.ascii_letters + s.digits + s.punctuation

random_password = ''.join([secrets.choice(chars) for _ in range(0,10)])

print(random_password)