# LLM Serving Issue Radar

_Last run: 2026-09-11T13:28+00:00_

**13 issues** — sgl-project/sglang: 4, vllm-project/vllm: 9 — 🆕 **13 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Build / Install / Platform](#build--install--platform) — 3

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#56402](https://github.com/vllm-project/vllm/issues/56402) [RFC]: Efficient Routed-Expert Replay with Prefix Omission and KV Cache Offloading

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#39087](https://github.com/sgl-project/sglang/issues/39087) [Bug] Quantized DFlash2 draft silently yields ~0% acceptance — no error, no warning (the quiet counterpart to #36599)

### vllm-project/vllm

- [Bug] 🆕 [#56457](https://github.com/vllm-project/vllm/issues/56457) [Bug] Qwen4Exp QSA indexer: per-chunk logits buffer grows with max_seq_len, caching allocator keeps every size, device OOM/hang on unified-memory GB10 (SM121) during long prefill

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#56389](https://github.com/vllm-project/vllm/issues/56389) [Bug]: DeepSeek-V4.1-Flash dsv4_topk Triton illegal memory access under high concurrency on H20; mitigated by max_num_seqs=256
- [Bug] 🆕 [#56370](https://github.com/vllm-project/vllm/issues/56370) [Bug]: Batch invariance is broken when sequence parallelism / async TP is enabled (`VLLM_BATCH_INVARIANT=1` + `pass_config.enable_sp`)

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#39070](https://github.com/sgl-project/sglang/issues/39070) [Bug] FLUX.2 rejects --attention-backend sage_attn: model-level whitelist excludes SAGE_ATTN (regression since #22423)
- [Bug] 🆕 [#38980](https://github.com/sgl-project/sglang/issues/38980) [Bug] sgl_kernel flash_attn: is_fa3_supported() accepts sm_89 but no sm_89 cubin ships, and `ver` is ignored

### vllm-project/vllm

- [Bug] 🆕 [#56428](https://github.com/vllm-project/vllm/issues/56428) [Bug]: Reasoning still returned in /responses while include_reasoning is set to false

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#39072](https://github.com/sgl-project/sglang/issues/39072) [Bug] GLM-5.3 crash on disagg decode + dp-attention + spec decode

### vllm-project/vllm

- [Bug] 🆕 [#56419](https://github.com/vllm-project/vllm/issues/56419) [Bug]: CPU Gated-DeltaNet — EngineCore dies when constrained decoding rejects all speculative draft tokens (num_accepted_tokens=0 violates causal_conv1d_update_cpu precondition)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#56384](https://github.com/vllm-project/vllm/issues/56384) [Bug]: [Bug][Docker] Recipe references vllm/vllm-openai-rocm:deepseekv41-flash-0909 but the image is not available on Docker Hub
- [Bug] 🆕 [#56363](https://github.com/vllm-project/vllm/issues/56363) [Bug]: Qwen3-VL fails when using modality-scoped image/video size kwargs (`images_kwargs` / `videos_kwargs`)
- [Bug] 🆕 [#56347](https://github.com/vllm-project/vllm/issues/56347) [Bug][ROCm]: DeepSeek-V4.1 segfaults on the 3rd decode token with FULL_DECODE_ONLY graphs unless --no-async-scheduling is set
