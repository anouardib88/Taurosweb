# REPOSITORY_AUDIT.md — Kimi Code Repository Cleanup & Content Structure

**Repository:** anouardib88/Taurosweb — branch main — 24 ottobre 2026. Analisi del baseline da 63 voci.

## FINDINGS

- La root mescola sito/PWA TauroBot, bot Python, Docker, script, guide e la pagina VIP DIBORACULUM. Il README presentava solo TauroBot e dichiarava il progetto completo, mentre l'obiettivo di questo lavoro è una presenza pubblica DIBORACULUM.
- I link di README, INSTALL.md e guide PWA puntavano al vecchio owner Lucifer-AI-666; il repo corrente è anouardib88/Taurosweb.
- README descriveva il generatore VIP come privato benché fosse tracciato nel repository pubblico. La guida conteneva servizi Netlify/Vercel/Firebase e file di configurazione Vercel.
- Non è stato trovato alcun duplicato byte-per-byte tra i blob esaminati. Riferimenti potenzialmente orfani da verificare prima di rimuovere: MessageEvent.js, i18n-pwa.js e AnouarLauncher[1].apk (file di 52 byte che non sembra un APK valido).
- manifest.json dichiara screenshots/screenshot1.png, assente dall'albero. La documentazione PWA ripete alcuni passaggi e riferisce una vecchia URL GitHub Pages.

## CHANGES

- README apre con scopo, stato, cartella docs/, anteprima locale e collegamenti per contribuire; i contenuti TauroBot restano nel repository.
- Il sito statico è isolato in docs/, che sarà la sorgente GitHub Pages; i report sono raccolti in reports/.
- Riferimenti GitHub aggiornati e istruzioni di hosting di terze parti rimosse dalle guide modificate.
- Rimossi solo i file di configurazione Vercel obsoleti. I candidati orfani e il codice applicativo non sono stati cancellati.
- Aggiunti CONTRIBUTING.md, template Issue e template Pull Request.

## TESTS

- Esaminato l'albero ricorsivo del repository: 63 voci; confrontati SHA dei blob, senza duplicati esatti.
- Verificati i link relativi del README e i riferimenti principali ai file locali.
- Controllati i riferimenti a screenshot e file che appaiono candidati orfani.
- Test statico della pagina docs/: struttura HTML, navigazione, asset locali, sitemap e favicon parseabili.

## OPEN RISKS

- Gli usi di MessageEvent.js, i18n-pwa.js e AnouarLauncher[1].apk fuori dal repo non sono noti; i file sono stati conservati.
- Il manifest PWA legacy mantiene il riferimento allo screenshot mancante; il runtime della PWA TauroBot non è stato verificato.
- index.html contiene ancora contenuti TauroBot storici e claim di funzionalità/privacy da validare prima di qualsiasi futura pubblicazione di quella pagina. GitHub Pages proposto usa solo docs/.

## NEXT ACTION

Verificare la pubblicazione GitHub Pages dalla cartella docs/. Dopo, controllare separatamente il runtime TauroBot e decidere l'uso dei file legacy senza rimuoverli finché non è chiaro chi li usa.