from utils import load_data, load_template, save_data
from flask import render_template_string

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return render_template_string(load_template('index.html'), notes=notes)

def submit(titulo,detalhes):
    data = { "titulo": titulo,
        "detalhes": detalhes,
    }
    save_data(data)