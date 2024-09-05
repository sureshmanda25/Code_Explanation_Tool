from flask import Flask, render_template, request, jsonify
from src.main import explain_code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        explanation = explain_code(code)
        return jsonify({'explanation': explanation})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)