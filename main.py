from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/konversi", methods=["POST"])
def konversi():
    suhu = float(request.form["suhu"])
    satuan = request.form["satuan"]
    satuan2 = request.form["satuan2"]
    hasil = 0

    if satuan == "Celcius" and satuan2 == "Celcius":
        hasil = suhu
        hasil = f"{round(hasil,2)}°"
        derajat = "°"
        satuan_hasil = "Celcius"
    elif satuan == "Celcius" and satuan2 == "Fahrenheit":
        hasil = suhu * 9/5 + 32
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Fahrenheit"
    elif satuan == "Celcius" and satuan2 == "Reamur":
        hasil = 4/5 * suhu
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Reamur"
    elif satuan == "Celcius" and satuan2 == "Kelvin":
        hasil = suhu + 273
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Kelvin"

    elif satuan == "Fahrenheit" and satuan2 == "Celcius":
        hasil = 5/9 * (suhu - 32)
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Celcius"
    elif satuan == "Fahrenheit" and satuan2 == "Fahrenheit":
        hasil = suhu
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Fahrenheit"
    elif satuan == "Fahrenheit" and satuan2 == "Reamur":
        hasil = 4/9 * (suhu - 32)
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Reamur"
    elif satuan == "Fahrenheit" and satuan2 == "Kelvin":
        hasil = 5/9 * (suhu - 32) + 273
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Kelvin"

    elif satuan == "Reamur" and satuan2 == "Celcius":
        hasil = 5/4 * suhu
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Celcius"
    elif satuan == "Reamur" and satuan2 == "Fahrenheit":
        hasil = 9/4 * suhu + 32
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Fahrenheit"
    elif satuan == "Reamur" and satuan2 == "Reamur":
        hasil = suhu
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Reamur"
    elif satuan == "Reamur" and satuan2 == "Kelvin":
        hasil = 5/4 * suhu + 273
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Kelvin"

    elif satuan == "Kelvin" and satuan2 == "Celcius":
        hasil = suhu - 273
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Celcius"
    elif satuan == "Kelvin" and satuan2 == "Fahrenheit":
        hasil = 9/5 * (suhu - 273) + 32
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Fahrenheit"
    elif satuan == "Kelvin" and satuan2 == "Reamur":
        hasil = 9/5 * (suhu - 273)
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Reamur"
    elif satuan == "Kelvin" and satuan2 == "Kelvin":
        hasil = suhu
        hasil = round(hasil,2)
        derajat = "°"
        satuan_hasil = "Kelvin"

    

    return render_template("konversi.html", suhu=suhu, satuan=satuan, hasil=hasil, satuan_hasil=satuan_hasil, derajat=derajat)

if __name__ == "__main__":
    app.run(debug=True)


