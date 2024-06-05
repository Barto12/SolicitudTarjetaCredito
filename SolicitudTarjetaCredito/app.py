from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def index():
    if 'tarjeta' in session:
        return render_template('confirmation.html', tarjeta=session['tarjeta'])
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    ingresos = float(request.form['ingresos'])

    if ingresos < 1:
        return render_template('index.html', error="El ingreso debe ser al menos 1 peso.")

    if ingresos >= 30000:
        limite = 60000
    else:
        limite = 5000

    tarjeta = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'ingresos': ingresos,
        'limite': limite
    }

    session['tarjeta'] = tarjeta
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('tarjeta', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
