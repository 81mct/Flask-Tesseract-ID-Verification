import cv2
import numpy as np
from PIL import Image
import pytesseract

# Configure Tesseract path (Update if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TesseractOCR:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
    
    def preprocess_image(self):
        """Convert image to grayscale and apply thresholding for better OCR accuracy."""
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(image_cv, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.image = Image.fromarray(thresh)
        return self
    
    def resize_image(self, scale_factor=2):
        """Resize image to enhance text readability."""
        width, height = self.image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        self.image = self.image.resize(new_size, Image.Resampling.LANCZOS)
        return self
    
    def extract_text(self):
        """Extract text using Tesseract OCR after preprocessing."""
        return pytesseract.image_to_string(self.image, lang='eng')
    
    def run_ocr(self):
        """Pipeline to run OCR with preprocessing."""
        self.preprocess_image().resize_image()
        extracted_text = self.extract_text()
        return extracted_text

# Example usage:
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # Update with the actual image path
    ocr = TesseractOCR(image_path)
    text = ocr.run_ocr()
    print("Extracted Text:", text)
