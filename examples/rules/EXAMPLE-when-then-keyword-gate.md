---
name: example-keyword-gate
kind: rule
temporal: standing
valid_from: 1970-01-01T00:00:00+00:00
valid_to: null
supersedes: null
keywords: [example, keyword-gate]
---

# EXAMPLE — keyword gate (public skeleton)

**When** the user message hits a high-risk keyword class for your stack
(tools that probe live sites, credential UIs, or rapid retries):

**Then**

1. Answer feasibility first in plain language.
2. Prefer local docs / offline fixtures over live probing.
3. Open tools only after the plan is clear; avoid spam retries.
4. If blocked by policy, say so once — do not invent a bypass.

**Not included here:** any personal rule text, school HW, or real account names.
Replace this EXAMPLE with your own when→then rules under `<your-ssot-root>/topest/rules/`.
