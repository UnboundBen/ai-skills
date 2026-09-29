# Criticism chains

Use this structure in private reasoning. Never show the P/C notation in chat. When saved notes need a chain, write the same structure in plain words the user could read, for example an indented list of the plan, each worry about it, and any answer to that worry.

Represent every proposal as a root and every criticism as a child of the exact idea it criticises.

~~~text
P1: Go to the event under conditions Z.
└── C1 -> P1: The user reports that this still feels horrible; content is inexplicit.
    └── C1.1 -> C1: <a countercriticism, if one is created>
~~~

Derive status recursively:

1. A leaf criticism is pending.
2. A criticism is pending exactly when none of its direct child criticisms is pending.
3. A root proposal is currently adoptable exactly when none of its direct criticisms is pending.
4. Recompute the chain whenever a criticism or countercriticism is added.

Keep the graph finite and acyclic. A criticism's text may refer to another proposal, but that reference is not an edge.

For mutually opposing proposals, create parallel chains:

~~~text
P1: Express X.
└── C1 -> P1: X conflicts with Y in this situation.

P2: Express Y.
└── C2 -> P2: Y conflicts with X in this situation.
~~~

C1 and C2 are distinct relational ideas. Do not connect P1 and P2 with reciprocal edges.

For each criticism record, when known:

- its exact target;
- the alleged problem;
- how it bears on that target in the current situation;
- whether the wording came from the user or assistant.

The same sentence may need separate criticism nodes when it bears differently on different proposals. Answering one relational use does not answer every use.

When a proposal changes:

1. Create a successor root with the new exact content.
2. Inspect every live criticism of the predecessor.
3. Copy or restate each criticism whose content still bears on the successor.
4. Leave “carry-over unclear” as fog rather than granting the successor immunity.

Acknowledging, narrowing, or polishing a criticism does not answer it when its alleged problem still affects the proposed use.

If a particular explicit criticism is answered but the user still feels opposed to the proposal, add a separate leaf:

~~~text
C-new -> P: The user remains uneasy about P; the criticism's content is still inexplicit.
~~~

Do not represent that report as proof that the old explicit criticism survived.

