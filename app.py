from flask import Flask , requests , secrets , string


def generate_id():

    characters = string.ascii_letters + string.digits

    secure_string = "".join(secrets.choice(characters) for i in range(6))

    return secure_string




app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)