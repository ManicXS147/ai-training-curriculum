## 1. Lint failures

| Row ID | Rule | Evidence |
|---|---|---|
| None | DB1, DB5, DB7 | Every claim, figure and assumption row has an ID and a quote or NOT IN SOURCE. Every option (A, B, C) has a cell for each of C1 to C5. No recommendation or ranking appears. |

## 2. Review findings

| Row ID | Rule | Evidence | I | A | Gate |
|---|---|---|---|---|---|
| FG-7 | DB3 | Source: "Move the two etch tool sets from Line A and Line B onto Line B". The row says the Line B set "is already on Line B" and labels it FIGURE FAILS (2 vs 1). The source never says this. It can also be read as both lines' sets ending up on Line B, with only Line A's moving. The frame says only "the Line A etch tools" move. The label states a count mismatch that the source does not establish. | 3 | 2 | Patch |
| AS-8 | DB4 | Impact is H, but the quote ("Weeks 7-8 Two-week shutdown: move and install the Line A tools") and the anchors point to a schedule or rework slip, which is M. This is inconsistent with AS-9 and AS-10, which are also schedule items and are rated M. | 2 | 1 | Keep |
| OPEN-7 | DB6 | Frame blast radius: "Etch operators and technicians on both lines, and the etch support team." OPEN-7 covers only support team size and workload. MISSING: operator and technician headcount, training on the moved tools, and shift coverage on both lines. | 3 | 1 | Keep |

## 3. Patch block

| Row ID | Rule | Corrected or added row, in full |
|---|---|---|
| FG-7 | DB3 | \| FG-7 \| "Move the two etch tool sets from Line A and Line B onto Line B" \| Two tool sets, from Line A and Line B, are consolidated onto Line B \| The timeline moves only the Line A tools (weeks 7-8). The source does not say whether the Line B set also moves. The frame says the Line A tools move. The number of sets moved cannot be checked against the stated "two" \| CANNOT RECOMPUTE (scope unclear; see OPEN-9) \| |
