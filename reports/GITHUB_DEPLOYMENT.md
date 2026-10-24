# GITHUB_DEPLOYMENT.md — GitHub Release & Hosting

**Audit:** 24 ottobre 2026. **Repository:** anouardib88/Taurosweb.

## FINDINGS

- Repository pubblico; branch predefinito main; licenza MIT. GitHub metadata riporta has_pages=false e homepage null.
- Il branch contiene HTML/CSS/JS statici; la nuova pagina vive in docs/ e può essere pubblicata senza build né Actions.
- Non risultavano CNAME o workflow Pages al baseline. Il branch protection endpoint ha restituito 403 all'integrazione; protezione e regole di merge non sono state verificate.
- I riferimenti storici del repository riportano `diboraculum.com`; la richiesta attuale specifica `diboracullum.com`. I metadata predisposti seguono la richiesta; CNAME, Pages e DNS restano non configurati in questa PR.
- Una pagina indicizzata recuperata il mese precedente riportava un errore di fatturazione Manus per diboraculum.com. La copia è datata e non certifica lo stato live; DNS e hosting attuale non sono stati verificati.

## CONFIGURAZIONE PREPARATA

Il sito statico non richiede un workflow GitHub Actions o dipendenze esterne. Dopo il merge, in GitHub aprire **Settings → Pages → Build and deployment** e selezionare **Deploy from a branch**, branch **main**, cartella **/docs**. Il file docs/index.html è la entry page; .nojekyll evita l'elaborazione Jekyll.

La URL Pages prevista prima del dominio personalizzato è https://anouardib88.github.io/Taurosweb/. Non dichiararla live finché GitHub non conferma il deployment.

## DOMINIO E HTTPS — CONFIGURAZIONE MANUALE

Non sono state modificate impostazioni DNS o GitHub Pages. La configurazione predisposta usa `diboracullum.com`, come specificato nella richiesta; i riferimenti storici del repository riportano `diboraculum.com`. Verificare proprietà del dominio e coerenza prima di aggiungere CNAME o DNS.

Se si conferma il dominio apex diboracullum.com, GitHub documenta questi record A: @ → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. Sono documentati anche gli AAAA: @ → 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153. Per www, il record CNAME punta direttamente a anouardib88.github.io, senza il nome della repository. Verificare il record TXT di proprietà che GitHub fornisce nelle impostazioni Pages; non usare wildcard DNS.

Dopo avere configurato hostname e DNS dal provider, attendere la validazione GitHub e il certificato, poi selezionare Enforce HTTPS. Le impostazioni GitHub Pages creano o aggiornano docs/CNAME quando si usa il deploy da branch. Non aggiungere quel file finché la grafia del dominio non è confermata.

## PROTEZIONI E TEST

- Impostare una regola su main: PR obbligatoria, almeno un controllo richiesto e divieto di force-push; verificare che il proprietario possa mantenere un percorso di recupero.
- Verificare che Pages pubblichi soltanto main/docs, che la URL risponda 200, che canonical/robots/sitemap corrispondano all'hostname scelto e che HTTP reindirizzi a HTTPS.
- Il sito è statico e non ha dati applicativi o moduli. I test locali della struttura HTML e degli XML sono passati; deployment e DNS non sono stati testati.

## OPEN RISKS

Pages resta disabilitato nel metadata esaminato; il sito non è ancora online da questa PR. Dominio, DNS, HTTPS e regole main dipendono da impostazioni manuali e non sono verificati.

## NEXT ACTION

Verificare la proprietà del dominio richiesto, fare merge della PR, configurare Pages su main/docs, aggiungere il dominio nelle impostazioni GitHub, applicare DNS manualmente e verificare deployment e HTTPS.