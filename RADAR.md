# LLM Serving Issue Radar

_Last run: 2026-10-16T13:30+00:00_

**13 issues** — sgl-project/sglang: 9, vllm-project/vllm: 4 — 🆕 **13 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#44635](https://github.com/sgl-project/sglang/issues/44635) [RFC] Context-parallel support for the unified L3 key scheme

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#44735](https://github.com/sgl-project/sglang/issues/44735) [Bug] HiCache host-tier hit on hybrid GDN model (Qwen3.8-Flash-Next) returns wrong output — kernel and direct io both affected
- [other] 🆕 ⚠maintainer-authored [#44675](https://github.com/sgl-project/sglang/issues/44675) [Roadmap] Intel CPU (Xeon) Backend Optimization (2026Q4)
- [other] 🆕 ⚠maintainer-authored [#44674](https://github.com/sgl-project/sglang/issues/44674) [Roadmap] Intel GPU (XPU) Backend Optimization (2026Q4)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [RFC] 🆕 [#44697](https://github.com/sgl-project/sglang/issues/44697) [RFC] MoE routing simulator for prefill imbalance profiling: balanced reference and GPU-faithful replay

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#62003](https://github.com/vllm-project/vllm/issues/62003) [Bug]: mamba_ssm_cache_dtype="float16" crashes mamba-family models at startup — bare kernel assertion with an empty message (selective_scan_fwd.cu:791)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#44745](https://github.com/sgl-project/sglang/issues/44745) [Bug] When client disconnect with `pause_generation(mode="abort")` and `release_memory_occupation` kills the scheduler
- [Bug] 🆕 [#44744](https://github.com/sgl-project/sglang/issues/44744) [Bug] `pause_generation(mode="retract")` while a request's grammar is compiling, then `release_memory_occupation` with an AssertionError kills the scheduler
- [other] 🆕 ⚠maintainer-authored [#44678](https://github.com/sgl-project/sglang/issues/44678) [Roadmap] Muse Spark Open Development & Optimization

### vllm-project/vllm

- [Performance] 🆕 ⚠maintainer-authored [#61998](https://github.com/vllm-project/vllm/issues/61998) [Performance]: Monolithic Triton top-k kernel falls back to full-vocab search on real logits (outlier gather misses)
- [Bug] 🆕 ⚠maintainer-authored [#61997](https://github.com/vllm-project/vllm/issues/61997) [Bug]: Split top-p mask kernel restarts its tie count every 8192 entries and over-keeps boundary ties

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#61972](https://github.com/vllm-project/vllm/issues/61972) [Bug]: --reasoning-parser qwen3: leading \n\n left in content after stripping the <think> block

## Build / Install / Platform

### sgl-project/sglang

- [Perf] 🆕 [#44656](https://github.com/sgl-project/sglang/issues/44656) [Perf] HiCache Throughput Loss Analysis in Long-Context MLA Workloads
