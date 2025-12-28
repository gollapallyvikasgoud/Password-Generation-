from flask import Flask, render_template, request
import random

app = Flask(__name__)

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?'
]

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        nr_letter = int(request.form["letters"])
        nr_symbols = int(request.form["symbols"])
        nr_number = int(request.form["numbers"])

        password_list = []

        for i in range(nr_letter):
            password_list.append(random.choice(letters))

        for i in range(nr_symbols):
            password_list.append(random.choice(symbols))

        for i in range(nr_number):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = "".join(password_list)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
