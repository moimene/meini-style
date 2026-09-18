# Evaluation results

No results have been recorded yet for the meini-style ruleset. The results of
the upstream project (ayghri/i-have-adhd) measured a different ruleset against
different cases and do not transfer.

Reproduce with the commands in [README.md](README.md). Record with any published
run:

| | |
|---|---|
| Date | |
| Model | pinned in `runners.example.json` |
| Runner CLI | |
| Cases | 16 (`cases.jsonl`) |
| Trials | |
| Judge | same model and runner, blind, one call per `(case, trial)` group |
| Reported cost | |

Baseline is the bare task prompt. Candidate is the same prompt with the
`meini-style` skill body injected as a response-style instruction. Apply the
release gate in [rubric.md](rubric.md) before publishing a claim.
