from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/14/15/enhanced/webdr02/anigif_enhanced-854-1402772731-5.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/14/15/enhanced/webdr05/anigif_enhanced-23403-1402773525-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr01/2012/12/17/13/anigif_enhanced-buzz-15518-1355769150-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2012/12/14/15/anigif_enhanced-buzz-25730-1355518361-8.gif?downsize=700:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/5/30/18/anigif_enhanced-buzz-898-1369953089-15.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr02/2013/8/20/11/anigif_enhanced-buzz-31256-1377012172-9.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
