from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        r = requests.get("https://mathwithsaqa.great-site.net/test_api.php", timeout=10)
        return r.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
