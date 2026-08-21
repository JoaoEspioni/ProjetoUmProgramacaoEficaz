from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "banco.db"
TEMPLATE_DIRS = [
    BASE_DIR / "static" / "templates",
    BASE_DIR / "templates",
]


def _get_connection():
    return sqlite3.connect(DB_PATH)


def _initialize_database():
    with _get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )

        tabela_nota_existe = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='nota'"
        ).fetchone()

        if tabela_nota_existe:
            conn.execute(
                "INSERT INTO note (title, content) SELECT titulo, detalhes FROM nota"
            )
            conn.execute("DROP TABLE nota")

def load_data():
    _initialize_database()

    with _get_connection() as conn:
        linhas = conn.execute(
            "SELECT id, title, content FROM note ORDER BY id"
        ).fetchall()

    return [
        {"id": nota_id, "titulo": titulo, "detalhes": detalhes}
        for nota_id, titulo, detalhes in linhas
    ]

def load_template(nome_arquivo):
    for template_dir in TEMPLATE_DIRS:
        caminho = template_dir / nome_arquivo
        if caminho.exists():
            with open(caminho, encoding="utf-8") as f:
                return f.read()

    raise FileNotFoundError(
        f"Template '{nome_arquivo}' nao encontrado em: "
        + ", ".join(str(d) for d in TEMPLATE_DIRS)
    )

def add_note(titulo, detalhes):
    _initialize_database()

    with _get_connection() as conn:
        conn.execute(
            "INSERT INTO note (title, content) VALUES (?, ?)",
            (titulo, detalhes),
        )
