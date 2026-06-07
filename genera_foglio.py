#!/usr/bin/env python3
"""Genera il CSV 'Spese Moto' da importare in Google Sheets.

Layout (un solo foglio, perche' l'import CSV crea una sola scheda):
  A-J  : RIFORNIMENTI (log carburante)  -> cresce verso il basso
  L-M  : RIEPILOGO (formule di sintesi)
  O-R  : SPESE VARIE (tagliandi, gomme, bollo, assicurazione, ...)

Colonne calcolate in automatico tramite ARRAYFORMULA: bastano le formule
sulla riga 2 e si estendono a tutta la colonna man mano che aggiungi righe.
L'utente compila solo: Data, Km, Litri, EUR/litro, Note (e la tabella SPESE VARIE).
"""
import csv

NCOLS = 18  # A..R

def col(letter):
    return ord(letter) - ord('A')

# griglia di righe; ogni riga e' una lista di NCOLS celle vuote
rows = []
def ensure(r):
    while len(rows) <= r:
        rows.append([""] * NCOLS)

def put(r, c, value):
    ensure(r)
    rows[r][col(c)] = value

# ---- Riga 1: intestazioni ----
put(0, 'A', "Data")
put(0, 'B', "Km (contachilometri)")
put(0, 'C', "Litri")
put(0, 'D', "€/litro")
put(0, 'E', "Costo € (auto)")
put(0, 'F', "Km percorsi (auto)")
put(0, 'G', "km/litro (auto)")
put(0, 'H', "L/100 km (auto)")
put(0, 'I', "€/km (auto)")
put(0, 'J', "Note")
# Spese varie (intestazioni sulla riga 1, colonne O-R)
put(0, 'O', "Data")
put(0, 'P', "Categoria")
put(0, 'Q', "Descrizione")
put(0, 'R', "Importo €")

# Sintassi formule per locale ITALIANO: separatore argomenti ';', decimali ','
# NB: i range DEVONO essere chiusi (es. C2:C1000), non aperti (C2:C):
#     su un foglio importato da CSV i range aperti danno #NAME?.
END = 400
# ---- Riga 2: ARRAYFORMULA (colonne calcolate) + prima riga di esempio ----
put(1, 'E', f'=ARRAYFORMULA(IF(C2:C{END}="";"";C2:C{END}*D2:D{END}))')
put(1, 'F', f'=ARRAYFORMULA(IF(B2:B{END}="";"";IF(ISNUMBER(B1:B{END-1});B2:B{END}-B1:B{END-1};"")))')
# km/l, L/100km, €/km: vuoti se mancano litri O km percorsi (es. primo pieno)
put(1, 'G', f'=ARRAYFORMULA(IFERROR(IF((C2:C{END}="")+(F2:F{END}="");"";F2:F{END}/C2:C{END});""))')
put(1, 'H', f'=ARRAYFORMULA(IFERROR(IF((C2:C{END}="")+(F2:F{END}="");"";C2:C{END}/F2:F{END}*100);""))')
put(1, 'I', f'=ARRAYFORMULA(IFERROR(IF((E2:E{END}="")+(F2:F{END}="");"";E2:E{END}/F2:F{END});""))')
# esempio (riga 2) — decimali con la virgola
put(1, 'A', "01/06/2026")
put(1, 'B', 10000)
put(1, 'C', 15)
put(1, 'D', "1,85")
put(1, 'J', "esempio – sostituisci")
# esempio spese varie (riga 2, O-R)
put(1, 'O', "05/06/2026")
put(1, 'P', "Tagliando")
put(1, 'Q', "Cambio olio + filtri")
put(1, 'R', 120)

# ---- Riga 3: secondo esempio (solo input; le formule scendono da sole) ----
put(2, 'A', "08/06/2026")
put(2, 'B', 10250)
put(2, 'C', 14)
put(2, 'D', "1,90")
put(2, 'J', "esempio – sostituisci")

# ---- Riepilogo (colonne L-M) ----
put(0, 'L', "— RIEPILOGO CARBURANTE —")
put(1, 'L', "Spesa totale (€)");          put(1, 'M', f"=SUM(E2:E{END})")
put(2, 'L', "Litri totali");              put(2, 'M', f"=SUM(C2:C{END})")
put(3, 'L', "Km percorsi totali");        put(3, 'M', f"=SUM(F2:F{END})")
# Medie per-distanza: escludono i litri/costi dei pieni senza km (es. il 1°).
# Denominatore = litri solo delle righe con km percorsi > 0.
put(4, 'L', "Consumo medio (km/l)");      put(4, 'M', f'=IFERROR(SUM(F2:F{END})/SUMIF(F2:F{END};">0";C2:C{END});"")')
put(5, 'L', "Consumo medio (L/100km)");   put(5, 'M', f'=IFERROR(SUMIF(F2:F{END};">0";C2:C{END})/SUM(F2:F{END})*100;"")')
put(6, 'L', "Costo medio (€/km)");        put(6, 'M', f'=IFERROR(SUMIF(F2:F{END};">0";E2:E{END})/SUM(F2:F{END});"")')
put(7, 'L', "Prezzo medio (€/litro)");    put(7, 'M', '=IFERROR(M2/M3;"")')
put(8, 'L', "N° rifornimenti");           put(8, 'M', f"=COUNT(C2:C{END})")
put(10, 'L', "— SPESE VARIE —")
put(11, 'L', "Totale spese varie (€)");   put(11, 'M', f"=SUM(R2:R{END})")
put(12, 'L', "TOTALE GENERALE (€)");      put(12, 'M', "=M2+M12")

# Padding: righe vuote pronte all'uso (comodita'). Le formule (range :400)
# funzionano comunque anche oltre la griglia, verificato empiricamente.
GRID = 150
ensure(GRID - 1)

with open("spese_moto.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for row in rows:
        w.writerow(row)

print(f"Scritte {len(rows)} righe x {NCOLS} colonne in spese_moto.csv")
