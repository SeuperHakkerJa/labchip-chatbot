from flask import Flask, request, jsonify
import rag  

app = Flask(__name__)

@app.route('/retrieve', methods=['POST'])
def retrieve():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify(error='Query parameter is required'), 400
    config = rag.RAG_Config(query=query)
    response = rag.retrieve(config)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
