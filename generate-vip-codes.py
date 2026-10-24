#!/usr/bin/env python3
"""Generatore VIP DIBORACULUM ritirato.

La precedente verifica avveniva lato browser e non era autenticazione.
Il codice generatore non produce più inviti. Non usare i codici storici per
proteggere dati o contenuti riservati.
"""

import sys


def main() -> int:
    print(
        "Generatore ritirato: la verifica VIP client-side non protegge contenuti. "
        "Consulta SECURITY.md.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
