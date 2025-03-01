# Flask Tesseract ID Verification

## Overview
This is a simple Flask web application that allows users to upload an image of an ID. The application extracts text from the uploaded image using Tesseract OCR and compares it with user-provided input to verify a match.

## Features
- Web interface built with Flask
- Upload an image file for ID verification
- Extract text from the image using Tesseract OCR
- Compare extracted text with user input
- Display verification results (Match or Mismatch)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Tesseract OCR (Download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract))
- Flask
- Pillow
- pytesseract

### Clone the Repository
```sh
 git clone https://github.com/81mct/Flask-Tesseract-ID-Verification.git
 cd Flask-Tesseract-ID-Verification
```

### Create and Activate Virtual Environment
```sh
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application
1. Ensure that Tesseract is installed and configured correctly.
2. Run the Flask application:
   ```sh
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure
```
flask_tesseract_app/
│── templates/
│   ├── index.html  # Upload form
│   ├── result.html  # Display verification results
│── uploads/  # Stores uploaded images
│── app.py  # Main Flask application
│── tesseract_utils.py  # Utility functions for image preprocessing
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions, feel free to reach out via GitHub Issues.

