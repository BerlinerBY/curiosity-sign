import zipfile


def save_signature(file_path, signature_path, len_hash):
    with zipfile.ZipFile(file_path, 'a') as document:
        document.write(signature_path, f'sign{len_hash}.png', compress_type=None)


def get_signature(file_path):
    sign_path = ''
    with zipfile.ZipFile(file_path, 'r') as document:
        list_of_file_name = document.namelist()

        for file_name in list_of_file_name:
            if file_name.startswith('sign'):
                document.extract(file_name)
                sign_path = file_name

    hash_len = sign_path[4:8]

    return sign_path, hash_len
