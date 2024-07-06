# Flask and Dash Project

This project demonstrates the creation of a Flask app with specific routes and a Dash app for data visualization. It also includes a Jupyter Notebook to showcase the usage of the Flask routes.

## Project Structure

flask_dash_project/
├── app.py
├── dash_app.py
├── venv/
├── notebooks/
│ ├── Flask_Usage.ipynb
│ └── Flask_Usage.html
├── data/
│ └── example.png
├── requirements.txt
└── README.md

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd flask_dash_project

   ```

2. Create and activate a virtual environment:

bash
Copy code
python3.8 -m venv venv
source venv/bin/activate

3. Install the required packages:

bash
Copy code
pip install -r requirements.txt

4. Run the Flask app:

bash
Copy code
python app.py

5. Run the Dash app:

bash
Copy code
python dash_app.py

6. Open the Jupyter Notebook:

bash
Copy code
jupyter notebook

## Usage

Access the Flask app at http://127.0.0.1:5000/
Access the Dash app at http://127.0.0.1:8050/
Use the Jupyter Notebook to demonstrate the Flask routes.

## Dependencies

Flask
Dash
Pillow
TextBlob
Jupyter

## License

This project is licensed under the MIT License.

markdown
Copy code
