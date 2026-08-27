from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Vulnerable Web Application"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"You searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True)