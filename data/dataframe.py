import sqlite3

conn = sqlite3.connect("clienti.db")
cursor = conn.cursor()

# Creazione tabella se non esiste già
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS clienti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    indirizzo TEXT NOT NULL,
    nome_azienda TEXT NOT NULL UNIQUE
)
"""
)

# cursor.execute("DELETE FROM clienti;")
conn.commit()
conn.close()
