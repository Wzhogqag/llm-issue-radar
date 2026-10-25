# LLM Serving Issue Radar

_Last run: 2026-10-25T13:26+00:00_

**11 issues** — sgl-project/sglang: 2, vllm-project/vllm: 9 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#63549](https://github.com/vllm-project/vllm/issues/63549) [Bug]: Async scheduling + preemption crashes Model Runner V1 with KeyError all_token_ids[req_id] in _update_states
- [Bug] 🆕 [#63519](https://github.com/vllm-project/vllm/issues/63519) [Bug]: Deferred block-free fence (#45357) does not cover speculator `propose()` KV writes in the V2 model runner

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Perf] 🆕 [#63517](https://github.com/vllm-project/vllm/issues/63517) [Perf][Qwen4Exp] Hybrid KV-cache capacity accounting: merged main-KV+indexer groups share one block table — slots/request are coverage-set; page bytes buy blocks via bytes_per_block

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#63536](https://github.com/vllm-project/vllm/issues/63536) [Bug]: [Usage]: RTX PRO 5000 (SM120) deadlocks at 3-4W during vLLM 0.32.0 startup with 70B NVFP4 model, even with --enforce-eager
- [Bug] 🆕 [#63514](https://github.com/vllm-project/vllm/issues/63514) [Bug]: `hadacore_transform` gives wrong results for odd row counts (INT4 per-token-head KV cache): garbage K/V and intermittent illegal memory access

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#46390](https://github.com/sgl-project/sglang/issues/46390) [Bug] multimodal_gen: cross-node pure-Ulysses H3 serve (1 GPU/node x 4 nodes) freezes at the first distributed generation - /health never binds with --warmup-mode off, 0% GPU on all ranks, zero errors

### vllm-project/vllm

- [Bug] 🆕 [#63573](https://github.com/vllm-project/vllm/issues/63573) [Bug][Anthropic API] /v1/messages/count_tokens requires --tool-call-parser when tools are present

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#63501](https://github.com/vllm-project/vllm/issues/63501) [RFC]: Select the MRV2 DBO microbatch count per step within an allocated capacity

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#46326](https://github.com/sgl-project/sglang/issues/46326) [Bug] ValueError: The checkpoint you are trying to load has model type `qwen4_exp` but Transformers does not recognize this architecture.

### vllm-project/vllm

- [Bug] 🆕 [#63505](https://github.com/vllm-project/vllm/issues/63505) [Bug]: Qwen3.8-27B (GDN hybrid) with PP=3 on sm_86: illegal memory access (Xid 31) with prefix caching, gibberish output without it; regression since v0.28.0 (v0.31.0, v0.32.0, both model runners)

## Uncategorized

### vllm-project/vllm

- [Feature] [#63470](https://github.com/vllm-project/vllm/issues/63470) [Feature]: Run Nemotron 3.5 Super VL without the --trust-remote-code flag
