import requests

# URL of the Flask app's /convert route
url = "http://127.0.0.1:5000/convert"

# Path to the image you want to convert
image_path = "image.png"  # Update the path as needed

# Specify the desired output format
data = {'format': 'JPEG'}

# Open the image file in binary mode
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}

    # Send the POST request to the /convert route
    response = requests.post(url, files=files, data=data)

    # Save the converted image
    if response.status_code == 200:
        with open('converted_image.jpeg', 'wb') as converted_file:
            converted_file.write(response.content)
        print("Image converted and saved successfully.")
    else:
        print("Failed to convert image:", response.text)
