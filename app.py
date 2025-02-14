from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from main import search_agent

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    name = data.get('name')
    summary_and_facts, profile_pic_url = search_agent(name)
    return jsonify({'summary_and_facts': summary_and_facts.to_dict(), 'picture_url': profile_pic_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)