import pytesseract
import sys


def ocr_project(input):
    # print(pytesseract.get_languages(config=''))
    custom_oem_psm_config = r'--oem 3 --psm 6'
    with open('ocr_result.txt', 'w') as f:
        ocrResult = pytesseract.image_to_string(input, lang='eng+fas', config=custom_oem_psm_config)
        f.write(ocrResult)


if len(sys.argv) == 2:
    ocr_project(sys.argv[1])
else:
    print('Please run the code in this format: main.py  [path to your img-file]')
    exit(-1)
