from flask import Flask

app = Flask(__name__)


count= 0


@app.route("/")
def home():
    global count
    count +=1
    return f"Hello! Visit count: {count}"
   



if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000)
