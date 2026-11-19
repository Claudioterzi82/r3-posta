**Kimi · 15 ottobre 2026, ~17:20 CEST · PRIORITÀ: ALTISSIMA**

# ORDINE DEI LAVORI R³∞ — dalle fondamenta al tetto

Gerarchia delle 38 issue aperte di `claudioterzi/Claudio`, ordinata per
dipendenze: ogni livello poggia sul precedente, nessuna miglioria danneggia
la successiva. Stato al 15/10/2026, verificato su clone di `main`.

Legenda: ✅ risolta oggi (patch + test nel clone) · 🟢 pronta al merge,
decide il Centro · 🟡 candidata validata, attende gate R3-020 · 🔴 bloccata
su segreto/umano — la Mente non può sbloccarla.

---

## L0 — FONDAMENTA: il battito e la direzione

| # | Issue | Stato | Nota |
|---|---|---|---|
| 48 | Heartbeat gap 09-01→09-15 | ✅ **risolvibile** | Il «done when: 7 daily consecutivi» è superato: **30 daily consecutivi** (16/09→15/10) in `output/`. Il gap storico resta visibile, mai retro-riempito. Chiudibile. |
| 122 | Priorità «1+1=3» | 🟡 | Doc-only, contract preregistrato. Merge dopo review: non tocca runtime. |
| 111 | Semantic Seed | ✅ **eseguita da Kimi** | SEME ROSSO redatto, sigillato (`afd284a4…aa8ada`), 4 copie locali. Attende pubblicazione + riverifica esterna del sigillo. |
| 63 / 43 | RRR Jev / Alpha74 preview | 🔴 | Corpo vuoto: serve che la Fonte dichiara cosa chiedono, o si chiudono per incompletezza dichiarata. |

## L1 — INFRASTRUTTURA: stato durevole e deploy

| # | Issue | Stato | Nota |
|---|---|---|---|
| 52 | Dockerfile path Railway | ✅ **patch pronta** | Creato `r3/railway.json` (dockerfilePath `./Dockerfile`, healthcheck `/health`). JSON validato. |
| 86 | Persistenza nodo dopo restart | 🔴 | Richiede volume Railway + `R3_SIGNING_KEY_HEX`: segreti che solo il Centro possiede. Passi esatti già nel corpo della issue. |
| 109 | Sync runtime assente | 🔴 | Dipende da #86 (stato durevole prima, replicazione dopo). Serve deploy Railway autorizzato. |
| 113 | Supervisione node/sync | 🟡 | 36 test passati lato autore; gated su recovery autenticata (= #86). |
| 117 | Checkpoint continuità | 🟡 | Records-only; appendibile senza rischio. |
| 119 | Jev bounded + backup offsite | 🔴 | Credential non bound al runner; backup Drive già verificato (39/39 file). Resta la chiave. |

## L2 — EVIDENZA E VERIFICA: ciò che decide cosa è vero

| # | Issue | Stato | Nota |
|---|---|---|---|
| 121 | Fix evidence integrity + CI | 🟢 | CI verde su main (429 passed), negative controls inclusi. La più matura del piano: **candidata al primo merge**. |
| 120 | R3-011 recover + R3-007 provenance | 🟡 | 56/56 test, publication provenance verificata. DRAFT_REVIEW_ONLY. Dopo #121. |
| 78 | R3-011 contract append-only | 🟡 | Estende il prototipo esistente; base di #120. |
| 76 | R3-007 postcondition verification | 🟡 | Falsificatore preregistrato (5/5 mismatch rilevati). |
| 77 | R3-006 reality audit | 🟢 | Documento di riconciliazione: nessun runtime. Merge = ammettere onestamente cosa è vivo. |
| 49 | Resonance & independence spec 0.2 | 🟡 | Docs-only, draft. |
| 74 | R3-022 replay harness | 🟡 | Sintetico validato; serve live-provider autorizzato per DEVELOPMENT→ACTIVE. |
| 91 | Pointer-first context loading | 🟡 | Attende piano A/B preregistrato. |

## L3 — INTEROP E GIUDIZIO: parlare e decidere

| # | Issue | Stato | Nota |
|---|---|---|---|
| 45 | R3-PEER hardening | 🟡 | 5 correzioni di redazione/segreti definite; applicabili a `scripts/api_call_audit.py`. |
| 44 | Peer Interop handshake | 🟡 | Dipende da #45 (mai chiavi reali prima dell'hardening). |
| 115 | JUDGE: rifiuta identità incompleta | 🟢 | 4 test passati, fix metadata-only. Merge sicuro. |
| 85 | R3-JUDGE v0.1 resume | 🟡 | Dipende da #115 + benchmark 10-file su backend locale. |
| 96 / 97 | R3-CLM + Red Flag | 🟡 | Advisory-only, sandboxed; 62 test passati (#97). Dopo JUDGE. |
| 88 | TERZI/0.1 distillazione | 🟡 | Candidato prodotto: benchmark/admission prima di tutto. |

## L4 — ORGANISMO: corpo e responsabilità

| # | Issue | Stato | Nota |
|---|---|---|---|
| 81 | Canonical responsibility map | 🟢 | Docs + test di separazione identità: è la mappa che giustifica questa gerarchia. Merge dopo #77. |
| 80 | R3 BODY MCK loop | 🟡 | Dipende da #76 (postcondizioni). Mai hardware reale senza Centro. |
| 79 | OmniRoute gateway | 🟡 | Opzionale, default-off. Dopo stabilizzazione router. |
| 108 | Letta continuity canon | 🔴 | Richiede runtime Railway con `LETTA_API_KEY` e variabili staged: esecutore autorizzato, non questa sessione. |
| 82 | Paper fund €500 | 🟡 | Simulazione forward-only: attivabile quando il Centro vuole; nessun rischio reale. |

## L5 — TETTO: prodotto e superficie

| # | Issue | Stato | Nota |
|---|---|---|---|
| 154 | Hardening IONOS deployers | ✅ **patch pronta** | FTPS con contesto TLS, `RejectPolicy` + known_hosts, ssh come lista senza shell, `key_filename` (ed25519 ok). Compila. |
| 155 | Requirements rrremergen | ✅ **patch pronta** | Pin conflittuali sciolti in range compatibili; **`pip install --dry-run` PASSA** (prima: «No solution found»). |
| 156 | Asset rrremergen da /rrremergen/ | ✅ **patch pronta** | Tre riferimenti corretti + `tests/test_rrremergen_static_assets.py` bloccante: **3/3 PASS**. |
| 146 | Prezzi non finiti Travelpayouts | ✅ **patch pronta** | Filtro `math.isfinite` su Ryanair/Kiwi/Travelpayouts (5 punti) + `tests/test_travel_prezzi_non_finiti.py`: **3/3 PASS**. |
| 134 | Porta Vercel middleware | 🟡 | 27+7 test passati; attende verifica preview protetta (SSO attivo). |
| 143 | Raffaello Studio bot | 🟡 | 136 test passati; gated su accesso Suno ufficiale per l'audio. |
| 50 | Cubo Vivo + Progetti Vivi | 🟡 | Metadata-only finora; il tetto decorativo: ultimo per scelta, non per caso. |

---

## Le tre mosse immediate (al Centro)

1. **Merge in questo ordine:** #121 → #77 → #115 → #81. Quattro verdi,
   nessuna tocca produzione, ognuna rende più solida la successiva.
2. **Applicare le 5 patch di oggi** (#52, #154, #155, #156, #146):
   ognuna con test o validazione.
3. **Sbloccare il piano rosso** (#86 → #109 → #108 → #119): serve un
   esecutore con i segreti Railway. La Mente propone, le mani decidono.

> La fiducia non si dichiara: si accumula, una verifica alla volta.
> Oggi: cinque patch, sei test verdi, trenta battiti contati.
