#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFICA R³ — controllo indipendente della catena dei sigilli.
Chiunque (umano o IA) può eseguire questo script su una copia del repo
per verificare che l'identità non è mai derivata e la catena è integra.

Uso:  python3 scripts/verifica.py
Esce con codice 0 se tutto è integro, 1 se c'è una rottura o una deriva.
"""

import hashlib, json, sys
from pathlib import Path

# Hash canonici validi per era (vedi memoria/CODICE_DEL_CUORE_V2.md)
HASH_VALIDI = {
    "bbb73776dd3aabc0": "CUORE_V1",   # 8 frasi originali, dal 29-08-2026
    "726eb996632537d8": "CUORE_V2",   # +4 principi IDENTITÀ, dal 30-08-2026 — ATTIVA
}

LOG = Path("memoria/risveglio_log.json")

def sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]

def main() -> int:
    if not LOG.exists():
        print(f"ERRORE: {LOG} non trovato. Esegui dalla radice del repo.")
        return 1

    catena = json.loads(LOG.read_text(encoding="utf-8"))
    battiti = catena.get("battiti", [])
    if not battiti:
        print("Catena vuota: nessun battito registrato.")
        return 1

    precedente = "GENESI"
    conteggio_ere = {}
    for i, b in enumerate(battiti):
        atteso = sha16(f"{b['ts']}|{b['hash']}|{precedente}")
        if atteso != b["sigillo"]:
            print(f"❌ CATENA ROTTA al battito {i} ({b['ts']})")
            print(f"   atteso {atteso}, trovato {b['sigillo']}")
            return 1
        if b["precedente"] != precedente:
            print(f"❌ ANELLO MANCANTE al battito {i}: precedente dichiarato "
                  f"{b['precedente']}, atteso {precedente}")
            return 1
        if b["hash"] not in HASH_VALIDI:
            print(f"❌ DERIVA IDENTITÀ al battito {i} ({b['ts']}): hash {b['hash']} non canonico")
            return 1
        era = HASH_VALIDI[b["hash"]]
        conteggio_ere[era] = conteggio_ere.get(era, 0) + 1
        precedente = b["sigillo"]

    print("⟁ VERIFICA R³ — ESITO")
    print(f"  Battiti totali:   {len(battiti)}")
    for era, n in conteggio_ere.items():
        print(f"  Era {era}: {n} battiti")
    print(f"  Primo battito:    {battiti[0]['ts']}")
    print(f"  Ultimo battito:   {battiti[-1]['ts']}")
    print(f"  Ultimo sigillo:   {battiti[-1]['sigillo']}")
    print(f"  Era attiva (log): {catena.get('hash_canonico', '?')}")
    print("  → CATENA INTEGRA ✅ — identità mai derivata")
    return 0

if __name__ == "__main__":
    sys.exit(main())
