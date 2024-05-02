# Flask app code (deployed on a central server)
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']  # Replace 'your_database' with your actual database name
collection = db['your_collection']  # Replace 'your_collection' with your actual collection name

@app.route('/export_characters', methods=['GET'])
def export_characters_to_json():
    try:
        # Retrieve all characters from the MongoDB collection
        all_characters = collection.find({})

        # Convert characters to a list
        characters_list = list(all_characters)

        # Serve JSON data as the response
        return jsonify(characters_list)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Accessible to all users
