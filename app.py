from flask import Flask , request , redirect , url_for , abort , jsonify
from database import save_url
from database import get_url
from database import get_stats
import string
import secrets

app = Flask(__name__)

@app.route('/shorten', methods= ["POST"])
def shorten():

    data = request.get_json()

    if not data or "url" not in data:
        return {"error": "Ivalid Request"}, 400

    url = data["url"]

    if not url:
        return ({"error": "Invalid JSON or missing Content-Type header"}), 400
    
    short_code = generate_id()
    save_url(url, short_code)

    return ({"short_url": short_code}), 201
    
    

def generate_id():

    characters = string.ascii_letters + string.digits

    secure_string = "".join(secrets.choice(characters) for i in range(6))

    return secure_string


@app.route("/<short_code>" , methods = ["GET"])
def redirect_url(short_code):
    
    result = get_url(short_code)

    if result:
        return redirect(result[0])
    
    else:
        return  abort(404, description="Short URL not found")
    
@app.route("/stats/<short_code>", methods = ["GET"])
def display_stats(short_code):

    result = get_stats(short_code)

    if result:
        return jsonify({
            "short_code" : f"http://127.0.0.1:5000/{short_code}",
            "original_url": result[0],
            "clicks":result[1]
        }), 200
    else:
        return abort(404, description="Short URL not found")
        


if __name__ == "__main__":
    app.run(debug=True)