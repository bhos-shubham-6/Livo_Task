# Livo AI SWE Intern Assessment - Option B

This folder contains a complete Option B submission package:

- `submission.md` - final write-up to paste in the form
- `qa_pairs.json` - 5 question-answer pairs with source references
- `methodology.md` - how questions were selected and what they test
- `scripts/fetch_transcripts.py` - helper script to pull YouTube transcripts

## Quick usage

1. Review/edit `submission.md` for your tone.
2. Submit content in the Google Form from your email.

## Optional: pull transcripts locally

Install dependency:

```bash
pip install youtube-transcript-api
```

Run:

```bash
python scripts/fetch_transcripts.py
```

This writes transcript text files into `transcripts/`.
