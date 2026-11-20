# LLM Serving Issue Radar

_Last run: 2026-11-20T13:22+00:00_

**20 issues** — sgl-project/sglang: 9, vllm-project/vllm: 11 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#51726](https://github.com/sgl-project/sglang/issues/51726) [Feature] diffusion/pi05: real-time chunking (RTC)
- [no-prefix] 🆕 ⚠no-prefix [#51834](https://github.com/sgl-project/sglang/issues/51834) SGLang: stop_regex is evaluated on the scheduler thread, so a crafted regex blocks all decoding for minutes

### vllm-project/vllm

- [RFC] 🆕 [#68938](https://github.com/vllm-project/vllm/issues/68938) [RFC]: Rank-local host backing and SM120 DCP for HiSparse

## Quantization

### sgl-project/sglang

- [RFC] 🆕 [#51733](https://github.com/sgl-project/sglang/issues/51733) [RFC] HiCache: Size and stage for unified memory (GB10 / DGX Spark)

### vllm-project/vllm

- [Bug] 🆕 [#68897](https://github.com/vllm-project/vllm/issues/68897) [Bug]: DeepSeek-V4-Flash + DSpark TP4 on SM120: intermittent CUDA_ERROR_ILLEGAL_ADDRESS in KV-cache sizing warm-up
- [Bug] 🆕 [#68848](https://github.com/vllm-project/vllm/issues/68848) [Bug]: GLM5.2 KV scale loading failure
- [Feature] 🆕 [#68849](https://github.com/vllm-project/vllm/issues/68849) [Feature]: Transformers backend: gpt-oss experts are never fused, and MXFP4 raises NotImplementedError

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#68919](https://github.com/vllm-project/vllm/issues/68919) [Bug][ROCm] GLM-5.3 with `index_topk_freq` > 1 dies at load in the AMD DeepSeek V3.2 loader: `KeyError 'layers.14.self_attn.indexer.k_norm.weight'` (v0.31.0 to v0.34.0)

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#68890](https://github.com/vllm-project/vllm/issues/68890) [Feature]: Support attention-only LoRA under MRV2 prefill context parallelism (PCP)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [other] 🆕 [#51740](https://github.com/sgl-project/sglang/issues/51740) [Benchmark] Qwen3.8-27B-FP8 at 256K on one RTX 4090 48GB: 18-batch code review — SGLang 0.5.23 vs FastLLM 1.9.2 / vLLM 0.34.0 / llama.cpp b12498
- [no-prefix] 🆕 ⚠no-prefix [#51835](https://github.com/sgl-project/sglang/issues/51835) SGLang: max_new_tokens and n have no server-side upper bounds, so one request can monopolize the scheduler

### vllm-project/vllm

- [other] 🆕 [#68877](https://github.com/vllm-project/vllm/issues/68877) [Benchmark] Qwen3.8-27B-FP8 at 256K on one RTX 4090 48GB: 18-batch code review — vLLM 0.34.0 vs FastLLM 1.9.2 / SGLang 0.5.23 / llama.cpp b12498

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#68906](https://github.com/vllm-project/vllm/issues/68906) [Bug]: DeepSeek-V4.1-Flash PP2 warmup hits the mHC residual assertion on H200 at the 20/20 split
- [RFC] 🆕 ⚠maintainer-authored [#68891](https://github.com/vllm-project/vllm/issues/68891) [RFC]: Token-Level Handoff for Encoder Disaggregation

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#51833](https://github.com/sgl-project/sglang/issues/51833) SGLang: structured output parameters are compiled without length or complexity limits, enabling denial of service

### vllm-project/vllm

- [Bug] 🆕 [#68870](https://github.com/vllm-project/vllm/issues/68870) [Bug]: Qwen3.5 BF16 crashes with DEBUG logging on GB10: CUDA graph capture/replay input mismatch (v0.34.0)
- [RFC] 🆕 [#68959](https://github.com/vllm-project/vllm/issues/68959) [RFC][XPU] Enable HiSparse on Intel XPU

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#51837](https://github.com/sgl-project/sglang/issues/51837) SGLang: multimodal requests accept unvalidated local file paths, enabling server-side arbitrary file reads
- [no-prefix] 🆕 ⚠no-prefix [#51836](https://github.com/sgl-project/sglang/issues/51836) SGLang: /slow_down accepts an unbounded sleep value without authentication, stalling every subsequent inference
- [no-prefix] 🆕 ⚠no-prefix [#51832](https://github.com/sgl-project/sglang/issues/51832) SGLang: /configure_logging dump folder is not validated, enabling arbitrary-path file writes
