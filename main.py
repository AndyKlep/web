from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template("4.html") # Внутри () пишем название html-файла в кавычках

@app.route("/new/")
def new():
    return "new page"

@app.route("/<password>/")
def hello_world2(password=None):
    if password == "1234":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"

if __name__ == '__main__':
    app.run(debug=True)
