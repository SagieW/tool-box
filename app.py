#imports#
#=======#
from flask import Flask, render_template, request
from database import *

from styleformer import Styleformer
import torch
import warnings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'


warnings.filterwarnings("ignore")
def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1234)

sf = Styleformer(style = 0)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/textconvertor", methods=['GET', 'POST'])
def textconvertor():
    if request.method == 'GET':
        return render_template("textconvertor.html")

    else:
        original_text = request.form['original_text']

        #styleFormer#
        converted_text = sf.transfer(original_text)

        if converted_text is not None:
            result = converted_text
        else:
            result = "Sorry! We couldn't find a good replacement. You may try again with a different phrasing."



        return render_template("textconvertor_result.html", result = result)        


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
