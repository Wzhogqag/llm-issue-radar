# LLM Serving Issue Radar

_Last run: 2026-08-22T13:29+00:00_

**12 issues** — sgl-project/sglang: 2, vllm-project/vllm: 10 — 🆕 **11 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Feature] 🆕 [#53277](https://github.com/vllm-project/vllm/issues/53277) [Feature]: Cache-aware waiting QoS with optional cooperative prefill preemption

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#53368](https://github.com/vllm-project/vllm/issues/53368) [Feature]: Expose CPU vs P2P attribution for multi-tier KV restores
- [RFC] 🆕 [#53371](https://github.com/vllm-project/vllm/issues/53371) [RFC]: Optimization: Take over a partial-hit block instead of CoW copy when ref_cnt == 1
- [no-prefix] 🆕 ⚠no-prefix [#53334](https://github.com/vllm-project/vllm/issues/53334) TurboQuant KV cache: two observations from an sm121 evaluation: hybrid-model init failure; fp16 zero-point overflow on large value outliers

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#35949](https://github.com/sgl-project/sglang/issues/35949) [Bug] Qwen 3.8 27b NVFP4 incorrect coordinate detection on image
- [other] [#35860](https://github.com/sgl-project/sglang/issues/35860) [Playground] Verified cell: Qwen3.8-27B / dgx-spark / nvfp4 / DFLASH2 / single

### vllm-project/vllm

- [Bug] 🆕 [#53320](https://github.com/vllm-project/vllm/issues/53320) [Bug]: DeepSeek-V4-Flash crashes at startup on 8x H20 (SM90) with v0.27.1 — Engine core initialization failed

## New Model Integration

### vllm-project/vllm

- [other] 🆕 [#53286](https://github.com/vllm-project/vllm/issues/53286) [New Model]: TR-HASH deterministic token-routed MoE

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#53363](https://github.com/vllm-project/vllm/issues/53363) [Bug]: tool_choice="required" not enforced with gemma4 tool parser — prose-only response returned with finish_reason="tool_calls" and empty tool_calls
- [Bug] 🆕 [#53323](https://github.com/vllm-project/vllm/issues/53323) [Bug]: [ROCm][Spec Decode]  DFlash2 acceptance length collapses with default ROCM_ATTN draft backend
- [Bug] 🆕 [#53305](https://github.com/vllm-project/vllm/issues/53305) [Bug]: Qwen3.5 generates infinite exclamation marks (!!!!...) in specific rounds of long sessions

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#53349](https://github.com/vllm-project/vllm/issues/53349) [Feature]: Opt-in omission of unset vLLM-specific extension fields from /v1/chat/completions responses
