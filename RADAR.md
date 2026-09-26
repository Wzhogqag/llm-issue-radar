# LLM Serving Issue Radar

_Last run: 2026-09-26T13:25+00:00_

**9 issues** — sgl-project/sglang: 4, vllm-project/vllm: 5 — 🆕 **9 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Quantization](#quantization) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#58774](https://github.com/vllm-project/vllm/issues/58774) [RFC]: Native span pooling for contextual chunk embeddings

## Quantization

### vllm-project/vllm

- [Performance] 🆕 [#58799](https://github.com/vllm-project/vllm/issues/58799) [Performance]: Suboptimal SM90 FP8 CUTLASS MoE dispatch on H20 EP8 — upstream fix proposed
- [Bug] 🆕 [#58742](https://github.com/vllm-project/vllm/issues/58742) [Bug]: MFU/MBU silently drops attention and FFN for GPTQ, AWQ, gpt-oss, DeepSeek-V4 FP8 and online-quantized models

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#41351](https://github.com/sgl-project/sglang/issues/41351) [Bug] Potential hybrid GDN Radix-cache selected-logprob drift on repeated branch scoring

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#58751](https://github.com/vllm-project/vllm/issues/58751) [RFC]: Universal Triton kernel autotuning at warmup

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#41299](https://github.com/sgl-project/sglang/issues/41299) [Bug][ROCm] Qwen3.8-Flash-Next (qwen4_exp) crashes with HSAIL hardware exception 0x1016 on the first 16k prefill chunk, gfx950 TP1

### vllm-project/vllm

- [Performance] 🆕 [#58804](https://github.com/vllm-project/vllm/issues/58804) [Performance][Bug]: Tiered Offloading

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#41332](https://github.com/sgl-project/sglang/issues/41332) Optional per-request settlement rail (HTTP 402) for metered self-hosted serving
- [no-prefix] 🆕 ⚠no-prefix [#41260](https://github.com/sgl-project/sglang/issues/41260) Does a keyless upstream have to go without model discovery?
