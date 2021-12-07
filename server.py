from flask import Flask, render_template, request, url_for, flash
import requests
from dotenv import load_dotenv
load_dotenv()
import os


# CREATE WEBAPP
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        word = request.form.get('word')
        url = f"https://owlbot.info/api/v4/dictionary/{word}"
        headers = {
            "Authorization": os.environ.get('API_SECRET_KEY')
        }
        response = requests.get(url=url, headers=headers).json()['definitions'][0]
        print(response)
        return render_template('index.html', results=response, word=word.title())
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
