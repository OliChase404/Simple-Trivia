from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(256), nullable=True)
    last_active = db.Column(db.DateTime, nullable=True)

@hybrid_property
def password_hash(self):
    raise AttributeError('password_hash is not a readable attribute')
@password_hash.setter
def password_hash(self, password):
    password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
    self._password_hash = password_hash.decode('utf-8')

def authenticate(self, password):
    return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


