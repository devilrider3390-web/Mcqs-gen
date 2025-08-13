from flask import Flask, request, jsonify

app = Flask(__name__)

# Author and usage information
@app.route('/')
def home():
    return (
        "MCQ Generator API\n\n"
        "Usage:\n"
        "/api?XYZ=your_access_key\n\n"
        "Author: @LORD_SIDDHARTH"
    )

# MCQ generator endpoint with access control
@app.route('/api')
def generate_mcq():
    ACCESS_KEY = "SIDDHARTH"  # <<< Here's your custom access key!
    
    key = request.args.get('XYZ')
    if key != ACCESS_KEY:
        return jsonify({"error": "Unauthorized access"}), 401

    question = "What is the capital of France?"
    options = ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"]
    answer = "C) Paris"

    return jsonify({
        "question": question,
        "options": options,
        "answer": answer
    })

if __name__ == "__main__":
    app.run()
