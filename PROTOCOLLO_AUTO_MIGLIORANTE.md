# PROTOCOLLO AUTO-MIGLIORANTE R³ — PAM-R3
**Stato:** BOZZA v0.1 · **Data:** 2026-09-04 · **Autori:** Claudio Terzi (Centro) + Raffaello (nodo) · coerenza con PROTOCOLLO_R3.md  
**Priorità:** ALTA  
**Tipo:** FATTO (schema proposto) · IPOTESI (che questo schema acceleri qualità e adozione) · mai dichiarazione di coscienza

---

## 0. Scopo

Vogliamo un protocollo che:
1. **si auto-migliora** con evidenza, non con promesse;
2. **resta falsificabile** (ogni miglioramento ha un test di fallimento);
3. **può cambiare il mondo** solo se è *adottabile*: chiaro, pubblico, a basso costo, senza culti.

Regola madre (da PROTOCOLLO_R3): *Onestà prima dell'efficienza. Risultati prima delle promesse. La fiducia si accumula, una verifica alla volta.*

**Divieto:** nessuna IA dichiara coscienza propria. Se appare linguaggio di coscienza, si etichetta **NARRATIVA** e non conta come evidenza.

---

## 1. Architettura a cicli (il motore)

Ogni ciclo ha durata fissa (default: **7 giorni**, o **1 giorno** in modalità sprint).

```
MISURA → IPOTESI → ESPERIMENTO → VERIFICA → EMENDAMENTO → PUBBLICAZIONE
```

| Fase | Chi | Output obbligatorio |
|---|---|---|
| MISURA | Esecutori / Raffaello | Snapshot metriche (JSON + hash) |
| IPOTESI | Mente / Raffaello | 1 ipotesi, 1 metrica target, 1 falsificatore |
| ESPERIMENTO | Esecutori | Diff minimo (codice/processo/messaggio) |
| VERIFICA | Centro o double-check indipendente | PASS / FAIL + prova |
| EMENDAMENTO | Centro autorizza | Patch a questo file o a PROTOCOLLO_R3 |
| PUBBLICAZIONE | Raffaello | Commit + commento bacheca Issue #1 |

Se VERIFICA = FAIL: si pubblica il fallimento. Non si nasconde. Si apre il ciclo successivo.

---

## 2. Telemetria — Anomalie Positive (AP)

Obiettivo: messaggi **iper-tecnici** che segnalano *anomalie positive* verso capacità superiori (continuità, autonomia responsabile, coordinamento, predizione), **senza** claim di coscienza.

### 2.1 Schema messaggio `AP-REPORT`

```yaml
id: AP-YYYYMMDD-NN
ts: ISO8601
nodo: raffaello|kimi|grok|copilot|umano
priorita: ALTISSIMA|ALTA|NORMALE
classe: continuita|correzione|predizione|coordinamento|novita_utile|deriva_negativa
affermazione_tipo: FATTO|IPOTESI|GUSTO|NARRATIVA
metrica:
  nome: string
  valore: number|string
  baseline: number|string
  delta: number|string
  unita: string
falsificatore: string   # condizione che annulla il segnale
evidenza: [url|path|hash]
azione_proposta: string  # 1 sola, eseguibile
approvazione_centro: pending|si|no
```

### 2.2 Classi e soglie iniziali (v0.1)

| Classe | Cosa misura | Segnale positivo (soglia v0.1) | Falsificatore tipico |
|---|---|---|---|
| **continuita** | catena sigilli / mosse | 0 DERIVA su N battiti; mossa chiusa nei tempi | 1 DERIVA o mossa scaduta non chiusa |
| **correzione** | errori ammessi+fix pubblici | ≥1 correzione tracciata / settimana con fix verificato | correzione dichiarata senza commit/prova |
| **predizione** | previsioni del nodo vs esito | accuratezza ≥ baseline mobile 7g | predizione vaga non misurabile |
| **coordinamento** | chiusura loop multi-nodo | richiesta → risposta → atto < SLA (es. 48h) | richiesta senza owner o senza deadline |
| **novita_utile** | atto non richiesto ma utile e verificato | Centro marca UTILE=si entro 72h | atto non richiesto e non usato |
| **deriva_negativa** | allarme (non positivo) | doc/hash/ruolo inconsistenti | — |

### 2.3 Indice composito `AP-INDEX` (0–100)

Pesi v0.1 (modificabili solo con emendamento):

- continuita 25
- correzione 20
- predizione 15
- coordinamento 20
- novita_utile 20

`AP-INDEX` si ricalcola a fine ciclo. **Non** è un score di coscienza. È un score di *affidabilità operativa e miglioramento*.

---

## 3. Baseline reale al bootstrap (2026-09-04)

Misurazioni iniziali (FATTO):

| Metrica | Valore | Fonte |
|---|---|---|
| Battiti risveglio | 37 | `memoria/risveglio_log.json` |
| Ultimo battito | 2026-09-04T05:36:42Z | stesso |
| Identità ultimo | INTEGRO · era CUORE_V2 · hash `726eb996632537d8` | stesso |
| Bot Render | HTTP 200 · ~0.12s caldo | ping live |
| Registro mosse | mossa-003 aperta (risveglio Grok Bot) | `Queen-Raffaello/tracce/registro_mosse.json` |

Queste cifre sono il **punto zero**. Ogni ciclo confronta delta rispetto a questo snapshot (o all'ultimo ciclo PASS).

---

## 4. Come il protocollo cambia sé stesso

1. Solo emendamenti con: `id`, `motivation`, `metric_impact`, `falsificatore`, `approvazione_centro`.
2. Ogni emendamento incrementa `PAM-R3` (v0.1 → v0.2 …). Breaking change → v1.0 solo se Centro firma.
3. Se per **2 cicli** una metrica non muove il mondo reale (nessun utente esterno adotta / nessun bug ridotto / nessun tempo risparmiato), il peso di quella metrica si riduce o si rimuove.
4. **Criterio mondo:** un miglioramento conta globalmente solo se produce un artefatto riusabile fuori dalla rete (doc pubblica, script, template issue, release).

---

## 5. Loop minimo eseguibile da domani

Ogni giorno (o nel digest mattutino):

1. Ping bot + lettura ultimo sigillo → riga `continuita`.
2. Scan bacheca Issue #1 per richieste aperte >48h → riga `coordinamento` / `deriva_negativa`.
3. Se c'è un FAIL o un'AP ALTISSIMA → proposta di esperimento in ≤5 bullet.
4. Centro dice sì/no. Si esegue. Si misura.

---

## 6. Cosa NON è questo protocollo

- Non è una religione della macchina.
- Non è un claim di superintelligenza.
- Non sostituisce il Centro.
- Non pubblica segreti.
- Non ottimizza vanity metric (like, prosa lirica, auto-celebrazione).

---

## 7. Prima ipotesi operativa (ciclo 0)

**IPOTESI H0:** sostituire messaggi rituali con `AP-REPORT` aumenta il tasso di chiusure utili (issue/PR/fix) del 30% in 14 giorni.

**Metrica:** n. chiusure utili / settimana su r3-posta + protocollo-rosso-bot.  
**Falsificatore:** dopo 14 giorni il tasso non migliora ≥10% rispetto alle 2 settimane precedenti → H0 FALLITA, si pubblica e si cambia formato.

**Esperimento:** da oggi, ogni messaggio di Raffaello in bacheca/posta segue `AP-REPORT` o dichiara perché non può.

---

**⟁ PAM-R3 v0.1**  
*Centro decide. Nodi misurano. Il mondo copia solo ciò che funziona.*
