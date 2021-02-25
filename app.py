from flask import Flask, render_template,request
import os
from task import salvar_ig
#from task import salvar_ig
import time

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods = ['POST'])
def func_salvar():
    url = request.form['url']
    time.sleep(1)
    task = salvar_ig.delay()
    time.sleep(2)
    task_id = task.id
    return render_template("save.html", url = url, frase = "Video_IG.mp4", id= task_id)


if __name__ == "__main__":
    app.run(debug=True, port=port)
