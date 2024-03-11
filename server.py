from flask import Flask, request, send_file
import requests
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process_image():
    # Extract image URL from the request
    image_url = request.json['image_url']
    image_name = secure_filename(image_url.split('/')[-1])
    input_path = os.path.join('inputs', image_name)
    output_path = 'output/'

    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(input_path, 'wb') as f:
            f.write(response.content)

    # Process the image (replace with your actual processing command)
    os.system(f"python run.py {input_path} --output-dir {output_path}")

    # For simplicity, assuming single output file named `mesh.obj`
    # Adjust according to your actual output
    output_file = os.path.join(output_path, 'mesh.obj')

    # Return the processed file
    return send_file(output_file, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
