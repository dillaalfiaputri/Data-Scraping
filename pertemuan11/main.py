# from flask import Flask

# app = Flask(__name__)

# @app.route("/via")
# def hello_Via():
#     return "<p>Hello, Via!</p>"

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run(debug=True)

# muncul nama /via
# from flask import Flask, redirect

# app = Flask(__name__)

# @app.route("/via")
# def hello_Via():
#     return "<p>Hello, Via!</p>"

# @app.route("/")
# def hello_world():
#     return redirect("/via")

# if __name__ == "__main__":
#     app.run(debug=True)

# menginputkan nama di browser
# from flask import Flask

# app = Flask(__name__)

# @app.route("/<nama>")
# def hello_nama(nama):
#     return f"<p>Hello, {nama}!</p>"

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

# @app.route("/")
# def home():
#     return """
#     <form action="/login" method="POST">
#         Username: <input type="text" name="username"><br>
#         Password: <input type="password" name="password"><br>
#         <button type="submit">Login</button>
#     </form>
#     """

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     return f"{username} , {password}"

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

@app.route("/login", methods=["GET"])
def login():
    user = request.args.get("user")
    password = request.args.get("pass")
    
    if user and password:
        return user + ":" + password
    return "Parameter user dan pass harus diisi!"

app.run(debug=True)