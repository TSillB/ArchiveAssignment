# The Archive

**Pair:** Tumi, Baraka **Repository:** [*(link)*](https://github.com/TSillB/ArchiveAssignment)

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | STRING | `MS001` |  |
| title | STRING | `Eridu Genesis` |  |
| city | STRING | `Timbuktu` |  |
| year | INTEGER | `1699` |  |
| condition | STRING | `good` |  |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | First Two Characters : `MS` Followed by 3 digits | `329` |
| title | At least 3 non-whitespace characters | `   ` |
| city | Must be among : `timbuktu, djenne, gao, walata, chinguetti` (Case-Insensitive) | `Nairobi` |
| year | Range : `600-1900` | `-230` |
| condition | Must be among : `fair, good, fragile` (Case-Insensitive) | `broken` |

### Who decided the year range?
We chose the range 600-1900 (CE) as the earliest of these cities was estimated to be made around 600 (CE) and of these Timbuktu and Chinguetti remain somewhat intact to this day but as our aim is to catalog historic manuscripts we choose to limit the year to 1900 (CE) which allows for semi-recent texts to be catalogued while not undermining the ancient writing with texts from the 20th and 21st century which had major influences from rapid industrialisation.

---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:**
- **(a)** Reject it. Only exact years enter the catalogue.

**Why:**
This allows us to keep a trustable and accurate archive which can be cited/used reliably without need to do extensive background review of the information stored.

**What it costs us:**
Many important texts are likely to be rejected as the date in which they were written may have been lost throughout its history.

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid |  |  |
| Abnormal | -2839 | invalid  |  |  |
| Extreme (low) | 600 | valid |  |  |
| Extreme (high) | 1900 | valid  |  |  |
| Boundary (below) | 599 | invalid |  |  |
| Boundary (above) | 1901 | invalid  |  |  |

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(partner 1 name)*:** One thing my partner did that I will steal: One thing I would do differently next time:

***(partner 2 name)*:** One thing my partner did that I will steal: One thing I would do differently next time:

---

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ ] Both of us can explain every line in this repository.

- [ ] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)
