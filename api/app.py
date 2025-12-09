from flask import Flask, jsonify,request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # Enable CORS for all routes




def GenerateGuestbookEntry(name,message):
    return {
        'name': name,
        'message': message
    }

guestbook_entries = [
    GenerateGuestbookEntry("boobs","sexwad")

];

@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Flask!'})


@app.route('/api/message')
def get_message():
    return jsonify({'message': 'Daijoubu Cheese Plate'})

@app.route('/api/guestbook/add', methods=['POST'])
def add_guestbook_entry():
    global guestbook_entires
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'error': 'Name and message are required'}), 400
    
    entry = GenerateGuestbookEntry(name,message)
    guestbook_entries.append(entry)
    return jsonify({'message': 'Entry added successfully'})
    

@app.route('/api/guestbook/entries')
def get_guestbook_entries():
    global guestbook_entires
    return jsonify({'entries': guestbook_entries})
                                      

if __name__ == '__main__':
    app.run(debug=True)