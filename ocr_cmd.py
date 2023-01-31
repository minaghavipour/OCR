import sys
from ocr import OCR


ocr_tool = OCR()
if len(sys.argv) == 2:
    ocr_tool.run_ocr(sys.argv[1])
else:
    print('Please run the code in this format: main.py  [path to your img-file]')
    exit(-1)
