from flask import Flask, render_template, request
from ai_client import AIClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = AIClient(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")
        response = client.generate_code(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
