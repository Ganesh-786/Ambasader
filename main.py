from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/electronics")
def electronics():
    return render_template("electronics.html")
@app.route("/cloths")
def cloths():
    return render_template("cloths.html")
@app.route("/homestyle")
def homestyle():
    return render_template("homestyle.html")


if __name__=='__main__':
    app.run(debug=True)
    