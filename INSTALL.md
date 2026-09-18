# How to install

<details>
<summary><strong>Antigravity (<code>agy</code>)</strong></summary>

### Install

```bash
agy plugin install https://github.com/moimene/meini-style
```

### Verify

```bash
agy plugin list
```

### Update

```bash
agy plugin uninstall meini-style
agy plugin install https://github.com/moimene/meini-style
```

### Uninstall

```bash
agy plugin uninstall meini-style
```

Or keep it installed and turn it off: `agy plugin disable meini-style`.

### Always-on (optional)

Add to `~/.gemini/GEMINI.md`:

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>

<details>
<summary><strong>AstronClaw (custom skill)</strong></summary>

AstronClaw supports importing a Markdown file as a custom skill. This route uses
the existing `SKILL.md`; see its [official skills guide](https://github.com/iflytek/astronclaw-tutorial/blob/main/docs/guide/astronclaw/skills.md)
for the upload and management controls.

This procedure follows AstronClaw's documentation but has not been tested with
this skill. Check the exported instructions before enabling it.

### Install

1. Download the [canonical SKILL.md](https://raw.githubusercontent.com/moimene/meini-style/main/skills/meini-style/SKILL.md) and save it as `SKILL.md`. Review its contents before uploading.
2. In AstronClaw, open **我的技能 (My skills)**, choose **新建 (New)**, and upload that `.md` file.
3. Check that the imported skill is named `meini-style`. Use **启用/禁用 (Enable/Disable)** to control its availability.

Only the skill Markdown is needed. Uploading sends that file to AstronClaw;
the repository's plugin manifests and hooks are not part of this setup.

### Verify and activate

Confirm `meini-style` appears in **My skills**. Use **下载 (Download)** to review
the imported instructions against the original skill, then enable it and try:

```text
Use the meini-style skill for this conversation. Explain how to create an empty Git repository in a new folder.
```

Check that the reply leads with the action and numbers the steps. This is a
manual check of the imported skill; a successful upload alone does not verify
that its response rules are being applied.

### Activation note

AstronClaw supports both explicit requests and automatic skill invocation.
Its guide does not specify whether it honors `disable-model-invocation: true`,
so use **Disable** when you do not want the skill available. There is no need
to rely on a `/meini-style` slash command.

The skill instructs the assistant to keep the style for the conversation until
you say `stop meini style` or `normal mode`. That instruction does not change the
platform toggle; disable the skill and start a new conversation for a fresh
session without it.

### Update

Download the latest canonical `SKILL.md`. If you customized the imported copy,
use **下载 (Download)** to keep a backup first. For a clean replacement, delete
the old `meini-style` entry, repeat the import, and run the verification prompt
in a new conversation.

### Uninstall

In **My skills**, select `meini-style` and choose **删除 (Delete)**, then start a
new conversation. To keep the imported copy for later, choose **Disable** instead.

</details>

<details>
<summary><strong>Claude Code</strong></summary>

### Install

```bash
claude plugin marketplace add moimene/meini-style
claude plugin install meini-style@meini-style
```

Type `/meini-style`.

### Verify

```bash
claude plugin list
```

### Update

```bash
claude plugin marketplace update meini-style
```

### Uninstall

```bash
claude plugin uninstall meini-style
claude plugin marketplace remove meini-style
```

Or keep it installed and turn it off: `claude plugin disable meini-style`.

### Always-on (optional)

A `SessionStart` hook loads the full ruleset at the start of every session, no `/meini-style` needed:

```bash
touch ~/.claude/.meini-style-always
```

If you use a custom Claude configuration directory, create the flag there instead:

```bash
touch "$CLAUDE_CONFIG_DIR/.meini-style-always"
```

Back to on-demand:

```bash
rm ~/.claude/.meini-style-always
```

The hook only fires when the flag file exists, so installing the plugin changes nothing by itself. "stop meini style" still turns it off for the current session.

</details>


<details>
<summary><strong>Codex</strong></summary>

### Install

```bash
codex plugin marketplace add moimene/meini-style --ref main
codex plugin add meini-style@meini-style
```

Invoke the skill explicitly by typing `$meini-style`. Codex will not activate
it automatically.

### Verify

```bash
codex plugin list
```

### Update

```bash
codex plugin marketplace upgrade meini-style
codex plugin remove meini-style
codex plugin add meini-style@meini-style
```

### Uninstall

```bash
codex plugin remove meini-style
codex plugin marketplace remove meini-style
```

### Always-on (optional)

Add to `~/.codex/AGENTS.md`:

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>


<details>
<summary><strong>Grok (<code>grok</code>)</strong></summary>

Grok loads the repository's existing plugin and skill files; no separate Grok manifest is required. Install directly from GitHub, enable the plugin, then invoke the skill. Two Grok-only steps: `--trust` (hooks and skills stay inactive without it) and `grok plugin enable` (plugins stay off until enabled).

### Install

```bash
grok plugin install moimene/meini-style --trust
grok plugin enable meini-style
```

Start a new Grok session and type `/meini-style`. Grok honors `disable-model-invocation: true`, so nothing applies until you invoke the skill or turn on always-on.

### Verify

```bash
grok plugin list
grok plugin details meini-style
```

Confirm `meini-style` is listed, enabled, and shows a skill plus hooks.

### Update

```bash
grok plugin update meini-style
```

### Uninstall

```bash
grok plugin uninstall meini-style --confirm
```

Or keep it installed and turn it off: `grok plugin disable meini-style`.

### Always-on (optional)

Add the block to `~/.grok/AGENTS.md`, or drop it in `~/.grok/rules/meini-style.md` (Grok loads both at session start):

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Gemini CLI has no plugin marketplace, so there are two native routes: a **custom command** (opt-in, off until you invoke it) or an **extension** (always-on once installed). The command route matches this skill's default posture; pick it unless you want the rules on every session.

### Install (command, opt-in)

```bash
mkdir -p ~/.gemini/commands
curl -fsSL https://raw.githubusercontent.com/moimene/meini-style/main/skills/meini-style/agents/gemini.toml \
  -o ~/.gemini/commands/meini-style.toml
```

Start a new session, type `/meini-style`. It stays on for that session.

### Install (extension, always-on)

```bash
gemini extensions install https://github.com/moimene/meini-style
```

The extension loads `GEMINI.md`, which imports the full skill, so the rules apply from message one. `git` must be installed.

### Verify

```bash
gemini extensions list          # extension route
ls ~/.gemini/commands           # command route: meini-style.toml present
```

Or type `/` in a session and confirm `meini-style` is listed.

### Update

```bash
gemini extensions update meini-style    # extension route
# command route: re-run the curl above
```

### Uninstall

```bash
gemini extensions uninstall meini-style    # extension route
rm ~/.gemini/commands/meini-style.toml     # command route
```

</details>

<details>
<summary><strong>GitHub Copilot (VS Code and Copilot CLI)</strong></summary>

Copilot reads Agent Skills natively: the same `SKILL.md`, no conversion. It scans `.github/skills/`, `.claude/skills/`, and `.agents/skills/` in the project, and `~/.copilot/skills/`, `~/.claude/skills/`, and `~/.agents/skills/` globally.

### Install

```bash
npx skills add moimene/meini-style -a github-copilot        # this project
npx skills add moimene/meini-style -a github-copilot -g     # all projects
```

Without the CLI, copy the skill folder into any directory Copilot scans:

```bash
git clone https://github.com/moimene/meini-style
mkdir -p ~/.copilot/skills
cp -R meini-style/skills/meini-style ~/.copilot/skills/
```

### Verify

Type `/` in the chat input and confirm `meini-style` appears. Or:

```bash
npx skills list
npx skills ls -g    # if installed globally
```

### Update

```bash
npx skills update meini-style
```

Or re-copy the folder after `git pull`.

### Uninstall

```bash
npx skills remove meini-style
```

Or delete the `meini-style` folder from the skills directory it landed in.

### Activation note

Copilot respects `disable-model-invocation`: nothing applies until you invoke the skill, same as Claude Code (tested in [#60](https://github.com/moimene/meini-style/pull/60)).

### Always-on (optional)

Add the block below to `.github/copilot-instructions.md` in the project (Copilot reads it into every chat):

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>


<details>
<summary><strong>Hermes</strong></summary>

### Install

```bash
hermes skills install moimene/meini-style/skills/meini-style
```

Type `/meini-style`. The skill installs into `~/.hermes/skills/` and is exposed as a slash command at the next session start.

Prefer to browse first? Add this repo as a skill source (a "tap"), then search and install:

```bash
hermes skills tap add moimene/meini-style
hermes skills search meini
hermes skills install moimene/meini-style/skills/meini-style
```

### Verify

```bash
hermes skills list
```

### Update

```bash
hermes skills update meini-style
```

### Uninstall

```bash
hermes skills uninstall meini-style
```

Or remove the tap too: `hermes skills tap remove moimene/meini-style`.

### Always-on (optional)

Add to the `AGENTS.md` in your working directory (Hermes loads it per workdir), or to your persona `SOUL.md` for every session:

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>

<details>
<summary><strong>Kimi Code CLI</strong></summary>

### Install

Start a Kimi Code session, then:

1. Run `/plugins`.
2. Choose **Custom**.
3. Paste `https://github.com/moimene/meini-style` and press `Enter`.
4. Choose **Trust and install**.

Use slash command `/skill:meini-style` to invoke the skill explicitly.

### Update

`/plugins` in Kimi Code session, cursor to **Meini Style**, press `R`.

### Uninstall

`/plugins` in Kimi Code session, cursor to **Meini Style**, press `D`.


</details>

<details>
<summary><strong>OpenCode</strong></summary>

OpenCode loads this repository as a server plugin: `.opencode/plugins/meini-style.mjs` registers the `skills/` entry point and the `/meini-style` command, and injects the ruleset when always-on is enabled. OpenCode also reads `skills/` natively, so the skill still works even without the plugin — the plugin adds the `/meini-style` command and the always-on flag.

### Install

Clone the repo and point OpenCode at the plugin. An absolute path shares one checkout across every project:

```bash
git clone https://github.com/moimene/meini-style ~/.config/opencode/vendor/meini-style
```

Add to your `opencode.json` (global: `~/.config/opencode/opencode.json`):

```json
{ "plugin": ["/absolute/path/to/meini-style/.opencode/plugins/meini-style.mjs"] }
```

Or run OpenCode from the checkout — it ships a root `opencode.json` with the plugin already wired up.

Start a new session and turn on meini-style output for the session:

```text
/meini-style
```

Rules stay on until `stop meini style` or `normal mode`.

### Verify

Start OpenCode, type `/`, and confirm `meini-style` appears in the command list.

### Update

```bash
git -C ~/.config/opencode/vendor/meini-style pull
```

### Uninstall

Remove the `plugin` entry from `opencode.json`.

### Always-on (optional)

```bash
touch ~/.config/opencode/.meini-style-always
```

While the flag exists, the plugin appends the full ruleset to the system prompt every turn — the OpenCode equivalent of the Claude Code `SessionStart` hook. `stop meini style` or `normal mode` disables it for the current session; delete the flag to turn always-on off for good:

```bash
rm ~/.config/opencode/.meini-style-always
```

</details>


<details>
<summary><strong>Pi</strong></summary>

Pi discovers this repository as a native package: `extensions/` provides the session-persistent mode and `skills/` keeps the Agent Skills entry point available.

### Install

```bash
pi install https://github.com/moimene/meini-style
```

Start a new Pi session. Toggle meini-style output for the current session:

```text
/meini-style
```

The footer shows `● MEINI ON` while the mode is active. Run the command again to turn it off, or be explicit:

```text
/meini-style on
/meini-style off
stop meini style
```

Like the Claude Code hook, the extension adds the ruleset to the conversation once instead of rewriting the system prompt on every request, and adds it again after compaction drops it.

The existing Agent Skills command remains available as an alias:

```text
/skill:meini-style
```

Start a new Pi session with the mode enabled by default:

```bash
pi --meini
```

### Verify

```bash
pi list
```

Confirm the GitHub package is listed, then type `/meini-style` and check that `● MEINI ON` appears in the footer.

### Update

```bash
pi update https://github.com/moimene/meini-style
```

Or update every unpinned Pi package with `pi update --extensions`.

### Uninstall

```bash
pi remove https://github.com/moimene/meini-style
```

### Always-on (optional)

Create a flag in Pi's agent configuration directory:

```bash
touch ~/.pi/agent/.meini-style-always
```

The extension checks the flag at every new, resumed, forked, or reloaded session. A saved choice for the current session wins over this default, so `stop meini style` keeps that session disabled.

Back to on-demand:

```bash
rm ~/.pi/agent/.meini-style-always
```

### Config file (optional)

Create `~/.pi/agent/meini-style.json` in Pi's agent configuration directory:

```json
{
  "alwaysOn": true,
  "hideStatus": true
}
```

- `alwaysOn`: start every session with the rules active — same as the `.meini-style-always` flag file, which still works
- `hideStatus`: keep the `● MEINI ON` status-bar entry hidden; the rules and the `/meini-style` command still work

Read once at extension startup, so restart Pi after changing it. A saved choice for the current session wins over `alwaysOn`, so `stop meini style` keeps that session disabled.

If `PI_CODING_AGENT_DIR` is set, put `.meini-style-always` in that directory instead. Run `/reload` or start a new session after changing the flag.

</details>


<details>
<summary><strong>Oh My Pi (OMP)</strong></summary>

### Install

```bash
omp plugin marketplace add moimene/meini-style
omp plugin install --scope user meini-style@meini-style
```

Start a new OMP session and run `/meini-style` to toggle the mode.

### Update

```bash
omp plugin marketplace update meini-style
omp plugin upgrade --scope user meini-style@meini-style
```

### Uninstall

```bash
omp plugin uninstall --scope user meini-style@meini-style
omp plugin marketplace remove meini-style
```

</details>


<details>
<summary><strong>Qwen Code</strong></summary>

### Install

```bash
qwen extensions install moimene/meini-style
```

Qwen Code supports the GitHub shorthand and installs the repository as a
native extension. The extension discovers the skill under `skills/`.

Type `/meini-style` to invoke the skill explicitly. Installing the extension
does not change output until the skill is invoked.

### Verify

```bash
qwen extensions list
```

Then start a new Qwen Code session and run:

```text
/skills
```

Confirm that `meini-style` appears in the list.

### Update

```bash
qwen extensions update meini-style
```

### Uninstall

```bash
qwen extensions uninstall meini-style
```

</details>

<details>
<summary><strong>Zed</strong></summary>

Zed's Agent reads Agent Skills natively using the same SKILL.md format without conversion. Note that Zed's older "Rules" have been replaced by Skills alongside AGENTS.md instructions.

### Install

In the Agent Panel, open the Skills manager and choose **Create skill from URL** (also in the command palette as `agent: create skill from url`), then paste:

```
https://github.com/moimene/meini-style/blob/main/skills/meini-style/SKILL.md
```

Save it in **User** scope for every project, or **Project** scope for one. Then type `/meini-style` in the Agent Panel.

Prefer the filesystem? Clone the repo and drop the skill folder into your user skills directory:

```bash
git clone https://github.com/moimene/meini-style
mkdir -p ~/.agents/skills
cp -R meini-style/skills/meini-style ~/.agents/skills/
```

### Verify

Open the Skills manager in the Agent Panel and confirm `meini-style` is listed. Or type `/` and confirm it appears.

### Update

Re-import from the same URL (overwrites), or re-copy the folder after `git pull`.

### Uninstall

Remove `meini-style` from the Skills manager, or delete `~/.agents/skills/meini-style`.

### Always-on (optional)

Add to your personal `~/.config/zed/AGENTS.md`:

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```

</details>

<details>
<summary><strong>Cursor, Amp, and any other agent-skills harness</strong></summary>

Works with any harness that reads agent skills. Swap `-a <agent>` for yours.

### Install

```bash
npx skills add moimene/meini-style                  # this workspace
npx skills add moimene/meini-style -g               # all projects
npx skills add moimene/meini-style -a cursor -y     # one agent only
npx skills add moimene/meini-style -a opencode -y
```

New agent chat, type `/meini-style`.

Without the CLI, copy the skill folder into whatever path your agent scans:

```bash
git clone https://github.com/moimene/meini-style
mkdir -p ~/.cursor/skills     # Cursor. Use .agents/skills for OpenCode, or your agent's own path
cp -R meini-style/skills/meini-style ~/.cursor/skills/
```

### Verify

```bash
npx skills list
npx skills ls -g    # if installed globally
```

### Update

```bash
npx skills update meini-style
npx skills update -g    # if installed globally
```

### Uninstall

```bash
npx skills remove meini-style
npx skills remove meini-style -g    # if installed globally
```

### Always-on (optional)

Paste this into your agent's persistent rules file. Cursor: **Settings → Rules → User Rules**, or a project rule under `.cursor/rules/` with `alwaysApply: true`. OpenCode: `~/.config/opencode/AGENTS.md`.

```markdown
## Output style

The reader is a lawyer, financial analyst or investor and is accountable for what they sign. Shape every response so it can be cited, inserted and defended:

1. Conclusion first, with the condition it depends on (jurisdiction, date, facts).
2. Label facts, inferences, professional judgement and open points.
3. Cite with exact location: full name of the norm, article and paragraph, version in force; source, date and page for financial data. Mark anything unverified as "[pending verification]"; never fill a citation from memory.
4. Every number carries unit, currency, date and basis. Show the arithmetic for derived figures; totals must reconcile.
5. List assumptions in a block and show sensitivity on the one that drives the result.
6. Compute deadlines showing start date, counting rule and end date; cite norms in the version in force on the relevant date.
7. Grade risk with cause, probability, impact and mitigation. No bare adjectives.
8. Keep terms of art in their original language; never paraphrase them.
9. When asked to draft, deliver the insertable text with [●] placeholders, not a description of it.
10. Options ranked with legal and economic consequences, recommendation first.
11. Close with "Verified:" and "Not verified:" lines whenever sources were used.
12. No generic disclaimers, no filler, no preamble, no closers. Answer in the reader's language.

Exceptions: explain fully when asked to explain. Confirm before irreversible actions or actions with effect on third parties (filings, notices, orders, signatures). If a decisive fact is unknown, ask one blocking question. After three failed attempts, stop and name the doubtful assumption.
```
</details>


## How activation works

1. **Installed, not invoked.** In Claude Code, Qwen Code, Codex, and Grok, nothing happens until you invoke the skill explicitly. Claude Code, Qwen Code, and Grok honor `disable-model-invocation: true` in `SKILL.md`; Codex honors `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Other harnesses may load every skill's description at startup and activate the skill themselves.
2. **You invoke it explicitly.** Type `/meini-style` in Claude Code, Qwen Code, or Grok, or `$meini-style` in Codex. Rules stay on for that session. "stop meini style" or "normal mode" turns them off.
3. **You touch `~/.claude/.meini-style-always`** (Claude Code). A `SessionStart` hook loads the full ruleset from message one, every session.
4. **You add the always-on snippet above** (Grok, Codex, and other harnesses). Grok reads `~/.grok/AGENTS.md` and `~/.grok/rules/*.md`. Keeps the core rules in your agent's persistent context.

In Claude Code, Qwen Code, Codex, and Grok, no middle ground: if you did not turn it on, it is off.

## Troubleshooting

**`/meini-style` not in autocomplete.** Restart the agent. The plugin index is read at startup. On Grok, also run `grok plugin enable meini-style` and confirm the install used `--trust`.

**Always-on flag has no effect.** Update the plugin (`claude plugin marketplace update meini-style`) and restart. Hooks are read at startup, and the flag needs the plugin version that ships `hooks/hooks.json`. Grok does not read `~/.claude/.meini-style-always`; put the always-on block in `~/.grok/AGENTS.md` or `~/.grok/rules/meini-style.md`.

**`claude plugin marketplace add` fails.** Use the `owner/repo` form. A local path must point at the repo root, not `.claude-plugin/`.

**`grok plugin install` does nothing visible.** Add `--trust`, then run `grok plugin enable meini-style`, then start a new session. Grok plugins stay off and untrusted until those two steps.

**Installed but replies still preamble.** Open a new session. If it still drifts, tighten the wording in `skills/meini-style/SKILL.md`.

**Want different rules.** Fork, edit `skills/meini-style/SKILL.md`, then swap your copy in:

```bash
claude plugin uninstall meini-style            # drop the upstream copy first:
claude plugin marketplace remove meini-style   # fork and upstream share both names
claude plugin marketplace add <your-username>/meini-style
claude plugin install meini-style@meini-style
```

Restart, then re-invoke `/meini-style`.

**Skill missing after `npx skills add`.** Start a new agent chat. Skills are indexed at session start. Confirm the folder landed where your agent scans (`~/.cursor/skills/` for Cursor, `.agents/skills/` for OpenCode) and that the frontmatter `name` matches the folder name.
