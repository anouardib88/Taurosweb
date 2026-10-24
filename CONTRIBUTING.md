# Contribuire

DIBORACULUM è in sviluppo. Prima di proporre una modifica, controlla le issue aperte e descrivi lo scopo del cambiamento.

## Sito statico

- Modifica i file del sito in `docs/`.
- Anteprima locale: `python3 -m http.server 8000 --directory docs`.
- Mantieni il sito statico: niente login, moduli o dati privati.
- Verifica titoli, link, sitemap e rendering mobile prima di aprire una PR.

## Repository applicativo

Per TauroBot, segui le istruzioni in README.md e INSTALL.md. Se una dipendenza o un servizio esterno è necessario, spiega il motivo nella PR.

## Sicurezza e pull request

- Non committare file `.env`, token, password, codici VIP, dati personali o log con informazioni reali.
- Per vulnerabilità, segui SECURITY.md; non usare issue pubbliche per dettagli sfruttabili.
- Nella PR indica problema, file interessati, modifica, comandi eseguiti e risultati.
