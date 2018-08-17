from flask import Flask, request, jsonify, make_response
from .models import Users, users, questions, questions
import re

app = Flask(__name__)
@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    user_data = request.get_json()
    #gets the user data for signing up
    first_name = str(user_data.get("first_name"))
    last_name = str(user_data.get("last_name"))
    username = str(user_data.get("username"))
    email = user_data.get("email")
    password = user_data.get("password")
    confirm_password = user_data.get("confirm_password")

    if not user_data:
        return jsonify({'message':'All fields are required'}),400

    if not first_name or first_name ==type(int) or first_name == " ":
        return jsonify({'message':'A valid first_name is required'}), 400

    if not last_name or last_name == type(int) or last_name == " ":
        return jsonify({"message":"A valid last_name is required"}), 400

    if not username or username == type(int) or username == " ":
        return jsonify({'message': 'A valid username is reuired'}), 400

    if not email or email =="":
        return jsonify({'message':'Email is required'}), 400

    if not password or password ==" " or len(password)< 8:
        return jsonify({'message':'Avalid password is required'}), 400
        
    if not confirm_password or confirm_password == " " or len(confirm_password)<8:
        return jsonify({'message':'Please confirm your password'}), 400

    users.append(user_data)
    return jsonify({'message':'you have successfully signed up'}), 201

#login endpoint
@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    user_data = request.get_json()
    username = str(user_data.get('username'))
    password = user_data.get('password')

    if not user_data:
        return jsonify({'message':'All fields are required'}), 400

    if not username or username == " " or len(username)<8 or username == type(int):
        return jsonify({'message':'A vaild username is required'}), 400

    if not password or password ==" " or len(password)<8:
        return jsonify({'message':'Availd password is required'}), 400

    users.append(user_data)
    return jsonify({'message':'you are successfully login.'}), 201


#get questions
@app.route('/api/v1/user/question', methods=["GET"])
def fetch_question():
    if len(questions)>0:
        return jsonify({"message":questions}), 302
    else:
        return jsonify({"message":"There are no questions found"}),400

