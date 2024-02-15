#pip install pytesseract
#pip install pillow
#pip install python-docx



from PIL import Image
import pytesseract
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def create_word_document(text, output_path):
    document = Document()
    document.add_paragraph(text)

    # Save the Word document
    document.save(output_path)


# Replace 'image1.jpg', 'image2.jpg', etc., with the paths to your image files
image_paths = ['Sample-Invoice-printable.png']

for i, image_path in enumerate(image_paths):
    output_text = extract_text_from_image(image_path)
    output_file = f'output_{i + 1}.docx'
    create_word_document(output_text, output_file)
    print(f'Text extracted from {image_path} and saved to {output_file}')
