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
    hasilawal = 0

    if satuan == "Celcius" and satuan2 == "Celcius":
        hasilawal = suhu
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "suhu"
        satuan_hasil = "Celcius"
        if hasilawal < 18:
            kategori = "Suhu Dingin"
        elif hasilawal > 18 and hasilawal < 28:
            kategori = "Suhu Normal"
        elif hasilawal > 27:
            kategori = "Suhu Panas"
    elif satuan == "Celcius" and satuan2 == "Fahrenheit":
        hasilawal = suhu * 9/5 + 32
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "9/5 x suhu + 32"
        satuan_hasil = "Fahrenheit"
        if hasilawal < 64:
            kategori = "Suhu Dingin"
        elif hasilawal > 64 and hasilawal < 81:
            kategori = "Suhu Normal"
        elif hasilawal > 80:
            kategori = "Suhu Panas"
    elif satuan == "Celcius" and satuan2 == "Reamur":
        hasilawal = 4/5 * suhu
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "4/5 x suhu"
        satuan_hasil = "Reamur"
        if hasilawal < 14.4:
            kategori = "Suhu Dingin"
        elif hasilawal > 14.4 and hasilawal <= 21.6:
            kategori = "Suhu Normal"
        elif hasilawal > 21.6:
            kategori = "Suhu Panas"
    elif satuan == "Celcius" and satuan2 == "Kelvin":
        hasilawal = suhu + 273
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "suhu + 273"
        satuan_hasil = "Kelvin"
        if hasilawal < 291.15:
            kategori = "Suhu Dingin"
        elif hasilawal > 291.15 and hasilawal <= 300.15:
            kategori = "Suhu Normal"
        elif hasilawal > 300.15:
            kategori = "Suhu Panas"

    elif satuan == "Fahrenheit" and satuan2 == "Celcius":
        hasilawal = 5/9 * (suhu - 32)
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "5/9 x (suhu - 32)"
        satuan_hasil = "Celcius"
        if hasilawal < 18:
            kategori = "Suhu Dingin"
        elif hasilawal > 18 and hasilawal < 28:
            kategori = "Suhu Normal"
        elif hasilawal > 27:
            kategori = "Suhu Panas"
    elif satuan == "Fahrenheit" and satuan2 == "Fahrenheit":
        hasilawal = suhu
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "suhu"
        satuan_hasil = "Fahrenheit"
        if hasilawal < 64:
            kategori = "Suhu Dingin"
        elif hasilawal > 64 and hasilawal < 81:
            kategori = "Suhu Normal"
        elif hasilawal > 80:
            kategori = "Suhu Panas"
    elif satuan == "Fahrenheit" and satuan2 == "Reamur":
        hasilawal = 4/9 * (suhu - 32)
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "4/9 x (suhu - 32)"
        satuan_hasil = "Reamur"
        if hasilawal < 14.4:
            kategori = "Suhu Dingin"
        elif hasilawal > 14.4 and hasilawal <= 21.6:
            kategori = "Suhu Normal"
        elif hasilawal > 21.6:
            kategori = "Suhu Panas"
    elif satuan == "Fahrenheit" and satuan2 == "Kelvin":
        hasilawal = 5/9 * (suhu - 32) + 273
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "5/9 x (suhu - 32) + 273"
        satuan_hasil = "Kelvin"
        if hasilawal < 291.15:
            kategori = "Suhu Dingin"
        elif hasilawal > 291.15 and hasilawal <= 300.15:
            kategori = "Suhu Normal"
        elif hasilawal > 300.15:
            kategori = "Suhu Panas"

    elif satuan == "Reamur" and satuan2 == "Celcius":
        hasilawal = 5/4 * suhu
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "5/4 x suhu"
        satuan_hasil = "Celcius"
        if hasilawal < 18:
            kategori = "Suhu Dingin"
        elif hasilawal > 18 and hasilawal < 28:
            kategori = "Suhu Normal"
        elif hasilawal > 27:
            kategori = "Suhu Panas"
    elif satuan == "Reamur" and satuan2 == "Fahrenheit":
        hasilawal = 9/4 * suhu + 32
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "9/4 x suhu + 32"
        satuan_hasil = "Fahrenheit"
        if hasilawal < 64:
            kategori = "Suhu Dingin"
        elif hasilawal > 64 and hasilawal < 81:
            kategori = "Suhu Normal"
        elif hasilawal > 80:
            kategori = "Suhu Panas"
    elif satuan == "Reamur" and satuan2 == "Reamur":
        hasilawal = suhu
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "suhu"
        satuan_hasil = "Reamur"
        if hasilawal < 14.4:
            kategori = "Suhu Dingin"
        elif hasilawal > 14.4 and hasilawal <= 21.6:
            kategori = "Suhu Normal"
        elif hasilawal > 21.6:
            kategori = "Suhu Panas"
    elif satuan == "Reamur" and satuan2 == "Kelvin":
        hasilawal = 5/4 * suhu + 273
        hasil = f"{round(hasilawal,2)}°"
        derajat = "°"
        rumus = "5/4 x suhu + 273"
        satuan_hasil = "Kelvin"
        if hasilawal < 291.15:
            kategori = "Suhu Dingin"
        elif hasilawal > 291.15 and hasilawal <= 300.15:
            kategori = "Suhu Normal"
        elif hasilawal > 300.15:
            kategori = "Suhu Panas"

    elif satuan == "Kelvin" and satuan2 == "Celcius":
        hasilawal = suhu - 273
        hasil = round(hasilawal,2)
        derajat = ""
        rumus = "suhu - 273"
        satuan_hasil = "Celcius"
        if hasilawal < 18:
            kategori = "Suhu Dingin"
        elif hasilawal > 18 and hasilawal < 28:
            kategori = "Suhu Normal"
        elif hasilawal > 27:
            kategori = "Suhu Panas"
    elif satuan == "Kelvin" and satuan2 == "Fahrenheit":
        hasilawal = 9/5 * (suhu - 273) + 32
        hasil = round(hasilawal,2)
        derajat = ""
        rumus = "9/5 x (suhu - 273) + 32"
        satuan_hasil = "Fahrenheit"
        if hasilawal < 64:
            kategori = "Suhu Dingin"
        elif hasilawal > 64 and hasilawal < 81:
            kategori = "Suhu Normal"
        elif hasilawal > 80:
            kategori = "Suhu Panas"
    elif satuan == "Kelvin" and satuan2 == "Reamur":
        hasilawal = 9/5 * (suhu - 273)
        hasil = round(hasilawal,2)
        derajat = ""
        rumus = "9/5 x (suhu - 273)"
        satuan_hasil = "Reamur"
        if hasilawal < 14.4:
            kategori = "Suhu Dingin"
        elif hasilawal > 14.4 and hasilawal <= 21.6:
            kategori = "Suhu Normal"
        elif hasilawal > 21.6:
            kategori = "Suhu Panas"
    elif satuan == "Kelvin" and satuan2 == "Kelvin":
        hasilawal = suhu
        hasil = round(hasilawal,2)
        derajat = ""
        rumus = "suhu"
        satuan_hasil = "Kelvin"
        if hasilawal < 291.15:
            kategori = "Suhu Dingin"
        elif hasilawal > 291.15 and hasilawal <= 300.15:
            kategori = "Suhu Normal"
        elif hasilawal > 300.15:
            kategori = "Suhu Panas"

    

    return render_template("konversi.html", suhu=suhu, satuan=satuan, hasil=hasil, hasilawal=hasilawal, rumus=rumus, satuan_hasil=satuan_hasil, derajat=derajat, kategori=kategori)

if __name__ == "__main__":
    app.run(debug=True)


