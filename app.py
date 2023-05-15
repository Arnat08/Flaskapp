from flask import Flask, jsonify
from database.database import Database

app = Flask(__name__)

database = Database('database/database.db')


@app.route('/api/users', methods=['GET'])
def get_users():
	data = database.select_database()
	return jsonify(data)


if __name__ == '__main__':
	app.run()