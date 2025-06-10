import customtkinter as ctk
import sqlite3
from components.clienti import Cliente
from components.mostra_clienti import ClientiView
from components.aggiungi_cliente import aggiungi_cliente as aggiungi_cliente_fin
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
            master=self, text="Mostra clienti", command=self.mostra_clienti
        )
        self.show_btn.grid(row=4, column=1, pady=10)

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
    app = App()
    app.mainloop()
