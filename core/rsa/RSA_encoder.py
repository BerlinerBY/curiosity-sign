import random
from core.rsa import preparation_of_numbers
import json


def word_processing(text):
    """

    :param text:
    :return:
    """
    # заменяем символы согласно словарю на их числовой эквивалент,
    # а затем сливаем все в одну строку
    text = ''.join(['1' + str('0' * (5 - len(str(ord(elem)))) + str(ord(elem))) for elem in text])
    mass_block = []

    start_i = 0
    bol = True
    while bol:
        while start_i <= len(text):
            i = random.randint(3, 10)
            if start_i == len(text):
                bol = False
                break
            elif start_i + i > len(text):
                mass_block.append('1' + text[start_i:])
                bol = False
                break
            else:
                mass_block.append('1' + text[start_i: start_i + i])
                start_i = start_i + i
        else:
            bol = False

    return mass_block


def encode(text_mass, e, n):
    array = []
    for elem in text_mass:
        array.append(str(pow(int(elem), e, n)))

    return array


def rsa_key(mass):
    difference = mass[2][1] - mass[1][1]
    last_key = ''
    if difference < 0:
        last_key = ',0'.join([str(mass[2][1]), str(difference)[1:]])
    elif difference >= 0:
        last_key = ',1'.join([str(mass[2][1]), str(difference)])
    return last_key


def get_key():
    # TODO пофиксить проблему с путем
    with open('/home/berlinerby/PycharmProjects/curiosity-sign/core/rsa/key.json', 'r') as file:
        data = json.load(file)
        e, d, n, _ = data.items()

    return e, d, n


def RSA(text):
    text_mass = word_processing(text)
    # mass_edn = preparation_of_numbers.main_func()
    mass_edn = get_key()

    encode_text = encode(text_mass, mass_edn[0][1], mass_edn[2][1])

    encoded_hash = ' '.join(encode_text)
    encode_key = rsa_key(mass_edn)

    return encoded_hash, len(encoded_hash), encode_key
