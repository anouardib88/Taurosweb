# SEO_AUDIT.md — Gemini Code SEO & Discoverability

**Repository:** anouardib88/Taurosweb — baseline main 24 ottobre 2026; confronto con la nuova pagina predisposta in questa PR.

## FINDINGS

- Baseline: index.html aveva title e description TauroBot, nessun canonical, Open Graph, Twitter card, JSON-LD, sitemap o robots dedicati. Il documento cominciava con codice prima del doctype.
- Baseline: DIBORACULUM non era spiegato nella homepage; navigazione con sezioni JavaScript e URL non stabili.
- La nuova pagina docs/index.html ha title e meta description specifici, canonical, Open Graph title/description/url, Twitter summary card e JSON-LD WebSite.
- La nuova pagina usa HTML semantico, un H1, sezioni H2/H3, navigazione ad anchor, link descrittivi, favicon SVG e layout responsive. L'icona decorativa SVG è nascosta ai lettori di schermo.
- Aggiunti docs/robots.txt e docs/sitemap.xml con un solo URL pubblico. La sitemap dichiara la data di aggiornamento 2026-10-24.
- Il sito non carica font, script, analytics o CDN esterni; non è stata aggiunta un'immagine Open Graph.
- La richiesta specifica `diboracullum.com` (due “l”), mentre i riferimenti storici del repository indicano `diboraculum.com` (una “l”). I metadati della nuova pagina seguono la richiesta; proprietà e DNS non sono stati verificati.

## CHANGES

Title, description, canonical, social metadata, schema.org, robots, sitemap e favicon sono pronti nella cartella docs/. La sorgente Pages prevista è main/docs, così il vecchio manifest PWA non viene pubblicato.

## TESTS

Parser HTML: documento valido, un H1, JSON-LD valido, nessun link generico #, sitemap e favicon XML validi. Non eseguiti browser, Lighthouse, Search Console, crawler Google o test DNS.

## OPEN RISKS

- Google non può indicizzare la versione finale finché Pages non è abilitato e dominio/HTTPS non sono configurati.
- Canonical, sitemap e robots sono predisposti per `diboracullum.com`. Prima della pubblicazione occorre confermare che il dominio richiesto sia posseduto e configurabile da chi gestisce il repository.
- Manca un'immagine Open Graph; il riepilogo social usa titolo e descrizione testuali.
- Le prestazioni mobile reali non sono state misurate con browser o Lighthouse.

## NEXT ACTION

Confermare il dominio, pubblicare main/docs, attivare HTTPS e verificare canonical, sitemap, robots e mobile da URL live; inviare la sitemap in Search Console solo dopo.