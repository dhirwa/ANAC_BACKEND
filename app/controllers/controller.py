from flask import Flask, jsonify, request,render_template
from flask_bcrypt import Bcrypt

app = Flask(__name__)

def get_username(first_name,last_name):
    username = (first_name+last_name).lower()
    return username

bcrypt = Bcrypt(app)


def changePass(json_data,pas):
    pwd_hash = bcrypt.generate_password_hash(pas)
    pas=pwd_hash
    return pas
