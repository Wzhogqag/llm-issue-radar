# LLM Serving Issue Radar

_Last run: 2026-08-13T13:50+00:00_

**18 issues** — sgl-project/sglang: 5, vllm-project/vllm: 13 — 🆕 **18 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 6
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#34676](https://github.com/sgl-project/sglang/issues/34676) [Bug] Hybrid Mamba prefill allocation failure kills scheduler instead of returning request to waiting queue

### vllm-project/vllm

- [RFC] 🆕 [#52113](https://github.com/vllm-project/vllm/issues/52113) [RFC]: Session-Aware KV Cache Hints for Agentic Workloads

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#52137](https://github.com/vllm-project/vllm/issues/52137) [Feature]: split local/external prefix-cache hits in `prompt_tokens_details`
- [no-prefix] 🆕 ⚠no-prefix [#52170](https://github.com/vllm-project/vllm/issues/52170) OffloadingConnector AssertionError in _build_store_jobs under MultiConnector with high concurrency multi-turn

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#52065](https://github.com/vllm-project/vllm/issues/52065) [Bug]: DeepSeek-V4-Flash-0731 + DSpark fails to start on vLLM 0.27.0 / H100 sm90 (DeepGEMM CUDA_ERROR_ILLEGAL_ADDRESS); works on 0.26.0

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#34718](https://github.com/sgl-project/sglang/issues/34718) [Bug] DeepSeek-V4 sparse attention indexer (`fp8_paged_mqa_logits`) illegal memory access with long-context requests

### vllm-project/vllm

- [RFC] 🆕 [#52167](https://github.com/vllm-project/vllm/issues/52167) [RFC]: Extended online quantization roadmap

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#52155](https://github.com/vllm-project/vllm/issues/52155) [Bug]: VLLM_BATCH_INVARIANT does not cover convolution, used in VAE blocks

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34740](https://github.com/sgl-project/sglang/issues/34740) [Bug] SGLANG_SIMULATE_ACC_LEN silently degrades detokenization to O(n²) — `predict.fill_(100)` emits a byte-fallback token, and the `endswith("\ufffd")` commit gate then never advances the incremental-detokenization offsets
- [Bug] 🆕 [#34720](https://github.com/sgl-project/sglang/issues/34720) [Bug] [XPU] Qwen3.5 GDN + speculative decode: causal_conv1d_update_xpu() got an unexpected keyword argument 'intermediate_conv_window'
- [Bug] 🆕 [#34719](https://github.com/sgl-project/sglang/issues/34719) [Bug] Scheduler crashes with AttributeError ('list' object has no attribute 'tolist') on mixed batches with token_ids_logprob — prefill and decode paths, v0.5.14–v0.5.17

### vllm-project/vllm

- [Bug] 🆕 [#52071](https://github.com/vllm-project/vllm/issues/52071) [Bug]: speculative decoding under pipeline parallelism produces wrong output with --no-async-scheduling
- [Bug] 🆕 [#52069](https://github.com/vllm-project/vllm/issues/52069) [Bug]: MTP speculative decoding cannot start under pipeline parallelism — SupportsPP demanded of the draft model
- [Feature] 🆕 ⚠maintainer-authored [#52053](https://github.com/vllm-project/vllm/issues/52053) [Feature][DSpark]: Evaluate STS for online DSpark confidence alignment

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#52089](https://github.com/vllm-project/vllm/issues/52089) [Bug]: Continuous Host Memory Growth / Possible Memory Leak with V2 Runner on Qwen3-14B and Qwen3-Rerank-4B
- [Feature] 🆕 ⚠maintainer-authored [#52057](https://github.com/vllm-project/vllm/issues/52057) [Feature][DSpark]: Improve Adaptive DSpark Online Profiling

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#52150](https://github.com/vllm-project/vllm/issues/52150) [Bug][ROCm/gfx942]: GLM-5.2-FP8 — first request after GPU idle emits garbage; piecewise CUDA graph cold replay corrupts the request's own prefill (workaround: cudagraph_mode=FULL_DECODE_ONLY)
- [Bug] 🆕 [#52109](https://github.com/vllm-project/vllm/issues/52109) [Bug][ROCm/gfx942]: DeepSeek-V4-Flash silent retrieval corruption for prompts ≥ ~4-5k tokens (AITER sparse indexer)
