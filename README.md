# Ben Davies' AI Skills

A public library of reusable skills I have made for working with AI agents.

The skills are plain Markdown instructions packaged around a `SKILL.md` entrypoint. They are not tied to one AI company or product: any agent that can load that convention—or incorporate the instructions another way—can use them.

The repository is the canonical source for the skills it contains. Installed copies are runtime copies and may be replaced from here.

## Skills

| Skill | Purpose | Invocation |
| --- | --- | --- |
| [`resolve-inner-conflict`](skills/resolve-inner-conflict/) | Find a way forward without forcing yourself past resistance, doubt, or indecision. | Explicit: `$resolve-inner-conflict` |

## Install a skill

Clone the repository, then run:

```bash
git clone https://github.com/UnboundBen/ai-skills.git
cd ai-skills
./scripts/install-skill resolve-inner-conflict
```

By default this installs to `~/.agents/skills`. If your AI tool reads skills from another location, pass that skill root explicitly:

```bash
./scripts/install-skill resolve-inner-conflict /path/to/skills
```

The installer refuses to replace an existing copy. Review or remove the existing copy first, then rerun it.

## Validate the library

```bash
python3 scripts/validate.py
```

The same validation runs on GitHub for every push and pull request. When your AI tool provides its own skill validator, run it against a changed skill as an additional compatibility check.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` using a lowercase hyphenated name.
2. Keep the skill self-contained unless a supporting script, reference, or asset changes its behaviour materially.
3. Add it to the table above.
4. Run `python3 scripts/validate.py` and any behavioural tests warranted by the skill.
5. Commit the canonical source before installing or distributing copies.

Do not publish private transcripts, credentials, personal maps, or machine-specific paths with a skill.

## Licence

[MIT](LICENSE)
