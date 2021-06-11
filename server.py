from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", numx = 8, numy = 8, even_color = "red", odd_color = "black")

@app.route('/play/<int:numx>/<int:numy>')
def play_num2(numx, numy):
    return render_template("index.html", numx = numx, numy = numy, even_color = "red", odd_color = "black")

@app.route('/play/<int:numx>/<int:numy>/<odd_color>/<even_color>')
def play_num3(numx, numy, odd_color, even_color):
    return render_template("index.html", numx = numx, numy = numy, even_color = even_color, odd_color = odd_color)

if __name__ == "__main__":
    app.run(debug = True)