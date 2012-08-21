from possimpable.model import twitter
from flask import Flask, render_template

app = Flask("possimpable")

@app.route("/")
def main():
    """Main and only page of the app"""

    twits = twitter.search_twits("-22.880018", "-43.410637", "50km")

    return render_template("main.html", twits=twits[0:1])