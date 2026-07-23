# LLM Serving Issue Radar

_Last run: 2026-07-23T14:00+00:00_

**22 issues** — sgl-project/sglang: 4, vllm-project/vllm: 18 — 🆕 **22 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 4
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#49584](https://github.com/vllm-project/vllm/issues/49584) [Bug]:  vllm0.25版本支持qwen3-vl fp8算子DeepGemmFp8BlockScaledMMKernel 走原始的deepgemm的后端
- [Bug] 🆕 [#49528](https://github.com/vllm-project/vllm/issues/49528) [Bug]: NIXL poll leaves transfers inflight when check_xfer_state raises
- [RFC] 🆕 [#49545](https://github.com/vllm-project/vllm/issues/49545) [RFC]: Speculative recompute fallback for slow remote KV cache loads

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32156](https://github.com/sgl-project/sglang/issues/32156) [Bug] Cannot load unsloth/Qwen3.6-35B-A3B-NVFP4

### vllm-project/vllm

- [Bug] 🆕 [#49594](https://github.com/vllm-project/vllm/issues/49594) [Bug]: deadlock / hang with GLM-5.2-FP8 EP+DP on GB200 - with ablation table
- [Bug] 🆕 [#49546](https://github.com/vllm-project/vllm/issues/49546) [Bug]: VLLM_MARLIN_INPUT_DTYPE=fp8 (Marlin W4A8-FP8) silently corrupts output on GB10/sm_121a — WNA16 INT4 MoE emits repeated </think> loop at temp 0 (kernel runs ~2.5% faster)
- [Perf] 🆕 ⚠maintainer-authored [#49529](https://github.com/vllm-project/vllm/issues/49529) [Perf][Kernel] Adopt PTX 9.4 `ldmatrix.s8.s4` (hardware INT4→INT8 expanding load) in W4A8-INT8 paths

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#49554](https://github.com/vllm-project/vllm/issues/49554) [Bug]: --moe-backend humming crashes at startup on NVIDIA GB10 / DGX Spark (humming NVML mem-clock query unsupported)
- [Feature] 🆕 [#49530](https://github.com/vllm-project/vllm/issues/49530) [Feature]: Make PG_WAIT_TIMEOUT configurable via environment variable
- [Feature] 🆕 [#49527](https://github.com/vllm-project/vllm/issues/49527) [Feature]: Make Ray placement group strategy configurable via VLLM_RAY_PG_STRATEGY

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#32124](https://github.com/sgl-project/sglang/issues/32124) [Feature] Skip redundant DeepGEMM all-M warmup when a compatible JIT cache is restored

### vllm-project/vllm

- [Bug] 🆕 [#49493](https://github.com/vllm-project/vllm/issues/49493) [Bug]: Harmony models reject namespace tool type in Responses API
- [Feature] 🆕 [#49537](https://github.com/vllm-project/vllm/issues/49537) [Feature]: kv-event support hyper-attention network
- [Feature] 🆕 [#49533](https://github.com/vllm-project/vllm/issues/49533) [Feature]: Support for Responses API `/v1/responses/input_tokens`

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#32176](https://github.com/sgl-project/sglang/issues/32176) [Bug] HiCache loadback 后 GLM-5.2 EAGLE acceptance 静默坍塌

### vllm-project/vllm

- [Bug] 🆕 [#49589](https://github.com/vllm-project/vllm/issues/49589) [Bug]: if passed temperature=0.0 there is no output of its value in telemetry span
- [Performance] 🆕 [#49548](https://github.com/vllm-project/vllm/issues/49548) [Performance]: Dynamic speculative decoding (num_speculative_tokens_per_batch_size) causes catastrophic aggregate-throughput collapse under concurrency at the batch-size threshold (MTP, V1/PIECEWISE)
- [Bug] 🆕 [#49497](https://github.com/vllm-project/vllm/issues/49497) [Bug]: FlashInfer sampler JIT crashes engine startup when nvcc isn't discoverable (default precompiled/wheel install) — no fallback to native sampler
- [Feature] 🆕 [#49562](https://github.com/vllm-project/vllm/issues/49562) [Feature] Support `extract_hidden_states` on Model Runner V2

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#32169](https://github.com/sgl-project/sglang/issues/32169) [Bug] InternVL2_5-2B fails to start: 'CLIPImageProcessor' object has no attribute 'tokenizer' in get_tokenizer_from_processor

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49559](https://github.com/vllm-project/vllm/issues/49559) [Bug]: QWEN 3.6-35Ba3B+DFlash (Train by Speculator) when vllm0.25.1 use V2, the acceptance rate is 0%.

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#49538](https://github.com/vllm-project/vllm/issues/49538) [Feature]: /metric has seconds delay
