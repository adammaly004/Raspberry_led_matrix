from flask import Flask, render_template, request


app = Flask(__name__)
app.static_folder = 'static'


def main(data):
    for item in data:
        item = item.split(", ")

        matrix = int(item[0]), int(item[1]), int(
            item[2]), int(item[3]), int(item[4])

        print(matrix)


@app.route('/', methods=["GET", "POST"])
def update():
    if request.method == 'POST':
        data = request.json
        main(data)

    return render_template("index.html")


app.run(debug=True, host='192.168.1.110', port="1111")
