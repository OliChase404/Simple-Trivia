from flask import Flask, request, jsonify, make_response, session
from config import app, db, bcrypt, migrate, metadata
from models import *

@app.route('/check_session', methods=['GET'])
def check_session():
    if session.get('user_id'):
        user = UserWarning.query.filter(UserWarning.id == session['user_id']).first()
        return jsonify({'user': user.to_dict()})
    else:
        return jsonify({'user': None})
    
