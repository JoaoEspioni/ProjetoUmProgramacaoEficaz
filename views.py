from utils import load_data, load_template, add_note, delete_note as remove_note, edit_note as update_note, favorite_note as mark_favorite_note

def get_notes():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            id=dados['id'],
            title=dados['titulo'],
            details=dados['detalhes'],
            favorite_icon='★' if dados['favorito'] else '☆',
            favorite_label='Desfavoritar' if dados['favorito'] else 'Favoritar',
        )
        for dados in load_data()
    ]
    return '\n'.join(notes_li)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)

def delete_note(note_id):
    remove_note(note_id)

def edit_note(note_id, titulo, detalhes):
    update_note(note_id, titulo, detalhes)

def favorite_note(note_id):
    mark_favorite_note(note_id)