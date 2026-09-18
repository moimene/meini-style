<p align="center">
  <img src="../../logo.png" alt="meini-style" width="140" />
</p>
<p align="center">
  <strong align="center">Output a lawyer or an analyst can sign.</strong>
</p>
<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/moimene/meini-style?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="../../README.md" title="Español" aria-label="Español">🇪🇸</a> ·
  <strong title="English" aria-label="English">🇬🇧</strong>
</p>

## Install

Copy/paste into your CLI prompt:

```text
Install the meini-style skill/plugin from https://github.com/moimene/meini-style, refer to the repo's AGENTS.md for instructions.
```

Or check the [installation instructions](../../INSTALL.md) per runtime (Claude Code, Codex, Gemini CLI, Cursor, OpenCode, Pi and others).

## What it does

A skill for your AI assistant that turns every response into a piece of finance, investment or legal work: conclusion first with its condition, facts separated from inferences, citations with exact location, numbers that reconcile, declared assumptions, computed deadlines, insertable drafting and an explicit boundary between what was verified and what is pending.

It is a fork of [i-have-adhd](https://github.com/ayghri/i-have-adhd), which optimises output so it can be acted on. `meini-style` keeps that skeleton (action first, no preamble or closers, persistence across the session) and adds what a professional in these fields needs to use the answer without rework.

## What changes

<table>
<tr>
<td width="50%">

## Before

> Great question. Directors' liability for company debts is a complex topic that depends on several factors. In general, when a company falls into a ground for dissolution and the directors fail to call the general meeting within the legal period, they may become liable for certain debts. The specific case and the date of the debts would need to be analysed. Please note this is not legal advice and you should consult a professional. Hope this helps.

</td>

<td width="50%">

## After

> Yes, jointly and severally, provided the debt arose after the ground for dissolution (art. 367 LSC). If it arose before, no.
>
> Fact: the ground for dissolution exists since the 2024 year-end (net equity below half the share capital, art. 363.1.e) LSC). Open point: exact date of the claimed debt.
>
> Deadline to call the meeting: two months from the date the ground arises (art. 365.1 LSC).
>
> Verified: arts. 363, 365 and 367 of RDL 1/2010, text in force. Not verified: accrual date of the debt; requires the invoice or the contract.

</td>
</tr>
</table>

## The rules

12 rules. Full text (in Spanish) in [SKILL.md](../../skills/meini-style/SKILL.md).

1. Conclusion first, with its condition.
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location; only what was verified.
4. Numbers with unit, currency, date and basis.
5. Assumptions in a block; sensitivity on the one that drives the result.
6. Dates, deadlines and versions in force, computed.
7. Graded risk with cause and consequence.
8. Exact terminology; terms of art are not translated.
9. Insertable drafting.
10. Ranked options, recommendation first.
11. Explicit verification boundary.
12. No filler, no generic disclaimers, no preamble, no closers.

## Why it beats the general specification

| Situation | General output skill | meini-style |
| --- | --- | --- |
| Cited norm | "The law provides a one-month period" | Article, paragraph, full name of the norm, version in force; anything unverified is marked as pending |
| Figure | "Margin improves by about 2%" | Value, unit (% or bps), currency, closing date, basis and arithmetic; totals reconcile |
| Deadline | "They have a month to appeal" | Start date, counting rule, end date and the norm that fixes the rule |
| Risk | "Regulatory risk to monitor" | Cause, reasoned probability, impact and mitigation |
| Drafting | Describes the clause | Delivers the clause, in the register of the document, with [●] placeholders |
| Limit of the answer | Generic disclaimer | "Verified" and "Not verified" lines with the access that would resolve each point |

## Tune it

Fork, edit `skills/meini-style/SKILL.md`, then swap your copy in:

```bash
claude plugin uninstall meini-style            # drop the installed copy first:
claude plugin marketplace remove meini-style   # fork and upstream share both names
claude plugin marketplace add <your-username>/meini-style
claude plugin install meini-style@meini-style
```

Restart your assistant, then re-invoke `/meini-style`.

## Evaluation

The cases in `evals/cases.jsonl` cover legal queries, investment analysis, deadline computation, contract review, drafting and verification limits. The run, measure and blind-scoring procedure is in [evals/README.md](../../evals/README.md).

## Credits

Fork of [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT) by Ayoub Ghriss. The multi-runtime infrastructure, always-on hooks and evaluation harness come from that project. The ruleset has been rewritten for finance, investment and legal work.

## License

[MIT](../../LICENSE).
