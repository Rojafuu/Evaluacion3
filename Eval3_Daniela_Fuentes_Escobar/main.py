from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtenemos el valor del botón presionado
        ejercicio = request.form.get('ejercicio')

        # Si el botón Ejercicio 1 fue presionado
        if ejercicio == '1':
            return redirect(url_for('ejercicio1'))

        # Si el botón Ejercicio 2 fue presionado
        elif ejercicio == '2':
            return redirect(url_for('ejercicio2'))

    # Si el método es GET, renderiza el HTML de inicio
    return render_template('home.html')


@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            # Obtener las notas y la asistencia del formulario
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Verificar que las notas estén entre 10 y 70, y la asistencia entre 0 y 100
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                return "Las notas deben estar entre 10 y 70."
            if not (0 <= asistencia <= 100):
                return "La asistencia debe estar entre 0 y 100."

            # Calcular el promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # Verificar el estado de aprobado o reprobado
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            # Renderizar el resultado
            return render_template('Ejercicio1.html', promedio=promedio, estado=estado)

        except ValueError:
            return "Por favor ingrese valores válidos."

    return render_template('Ejercicio1.html')


@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener los nombres del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Verificar cuál nombre tiene más caracteres
        nombres = [(nombre1, len(nombre1)), (nombre2, len(nombre2)), (nombre3, len(nombre3))]
        nombre_mayor = max(nombres, key=lambda x: x[1])  # Obtener el nombre con más caracteres

        return render_template('Ejercicio2.html', nombre_mayor=nombre_mayor, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)

    return render_template('Ejercicio2.html', nombre1='', nombre2='', nombre3='')



if __name__ == '__main__':
    app.run(debug=True)
