import os
from huggingface_hub import HfFolder, Repository
from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask import Flask, request, jsonify, render_template
import re

hf_token = '**'
repo_name = "**"
username = '**'
model_repo = os.path.join(username, repo_name)
dwnld_tokenizer = T5Tokenizer.from_pretrained(model_repo, token = hf_token)
dwnld_model = T5ForConditionalGeneration.from_pretrained(model_repo)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    test_text = [text for text in request.form.values()]
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', test_text[0])
    generated_text = ''
    for sentence in sentences:
        delimiter = sentence[-1]
        input_ids = dwnld_tokenizer(sentence[:-1], return_tensors="pt").input_ids
        output_tokens = dwnld_model.generate(input_ids, max_length=50, num_return_sequences=1)
        output = dwnld_tokenizer.decode(output_tokens[0], skip_special_tokens=True)
        generated_text += output + delimiter + ' '

    return render_template('index.html', input_text = test_text[0], prediction_text=generated_text)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
