from flask import Flask, render_template, request, redirect
from utils import get_note
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

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        detalhes = request.form.get('detalhes')
        views.edit_note(note_id, titulo, detalhes)
        return redirect('/')
    else:
        return render_template("edit.html", note=get_note(note_id))


@app.route('/favorite/<int:note_id>', methods=['GET'])
def favoritar(note_id):
    
    views.favorite_note(note_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)