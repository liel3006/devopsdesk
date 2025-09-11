from flask import Flask

app = Flask(__name__)
@app.get("/")
def home():
return ("בוקר טוב ליאל")
# liel
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)