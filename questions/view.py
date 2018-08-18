from flask import Flask, request, jsonify, make_response
from .models import question, question
import re

app = Flask(__name_
#get questions
@app.route("/api/v1/user/question", methods=["GET"])
def fetch_question():
    if len(questions)>0:
        return jsonify({"message":questions}), 302
    else:
        return jsonify({"message":"There are no questions found"}),400