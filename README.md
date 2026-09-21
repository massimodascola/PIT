# Pit

**Pit** — tracker dei pieni, dei consumi, delle spese e delle scadenze dei tuoi veicoli.
App web in **un solo file** (`index.html`), senza backend: i dati restano sul
tuo dispositivo (localStorage del browser). Installabile come **PWA** e
utilizzabile **offline**.

## Design (v2)
- **Carta, inchiostro, un solo accento**: fondo `#F7F5F1`, testo `#15140F`,
  rosso Pit `#D6442B` solo per azioni e segnali. Numeri in **IBM Plex Mono**,
  testi in **Schibsted Grotesk** (Google Fonts, messi in cache dal service worker
  per l'uso offline).
- **Segue il tema del dispositivo**: chiaro «carta» o scuro «notte in officina»
  (fondo `#131211`, superfici `#1C1B18`, testo `#F4F1EA`, segnale `#FF5A3D`),
  in automatico e senza ricaricare. I colori stanno tutti nelle variabili CSS
  in cima a `index.html`.
- **Un numero che conta per schermata**: la Panoramica mostra la spesa del mese,
  il confronto con il mese prima, gli ultimi sei mesi, il consumo degli ultimi
  sei pieni (tratteggiata la media di sempre) e due indicatori (costo al km,
  prezzo al litro).
- **Inserire è un'azione**: Pieni, Spese e Scadenze si aprono sulla lista; il
  modulo compare in una sheet dal pulsante rosso «+». Toccando una voce la si
  modifica o elimina.

## Funzionalità
- **Setup guidato al primo avvio** (tre passi): veicolo, carburante e km di
  partenza, scadenze principali. «Ho già un backup» ripristina da file JSON o dal
  Gist della sincronizzazione.
- **Quattro schede**: Panoramica, Pieni, Spese, Scadenze (barra in basso).
- **Più veicoli**: si cambia veicolo toccando il nome in alto nella Panoramica;
  un veicolo nuovo si aggiunge con lo stesso setup guidato.
- **Pieni**: lista per mese con km/l di ogni pieno (migliore in verde, peggiore in
  rosso), totali dell'anno scelto e **confronto distributori** in fondo.
  Calcolo del consumo «da pieno a pieno»: i rabbocchi confluiscono nel pieno dopo.
- **Spese**: totale dell'anno oltre al carburante, barre per categoria, elenco.
- **Scadenze** con urgenza a colori (scaduta / entro 30 giorni / ok); quelle
  vicine compaiono anche in Panoramica.
- **Analisi** (toccando la cifra grande): spesa per mese, consumo, prezzo pagato
  per carburante, costo al km, totali.
- **Unità per carburante**: litri per benzina, diesel e GPL; kg per il metano;
  kWh per l'elettrico.
- **Scansione scontrino con AI**: nella sheet «Nuovo pieno», una foto e un
  servizio di visione (Anthropic, OpenAI o Google, con la *tua* chiave API,
  salvata solo sul dispositivo) compila data, litri, prezzo e benzinaio.
- **Sincronizzazione tra dispositivi via GitHub Gist** (token con scope `gist`,
  salvato solo sul dispositivo).
- Backup/ripristino in **JSON** (tutti i veicoli) ed export **CSV** (veicolo in uso).

Impostazioni (veicoli, chiave AI, sincronizzazione, backup) stanno nel menù
in alto a destra della Panoramica.

## Dati e compatibilità
I dati restano nella chiave `moto_data_v1` del localStorage, schema `v2`.
La v2 del design aggiunge al veicolo due campi facoltativi: `fuel` (carburante
principale) e `kmStart` (km di partenza dal setup). I dati e i backup della
versione precedente si aprono senza conversioni e senza passare dal setup.

## Uso in locale
Apri direttamente `index.html` nel browser, oppure servi la cartella
(es. `python3 -m http.server`): il service worker e l'uso offline funzionano
solo via http/https.

## Installazione su telefono (PWA)
Apri il link pubblicato (GitHub Pages) sul telefono → menù del browser →
**"Aggiungi a schermata Home"**. Avrai l'icona e l'uso offline.

## Struttura
- `index.html` — l'app completa (UI, logica, grafici SVG).
- `manifest.webmanifest` — metadati PWA (nome, icona, colori).
- `sw.js` — service worker (cache offline; network-first sull'HTML, font in cache).
- `icon-180.png`, `icon-192.png`, `icon-512.png` — icone della home screen.
