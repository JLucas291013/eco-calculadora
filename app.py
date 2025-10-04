from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
          
@app.route("/<size>")
def size(size):
    return render_template ('lamparas.html',
                            size_home=size)

@app.route("/<size>/<num_lamparas>")
def dispozitivos (size,num_lamparas):
    print(f"size: {size}, num_lamparas: {num_lamparas}")
    return render_template('dispozitivos.html',
                           size_home=size,
                           num_lamparas=num_lamparas)

@app.route("/<size>/<num_lamparas>/<num_dispositivos>")
def nose ( size ,num_lamparas, num_dispositivos):
    factor_casa_grande = 1000
    factor_casa_mediana = 500
    factor_casa_pequeña = 250

    factor_lampara = int(num_lamparas)*10
    factor_dispositivo = int(num_dispositivos)*150

    if int(size) == 1:
        total_consumo = factor_casa_pequeña + factor_lampara + factor_dispositivo
    elif int(size) == 2:
        total_consumo = factor_casa_mediana + factor_lampara + factor_dispositivo

    elif int(size) == 3:
        total_consumo = factor_casa_grande + factor_lampara + factor_dispositivo

    print(f"size: {size}, num_lamparas: {num_lamparas}, num_dispositivos: {num_dispositivos}")
    return render_template('nose.html',
                           total_consumo=total_consumo)

app.run(debug=True)