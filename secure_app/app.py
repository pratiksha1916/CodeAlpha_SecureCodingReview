from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Secure Web Application"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    safe_query = escape(query)
    return render_template_string(
        "<h3>You searched for: {{ query }}</h3>",
        query=safe_query
    )

if __name__ == "__main__":
    app.run(debug=True)