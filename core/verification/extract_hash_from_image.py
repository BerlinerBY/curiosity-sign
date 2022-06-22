import os

import numpy as np
import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from core.rsa import RSA_decryptor
from core.general_metods import get_data, open_docx
from core.signing import make_encrypted_hash


class VerificationScript(QThread):
    def __init__(self, path, key):
        super(VerificationScript, self).__init__()

        self.path = path
        self.key = key

    count_percent = pyqtSignal(int)
    global_finish = pyqtSignal(str)

    def run(self):
        if self.path == '' and self.key == '' or self.path[-4:] != "docx" and self.key == '':
            self.global_finish.emit('Please enter path to DOCX file and verification key')
        elif self.key == '':
            self.global_finish.emit('Please enter verification key...')
        elif self.path == '' or self.path[-4:] != "docx":
            self.global_finish.emit('Please enter path to DOCX file...')
        else:
            signature, hash_len = open_docx.get_signature(self.path)
            count = 5
            self.count_percent.emit(count)

            recovery_hash, count = self.decode(signature, count, hash_len)
            os.remove(signature)

            hash_value = RSA_decryptor.decryption(str(self.key), str(recovery_hash))

            message = get_data.get_text(self.path)

            hashing_message = make_encrypted_hash.get_hash(message)

            if hash_value == hashing_message:
                self.global_finish.emit('successful')
            else:
                self.global_finish.emit('filed')
            count = count + 5
            self.count_percent.emit(count)

    def decode(self, address, count, len_text):
        """

        :param address: It is path of stegocontainer with our information
        :param count: Value for update progress bar
        :param len_text:

        :return:
        """
        len_text = int(len_text) * 4

        count = count + 20
        self.count_percent.emit(count)

        img = cv2.imread(address)
        image = np.array(img)

        copy_image = np.copy(np.nditer(image))  # make 1D array from 3D

        text_array = []
        step_key = 653
        variable_for_recursion = 0

        count = count + 20
        self.count_percent.emit(count)

        def download_info(value):
            binary_value = ('0' * (8 - len(str(bin(value)[2:]))) + str(bin(value)[2:]))
            if binary_value[-2:] == '00':
                text_array.append(binary_value[-2:])
            elif binary_value[-2:] == '01':
                text_array.append(binary_value[-2:])
            elif binary_value[-2:] == '10':
                text_array.append(binary_value[-2:])
            elif binary_value[-2:] == '11':
                text_array.append(binary_value[-2:])

        run = True
        while run:
            if len(text_array) < len_text:
                download_info(copy_image[variable_for_recursion])
                if variable_for_recursion + step_key <= len(copy_image):
                    variable_for_recursion += step_key
                elif variable_for_recursion + step_key > len(copy_image):
                    variable_for_recursion += step_key - len(copy_image)
            else:
                run = False

        count = count + 30
        self.count_percent.emit(count)

        bufer_text_array = []

        i = 0
        while i < len(text_array):
            string = ""
            for j in range(4):
                string += text_array[i + j]
            bufer_text_array.append(chr(int(string, 2)))
            i += 4

        count = count + 20
        self.count_percent.emit(count)

        return ''.join(bufer_text_array), count
