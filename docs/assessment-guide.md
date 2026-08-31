# Assessment authoring guide

The curriculum contains exactly 1,250 original four-option, single-answer questions: 50 in each assessment-enabled lab from Lab 01 through Lab 25.

## Per-lab difficulty mix

Every assessment-enabled lab contains:

- 15 foundational questions
- 25 applied scenario questions
- 10 advanced troubleshooting or design questions

Correct-answer positions A–D must each occur 12 or 13 times in a lab.

## Lab allocation

- Identity and governance: Labs 01–05, 50 questions each (250 domain total).
- Storage: Labs 06–09, 50 questions each (200 domain total).
- Compute: Labs 10–16, 50 questions each (350 domain total).
- Networking: Labs 17–21, 50 questions each (250 domain total).
- Monitoring and recovery: Labs 22–25, 50 questions each (200 domain total).
- Lab 00 and Capstones 26–27 have no separate assessment directories.

## Files and rules

- `assessment/questions.yml` is the source of truth.
- `assessment/QUESTIONS.md` contains no answers or answer-key metadata.
- `assessment/ANSWERS.md` explains the correct option and every distractor.
- Every question maps only to objective IDs in its lab's declared assessment domain.
- Every official objective appears in at least one question.
- Use current official Microsoft sources and never use exam dumps or copied practice questions.
