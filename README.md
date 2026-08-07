# ai-engineering

Working through an AI engineering syllabus, one lesson per directory. Each lesson is
small, runnable code that makes a single concept concrete.

Lesson directories are named `NN_snake_case`, so paths need no quoting in the shell and
stay importable from Python.

## Setup

The project is managed with [uv](https://docs.astral.sh/uv/) and pinned to Python 3.14.

```bash
uv sync
```

## Lessons

### 01 — Tokenization, context, and cost

```bash
uv run 01_tokenization_context_cost/token_calc.py
```

Encodes example strings with `tiktoken`'s `cl100k_base` encoding and prints the
individual token pieces, so you can see exactly where the tokenizer splits text.

Two things the output makes obvious:

**Tokenizers are not language-neutral.** Equal-length strings do not cost the same:

| Text | Characters | Tokens | Pieces |
| --- | --- | --- | --- |
| `Hello, world!` | 13 | 4 | `Hello` `,` ` world` `!` |
| `Jambo, dunia!` | 13 | 6 | `Jam` `bo` `,` ` dun` `ia` `!` |

The Swahili greeting fragments into subwords because those words are not in the
vocabulary, so the same sentence costs 50% more to send. Kenya-specific terms behave the
same way — `M-Pesa` splits into `M` `-P` `esa`, `CBK` into `CB` `K` — while
`The Central Bank of Kenya` is 5 clean tokens because each word is common English.

**The ~4-characters-per-token rule is only a rough average.** The script encodes 400
repeated characters and gets 50 tokens — about 8 characters per token, since the
tokenizer merges long runs of a repeated character into single tokens. The heuristic is
useful for estimating typical prose, not for any specific string.
