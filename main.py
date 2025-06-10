import customtkinter as ctk
import sqlite3
from compoonents.clienti import Cliente
import tkinter.messagebox as msg



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Registra fatture")
        self.geometry("900x500")

        span_x = 50
        label_width = 300
        entry_width = 300

        # Colonna 0
        self.nome_label = ctk.CTkLabel(
            master=self, text="Nome", width=label_width, justify="center"
        )
        self.nome_label.grid(row=0, column=0, padx=span_x, pady=(20, 0))

        self.nome_entry = ctk.CTkEntry(
            master=self, width=entry_width, placeholder_text="nome..."
        )
        self.nome_entry.grid(row=1, column=0, padx=span_x, pady=(0, 20))

        self.cognome_label = ctk.CTkLabel(
            master=self, text="Cognome", width=label_width, justify="center"
        )
        self.cognome_label.grid(row=2, column=0, padx=span_x, pady=(20, 0))

        self.cognome_entry = ctk.CTkEntry(
            master=self, width=entry_width, placeholder_text="cognome..."
        )
        self.cognome_entry.grid(row=3, column=0, padx=span_x, pady=(0, 20))

        # Colonna 1
        self.indirizzo_label = ctk.CTkLabel(
            master=self, text="Indirizzo", width=label_width, justify="center"
        )
        self.indirizzo_label.grid(row=0, column=1, padx=span_x, pady=(20, 0))

        self.indirizzo_entry = ctk.CTkEntry(
            master=self, width=entry_width, placeholder_text="indirizzo..."
        )
        self.indirizzo_entry.grid(row=1, column=1, padx=span_x, pady=(0, 20))

        self.azienda_label = ctk.CTkLabel(
            master=self, text="Nome azienda", width=label_width, justify="center"
        )
        self.azienda_label.grid(row=2, column=1, padx=span_x, pady=(20, 0))

        self.azienda_entry = ctk.CTkEntry(
            master=self, width=entry_width, placeholder_text="nome azienda..."
        )
        self.azienda_entry.grid(row=3, column=1, padx=span_x, pady=(0, 20))

        # Configura le colonne per ridimensionamento
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.add_btn = ctk.CTkButton(
            master=self, text="Aggiungi cliente", command=self.aggiungi_cliente
        )
        self.add_btn.grid(row=4, column=0, pady=10)

        self.show_btn = ctk.CTkButton(
            master=self, text="Aggiungi cliente", command=self.mostra_clienti
        )
        self.show_btn.grid(row=4, column=1, pady=10)

    def aggiungi_cliente(self):

        try:
            # Normalizzazione nome_azienda
            nome_azienda = self.azienda_entry.get().strip().lower().capitalize()

            # Creazione oggetto Cliente con azienda normalizzata
            cliente = Cliente(
                nome=self.nome_entry.get().strip().lower().capitalize(),
                cognome=self.cognome_entry.get().strip().lower().capitalize(),
                indirizzo=self.indirizzo_entry.get().strip().lower().capitalize(),
                nome_azienda=nome_azienda,
            )

            # Verifica che tutti i campi siano compilati
            if not all(
                [cliente.nome, cliente.cognome, cliente.indirizzo, cliente.nome_azienda]
            ):
                msg.showwarning("Campi mancanti", "Compila tutti i campi!")
                return

            # Connessione al DB
            conn = sqlite3.connect("./data/clienti.db")
            cursor = conn.cursor()

            # Verifica se nome_azienda esiste già (ignora maiuscole/minuscole)
            cursor.execute(
                "SELECT COUNT(*) FROM clienti WHERE LOWER(nome_azienda) = ?",
                (cliente.nome_azienda.lower(),),
            )
            esiste = cursor.fetchone()[0]

            if esiste:
                msg.showwarning(
                    "Duplicato",
                    f"L'azienda '{cliente.nome_azienda}' è già presente nel database.",
                )
                return

            # Inserimento nel DB
            cursor.execute(
                """
                INSERT INTO clienti (nome, cognome, indirizzo, nome_azienda)
                VALUES (?, ?, ?, ?)
                """,
                (
                    cliente.nome,
                    cliente.cognome,
                    cliente.indirizzo,
                    cliente.nome_azienda,
                ),
            )
            conn.commit()

            # Conferma visiva e pulizia dei campi
            # TODO
            # msg.showinfo(
            #     "Successo",
            #     f"Cliente per '{cliente.nome_azienda}' aggiunto correttamente!",
            # )
            self.nome_entry.delete(0, "end")
            self.cognome_entry.delete(0, "end")
            self.indirizzo_entry.delete(0, "end")
            self.azienda_entry.delete(0, "end")

        except Exception as e:
            msg.showerror("Errore", f"Errore durante l'inserimento: {e}")
        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                conn.close()

    # TODO
    # def mostra_successo(messaggio, positive=True):
    #     # Aggiorna il testo e lo stile della label di stato
    #     if positive:
    #         colore = "lightgreen"
    #         bg_colore = "darkgreen"
    #     else:
    #         colore = "lightred"
    #         bg_colore = "darkred"
    #         status_label.config(text=messaggio, bg=colore, fg=bg_colore)

    def mostra_clienti(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
