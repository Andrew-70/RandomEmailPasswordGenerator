from flask import Flask, jsonify
import random
import string

app= Flask(__name__)
@app.route('/')
def generate_random_email(domain='bugie.com', email_prefix='qauser'):
    random_email_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))
    email = f'{random_string}_{email_prefix}@{domain}'

    random_password_length = 8
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_password_length))
    password = random_string
    random_info = {'email': email, 'password': password}
    return jsonify(random_info)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)