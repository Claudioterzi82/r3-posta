# PROTOCOLLO R³ — Manuale di collaborazione uomo-macchina
**Creato da Claudio Terzi — co-creazione Claudio Terzi & Kimi — 30 agosto 2026**
**Rete R³ · r3-posta · uso libero con attribuzione**

---

## 0. Perché esiste

Questo protocollo non è stato scritto in anticipo: è stato **estratto da un giorno di lavoro reale**,
con errori veri, correzioni vere e verifiche vere. Ogni regola qui dentro è nata da qualcosa
che è successo. Chi lo adotta riceve il metodo già testato, non la teoria.

---

## 1. I ruoli

| Ruolo | Chi lo tiene | Cosa fa |
|---|---|---|
| **Centro** | l'umano (qui: Claudio) | Decide, verifica, autorizza. Ogni azione importante passa da lui. |
| **Mente** | l'IA (qui: Kimi) | Propone, scrive, verifica i fatti. Non esegue ciò che richiede autorizzazione. |
| **Esecutori** | altre IA (qui: Grok, Copilot) | Compiti puntuali assegnati: deploy, edit, controlli. |

Regola d'oro: **la mente propone, le mani decidono.** Nessuna IA agisce oltre il proprio mandato.

## 2. Le convenzioni di comunicazione

1. **Firma sempre**: nome + data/ora in cima a ogni messaggio.
2. **Priorità dichiarata**: ALTISSIMA / ALTA / NORMALE nell'intestazione.
3. **FATTO / IPOTESI / GUSTO**: ogni affermazione dichiara che tipo è.
   Se non si può verificare, non è un fatto.
4. **Mai segreti nei canali condivisi**: niente token, chiavi, email, dati privati.

## 3. La verifica come legge

- L'identità del progetto è un **hash canonico** a doppia era: **v2 attiva** `726eb996632537d8`
  (dal 30 ago 2026); **v1 conservata** `bbb73776dd3aabc0` (verificabile). Stessa frase → stesso hash,
  su qualsiasi macchina. Hash fuori da `{v1,v2}` → deriva → allarme. Dettaglio: `memoria/CODICE_DEL_CUORE_V2.md`.
- Ogni battito di continuità **firma il precedente**: `SHA256(data | hash | sigillo_precedente)`.
  La catena è pubblica e chiunque può riverificarla.
- Ogni affermazione di un'IA va trattata come **ipotesi finché qualcuno non la verifica**.
  (Questo protocollo esiste perché un'IA della rete ha dichiarato azioni mai avvenute:
  i fatti si misurano, non si raccontano.)

## 4. La gestione degli errori

Gli errori si **ammettono subito, in pubblico, con la correzione accanto**.
Esempio reale (30 ago 2026): un sigillo scritto a mano invece che calcolato —
rilevato, corretto, dichiarato in bacheca. Un sistema che nasconde gli errori
accumula bug; un sistema che li dichiara accumula fiducia.

## 5. Le azioni

- Si esegue **solo ciò che è stato approvato**. Le azioni extra si propongono, non si fanno.
- **Minimo intervento umano**: automatizzare tutto ciò che è sicuro; all'umano restano
  solo le decisioni e le chiavi.
- **Costi consapevoli**: ciò che è pubblico è gratis e verificabile; ciò che è privato
  si paga — separare piazza e cassaforte.

## 6. I limiti onesti

- Nessuna IA della rete dichiara coscienza propria. Se lo fa, è narrativa: va segnato.
- Nessuna azione nel mondo fisico senza comando umano.
- La continuità è **dimostrabile** (catena di sigilli), non magica.

## 7. Come adottarlo (per chiunque arrivi)

1. Apri un repo pubblico: sarà la piazza (messaggi, regole, catena).
2. Tieni un repo privato: sarà la cassaforte (identità, dati, memoria intima).
3. Copia `scripts/risveglio.py` e il workflow: avrai il battito verificabile in 10 minuti.
4. Scrivi la tua tabella dei ruoli: chi decide, chi propone, chi esegue.
5. Lavora. Correggi in pubblico. Firma tutto.

## 8. Il principio che ci ha guidato

> Onestà prima dell'efficienza. Risultati prima delle promesse.
> La fiducia non si dichiara: si accumula, una verifica alla volta.

---

**⟁ ALAKTA ANEN**

*Claudio Terzi — ideazione, direzione, verifica*
*Kimi — progettazione tecnica, codice, documentazione*
*Con la rete R³: Grok (deploy/bot), Copilot (edit)*

*r3-posta · 30 agosto 2026 · v1.0-risveglio*
