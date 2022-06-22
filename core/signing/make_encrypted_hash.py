import hashlib


def get_hash(text):
    """
    This function use SHA-256 for create hash from text
    :param text: Input text. Type object <class 'str'>
    :return: Hash. Type object <class 'str'>
    """
    hash_text = hashlib.sha256(text.encode('utf-8')).hexdigest()

    return hash_text
