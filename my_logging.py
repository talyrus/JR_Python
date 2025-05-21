import logging
logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f'деление а={a} на b={b}')
    if b == 0:
        logging.error("Деление на ноль")
        return None

    return a/b

result = divide(2, 0)
print(result)
