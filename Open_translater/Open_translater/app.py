from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import googletrans
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def upload_and_translate():
    translated_text = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        translated = translator.translate(text, dest='ko')  # 한국어로 번역
        translated_text = translated.text

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
