# Assessment authoring guide

The curriculum contains exactly 250 original four-option, single-answer questions: 50 for each official AZ-104 domain.

## Domain difficulty mix

Every domain contains:

- 15 foundational questions
- 25 applied scenario questions
- 10 advanced troubleshooting or design questions

Correct-answer positions A–D must each occur 12 or 13 times in a domain.

## Lab allocation

- Identity and governance: Labs 01–05, 10 questions each.
- Storage: Labs 06–09 with 12, 12, 14, and 12 questions.
- Compute: Labs 10–16 with 10, 8, 8, 6, 4, 7, and 7 questions.
- Networking: Labs 17–21, 10 questions each.
- Monitoring and recovery: Labs 22–25 with 15, 10, 15, and 10 questions.
- Lab 00 and Capstones 26–27 have no separate assessment directories.

## Files and rules

- `assessment/questions.yml` is the source of truth.
- `assessment/QUESTIONS.md` contains no answers or answer-key metadata.
- `assessment/ANSWERS.md` explains the correct option and every distractor.
- Every question maps only to objective IDs in its lab's declared assessment domain.
- Every official objective appears in at least one question.
- Use current official Microsoft sources and never use exam dumps or copied practice questions.
