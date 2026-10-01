# LLM Serving Issue Radar

_Last run: 2026-10-01T13:34+00:00_

**18 issues** — sgl-project/sglang: 7, vllm-project/vllm: 11 — 🆕 **18 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 4
- [Quantization](#quantization) — 7
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#59538](https://github.com/vllm-project/vllm/issues/59538) [RFC]: A Reusable KV Compression Layer for Transfer and Storage

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#42012](https://github.com/sgl-project/sglang/issues/42012) [Bug] GLM-5.3-Flash on SM120: fa4 attention backend crashes at CUDA-graph capture (hybrid extend reshape) — triton is the only working backend

### vllm-project/vllm

- [Performance] 🆕 [#59548](https://github.com/vllm-project/vllm/issues/59548) [Performance]: spec-decode boot-to-boot throughput dispersion on L4 (CV up to 13.92%), resolved in 0.30.0
- [Performance] 🆕 [#59534](https://github.com/vllm-project/vllm/issues/59534) [Performance]: FlashAttention backend rebuilds KV-cache views on every call (+~21 µs CPU/layer since #44455)
- [Feature] 🆕 [#59498](https://github.com/vllm-project/vllm/issues/59498) [Feature]: Route FlashInfer sparse-MLA decode autotune through the PP-aware tuning group and cache

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#41939](https://github.com/sgl-project/sglang/issues/41939) [Bug] GLM-5.3-Flash NVFP4 at TP4 loops in reasoning with no final answer on B200/B300
- [no-prefix] 🆕 ⚠no-prefix [#42024](https://github.com/sgl-project/sglang/issues/42024) Benchmark: Qwen3.8-27B FP8 on H200 with bfloat16 SSM state (24 speed rows, 4 full GSM8K scores)
- [no-prefix] 🆕 ⚠no-prefix [#41938](https://github.com/sgl-project/sglang/issues/41938) Benchmark: Qwen3.8-27B FP8 on H200 with float32 SSM state (24 speed rows, 4 full GSM8K scores)

### vllm-project/vllm

- [Bug] 🆕 [#59551](https://github.com/vllm-project/vllm/issues/59551) [Bug]: Qwen3.6-35B-A3B model with TP 2 and DP 2 returns gibberish output on Intel B70 cards
- [other] 🆕 [#59575](https://github.com/vllm-project/vllm/issues/59575) [ROCm][AMD] Qwen3.8-Flash-Next gfx950 / MI355X Performance Optimization
- [other] 🆕 [#59560](https://github.com/vllm-project/vllm/issues/59560) [ROCm][Perf]: Tune FP8 Gemma4 MLP gate-up and down projs for prefills on gfx942
- [RFC] 🆕 [#59502](https://github.com/vllm-project/vllm/issues/59502) [RFC]: Modulewise weight reload

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Performance] 🆕 [#59520](https://github.com/vllm-project/vllm/issues/59520) [Performance]: Default CUDA GDN wrapper regresses non-spec Qwen3.5 throughput on H200

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#42052](https://github.com/sgl-project/sglang/issues/42052) [Feature] Native GPT-Neo support

## Sampling / Speculative Decoding

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#41946](https://github.com/sgl-project/sglang/issues/41946) Benchmark: DeepSeek-V4.1-Flash B200/B300 TP4/EP4 (28 speed rows, 4 full GSM8K scores)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#59576](https://github.com/vllm-project/vllm/issues/59576) [Bug]: Rust vllm-bench ignores usage.prompt_tokens, under-reporting total input tokens

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#59569](https://github.com/vllm-project/vllm/issues/59569) [Bug]: [KV Offload][P2P] Store-job timeout unpins slots under an in-flight transfer, which then reports success

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#41995](https://github.com/sgl-project/sglang/issues/41995) [Bug] Security Report
