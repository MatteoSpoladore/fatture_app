from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    cognome: str
    indirizzo: str
    nome_azienda: str
