from flask import Flask, render_template

app = Flask("possimpable")

@app.route("/")
def main():
    return render_template("main.html")