from flask import Flask, render_template, request, redirect
from app import PixelArt, RunText

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=["GET", "POST"])
def update():
    if request.method == 'POST':
        data = request.json
        pixel_art = PixelArt(data)

        if (not pixel_art.process()):
            pixel_art.print_help()

    return render_template("index.html")


@app.route('/text', methods=["GET", "POST"])
def text():
    text = request.form['text']
    color = [255, 255, 255]
    if text != "":
        runtext = RunText(text, color)

        if (not runtext.process()):
            runtext.print_help()
    return redirect("/")


app.run(debug=True, host='192.168.1.129', port="1111")
