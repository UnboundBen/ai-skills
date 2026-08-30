# Repository contract

This repository is the canonical public source for Ben's authored AI skills. Work only on source files here; treat copies under `~/.agents/skills`, `~/.codex/skills`, plugin caches, archives, and build outputs as derived installations.

When adding or changing a skill:

1. Read the complete target `SKILL.md` and every supporting resource the change touches.
2. Preserve the skill's trigger, user authority, completion criterion, and known semantic guardrails. Prefer a narrow correction over accumulating example-specific rules.
3. Keep private transcripts, personal maps, credentials, account data, and machine-specific paths out of the public tree.
4. Keep each meaning in one maintained location. Put conditional detail behind a pointer only when that branch does not belong in every invocation.
5. Update the README catalogue when a skill is added, renamed, or removed.
6. Run `python3 scripts/validate.py`, the local OpenAI validator when available, and any skill-specific behavioural tests.
7. Review the diff before committing. Publishing, installing, releasing, or replacing an installed copy remains a separate action requiring the authority granted for that action.

Do not import installed or third-party skills merely because they are discoverable locally. Establish authorship and public suitability first.
