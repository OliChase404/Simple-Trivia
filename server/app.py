from flask import Flask, request, jsonify, make_response, session
from config import app, db, bcrypt, migrate, metadata
from datetime import datetime
from models import *

@app.route('/check_session', methods=['GET'])
def check_session():
    if session.get('user_id'):
        user = User.query.filter(User.id == session['user_id']).first()
        user.last_active = datetime.utcnow()
        db.session.commit()
        return jsonify({'user': user.to_dict()})
    else:
        return jsonify({'user': None})
    
@app.route('/login', methods=['POST'])
def login():
    request_json = request.get_json()
    email = request_json.get('email')
    password = request_json.get('password')
    user = User.query.filter(User.email == email).first()
    if user and user.authenticate(password):
        session['user_id'] = user.id
        return jsonify({'user': user.to_dict()})
    else:
        return {'error': 'Invalid credentials'}, 401
    
@app.route('/logout', methods=['DELETE'])
def logout():
    session.clear()
    return {'message': 'Successfully logged out'}

@app.route('/signup', methods=['POST'])
def signup():
    request_json = request.get_json()
    new_user = User(
        username=request_json.get('username'),
        email=request_json.get('email'),
        password_hash=request_json.get('password'),
        last_active=datetime.utcnow()
    )
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return jsonify({'user': new_user.to_dict()})


@app.route('/users', methods=['GET'])
def users_index():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def users_show(id):
    user = User.query.get(id)
    if request.method == 'GET':
        return jsonify({'user': user.to_dict()})
    elif request.method == 'PATCH':
        request_json = request.get_json()
        user.username = request_json.get('username', user.username)
        user.email = request_json.get('email', user.email)
        user.image_url = request_json.get('image_url', user.image_url)
        user.last_active = datetime.utcnow()
        db.session.commit()
        return jsonify({'user': user.to_dict()})
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Successfully deleted user'})