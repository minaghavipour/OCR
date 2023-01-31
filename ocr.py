import os
from pdf2image import convert_from_path
import pytesseract


class OCR:
    def __int__(self):
        pass

    @staticmethod
    def img_to_str(img_file):
        custom_oem_psm_config = r'--oem 3 --psm 6'
        ocr_text = pytesseract.image_to_string(img_file, lang='eng+fas', config=custom_oem_psm_config)
        return ocr_text

    @staticmethod
    def pdf_to_str(pdf_file):
        ocr_text = ''
        custom_oem_psm_config = r'--oem 3 --psm 6'
        doc = convert_from_path(pdf_file)
        for img_number, img_data in enumerate(doc):
            page_content = pytesseract.image_to_string(img_data, lang='eng+fas', config=custom_oem_psm_config)
            page_content = '***PDF Page {}***\n'.format(img_number + 1) + page_content
            ocr_text = ocr_text + ' ' + page_content
        return ocr_text

    def run_ocr(self, input_file):
        # print(pytesseract.get_languages(config=''))
        path, file_name = os.path.split(input_file)
        file_basename, file_extension = os.path.splitext(file_name)
        with open(os.path.join(path, "ocr_result.txt"), 'w') as f:
            if file_extension == '.pdf':
                ocr_text = self.pdf_to_str(input_file)
            else:
                ocr_text = self.img_to_str(input_file)
            f.write(ocr_text)
        return ocr_text