from flask import Flask, request, send_file
import requests
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    # Generate a unique ID for this request
    unique_id = str(uuid.uuid4())

    # Extract image URL from the request
    image_url = request.json['image_url']
    image_name = secure_filename(image_url.split('/')[-1])

    # Create directories for inputs and outputs based on unique_id
    input_dir = os.path.join('inputs', unique_id)
    output_dir_base = os.path.join('output', f"output-{unique_id}")
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir_base, exist_ok=True)

    input_path = os.path.join(input_dir, image_name)
    output_path = os.path.join(output_dir_base, "0")  # Assuming processing script creates this subdirectory

    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(input_path, 'wb') as f:
            f.write(response.content)

    # Process the image
    # Note: Modify your command to reflect the correct processing script and parameters
    os.system(f"python run.py {input_path} --output-dir {output_path}")

    # Define the expected output .obj file path
    obj_file_path = os.path.join(output_path, "mesh.obj")

    # Check if the .obj file exists, and return it
    if os.path.exists(obj_file_path):
        return send_file(obj_file_path, as_attachment=True)
    else:
        # Handle the case where the .obj file does not exist
        return "Output file not found.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
