# LLM Serving Issue Radar

_Last run: 2026-10-14T13:28+00:00_

**17 issues** — sgl-project/sglang: 7, vllm-project/vllm: 10 — 🆕 **17 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 3

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#44186](https://github.com/sgl-project/sglang/issues/44186) ADR: releasing decode KV pages after a failed PD transfer

### vllm-project/vllm

- [Bug] 🆕 [#61526](https://github.com/vllm-project/vllm/issues/61526) [Bug]: NixlConnector silently corrupts Mamba2 conv state under heterogeneous TP when n_groups is not divisible by TP (e.g. granite-4.0-h, n_groups=1)
- [Performance] 🆕 [#61604](https://github.com/vllm-project/vllm/issues/61604) [Performance]: Waiting requests re-walk their whole prefix-cache hit on every scheduling step

## Attention Backend

### vllm-project/vllm

- [RFC] 🆕 [#61626](https://github.com/vllm-project/vllm/issues/61626) [RFC]: Porting Sequence Parallelism & Async TP to manual fusion

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#44291](https://github.com/sgl-project/sglang/issues/44291) [Bug] EP2 (tp=2 + ep=2) crashes with illegal memory access on Qwen3.8-Flash-Next-NVFP4 (RTX PRO 6000, sm_120)
- [Bug] 🆕 [#44178](https://github.com/sgl-project/sglang/issues/44178) [Bug] DeepSeek-V4.1-Flash on SM120: historical report of NCCL initialization failure with DSPARK

## Distributed / TP / PP / EP

### sgl-project/sglang

- [RFC] 🆕 [#44171](https://github.com/sgl-project/sglang/issues/44171) [RFC] Preserve multimodal identity end to end: precomputed inputs, collision-safe KV reuse, and KV-event parity

### vllm-project/vllm

- [Feature] 🆕 [#61631](https://github.com/vllm-project/vllm/issues/61631) [Feature]: Gated contributor PRs show as failed checks, and offloader paths have no CODEOWNERS

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#61608](https://github.com/vllm-project/vllm/issues/61608) [Bug]: enable_tower_connector_lora: get_mm_lora_token_counts() under-sizes punica wrappers in 8 models (startup/runtime token_lora_mapping asserts)
- [Feature] 🆕 [#61629](https://github.com/vllm-project/vllm/issues/61629) [Feature]: Support logprobs / top_logprobs for gpt-oss (Harmony) models in /v1/responses

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#44284](https://github.com/sgl-project/sglang/issues/44284) Breakable prefill CUDA graph backend trips torch CachingHostAllocator assert (`use_count > 0`) when graphs are re-captured after destruction

### vllm-project/vllm

- [Bug] 🆕 [#61632](https://github.com/vllm-project/vllm/issues/61632) [Bug]: Olmo3 tool parser (non-streaming) drops the tool call when a string argument contains "</function_calls>"
- [RFC] 🆕 [#61539](https://github.com/vllm-project/vllm/issues/61539) [RFC]: Explicit row layouts for routed-expert capture

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#61603](https://github.com/vllm-project/vllm/issues/61603) [Bug]: NemotronH/Mamba2: _chunk_scan_fwd_kernel nondeterministically emits NaN rows on sm90 (H20) for 8 of 23 autotune configs (warps=4, stages>=2, M/N>=64)

## Uncategorized

### sgl-project/sglang

- [Feature] 🆕 [#44172](https://github.com/sgl-project/sglang/issues/44172) [Feature] Could you include the sgl-model-gateway container image alongside each version release?
- [other] 🆕 [#44206](https://github.com/sgl-project/sglang/issues/44206) [Tracking][Mori] PRs for Community Review

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#61597](https://github.com/vllm-project/vllm/issues/61597) test
