from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import query
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    # Here, get your bot's response based on the incoming message.
    response = query(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
