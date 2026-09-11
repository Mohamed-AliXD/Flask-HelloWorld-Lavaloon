"""
app.py

A very simple Flask application with three routes:
- "/" renders an HTML page.
- "/api/hello" returns JSON data.
- "/about" renders a simple text response.
"""

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page using an HTML template."""
    return render_template("index.html")


@app.route("/api/hello")
def api_hello():
    """Return a simple JSON message."""
    data = {
        "message": "Hello, World!"
    }
    return jsonify(data)


@app.route("/about")
def about():
    """Return a simple text response about this project."""
    return "This is a simple Flask project made to practice routes, templates, and JSON."


if __name__ == "__main__":
    app.run(debug=True)
