# Guida Installazione PWA - TauroBot 3.0 Ultimate

## 📱 Cos'è una Progressive Web App (PWA)?

Una PWA è un'applicazione web che può essere installata sul tuo dispositivo (Android, iOS, Desktop) e funziona come un'app nativa, anche offline!

## ✨ Vantaggi della PWA TauroBot

- 📲 **Installabile**: Aggiungi l'app alla home screen
- 🚀 **Veloce**: Caricamento istantaneo con cache
- 📴 **Offline**: Funziona anche senza connessione
- 🔔 **Notifiche**: Supporto per push notifications (futuro)
- 💾 **Leggera**: Nessun download da store, meno spazio
- 🔄 **Auto-update**: Aggiornamenti automatici

## 📋 Requisiti

- Server web (HTTPS obbligatorio per PWA)
- Browser moderno (Chrome, Firefox, Safari, Edge)

## 🚀 Setup Rapido

### 1. Genera le Icone

```bash
# Genera le icone SVG
python generate_pwa_icons.py

# Converti SVG in PNG (opzionale, usa uno di questi metodi):
# Metodo 1: ImageMagick
for size in 72 96 128 144 152 192 384 512; do
    convert icons/icon-${size}x${size}.svg icons/icon-${size}x${size}.png
done

# Metodo 2: Online converter
# Carica i file SVG su https://cloudconvert.com/svg-to-png
```

### 2. Configura il Server Web

La PWA richiede HTTPS. Opzioni:

#### Opzione A: Server locale con HTTPS (per test)
```bash
# Installa mkcert per certificati locali
# Su macOS: brew install mkcert
# Su Linux: apt install mkcert

# Crea certificati
mkcert -install
mkcert localhost

# Avvia server HTTPS
python -m http.server 8443 --bind localhost
```

#### Opzione B: GitHub Pages per il sito statico

La presentazione pubblica DIBORACULUM è predisposta per GitHub Pages dalla cartella `docs/`. Questo pubblica soltanto i file statici scelti e non avvia il bot, non configura un backend e non rende verificata la PWA TauroBot.

### 3. Pubblicazione del sito DIBORACULUM

Per il sito statico, seleziona in GitHub **Settings → Pages → Deploy from a branch → main → /docs**. I dettagli su dominio, DNS e HTTPS sono in [reports/GITHUB_DEPLOYMENT.md](reports/GITHUB_DEPLOYMENT.md).

Questa procedura non pubblica né certifica il funzionamento dell'applicazione TauroBot descritta in questa guida. Non sono configurati provider alternativi in questo repository.

## 📲 Come Installare la PWA

### Su Android (Chrome)

1. Apri il sito in Chrome
2. Clicca sul pulsante "📱 Installa App" che appare
   - OPPURE: Menu (⋮) → "Aggiungi a schermata Home"
3. Conferma l'installazione
4. L'app apparirà nella home screen!

### Su iOS (Safari)

1. Apri il sito in Safari
2. Tocca il pulsante Condividi (⬆️)
3. Scorri e tocca "Aggiungi a Home"
4. Conferma e dai un nome all'app
5. L'icona apparirà nella home screen!

### Su Desktop (Chrome/Edge)

1. Apri il sito in Chrome o Edge
2. Guarda la barra degli indirizzi per l'icona di installazione (+)
3. Clicca su "Installa"
4. L'app si aprirà in una finestra dedicata!

## 🔧 Personalizzazione

### Modificare i Colori

Modifica `manifest.json`:
```json
{
  "background_color": "#1a1a2e",  // Colore sfondo splash screen
  "theme_color": "#667eea"        // Colore barra superiore
}
```

### Modificare il Nome

Modifica `manifest.json`:
```json
{
  "name": "Il Tuo Nome Completo",
  "short_name": "Nome Corto"  // Max 12 caratteri per home screen
}
```

### Aggiungere Funzionalità Offline

Il Service Worker in `service-worker.js` gestisce la cache. Aggiungi file alla lista:
```javascript
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/style.css',      // Aggiungi altri file
  '/script.js'
];
```

## 🧪 Test della PWA

### Lighthouse (Chrome DevTools)

1. Apri Chrome DevTools (F12)
2. Tab "Lighthouse"
3. Seleziona "Progressive Web App"
4. Clicca "Generate report"
5. Verifica il punteggio (target: >90)

### Test Manuale

- ✅ Installazione funziona
- ✅ App si apre in modalità standalone
- ✅ Funziona offline (dopo prima visita)
- ✅ Icona appare correttamente
- ✅ Splash screen appare al lancio
- ✅ Service Worker registrato

## 🔍 Debugging

### Service Worker non si registra
```bash
# Verifica HTTPS
# Controlla console browser per errori
# Assicurati che service-worker.js sia accessibile
```

### Icone non appaiono
```bash
# Verifica che i file esistano in /icons/
# Controlla percorsi in manifest.json
# Verifica MIME type (deve essere image/png)
```

### Cache non funziona
```bash
# Apri DevTools → Application → Service Workers
# Clicca "Unregister" e ricarica
# Verifica liste urlsToCache in service-worker.js
```

## 📊 Monitoring

Dopo il deploy, monitora:
- **Google Search Console**: Errori PWA
- **Browser DevTools**: Network, Cache, Service Worker
- **Verifica manuale**: caricamento, installazione e service worker

## 🎯 Prossimi Passi

1. ✅ Genera e aggiungi icone PNG
2. ✅ Testa localmente con HTTPS
3. ✅ Verifica GitHub Pages dalla cartella docs/
4. ✅ Test su dispositivi reali
5. ✅ Condividi il link!

## 🆘 Supporto

Se hai problemi:
1. Controlla la console del browser (F12)
2. Verifica che il sito sia servito su HTTPS
3. Prova in modalità incognito
4. Apri una issue su GitHub

## 🎉 Congratulazioni!

Ora hai una PWA funzionante che gli utenti possono installare come app nativa! 🚀

---

*TauroBot 3.0 Ultimate - PWA Edition*
