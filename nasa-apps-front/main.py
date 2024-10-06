from flask import Flask, request, jsonify, render_template
import os
from flask_assets import Environment, Bundle

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up Flask-Assets
assets = Environment(app)
css = Bundle("src/input.css", output="src/output.css")
assets.register("css", css)
css.build()

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Run your custom code on the uploaded file
        result = process_file(filepath)

        return jsonify({"result": result})


def process_file(filepath):
    # Your logic to process the file and return a number
    with open(filepath, 'r') as f:
        data = f.read()
        # Do something with the data and return a number
        return len(data)  # Placeholder, replace with your custom logic


@app.route('/')
def index():
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)
