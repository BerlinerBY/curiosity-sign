import re
import zipfile


def get_text(path):
    docx = zipfile.ZipFile(path)
    text = docx.read('word/document.xml').decode('utf-8')
    cleaned_text = re.sub('<(.|\n)*?>', '', text)
    docx.close()

    return cleaned_text
