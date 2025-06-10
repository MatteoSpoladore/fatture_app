import sqlite3
import pandas as pd

# Connessione al database
conn = sqlite3.connect("clienti.db")

# Caricamento dei dati in un DataFrame
df = pd.read_sql_query("SELECT * FROM clienti", conn)


# Visualizzazione del DataFrame
print(df)

# Chiusura della connessione
conn.close()
