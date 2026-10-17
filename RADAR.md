# LLM Serving Issue Radar

_Last run: 2026-10-17T13:25+00:00_

**21 issues** — sgl-project/sglang: 5, vllm-project/vllm: 16 — 🆕 **21 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 7
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [other] 🆕 [#62083](https://github.com/vllm-project/vllm/issues/62083) [RFC / Research Showcase] SPICY-KV: 28.6x–50x Pre-RoPE Algebraic Multigrid KV Compression + 4-Byte Subgrid Variance Calibration (91.7%–100% RULER Recall on DeepSeek-R1 7B & 1.5B)
- [RFC] 🆕 [#62145](https://github.com/vllm-project/vllm/issues/62145) [RFC]: Request-scoped auxiliary decision heads on a shared generative backbone

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#62100](https://github.com/vllm-project/vllm/issues/62100) [RFC][Experimental]: Model- and platform-customized KV cache planning
- [RFC] 🆕 [#62150](https://github.com/vllm-project/vllm/issues/62150) [RFC]: PD disaggregation + RL lifecycle (pause, sleep, abort) tracking

## Attention Backend

### sgl-project/sglang

- [other] 🆕 [#44786](https://github.com/sgl-project/sglang/issues/44786) [RFC / Feature] SPICY-KV: 28.6x–50x Pre-RoPE Algebraic Multigrid KV Compression for RadixAttention & Long-CoT (91.7%–100% RULER Recall & 100% Shared-Prefix Multi-Query Reuse)

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#62156](https://github.com/vllm-project/vllm/issues/62156) [Bug]: sharded_state can't round-trip models with attention/KV-cache scale params (Missing keys ...attn.q_scale, k_scale, v_scale, prob_scale)
- [Bug] 🆕 [#62136](https://github.com/vllm-project/vllm/issues/62136) [Bug]:  quantization="mxfp8" + moe_backend="humming" crashes weight conversion with a bare KeyError: 'weight_scale' — the MXFP8 oracle selects humming, then a third-party schema converter raises
- [Bug] 🆕 [#62105](https://github.com/vllm-project/vllm/issues/62105) [Bug]: `--load-format ipc_cache` leaves MoE routers on meta placeholders (illegal memory access, meta-tensor errors)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#62118](https://github.com/vllm-project/vllm/issues/62118) [Bug]: Qwen3.8-Flash-Next (qwen4_exp) deadlocks on RTX 6000D (SM120) — hangs in JIT warmup and at first real request (GDN/hyperconnection kernels); Qwen3.8-27B works fine on the same box
- [Bug] 🆕 [#62116](https://github.com/vllm-project/vllm/issues/62116) [Bug]: GDN chunk/prefill path overflows fp16 with a large fp32 SSM state (chunk-path follow-up to #54146)

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#44885](https://github.com/sgl-project/sglang/issues/44885) [Feature] kv-shard: Pass Q instead of KV for short prefills with long cached prefixes

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#44840](https://github.com/sgl-project/sglang/issues/44840) [Bug] `pause_generation(abort)` + `release_memory_occupation` right after a client disconnect crashes scheduler
- [Bug] 🆕 [#44835](https://github.com/sgl-project/sglang/issues/44835) [Bug] With `pause_generation(in_place)` then `pause_generation(abort)`, the server hangs until killed by watchdog
- [Bug] 🆕 [#44834](https://github.com/sgl-project/sglang/issues/44834) [Bug] `update_weights_from_disk` after `release_memory_occupation` is accepted and crashes the scheduler (segfault in `weight_loader`)

### vllm-project/vllm

- [Bug] 🆕 [#62153](https://github.com/vllm-project/vllm/issues/62153) [Bug]: Mamba2 hybrid models crash once the prompt is longer than block_size (regression from #57329)
- [Bug] 🆕 [#62143](https://github.com/vllm-project/vllm/issues/62143) [Bug]: Model Runner V2 hangs during speculative decoding warmup with pipeline parallelism
- [Bug] 🆕 [#62094](https://github.com/vllm-project/vllm/issues/62094) [Bug]: Adaptive verification fails at startup with the default attention backend on FA2 GPUs
- [other] 🆕 [#62130](https://github.com/vllm-project/vllm/issues/62130) [Spec Decode] Compose grammar-constrained sampling with EAGLE speculative decoding

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#62096](https://github.com/vllm-project/vllm/issues/62096) [Feature]: Default to NextTokenPrediction Read strategy for text generation models for /v1/systemone and /v1/decisions
- [Bug] 🆕 ⚠maintainer-authored [#62085](https://github.com/vllm-project/vllm/issues/62085) [Bug]: Stop sequences match inside reasoning, so responses come back empty (breaks Claude Code auto mode)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#62121](https://github.com/vllm-project/vllm/issues/62121) [Bug]: Race condition in multimodal drift recovery causes HTTP 500 (AssertionError: Expected a cached item)
