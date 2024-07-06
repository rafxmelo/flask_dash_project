from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Flask App. Use the following routes:",
        "routes": {
            "/convert": "POST method to convert an image from one type to another",
            "/analyze": "Analyze text for sentiment analysis"
        },
        "image_formats": ["JPEG", "PNG", "BMP"]
    })

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['image']
    output_format = request.form['format'].upper()

    if output_format not in ["JPEG", "PNG", "BMP"]:
        return "Invalid format", 400

    image = Image.open(file.stream)
    img_io = io.BytesIO()
    image.save(img_io, output_format)
    img_io.seek(0)

    return send_file(img_io, mimetype=f'data/{output_format.lower()}')

@app.route('/analyze', methods=['GET'])
def analyze():
    text = request.args.get('text')
    if not text:
        return "No text provided", 400

    blob = TextBlob(text)
    return jsonify({
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    })

if __name__ == '__main__':
    app.run(debug=True)
