from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import os

# Configure Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Tesseract path (update if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Upload and process image
@app.route('/upload', methods=['POST'])
def upload():
    if 'id_image' not in request.files:
        return "No file part"
    
    file = request.files['id_image']
    if file.filename == '':
        return "No selected file"
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Extract text using Tesseract
    image = Image.open(filepath)
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    
    # Get user input
    user_text = request.form.get('user_input', '').strip().lower()
    
    # Compare extracted text with user input
    match = user_text in extracted_text.lower()
    
    return render_template('result.html', match=match)

if __name__ == '__main__':
    app.run(debug=True)
