import random

opening = ["hi", "hello", "morning", "evening", "hey"]
closing = ["bye", "adios", "ok"]

def greet():
    return opening[random.randint(0, 100) % 3]

def close():
    return closing[random.randint(0, 100) % 3]

print greet()
print close()
