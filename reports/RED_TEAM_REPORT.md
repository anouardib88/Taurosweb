# RED_TEAM_REPORT.md — Grok Code Red Team / Critic

**Repository:** anouardib88/Taurosweb — baseline main, 24 ottobre 2026. Analisi statica, senza test browser.

## FINDINGS

### 1. La homepage storica presentava TauroBot, non DIBORACULUM

**PROBLEMA:** Title, H1, navigazione e contenuto di index.html descrivono TauroBot; DIBORACULUM compareva soprattutto nella pagina VIP.
**IMPATTO:** Il visitatore non capiva cosa fosse il brand richiesto né quale fosse il progetto ufficiale.
**GRAVITÀ:** P1.
**FILE/PAGINA:** index.html, README.md, diboraculum-vip.html.
**CORREZIONE PROPOSTA:** Pubblicare la presentazione verificabile separatamente in docs/ e collegarla a GitHub.

### 2. La pagina VIP prometteva una protezione inesistente

**PROBLEMA:** Il browser scaricava già la logica e il contenuto; la verifica era client-side.
**IMPATTO:** Codici generabili e falsa aspettativa di area privata. Non è stata trovata prova che dati privati fossero protetti o esposti tramite il gate.
**GRAVITÀ:** P0 condizionale se esistono contenuti riservati collegati; altrimenti P1 di fiducia.
**FILE/PAGINA:** diboraculum-vip.html, generate-vip-codes.py, README.md.
**CORREZIONE PROPOSTA:** Ritirare il gate e dichiarare che una pagina statica non è autenticazione.

### 3. Claim di prodotto non supportati o incoerenti

**PROBLEMA:** La pagina legacy dichiara disponibilità 24/7, testimonianze e garanzie ampie di privacy senza prove leggibili nella pagina. La demo è simulata, ma il titolo la chiamava Live.
**IMPATTO:** Rischio di fiducia e reputazione; le promesse possono essere interpretate come stato attuale.
**GRAVITÀ:** P1.
**FILE/PAGINA:** index.html, sezioni Demo, testimonianze e Privacy.
**CORREZIONE PROPOSTA:** La nuova pagina si limita a indicare che il progetto è in sviluppo e non attribuisce funzioni non verificate. I claim della pagina legacy restano da convalidare prima di riutilizzarla.

### 4. Documento legacy malformato e navigazione dipendente da JavaScript

**PROBLEMA:** index.html contieneva codice prima del doctype e chiusure HTML duplicate; i link della navigazione dipendono da onclick.
**IMPATTO:** Rendering e navigazione fragili, soprattutto senza JavaScript e per crawler.
**GRAVITÀ:** P1 per la vecchia homepage; non blocca il nuovo sito isolato in docs/.
**FILE/PAGINA:** index.html.
**CORREZIONE PROPOSTA:** Conservare il codice applicativo legacy, ma non usarlo come pagina pubblica DIBORACULUM finché non viene revisionato.

### 5. PII, CTA e dominio

**PROBLEMA:** Email personale e URL GitHub vecchi erano presenti nei contenuti. La richiesta specifica `diboracullum.com`, mentre i riferimenti storici del repository usano `diboraculum.com`; i metadati predisposti seguono la richiesta e la proprietà del dominio resta da verificare.
**IMPATTO:** Esposizione di contatti e rischio di configurare il dominio sbagliato.
**GRAVITÀ:** P1 per il dominio; P2 per il contatto, salvo che fosse destinato al pubblico.
**FILE/PAGINA:** index.html, README.md, guide PWA.
**CORREZIONE PROPOSTA:** Rimuovere email dalla HEAD pubblica, usare link GitHub con destinazioni chiare e non impostare DNS fino alla conferma della grafia.

## CHANGES

La nuova homepage docs/ chiarisce progetto, stato, destinatari e autore; usa CTA reali verso sorgenti, commit e issues. La pagina VIP è ritirata. Il sito pubblicato da Pages sarà solo docs/, non la pagina legacy TauroBot.

## TESTS

HTML e link del nuovo sito sono stati verificati con parser statico; nessun browser, Lighthouse o test di disponibilità live è stato eseguito.

## OPEN RISKS

Restano da verificare i claim e la validità della vecchia pagina TauroBot se qualcuno la pubblicasse separatamente; dominio e DNS restano da confermare; il sito non è ancora live.

## NEXT ACTION

Abilitare Pages da main/docs, confermare hostname e DNS, poi testare URL, HTTPS, mobile e accessibilità sulla pubblicazione effettiva.