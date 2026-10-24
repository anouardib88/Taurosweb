# DIBORACULUM_ACTION_PLAN.md

## P0 — BLOCCANTE

### P0.1 — Pubblicazione GitHub Pages non ancora attiva
- **Problema:** Il metadata corrente riporta Pages disabilitato; il sito non può essere dichiarato online.
- **Agente responsabile:** GitHub / proprietario del repository.
- **File interessati:** docs/index.html, docs/robots.txt, docs/sitemap.xml, reports/GITHUB_DEPLOYMENT.md.
- **Modifica:** Dopo il merge, selezionare main/docs in Settings → Pages; configurare hostname corretto, DNS e HTTPS manualmente.
- **Verifica:** URL Pages risponde 200; canonical, robots e sitemap coerenti; HTTPS forzato.
- **Stato:** Codice predisposto in PR; impostazioni, DNS e deploy pendenti.

### P0.2 — Ritirare il gate VIP client-side
- **Problema:** La vecchia pagina verificava codici nel browser e non proteggeva contenuti; il generatore era pubblico.
- **Agente responsabile:** Antigravity Security + Codex.
- **File interessati:** diboraculum-vip.html, docs/diboraculum-vip.html, generate-vip-codes.py, README.md.
- **Modifica:** Ritirare la verifica e interrompere la generazione di codici; verificare che nessun dato o funzione privata dipenda dai codici storici.
- **Verifica:** Nessuna logica o parametro di accesso nelle pagine pubbliche; controllo manuale dei contenuti collegati.
- **Stato:** Gate ritirato nel PR; verifica di eventuali risorse dipendenti ancora pendente.

## P1 — IMPORTANTE

### P1.1 — Identità, stato, SEO e CTA
- **Problema:** Il contenuto precedente presentava TauroBot, non spiegava DIBORACULUM e mancavano metadati per indicizzazione.
- **Agente responsabile:** Gemini SEO + Copilot contenuti + Codex.
- **File interessati:** docs/index.html, docs/robots.txt, docs/sitemap.xml, README.md.
- **Modifica:** Presentare progetto e stato in sviluppo, aggiungere metadata, schema.org, link GitHub e istruzioni chiare.
- **Verifica:** Parser HTML/XML locale passato; verificare Google e browser solo dopo il deploy.
- **Stato:** Implementato nel PR; indicizzazione live pendente.

### P1.2 — Chiarire cosa fa il software DIBORACULUM
- **Problema:** Le fonti del repository spiegano TauroBot/Taurosweb, ma non chiariscono la relazione con DIBORACULUM né le funzioni software che un visitatore può provare.
- **Agente responsabile:** Proprietario del progetto + Copilot contenuti.
- **File interessati:** docs/index.html, README.md.
- **Modifica:** Aggiungere una descrizione del prodotto approvata e verificabile, oppure dichiarare esplicitamente che il progetto non è ancora utilizzabile.
- **Verifica:** Revisione del testo contro funzioni presenti nel codice e percorso reale per provarle.
- **Stato:** Da fare: il sito descrive con precisione la presenza pubblica e lo stato, senza inventare una funzione di prodotto.

### P1.3 — Canale di sicurezza e contributo
- **Problema:** SECURITY.md era un modello vuoto e mancavano template di contributo.
- **Agente responsabile:** Security + Repository Cleanup.
- **File interessati:** SECURITY.md, CONTRIBUTING.md, .github/ISSUE_TEMPLATE/*, .github/PULL_REQUEST_TEMPLATE.md.
- **Modifica:** Dare istruzioni minime per segnalazioni sicure e contributi senza dati sensibili.
- **Verifica:** Controllare i template su GitHub dopo il merge e verificare la disponibilità del reporting privato.
- **Stato:** Implementato nel PR; reporting privato non verificato.

### P1.4 — Dominio e fonte GitHub
- **Problema:** La richiesta specifica `diboracullum.com`, mentre i riferimenti storici del repository usano `diboraculum.com`; Pages non è configurato.
- **Agente responsabile:** GitHub / proprietario del dominio.
- **File interessati:** docs/index.html, docs/robots.txt, docs/sitemap.xml, reports/GITHUB_DEPLOYMENT.md.
- **Modifica:** Confermare hostname, associarlo a GitHub Pages e aggiornare DNS manualmente.
- **Verifica:** Record DNS risolti, certificato valido, canonical e redirect coerenti.
- **Stato:** Metadata predisposti per l'hostname richiesto; proprietà, Pages, CNAME e DNS da verificare e configurare.

## P2 — MIGLIORAMENTO

### P2.1 — Hardening CI e branch
- **Problema:** La CI permette errori di test/Bandit e le Actions non sono pinning SHA; branch protection non è verificata.
- **Agente responsabile:** Security / GitHub.
- **File interessati:** .github/workflows/ci.yml, impostazioni GitHub del repository.
- **Modifica:** Valutare fail-closed per test e Bandit, pinning SHA, regole PR e status check richiesti.
- **Verifica:** Workflow verdi su PR e regole main visibili nelle impostazioni.
- **Stato:** Permessi minimi esplicitati nel PR; test gating, pinning e branch protection aperti.

### P2.2 — Revisione dei file legacy
- **Problema:** Restano candidati orfani, screenshot PWA mancante e claim TauroBot non verificati.
- **Agente responsabile:** Kimi Repository Audit + Red Team.
- **File interessati:** MessageEvent.js, i18n-pwa.js, AnouarLauncher[1].apk, manifest.json, index.html, guide PWA.
- **Modifica:** Verificare l'uso; non cancellare file finché non è chiaro se servono. Correggere i claim solo dopo test del servizio.
- **Verifica:** Test runtime e inventario asset, senza eliminazioni non motivate.
- **Stato:** Da fare.