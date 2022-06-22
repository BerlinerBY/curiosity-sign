import numpy as np
import cv2
from textwrap import wrap
from PyQt5.QtCore import QThread, pyqtSignal
from core.rsa import RSA_encoder
from core.general_metods import get_data, open_docx
from core.signing import make_encrypted_hash


class SignScript(QThread):
    def __init__(self, path):
        super(SignScript, self).__init__()

        self.path = path

    count_percent = pyqtSignal(int)
    sign_notification = pyqtSignal(str)

    sign_path = '/home/berlinerby/PycharmProjects/curiosity-sign/core/signature.png'

    def run(self):
        if self.path == '':
            self.sign_notification.emit('Please enter path to DOCX file...')
        elif self.path[-4:] != "docx":
            self.sign_notification.emit('Please enter path to DOCX file...')
        else:
            message = get_data.get_text(self.path)
            count = 5
            self.count_percent.emit(count)

            hashing_message = make_encrypted_hash.get_hash(message)
            count = count + 5
            self.count_percent.emit(count)

            encrypt_rsa_hash, hash_len, rsa_key = RSA_encoder.RSA(hashing_message)
            count = count + 5
            self.count_percent.emit(count)

            count = self.hide(self.sign_path, '%s' % encrypt_rsa_hash, self.sign_path, count)
            count = count + 5
            self.count_percent.emit(count)

            open_docx.save_signature(self.path, self.sign_path, hash_len)

            count = count + 15
            self.count_percent.emit(count)
            self.sign_notification.emit('finish')

    def hide(self, address, text, save_address, count):
        """


        :param address: It is path of container for changing bytes
        :param text: It is message from user. the script will process it and convert it to bit form
        :param save_address: It is path, name and format of saved image
        :param count: Value for update progress bar

        :return:
        """
        text_array = np.array([bin(ord(elem))[2:] for elem in text], dtype=object)

        for i in range(len(text_array)):
            if len(text_array[i]) < 8:
                text_array[i] = (str('0' * (8 - len(text_array[i])))) + str(text_array[i])
            else:
                continue

        redaction_text_array = np.array(['+'], dtype=object)

        for elem in text_array:
            if redaction_text_array[0] == '+':
                redaction_text_array = np.delete(redaction_text_array, 0)
                element = wrap(elem, 2)
                redaction_text_array = np.concatenate((redaction_text_array, element), axis=0)
            else:
                element = wrap(elem, 2)
                redaction_text_array = np.concatenate((redaction_text_array, element), axis=0)

        count = count + 20
        self.count_percent.emit(count)

        '''open image and manipulation of bytes in pixels'''

        img = cv2.imread(address)
        image = np.array(img)
        height, width, depth = image.shape
        copy_image = np.copy(np.nditer(image))  # make 1D array from 3D

        step_key = 653

        variable_for_recursion = 0

        count = count + 20
        self.count_percent.emit(count)

        def lsb(functions_value, elem):
            value = bin(functions_value)[2:]  # 127 -> 1111 111
            value = ('0' * (8 - len(str(value))) + str(value))  # 1111 111 -> 0111 1111
            if value[-2:] == '01':
                value = bin(int(str(value), 2) - 1)[2:]
            elif value[-2:] == '10':
                value = bin(int(str(value), 2) - 2)[2:]
            elif value[-2:] == '11':
                value = bin(int(str(value), 2) - 3)[2:]  # 111 1100
            else:
                pass
            value = ('0' * (8 - len(str(value))) + str(value))
            #      (0111 1100) + (elem from stack = 01) = 0111 1101
            return int(bin(int(str(value), 2) + int(str(elem), 2))[2:], 2)

        for elem in redaction_text_array:
            copy_image[variable_for_recursion] = lsb(copy_image[variable_for_recursion], elem)
            if variable_for_recursion + step_key <= len(copy_image):
                variable_for_recursion += step_key
            elif variable_for_recursion + step_key > len(copy_image):
                variable_for_recursion = variable_for_recursion + step_key - len(copy_image)

        count = count + 20
        self.count_percent.emit(count)

        cv2.imwrite(save_address,
                    np.copy(copy_image.reshape(height, width, depth)))  # make 3D array and save modified image

        count = count + 5
        self.count_percent.emit(count)

        return count
