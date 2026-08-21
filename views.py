from utils import load_data, load_template, add_note

def get_notes():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    return '\n'.join(notes_li)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)