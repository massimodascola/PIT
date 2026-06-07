# Spese Moto 🏍️

Tracker dei rifornimenti, dei consumi e delle spese della moto.
App web in **un solo file** (`index.html`), senza backend: i dati restano sul
tuo dispositivo (localStorage del browser). Installabile come **PWA** e
utilizzabile **offline**.

## Funzionalità
- Inserimento rifornimenti: data, km (contachilometri), litri, €/litro, **tipo carburante**.
- Calcoli automatici: costo, km percorsi, **km/litro**, L/100 km, €/km.
- Spese varie (tagliando, gomme, bollo, assicurazione, …).
- Riepilogo: spesa carburante/varie, totale, **consumo medio**, prezzo medio, costo al km.
- 4 grafici (SVG, nessuna dipendenza esterna): consumo, prezzo carburante, spesa per mese, costo al km.
- Backup/ripristino dati in **JSON** ed export **CSV**.

> Il consumo medio esclude i litri dei pieni senza km associati (es. il primissimo
> rifornimento), così la media non viene falsata.

## Uso
Apri l'app, scorri ai moduli "Aggiungi rifornimento" / "Aggiungi spesa varia",
compila e premi **+ Aggiungi**. I dati di esempio spariscono al primo inserimento
(o premi **Svuota tutto**). Fai ogni tanto un **Backup (JSON)**: i dati vivono nel
browser di quel dispositivo, non sul cloud.

In locale: apri direttamente `index.html` nel browser (il service worker si attiva
solo via http/https, quindi l'offline-PWA funziona dalla versione pubblicata).

## Installazione su telefono (PWA)
Apri il link pubblicato (GitHub Pages) sul telefono → menù del browser →
**"Aggiungi a schermata Home"**. Avrai l'icona e l'uso offline.

## Struttura
- `index.html` — l'app completa (UI, logica, grafici).
- `manifest.webmanifest` — metadati PWA (nome, icona, colori).
- `sw.js` — service worker (cache offline; network-first sull'HTML).

### Alternativa su Google Sheets (storico)
`genera_foglio.py` + `spese_moto.csv` sono un primo tentativo che generava un
Google Sheet con le stesse formule. Mantenuti come riferimento; l'app è la via principale.
