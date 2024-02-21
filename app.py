from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
from jose import jwt, jwk
from jose.utils import base64url_decode
from jose.exceptions import JWTError
import requests
import secrets

app = Flask(__name__, template_folder='templates')
CORS(app, supports_credentials=True)
app.secret_key = secrets.token_hex(32)

client = MongoClient("mongodb://localhost:27017")
app.db = client.Astrologi
users_collection = app.db.users

AUTH0_DOMAIN = 'dev-whbba5qnfveb88fc.us.auth0.com'
ALGORITHMS = ['RS256']


# Время жизни токена доступа (например, 1 час)
ACCESS_TOKEN_EXPIRY = timedelta(hours=1)

# Функция для добавления пользователя в базу данных
def add_user_to_database(email):
    # Реализация добавления пользователя в базу данных
    pass


# Функция для проверки действительности idTokenHash
@app.route('/test', methods=["POST"])
def verify_auth0_token():
    data = request.json
    id_token_hash = data.get('id_token_hash')
    accessToken = data.get('accessToken')

    # Получаем JWKS от Auth0
    jwks_url = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
    jwks = requests.get(jwks_url).json()

    # Декодируем заголовок токена для получения kid
    headers = jwt.get_unverified_headers(id_token_hash)
    kid = headers['kid']

    # Ищем ключ в JWKS
    key_index = -1
    for i in range(len(jwks['keys'])):
        if kid == jwks['keys'][i]['kid']:
            key_index = i
            break

    if key_index == -1:
        return jsonify({"success": False, "error": "Appropriate key not found in JWKS"}), 400

    # Строим jwk из ключа и декодируем токен
    key = jwk.construct(jwks['keys'][key_index])
    message, encoded_sig = id_token_hash.rsplit('.', 1)
    decoded_sig = base64url_decode(encoded_sig.encode('utf-8'))

    if not key.verify(message.encode('utf-8'), decoded_sig):
        return jsonify({"success": False, "error": "Signature verification failed"}), 400

    try:
        # Верификация токена
        payload = jwt.decode(
            id_token_hash,
            key.to_dict(),
            algorithms=ALGORITHMS,
            audience='ab7q8GJ0KvwbL0zAC6UwwLaQcXjgbUGT',
            issuer=f'https://{AUTH0_DOMAIN}/',
            access_token=accessToken
        )

        # Проверки после верификации
        if payload['email_verified']:
            return jsonify({"success": True, "user_info": payload}), 200
        else:
            return jsonify({"success": False, "error": "Email not verified"}), 400

    except JWTError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    

# Генерация токена доступа
def generate_access_token(email):
    payload = {
        'email': email,
        'exp': datetime.utcnow() + ACCESS_TOKEN_EXPIRY
    }
    access_token = jwt.encode(payload, app.secret_key, algorithm='HS256')
    return access_token

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/<path:path>', methods=["GET"])
def catch_all(path):
    return render_template('index.html')


@app.route('/register', methods=["POST"])
def regist():
    data = request.json
    birthDate = data.get('birthDate')
    answer = data.get('answer')
    email = data.get('email')
    idTokenHash = data.get('idToken') # Хешируем токен
    accessTokenHash = data.get('accessToken')  # Хешируем токен

    users_collection.insert_one({
        "birthDate": birthDate,
        "answer": answer,
        "email": email,
        "idTokenHash": idTokenHash,
        "accessTokenHash": accessTokenHash,
    })
    return jsonify({"message": "User registered successfully"}), 200


# @app.route('/api/checldatebird', methods=["POST"])
# def cheakbirddate():
    data = request.json
    idToken = data.get('idToken')
    accessToken = data.get('accessToken')
    email = data.get('email')

    # Здесь вам нужно провести проверку пользователя в базе данных
    # Используйте email как постоянный идентификатор пользователя
    # Проверьте существует ли пользователь с данным email
    # Затем, если вы используете токены, убедитесь, что они действительны
    # Можно использовать библиотеки для проверки токенов, такие как PyJWT

    if user_exists(email):
        # Пользователь прошел проверку
        return jsonify({"message": "User verified successfully"}), 200
    else:
        # Пользователь не прошел проверку
        return jsonify({"message": "User verification failed"}), 401



if __name__ == "__main__":
    app.run(debug=True)