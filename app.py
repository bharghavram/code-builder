from flask import Flask, request, render_template, jsonify
from generator import code_builder

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")  

@app.route('/get-response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        prompt = data.get('text', '')

        result=code_builder(prompt)
        return jsonify({
            "response": result.text,
            "length": len(result.text),
            "tokens": len(result.text.split())
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
