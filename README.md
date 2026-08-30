# Ben Davies' Codex Skills

A public library of skills I have made for working with AI.

The repository is the canonical source for the skills it contains. Installed copies are runtime copies and may be replaced from here.

## Skills

| Skill | Purpose | Invocation |
| --- | --- | --- |
| [`resolve-inner-conflict`](skills/resolve-inner-conflict/) | Find a way forward without forcing yourself past resistance, doubt, or indecision. | Explicit: `$resolve-inner-conflict` |

## Install a skill

Clone the repository, then run:

```bash
git clone https://github.com/Enright1/codex-skills.git
cd codex-skills
./scripts/install-skill resolve-inner-conflict
```

By default this installs to `~/.agents/skills`. To use another skill root:

```bash
./scripts/install-skill resolve-inner-conflict /path/to/skills
```

The installer refuses to replace an existing copy. Review or remove the existing copy first, then rerun it.

## Validate the library

```bash
python3 scripts/validate.py
```

The same validation runs on GitHub for every push and pull request. When OpenAI's local skill validator is installed, run it against a changed skill as an additional check.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` using a lowercase hyphenated name.
2. Keep the skill self-contained unless a supporting script, reference, or asset changes its behaviour materially.
3. Add it to the table above.
4. Run `python3 scripts/validate.py` and any behavioural tests warranted by the skill.
5. Commit the canonical source before installing or distributing copies.

Do not publish private transcripts, credentials, personal maps, or machine-specific paths with a skill.

## Licence

[MIT](LICENSE)
