# Pit

**Pit** tracks your vehicles' fill-ups, fuel consumption, expenses and deadlines.
A web app in **a single file** (`index.html`) with no backend: your data stays
on your device (the browser's localStorage). It installs as a **PWA** and works
**offline**.

**[Open the app](https://massimodascola.github.io/pit/)** · [Leggi in italiano](README.it.md)

> **Language:** the app's interface is in Italian. This README is in English;
> an Italian translation is in [README.it.md](README.it.md).

## Using it on your phone

Open **[massimodascola.github.io/pit](https://massimodascola.github.io/pit/)** on your phone, then:

* **iPhone (Safari)**: Share → **Add to Home Screen**.
* **Android (Chrome)**: menu ⋮ → **Add to Home screen** or **Install app**.

You get an icon on the Home Screen and the app works offline. Your data stays
on the device: everyone who opens the link starts from zero.

## Features

* **Guided setup on first launch** (three steps): vehicle, fuel and starting
  mileage, main deadlines. "Ho già un backup" (I already have a backup)
  restores from a JSON file or from the sync Gist.
* **Four tabs**: Overview, Fill-ups, Expenses, Deadlines (bar at the bottom).
* **Several vehicles**: switch vehicle by tapping its name at the top of the
  Overview; a new vehicle is added with the same guided setup.
* **Fill-ups**: list by month with the km/l of each fill-up (best in green,
  worst in red), totals for the chosen year and a **fuel station comparison**
  at the bottom. Consumption is calculated "from full tank to full tank":
  top-ups are merged into the next full fill-up.
* **Expenses**: yearly total beyond fuel, bars by category, list.
* **Deadlines** color-coded by urgency (overdue / within 30 days / ok); the
  upcoming ones also appear in the Overview.
* **Analysis** (tap the big figure): spending by month, consumption, price paid
  per fuel, cost per km, totals.
* **Units per fuel**: liters for petrol, diesel and LPG; kg for natural gas
  (CNG); kWh for electric.
* **Receipt scan with AI**: in the "Nuovo pieno" (new fill-up) sheet, a photo
  and a vision service (Anthropic, OpenAI or Google, with *your own* API key,
  stored only on the device) fill in date, liters, price and station.
* **Sync between devices through a GitHub Gist** (token with the `gist` scope,
  stored only on the device).
* Backup and restore as **JSON** (all vehicles) and **CSV** export (current
  vehicle).

Settings (vehicles, AI key, sync, backup) are in the menu at the top right of
the Overview.

## Design (v2)

* **Paper, ink, a single accent**: background `#F7F5F1`, text `#15140F`, Pit
  red `#D6442B` only for actions and signals. Numbers in **IBM Plex Mono**,
  text in **Schibsted Grotesk** (Google Fonts, cached by the service worker for
  offline use).
* **Follows the device theme**: light "paper" or dark "night in the workshop"
  (background `#131211`, surfaces `#1C1B18`, text `#F4F1EA`, signal `#FF5A3D`),
  automatically and without reloading. All colors are CSS variables at the top
  of `index.html`.
* **One number that matters per screen**: the Overview shows the month's
  spending, the comparison with the previous month, the last six months, the
  consumption of the last six fill-ups (the all-time average dashed) and two
  indicators (cost per km, price per liter).
* **Adding is an action**: Fill-ups, Expenses and Deadlines open on the list;
  the form appears in a sheet from the red "+" button. Tap an entry to edit or
  delete it.

## Privacy

* All data stays in the browser's `localStorage`. No server, no telemetry.
* The AI receipt scan is optional: the photo goes straight from your device to
  the provider you chose, with your own key.
* The optional Gist sync stores your data in a secret Gist on your own GitHub
  account. The token stays on the device; if the device is compromised, revoke
  it on GitHub (Settings → Developer settings → Personal access tokens).
* Fonts are loaded from Google Fonts on first use, then cached.

## Data and compatibility

Data lives in the `moto_data_v1` localStorage key, schema `v2`. Design v2 adds
two optional fields to each vehicle: `fuel` (main fuel) and `kmStart` (starting
mileage from the setup). Data and backups from the previous version open
without conversion and without going through the setup.

## Running it locally

Open `index.html` directly in the browser, or serve the folder (for example
`python3 -m http.server`): the service worker and offline use only work over
http/https.

To publish your own copy, fork this repository and turn on **Settings → Pages →
Branch: `main`, folder: `/ (root)`**.

## Structure

* `index.html`: the whole app (UI, logic, SVG charts).
* `manifest.webmanifest`: PWA metadata (name, icon, colors).
* `sw.js`: service worker (offline cache; network-first on the HTML, fonts
  cached).
* `icon-180.png`, `icon-192.png`, `icon-512.png`: Home Screen icons.

## License

MIT, see [LICENSE](LICENSE). Made by [Massimo D'Ascola](https://github.com/massimodascola).
