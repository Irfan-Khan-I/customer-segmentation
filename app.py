import os
import sys
import logging
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import sklearn

# Print scikit-learn version for debugging
print(f"scikit-learn version: {sklearn.__version__}")

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.data_preprocessing import preprocess_data
from models.segmentation import demographic_segmentation

app = Flask(__name__)

# Define a directory for uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Secure the filename and save it to the upload folder
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        # Load and preprocess the data
        data = pd.read_csv(file_path)
        processed_data = preprocess_data(data)

        # Perform segmentation
        try:
            segmented_data = demographic_segmentation(processed_data)
        except ValueError as e:
            return jsonify({'error': str(e)})

        # Return the segmented data as JSON
        return jsonify(segmented_data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        # Clean up the saved file
        if os.path.exists(file_path):
            os.remove(file_path)


def allowed_file(filename):
    """Check if the file is allowed based on its extension."""
    allowed_extensions = {'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    app.run(debug=True)
