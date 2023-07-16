import random
import string

# Символы, иероглифы и цифры, которые будут использоваться для генерации пароля
symbols = string.ascii_letters + string.digits + '！＠＃＄％＾＆＊（）＿＋－＝｛｝【】；：’“，。《》？／'

# Функция для генерации пароля заданной длины
def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(symbols)
    return password

# Пример использования функции для генерации пароля длиной 8 символов
password = generate_password(8)
print(password)
