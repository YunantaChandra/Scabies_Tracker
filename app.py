# from process import preparation, generate_response
from flask import Flask, render_template, request
from model import load, prediksi

# download nltk
# preparation()

#Start 
app = Flask(__name__)
app.static_folder = 'static'

# load model dan scaler
load()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/learnmore")
def learnmore():
    return render_template("1-learnmore.html")

@app.route("/mulai")
def mulai():
    return render_template("2-mulai.html")

@app.route("/tentang")
def tentang():
    return render_template("3-tentang.html")

@app.route("/team")
def team():
    return render_template("4-team.html")

@app.route("/predict", methods=["POST"])
def predict():
    # menangkap data yang diinput user melalui form
    ras = int(request.form['ras'])
    gejala1 = int(request.form['gejala1'])
    gejala2 = int(request.form['gejala2'])
    gejala3 = int(request.form['gejala3'])
    gejala4 = int(request.form['gejala4'])
    gejala5 = int(request.form['gejala5'])
    gejala6 = int(request.form['gejala6'])
    gejala7 = int(request.form['gejala7'])
    gejala8 = int(request.form['gejala8'])
    gejala9 = int(request.form['gejala9'])
    gejala10 = int(request.form['gejala10'])
    gejala11 = int(request.form['gejala11'])
    gejala12 = int(request.form['gejala12'])
    gejala13 = int(request.form['gejala13'])
    gejala14 = int(request.form['gejala14'])
    gejala15 = int(request.form['gejala15'])
    gejala16 = int(request.form['gejala16'])
    gejala17 = int(request.form['gejala17'])
    gejala18 = int(request.form['gejala18'])
    gejala19 = int(request.form['gejala19'])
    gejala20 = int(request.form['gejala20'])
    gejala21 = int(request.form['gejala21'])

     # melakukan prediksi menggunakan model yang telah dibuat
    data = [[ras, gejala1, gejala2, gejala3, gejala4, gejala5, gejala6, gejala7, gejala8, gejala9, gejala10, gejala11, gejala12, gejala13, gejala14, gejala15, gejala16, gejala17, gejala18, gejala19, gejala20, gejala21]]
    prediction_result = prediksi(data)
    return render_template('2-mulai.html', hasil_prediksi=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)