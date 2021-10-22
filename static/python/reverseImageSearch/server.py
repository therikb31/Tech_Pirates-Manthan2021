import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if(request.method=="POST"):
        file = request.files["query_img"]
        img = Image.open(file.stream)
        uploaded_img_path = "static/python/reverseImageSearch/uploaded/" + datetime.now().isoformat().replace(":",".")+"_"+file.filename
        img.save(uploaded_img_path) 
        return render_template("index.html",query_path=uploaded_img_path)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug="True")