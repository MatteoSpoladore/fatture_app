import customtkinter as ctk
from Client_page import ClientiPage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Invoice/Client tracker - CustomTkinter")
        self.geometry("800x500")

        # Layout principale: Sidebar + Contenuto
        self.grid_columnconfigure(
            1, weight=1
        )  # Colonna 1 (dove c'è il container) si espande
        self.grid_rowconfigure(0, weight=1)  # Riga 0 si espande

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.create_sidebar()

        # Container per le pagine
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.show_page(HomePage)

    def create_sidebar(self):
        ctk.CTkLabel(self.sidebar, text="Navigazione", font=("Arial", 16)).pack(pady=20)

        ctk.CTkButton(
            self.sidebar, text="Home", command=lambda: self.show_page(HomePage)
        ).pack(pady=10, fill="x", padx=20)
        ctk.CTkButton(
            self.sidebar, text="Pagina 2", command=lambda: self.show_page(PageTwo)
        ).pack(pady=10, fill="x", padx=20)
        ctk.CTkButton(
            self.sidebar,
            text="Gestione Clienti",
            command=lambda: self.show_page(ClientiPage),
        ).pack(pady=10, fill="x", padx=20)

    def show_page(self, page_class):
        if page_class not in self.pages:
            page = page_class(self.container, self)
            self.pages[page_class] = page
            page.grid(row=0, column=0, sticky="nsew")
        self.pages[page_class].tkraise()


# Pagine -------------------------------------
class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ctk.CTkLabel(self, text="🏠 Home Page", font=("Arial", 24)).pack(pady=40)
        ctk.CTkLabel(self, text="Benvenuto nella pagina principale!").pack()


class PageTwo(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ctk.CTkLabel(self, text="📄 Pagina 2", font=("Arial", 24)).pack(pady=40)
        ctk.CTkLabel(self, text="Contenuto della seconda pagina.").pack()


class PageThree(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ctk.CTkLabel(self, text="📊 Pagina 3", font=("Arial", 24)).pack(pady=40)
        ctk.CTkLabel(self, text="Contenuti analitici o altro.").pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
