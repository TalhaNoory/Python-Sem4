#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pymysql 


app = Flask(__name__)

@app.route('/api/states', methods=['GET'])
def get_states():
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Ex1') 
    #return jsonify({'tasks': tasks})

    cursor = cnx.cursor()
    query = ("SELECT * FROM Ex2")
    cursor.execute(query)

    cursor.close()
    cnx.close()
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
