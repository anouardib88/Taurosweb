# DIBORACULUM — sito pubblico e repository Taurosweb

## Il sito pubblico

DIBORACULUM è una presentazione informativa di un progetto software in sviluppo. Il sito non dichiara l'applicazione pronta all'uso e non offre login o contenuti privati.

- Sorgenti del sito: [docs/](https://github.com/anouardib88/Taurosweb/tree/main/docs)
- Repository: [anouardib88/Taurosweb](https://github.com/anouardib88/Taurosweb)
- Contributi e segnalazioni: [GitHub Issues](https://github.com/anouardib88/Taurosweb/issues)
- Pubblicazione GitHub Pages e dominio: [reports/GITHUB_DEPLOYMENT.md](reports/GITHUB_DEPLOYMENT.md)
- Piano e audit: [piano d'azione](DIBORACULUM_ACTION_PLAN.md), [sicurezza](reports/SECURITY_REPORT.md), [repository](reports/REPOSITORY_AUDIT.md), [red team](reports/RED_TEAM_REPORT.md), [SEO](reports/SEO_AUDIT.md), [contenuti e CTA](reports/CONTENT_CTA_REPORT.md)

La pubblicazione è predisposta per GitHub Pages dalla cartella `docs/` del branch `main`. Per un'anteprima locale:

```bash
python3 -m http.server 8000 --directory docs
```

Il dominio richiesto è `diboracullum.com` (due “l” consecutive). Il repository storico riporta `diboraculum.com` (una “l”). I metadati del nuovo sito seguono la grafia richiesta; CNAME, Pages, proprietà del dominio e DNS restano da verificare prima della pubblicazione. Anche la relazione tra DIBORACULUM e il codice TauroBot/Taurosweb presente nel repository va chiarita prima di descrivere funzioni di prodotto.

## Taurosweb — contenuti applicativi del repository


![Avatar del proprietario](https://avatars.githubusercontent.com/u/198739241?s=48&v=4)

### Descrizione
Taurosweb contiene il codice, le configurazioni e la PWA storica di **TauroBot 3.0** per Telegram. Le descrizioni funzionali che seguono provengono dai documenti preesistenti; il servizio e le singole funzioni non sono stati verificati in questo audit.

---

## Caratteristiche principali
- **Integrazione con Ollama:** Gestione avanzata delle conversazioni con memoria contestuale.
- **Memoria persistente:** Capacità di ricordare informazioni tra le sessioni per una migliore continuità.
- **Sintesi vocale:** Supporto per la conversione testo-voce per risposte vocali.
- **Anima hacker:** Funzionalità avanzate e personalizzabili per utenti esperti.
- **Compatibilità Telegram:** Facile integrazione e utilizzo tramite la piattaforma Telegram.
- **📱 Progressive Web App (PWA):** Installabile su Android, iOS e Desktop come app nativa!
- **🐳 Docker Ready:** Containerizzazione completa con docker-compose
- **🌍 Multi-lingua:** il repository contiene file di localizzazione; copertura runtime da verificare
- **🛡️ Rate Limiting:** Protezione anti-spam integrata
- **⚙️ CI/CD:** GitHub Actions per test automatici e deploy

---

## Stato del progetto

- Il repository contiene il codice di TauroBot e il sito informativo DIBORACULUM in `docs/`.
- DIBORACULUM è in sviluppo. La presenza di una funzione nel README non prova che il servizio sia attualmente online o pronto per produzione.
- Il repository è pubblico; non sono state trovate release GitHub pubblicate nell'audit.

## Installazione

⚠️ **Per istruzioni dettagliate di installazione, vedi [INSTALL.md](INSTALL.md)**

### Quick Start

#### Metodo 1: Automatico (Consigliato)
1. Clona il repository:
   ```bash
   git clone https://github.com/anouardib88/Taurosweb.git
   cd Taurosweb
   ```
2. Esegui lo script di setup:
   ```bash
   ./setup.sh
   ```
3. Configura il tuo token in `.env`
4. Avvia Ollama:
   ```bash
   ollama serve
   ```
5. Avvia il bot:
   ```bash
   ./run.sh
   # oppure
   python3 run.py
   ```

#### Metodo 2: Manuale
1. Clona il repository:
   ```bash
   git clone https://github.com/anouardib88/Taurosweb.git
   cd Taurosweb
   ```
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura le variabili d'ambiente:
   ```bash
   cp .env.example .env
   # Modifica .env con il tuo TELEGRAM_BOT_TOKEN
   ```
4. Avvia Ollama:
   ```bash
   ollama serve
   ```
5. Avvia il bot:
   ```bash
   python bot.py
   ```

#### Metodo 3: Docker (Raccomandato per produzione)
```bash
# Clona e configura
git clone https://github.com/anouardib88/Taurosweb.git
cd Taurosweb
cp .env.example .env
# Modifica .env con il tuo TELEGRAM_BOT_TOKEN

# Avvia tutto con Docker Compose
docker-compose up -d

# Scarica un modello Ollama
docker exec -it ollama ollama pull llama2

# Visualizza i log
docker-compose logs -f taurobot
```

Per maggiori dettagli, consulta la [guida di installazione completa](INSTALL.md).

---

## Configurazione

Il bot si configura tramite due file principali:

### File .env (richiesto)
Copia `.env.example` in `.env` e configura:
- `TELEGRAM_BOT_TOKEN` - Token del bot Telegram (da @BotFather)
- `OLLAMA_HOST` - Indirizzo server Ollama (default: http://localhost:11434)
- `OLLAMA_MODEL` - Modello AI da usare (default: llama2)
- Altri parametri opzionali per logging, memoria, ecc.

### File config.yml (opzionale)
Personalizza parametri avanzati:
- Configurazione AI (temperatura, max tokens, context window)
- Impostazioni memoria (ritenzione, salvataggio automatico)
- Parametri sintesi vocale (lingua, velocità, volume)
- Limiti e rate limiting

Vedi [INSTALL.md](INSTALL.md) per dettagli completi.

---

## Uso

### Avvio del Bot
```bash
python bot.py
```

### Comandi Telegram Disponibili
| Comando | Descrizione |
|---------|-------------|
| `/start` | Avvia il bot e mostra il messaggio di benvenuto |
| `/help` | Mostra aiuto e lista comandi |
| `/clear` | Cancella la memoria della conversazione |
| `/stats` | Mostra statistiche sulla memoria |
| `/voice` | Abilita/disabilita risposte vocali |
| `/lang` | Cambia lingua (es. `/lang en`) |
| `/admin` | Dashboard admin (solo admin) |
| `/code` | Genera codice (es. `/code python hello world`) |
| `/translate` | Traduci testo (es. `/translate en Ciao mondo`) |
| `/remind` | Promemoria (es. `/remind tra 5 minuti Chiamare Mario`) |

### 🌍 Lingue Supportate
- 🇮🇹 Italiano (default)
- 🇬🇧 English
- 🇪🇸 Español
- 🇫🇷 Français
- 🇩🇪 Deutsch
- 🇲🇦 الدارجة المغربية (Darija)

### 👥 Supporto Gruppi
Il bot funziona anche nei gruppi Telegram! Rispondendo solo quando:
- Viene menzionato con `@TauroBot`
- Si risponde a un suo messaggio

### Interazione
Invia semplicemente un messaggio al bot su Telegram e ti risponderà utilizzando:
- 🧠 Intelligenza artificiale (tramite Ollama)
- 💾 Memoria persistente delle conversazioni passate
- 🔊 Risposte vocali (opzionale)

### Test
Esegui i test per verificare l'installazione:
```bash
python test_bot.py
```

### 📱 Progressive Web App (PWA)
L'interfaccia web può essere installata come app su qualsiasi dispositivo!

**Quick Start PWA:**
```bash
# 1. Genera le icone (già fatto)
python generate_pwa_icons.py

# 2. Servi il sito con HTTPS (richiesto per PWA)
# Opzione A: Deploy su GitHub Pages (consigliato)
# Opzione B: Usa server HTTPS locale per test

# 3. Apri index.html nel browser
# 4. Clicca sul pulsante "📱 Installa App"
```

**Funzionalità PWA:**
- ✅ Installabile su Android, iOS, Desktop
- ✅ Funziona offline dopo prima visita
- ✅ Icona dedicata sulla home screen
- ✅ Splash screen al lancio
- ✅ Aggiornamenti automatici
- ✅ Pulsanti di installazione interattivi
- ✅ Feedback visivo e animazioni

**Documentazione PWA:**
- 📖 [Guida Installazione PWA](PWA_INSTALL.md) - Come installare e configurare
- 🎯 [Guida Interazione PWA](PWA_INTERACTION_GUIDE.md) - Come interagire con l'app installata

---

## Struttura del Progetto

```
Taurosweb/
├── bot.py                      # Bot Telegram principale
├── memory.py                   # Sistema memoria persistente
├── voice.py                    # Sistema sintesi vocale (TTS)
├── rate_limiter.py             # Sistema anti-spam / rate limiting
├── test_bot.py                 # Suite di test
├── run.py                      # Script Python per avviare il bot
├── run.sh                      # Script Bash per avviare il bot
├── setup.sh                    # Script di setup automatico
├── config.yml                  # Configurazione bot
├── requirements.txt            # Dipendenze Python
├── .env.example                # Template variabili d'ambiente
├── .gitignore                  # File esclusi da git
├── Dockerfile                  # Container Docker
├── docker-compose.yml          # Orchestrazione Docker + Ollama
├── .dockerignore               # File esclusi da Docker
├── README.md                   # Questo file
├── INSTALL.md                  # Guida installazione dettagliata
├── PWA_INSTALL.md              # Guida installazione PWA
├── LICENSE                     # Licenza MIT
├── SECURITY.md                 # Policy di sicurezza
├── index.html                  # Interfaccia web PWA
├── manifest.json               # PWA manifest
├── service-worker.js           # Service worker per PWA
├── generate_pwa_icons.py       # Generatore icone PWA
├── i18n/                       # Traduzioni multi-lingua
│   ├── __init__.py             # Modulo i18n
│   ├── it.json                 # Italiano 🇮🇹
│   ├── en.json                 # English 🇬🇧
│   ├── es.json                 # Español 🇪🇸
│   ├── fr.json                 # Français 🇫🇷
│   └── de.json                 # Deutsch 🇩🇪
├── icons/                      # Icone PWA (SVG)
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI/CD
```

---

## Contributi

Contributi e miglioramenti sono benvenuti!

Per contribuire:
1. Fai fork del repository.
2. Crea un branch per la tua feature o correzione.
3. Invia una pull request descrivendo le modifiche apportate.

---

## Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file LICENSE per maggiori dettagli.

---

## Contatti

Per domande o supporto, apri una issue su GitHub o contatta gli sviluppatori tramite Telegram.

---

*Taurosweb - Il tuo bot AI avanzato per Telegram con memoria, sintesi vocale e anima hacker.*

[Visita il repository su GitHub](https://github.com/anouardib88/Taurosweb)

---

## Accesso VIP ritirato

Il precedente controllo VIP verificava il codice nel browser e non costituiva autenticazione. La pagina e il generatore sono stati ritirati; non usare codici già emessi per proteggere contenuti o dati. La pagina pubblica attuale è statica e non contiene un'area riservata.

Per segnalare problemi o proporre modifiche, usa [GitHub Issues](https://github.com/anouardib88/Taurosweb/issues).
