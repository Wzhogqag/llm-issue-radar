# LLM Serving Issue Radar

_Last run: 2026-10-21T13:30+00:00_

**16 issues** — sgl-project/sglang: 5, vllm-project/vllm: 11 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#45510](https://github.com/sgl-project/sglang/issues/45510) [Bug] --max-queued-requests 0 with priority scheduling crashes the scheduler on an empty queue
- [RFC] 🆕 [#45547](https://github.com/sgl-project/sglang/issues/45547) [RFC] adapter hisparse to npu

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#45527](https://github.com/sgl-project/sglang/issues/45527) [RFC] PD disaggregation: send the last KV chunk from later PP stages as soon as their forward finishes

### vllm-project/vllm

- [Performance] 🆕 [#62862](https://github.com/vllm-project/vllm/issues/62862) [Performance]: MultiConnector([NixlConnector, OffloadingConnector]) disables divergent local hybrid cache hits on Decode
- [Bug] 🆕 [#62808](https://github.com/vllm-project/vllm/issues/62808) [Bug]: Built-in LMCacheConnectorV1 does not forward shutdown(), so LMCache never stops and EngineCore is force-killed

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#62820](https://github.com/vllm-project/vllm/issues/62820) [Bug]: FlashInfer fp4_gemm autotune changes temperature-0 tokens on Qwen3.8-27B NVFP4 (SM120)
- [Bug] 🆕 [#62803](https://github.com/vllm-project/vllm/issues/62803) [Bug]: Investigate uniform decision scores for a D3 checkpoint loaded as Qwen3.5

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#62801](https://github.com/vllm-project/vllm/issues/62801) [Bug]: MoE LoRA accepts incompatible round-robin expert placement with EP

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#45563](https://github.com/sgl-project/sglang/issues/45563) [Bug] HiCache NIXL L3: under O_DIRECT the DSA indexer sidecar is never written, and the 0-byte objects are restored as hits, so restored prefixes get zero index-K (silent output change, EAGLE accept collapse)
- [Bug] 🆕 [#45525](https://github.com/sgl-project/sglang/issues/45525) [Bug] DeepSeek-V4-Flash: speculative and ordinary decoding produce different greedy outputs

### vllm-project/vllm

- [Bug] 🆕 [#62851](https://github.com/vllm-project/vllm/issues/62851) [Bug]: Qwen3.6 GDN greedy DFlash2 divergence from batch-dependent numerics and preemption/recompute (v0.31.0)
- [RFC] 🆕 [#62818](https://github.com/vllm-project/vllm/issues/62818) [RFC]: Preserve output distribution under structured-output + speculative decoding

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#62865](https://github.com/vllm-project/vllm/issues/62865) [Bug]: Compile mode 2 leads to incorrect kernels when the Transformers backend is used
- [other] 🆕 [#62844](https://github.com/vllm-project/vllm/issues/62844) [Installation]: [ROCm] Gemma4 multimodal model fails to start on vLLM 0.32.0 due to excessive video encoder memory reservation (negative KV cache)
- [other] 🆕 [#62842](https://github.com/vllm-project/vllm/issues/62842) [Installation]: cu129
- [other] 🆕 [#62804](https://github.com/vllm-project/vllm/issues/62804) [Feature / Question]::  /v1/systemone rejects image inputs on standard multimodal VLMs with "this model does not take image inputs"
