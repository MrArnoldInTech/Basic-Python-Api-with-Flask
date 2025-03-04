from flask import Flask, request, jsonify 

app = Flask(__name__)

# Basic flask setup with API 

# @app.route("/")
# def home():
#     return "Home"


#Testing with a get Route.
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra: 
        user_data["extra"] = extra

    return jsonify(user_data), 200

# Only accepted route is post 
@app.route("/create-user", methods=["POST"])
# My Function
def create_user():
    #Will get the data that was given in the body
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)