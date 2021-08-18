from flask import Flask, render_template, request
from app import PixelArt

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


app.run(debug=True, host='your_ip', port="your_port")
