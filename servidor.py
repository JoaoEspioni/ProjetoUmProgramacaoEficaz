from flask import Flask, render_template, request, redirect
import views

app = Flask(__name__, template_folder='static/templates')
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template("index.html", notes=views.get_notes())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:note_id>', methods=['GET'])
def delete(note_id):
    views.delete_note(note_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)