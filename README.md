# LLM Serving Issue Radar

A daily digest of **unclaimed, actionable issues** in [vLLM](https://github.com/vllm-project/vllm)
and [SGLang](https://github.com/sgl-project/sglang) — classified by subsystem so you can spot
where the two projects are wrestling with the same problem.

## What it does

A six-stage pipeline (`radar.py`, standard library + `gh` CLI, no extra deps):

| Stage | Output |
|-------|--------|
| **Fetch**    | Recent open issues per repo via GitHub REST |
| **Filter**   | Drops PRs, bots, assigned, stale, empty templates |
| **PR-check** | Skips issues that already have an open PR (timeline scan) |
| **Classify** | Buckets into 10 subsystems (scheduler, KV cache, attention, quantization, …) |
| **Rank**     | Freshness × approachability × repro signal |
| **Write**    | Emits [`RADAR.md`](RADAR.md), one section per category |

Both repos appear under the same category headers, so it's a two-column read:
what's open on the vLLM side vs. the SGLang side of the same concept.

## Running it

**Locally** — requires `gh` CLI logged in:

```bash
python3 radar.py
```

**In GitHub Actions** — see [`.github/workflows/radar.yml`](.github/workflows/radar.yml).
The daily cron will be turned on once the pipeline is validated end-to-end.

## Configuration

Watchlist, category rules, and limits live in [`config.json`](config.json). Keywords
are case-insensitive substring matches; path patterns match against issue body.

## Design notes

- **Standard library only.** The GitHub REST endpoints are small enough to hit
  through `gh api` without a client library.
- **No Search API.** Rate limits are aggressive; the list + timeline endpoints
  are enough.
- **State lives in `seen.json`.** No database — CI commits the file back to the
  repo so the next run knows what's new.

## Status

Scaffold. See phase checklist in the setup log.
