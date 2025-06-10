import sqlite3
import tkinter.messagebox as msg
from components.clienti import Cliente

def aggiungi_cliente(nome, cognome, indirizzo, nome_azienda, clear_fields_callback=None):
    try:
        # Normalizza i dati
        cliente = Cliente(
            nome=nome.strip().lower().capitalize(),
            cognome=cognome.strip().lower().capitalize(),
            indirizzo=indirizzo.strip().lower().capitalize(),
            nome_azienda=nome_azienda.strip().lower().capitalize(),
        )

        if not all([cliente.nome, cliente.cognome, cliente.indirizzo, cliente.nome_azienda]):
            msg.showwarning("Campi mancanti", "Compila tutti i campi!")
            return

        conn = sqlite3.connect("./data/clienti.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM clienti WHERE LOWER(nome_azienda) = ?",
            (cliente.nome_azienda.lower(),)
        )
        if cursor.fetchone()[0]:
            msg.showwarning("Duplicato", f"L'azienda '{cliente.nome_azienda}' è già presente nel database.")
            return

        cursor.execute(
            """
            INSERT INTO clienti (nome, cognome, indirizzo, nome_azienda)
            VALUES (?, ?, ?, ?)
            """,
            (cliente.nome, cliente.cognome, cliente.indirizzo, cliente.nome_azienda)
        )
        conn.commit()

        if clear_fields_callback:
            clear_fields_callback()

    except Exception as e:
        msg.showerror("Errore", f"Errore durante l'inserimento: {e}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()
