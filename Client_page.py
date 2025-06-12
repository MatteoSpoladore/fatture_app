import customtkinter as ctk

# import sqlite3
# from components.clienti import Cliente
from components.mostra_clienti import ClientiView
from components.aggiungi_cliente import aggiungi_cliente as aggiungi_cliente_fin
import tkinter.messagebox as msg


class ClientiPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        # class App(ctk.CTk):
        #     def __init__(self):
        #         super().__init__()
        #         self.title("Registra Clienti")
        #         self.geometry("900x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.nome_entry = self.crea_label_entry("Nome", "nome...", 0, 0)
        self.cognome_entry = self.crea_label_entry("Cognome", "cognome...", 2, 0)
        self.indirizzo_entry = self.crea_label_entry("Indirizzo", "indirizzo...", 0, 1)
        self.azienda_entry = self.crea_label_entry(
            "Nome azienda", "nome azienda...", 2, 1
        )

        self.crea_bottoni()

    def crea_label_entry(self, testo, placeholder, row, col):
        label = ctk.CTkLabel(self, text=testo, justify="center", width=300)
        label.grid(row=row, column=col, padx=50, pady=(20, 0))
        entry = ctk.CTkEntry(self, width=300, placeholder_text=placeholder)
        entry.grid(row=row + 1, column=col, padx=50, pady=(0, 20))
        return entry

    def crea_bottoni(self):
        ctk.CTkButton(
            self, text="Aggiungi cliente", command=self.aggiungi_cliente
        ).grid(row=4, column=0, pady=10)
        ctk.CTkButton(self, text="Mostra clienti", command=self.mostra_clienti).grid(
            row=4, column=1, pady=10
        )

    def aggiungi_cliente(self):
        aggiungi_cliente_fin(
            nome=self.nome_entry.get(),
            cognome=self.cognome_entry.get(),
            indirizzo=self.indirizzo_entry.get(),
            nome_azienda=self.azienda_entry.get(),
            clear_fields_callback=self.clear_entries,  # funzione che pulisce i campi
        )

    def clear_entries(self):
        self.nome_entry.delete(0, "end")
        self.cognome_entry.delete(0, "end")
        self.indirizzo_entry.delete(0, "end")
        self.azienda_entry.delete(0, "end")

    def mostra_clienti(self):
        ClientiView(self)


if __name__ == "__main__":
    app = ClientiPage()
    app.mainloop()
