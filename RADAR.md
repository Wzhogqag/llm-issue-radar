# LLM Serving Issue Radar

_Last run: 2026-11-12T13:23+00:00_

**14 issues** — sgl-project/sglang: 6, vllm-project/vllm: 8 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#50073](https://github.com/sgl-project/sglang/issues/50073) [Bug] collective_rpc unreliable

## Attention Backend

### vllm-project/vllm

- [RFC] 🆕 [#67176](https://github.com/vllm-project/vllm/issues/67176) [RFC]: UltraQuant: the scale constant c = 0.156 is MSE-optimal before the UE8M0 snap, not after; c ≈ 0.2 cuts KV-quantization KL by 40–56% at no cost

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#50030](https://github.com/sgl-project/sglang/issues/50030) [Bug] --enable-hisparse fails at start-up for GLM-5.3-Flash: 'HybridLinearKVPool' object has no attribute 'register_mapping'

### vllm-project/vllm

- [other] 🆕 [#67169](https://github.com/vllm-project/vllm/issues/67169) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#50103](https://github.com/sgl-project/sglang/issues/50103) [Bug] Qwen3-VL on Hopper: the default prefill_decode_interval=22 lowers request throughput on long-prompt and text traffic (interval 0 is 9.5–36% faster)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#50037](https://github.com/sgl-project/sglang/issues/50037) [Bug] Qwen3.5 long-context prefill can produce NaNs in the Blackwell CuTe DSL GDN inverse kernel
- [Feature] 🆕 [#50087](https://github.com/sgl-project/sglang/issues/50087) [Feature] Non-intrusive dumps cannot distinguish draft vs target model under DSPARK (both are TARGET_VERIFY)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#67137](https://github.com/vllm-project/vllm/issues/67137) [Bug]: `vllm launch render` accepts `--lora-modules` but returns 404 for the adapter name on `/render` and `/derender`
- [Feature] 🆕 [#67231](https://github.com/vllm-project/vllm/issues/67231) [Feature]:  Support Hugging Face Tokenizers v1
- [RFC] 🆕 [#67197](https://github.com/vllm-project/vllm/issues/67197) [RFC]: Resource bound for the `/tokenize` endpoint

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#67183](https://github.com/vllm-project/vllm/issues/67183) [Bug]: Regression from #47692 - `--data-parallel-start-rank 0` with `data_parallel_size == 1` crashes at startup ("data_parallel_external_lb can only be set when data_parallel_size > 1")

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#50045](https://github.com/sgl-project/sglang/issues/50045) SGLang 1.0 Release Tracker

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#67204](https://github.com/vllm-project/vllm/issues/67204) [Feature]: Add a workload-aware E+PD sizing example
- [Feature] 🆕 [#67170](https://github.com/vllm-project/vllm/issues/67170) [Feature]:
