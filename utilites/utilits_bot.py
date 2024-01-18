from PIL import Image, ImageEnhance
import easyocr
import os
import re
import requests
import json

PATTERN2 = re.compile(r'\b[A-Za-z]{4}\d{7}\b')
PATTERN = re.compile(r'\b[A-Z]{4}\s+?(\d+)\s?\d')


def detect_number(text: str):

    match = PATTERN.search(text)
    if match:
        container_number = match.group(0)
        return ''.join(container_number.split())
    else:
        print("Номер контейнера не найден.")
 
 
def image_enchance(image_path: str):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    new_name = os.path.splitext(image_path)[0] + '-enhance' + os.path.splitext(image_path)[1]
    image.save(new_name)
    os.remove(image_path)
    return new_name
            
        
def image_to_text(image_path: str) -> str:
    new_name = image_enchance(image_path)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(new_name, detail=0)
    conteiner_number = ' '.join([i for i in result])
    print(conteiner_number)
    conteiner = detect_number(conteiner_number)
    os.remove(new_name)
    return conteiner

def coincidence(text: str):
    if re.search(PATTERN2, text):
        return True
    else:
        return False


def data_cont(contNum: str) -> json:
    url = f'http://83.68.49.221:8080/status_cont/{contNum}/?format=json'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # img = 'images\images.jpg'
    # print(image_to_text(img))
    # data = data_cont('NEPU4570390')
    # for dat in data.get("result"):
    #     print(dat.get("ContNum"))
    text = '''Контейнер: NEPU4570390
Заявки:'''
    print(len(text))