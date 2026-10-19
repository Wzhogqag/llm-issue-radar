# LLM Serving Issue Radar

_Last run: 2026-10-19T13:34+00:00_

**6 issues** — sgl-project/sglang: 3, vllm-project/vllm: 3 — 🆕 **6 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#45074](https://github.com/sgl-project/sglang/issues/45074) [Feature] Offline batch runner for OpenAI batch files (follow-up to #7427)
- [RFC] 🆕 ⚠maintainer-authored [#45128](https://github.com/sgl-project/sglang/issues/45128) [RFC] linker: Prefetch SSD-resident KV while the request is queued

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#62388](https://github.com/vllm-project/vllm/issues/62388) [Feature]: HF3FSKVConnector: support models with more than one KV cache shape (e.g. MLA + DSA indexer)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#62460](https://github.com/vllm-project/vllm/issues/62460) [Bug][Rust Frontend] /v1/completions rejects an array of prompts

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#45159](https://github.com/sgl-project/sglang/issues/45159) [Bug] GLM-5.3-Flash on 8×H20 (TP8/EP8) with EAGLE: CUDA illegal memory access in run_eagle_verify → build_grammar_vocab_mask

## Performance / Memory / OOM

### vllm-project/vllm

- [Perf] 🆕 [#62442](https://github.com/vllm-project/vllm/issues/62442) [Perf]: ~2x decode throughput regression for structured outputs since #45424 (apply_grammar_bitmask staging), not fixed by #49919
