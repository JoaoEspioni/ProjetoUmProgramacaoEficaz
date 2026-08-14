import json
from pathlib import Path


def load_data(nome_arquivo='notes.json'):
    caminho_arquivo = Path(__file__).resolve().parent / 'static' / 'data' / nome_arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_template(nome_template):
    base_dir = Path(__file__).resolve().parent
    caminho_template = base_dir / 'static' / 'templates' / nome_template

    with open(caminho_template, 'r', encoding='utf-8') as file:
        template = file.read()
    return template