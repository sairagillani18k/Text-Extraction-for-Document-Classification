# Text-Extraction-for-Document-Classification

This Python script utilizes Tesseract OCR for extracting text from images and creates Word documents with the extracted text.

## Dependencies

Make sure to install the required Python packages using the following commands:
`pip install -r requirements.txt`

Additionally, you need to install Tesseract OCR. Follow the steps below:

Download the Tesseract OCR executable from https://sourceforge.net/projects/tesseract-ocr.mirror/.

Install Tesseract OCR and remember the installation path.

# Change this path
Update the path to the Tesseract executable in the script:
`pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\Tesseract-OCR\tesseract.exe'` # Change this path

# Usage
Install the dependencies as mentioned above.

Download and install Tesseract OCR from the provided link. Update the path in the script accordingly.

Replace the placeholder image paths in the script with the paths to your image files:

`image_paths = ['Sample-Invoice-printable.png']`

# Run the Code
`python script_name.py`
