# SECURITY_REPORT.md — Antigravity Security & Architecture

**Repository:** anouardib88/Taurosweb — branch main esaminato il 24 ottobre 2026. **Riferimento:** commit d28bb90d052bab4aff5aa1ed3501114034fe06be. Audit del baseline GitHub; proposta correttiva inclusa in questa PR.

## FINDINGS

- **P0 condizionale — gate VIP presentato come privato, ma controllato solo nel browser.** I parametri e la logica erano in diboraculum-vip.html e generate-vip-codes.py, entrambi nel repository pubblico; README descriveva il metodo come privato. Non è stata trovata prova che contenuti riservati dipendessero dal gate. La pagina non costituisce autenticazione.
- **P1 — input della demo inserito in innerHTML.** index.html interpolava il testo digitato dal visitatore nel markup. L'evidenza indica iniezione DOM nel browser di chi invia il testo, non XSS persistente o tra utenti.
- **P1 — email personale presente in file pubblici.** L'indirizzo compare in README.md, index.html, CHANGES.md e PWA_INTERACTION_GUIDE.md.
- **P2 — pattern di esclusione env incompleto.** .gitignore escludeva .env e .env.local ma non tutte le varianti .env.*. .env.example contiene segnaposto; non è stato trovato un .env tracciato.
- **P2 — permessi Actions in parte impliciti.** ci.yml non dichiarava un permesso predefinito; i job Docker e Release hanno esigenze diverse. Le verifiche pytest e Bandit possono continuare anche in caso di errore; le Action esistenti usano tag modificabili.
- **P2 — hosting residuo.** vercel.json, .vercelignore e .vercel-deploy-trigger erano ancora presenti. La pagina VIP caricava Google Fonts.
- **P2 — SECURITY.md era il modello generico GitHub**, con versioni non pertinenti e senza un canale utilizzabile.

## CHANGES

- La vecchia pagina VIP in root e la pagina pubblicata da docs/ mostrano ora una nota di ritiro, senza validazione o segreto client-side.
- generate-vip-codes.py rimane come percorso compatibile, ma termina con un avviso e non genera codici.
- La demo in index.html inserisce l'input utente con textContent e nodi DOM, non con innerHTML.
- L'email è stata rimossa dai file pubblici modificati e i contatti rimandano a GitHub Issues.
- .gitignore ora ignora le varianti .env* e mantiene tracciabile solo .env.example.
- ci.yml dichiara contents: read come default e contents: write soltanto per la Release.
- I tre file di configurazione Vercel sono rimossi dal branch; la nuova pagina non usa font, script, analytics o CDN esterni.
- SECURITY.md ora descrive il canale GitHub privato solo se disponibile, senza promettere tempi non verificati.

## TESTS

- Audit statico del baseline tramite integrazione GitHub; scansione di 40 file testuali senza trovare valori con forma di credenziali API.
- Verifica locale della nuova pagina: HTML parseabile, un solo H1, JSON-LD valido, nessuno script eseguibile, nessuna richiesta a terze parti, sitemap e favicon XML valide.
- La pagina VIP aggiornata non contiene logica di accesso o parametro pepper.
- Non eseguiti test del bot o scansioni della cronologia Git.

## OPEN RISKS

- I commit storici conservano il vecchio codice VIP e i riferimenti all'email. Non è stata riscritta la cronologia; il vecchio valore VIP non è una credenziale di provider ma non va considerato segreto.
- Non è stato possibile verificare la protezione del branch: l'endpoint di branch protection ha restituito 403 all'integrazione.
- Il repository è pubblico e GitHub Pages non risultava abilitato; DNS, HTTPS live e segreti GitHub non sono stati verificati.
- La CI continua a permettere errori di pytest/Bandit e usa riferimenti Action non pinning SHA: revisione separata consigliata.

## NEXT ACTION

Confermare che nessun contenuto privato o funzione server-side si sia basato sui vecchi codici; poi abilitare GitHub Pages, proteggere main e verificare DNS/HTTPS prima di considerare il sito online.