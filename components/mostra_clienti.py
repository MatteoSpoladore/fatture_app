import customtkinter as ctk
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as msg


class ClientiView(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Modifica clienti registrati")
        self.geometry("900x400")

        self.transient(master)
        self.grab_set()  # opzione: blocca interazione con master finché è aperta
        self.focus_set()  # porta il focus sulla finestra

        self.columns = ("id", "nome", "cognome", "indirizzo", "nome_azienda")

        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        for col in self.columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(fill="both", expand=True)

        self.edit_entry = None

        self.carica_dati()

        self.tree.bind("<Double-1>", self.on_double_click)

    def carica_dati(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("./data/clienti.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cognome, indirizzo, nome_azienda FROM clienti")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        cursor.close()
        conn.close()

    def on_double_click(self, event):
        if self.edit_entry is not None:
            return

        region = self.tree.identify("region", event.x, event.y)
        if region != "cell":
            return

        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        if not row_id or column == "#1":  # non modificare id
            return

        x, y, width, height = self.tree.bbox(row_id, column)
        valore_corrente = self.tree.set(row_id, column)

        tree_x = self.tree.winfo_rootx()
        tree_y = self.tree.winfo_rooty()
        self_x = self.winfo_rootx()
        self_y = self.winfo_rooty()

        rel_x = tree_x - self_x  # + x
        rel_y = tree_y - self_y + y

        self.edit_entry = ctk.CTkEntry(self, width=width, height=height)
        self.edit_entry.place(x=rel_x, y=rel_y + height)

        self.edit_entry.insert(0, valore_corrente)
        self.edit_entry.focus()

        def salva_modifica(event=None):  # event è corretto per usare bind dopo
            nuovo_valore = self.edit_entry.get().strip()
            col_idx = int(column.replace("#", "")) - 1

            if nuovo_valore == valore_corrente or nuovo_valore == "":
                self.edit_entry.destroy()
                self.edit_entry = None
                return

            self.tree.set(row_id, column, nuovo_valore)
            cliente_id = self.tree.set(row_id, "id")
            nomi_colonne = ["id", "nome", "cognome", "indirizzo", "nome_azienda"]
            col_name = nomi_colonne[col_idx]

            try:
                conn = sqlite3.connect("./data/clienti.db")
                cursor = conn.cursor()
                query = f"UPDATE clienti SET {col_name} = ? WHERE id = ?"
                cursor.execute(query, (nuovo_valore, cliente_id))
                conn.commit()
                cursor.close()
                conn.close()
            except Exception as e:
                msg.showerror("Errore aggiornamento", f"Errore: {e}")

            self.edit_entry.destroy()
            self.edit_entry = None

        self.edit_entry.bind("<Return>", salva_modifica)
        self.edit_entry.bind(
            "<FocusOut>",
            lambda e: self.edit_entry.destroy() or setattr(self, "edit_entry", None),
        )
