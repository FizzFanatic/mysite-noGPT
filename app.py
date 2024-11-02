# app.py
# импортируем нужные библиотеки

from flask import Flask, render_template


# экземпляр класса
app = Flask(__name__)


@app.route("/", methods=["GET"])
def main_menu():
    return render_template("index.html")


@app.route("/tools", methods=["GET"])
def page_tools():
    return render_template("tools.html")


@app.route("/services", methods=["GET"])
def page_services():
    return render_template("services.html")


@app.route("/academy", methods=["GET"])
def page_academy():
    return render_template("academy.html")


# if __name__ == '__main__':
#     app.run(debug=True)