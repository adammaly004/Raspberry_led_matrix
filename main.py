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

    return render_template("index.html", draw=True)


@app.route('/text', methods=["GET", "POST"])
def text():
    if request.method == 'POST':
        text = request.form['text']
        test = request.form['color'].lstrip('#')
        color = list(int(test[i:i+2], 16) for i in (0, 2, 4))

        if text != "" and color != [0, 0, 0]:
            runtext = RunText(text, color)
            if (not runtext.process()):
                runtext.print_help()

    return render_template("index.html", draw=False)


app.run(debug=True, host='192.168.1.129', port="1111")
