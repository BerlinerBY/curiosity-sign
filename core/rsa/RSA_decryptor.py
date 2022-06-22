def decryption(rsa_key, text):
    """
    Function which decrypts the input string

    :param rsa_key: Type object <class 'str'>
    :param text: Type object <class 'str'>
    :return:
    """
    key_array = rsa_key.split(",")
    mod = int(key_array[0])
    d = 0
    if key_array[1][0] == '1':
        d = mod - int(key_array[1][1:])
    elif key_array[1][0] == '0':
        d = mod + int(key_array[1][1:])

    mass = [a for a in text.split(" ")]

    array = []

    for elem in mass:
        array.append(str(pow(int(elem), d, mod))[1:])

    text = "".join(array)

    mass_block = []
    i = 0
    while i < len(text):
        ord_symbol = text[i: i + 6]
        for j in range(1, len(ord_symbol)):
            if ord_symbol[j] == '0':
                continue
            else:
                mass_block.append(chr(int(ord_symbol[j:])))
                break

        i += 6

    return "".join(mass_block)
