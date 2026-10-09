from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Welcome to Smart Campus Assistant 🎓</h1>
    <p>Your AI-powered campus companion.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)