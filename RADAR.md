# LLM Serving Issue Radar

_Last run: 2026-07-31T14:00+00:00_

**11 issues** — sgl-project/sglang: 7, vllm-project/vllm: 4 — 🆕 **11 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#33035](https://github.com/sgl-project/sglang/issues/33035) [Feature] Add bounded pre-scheduler admission control for multimodal requests to prevent CPU OOM

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#32983](https://github.com/sgl-project/sglang/issues/32983) [Bug] SGLang router using cache_aware policy picks same replica repeatedly on cache miss at low concurrency. triggers poor KV cache memory utilization

### vllm-project/vllm

- [Feature] 🆕 [#50509](https://github.com/vllm-project/vllm/issues/50509) [Feature]: Allow an explicit expert override of the startup KV capacity check

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#33015](https://github.com/sgl-project/sglang/issues/33015) [Bug]  Dockerised SGLang for ROCM with gfx1150 cannot load a quantised model: use of undeclared identifier '__cvta_generic_to_shared'
- [Bug] 🆕 [#32965](https://github.com/sgl-project/sglang/issues/32965) [Bug][AMD gfx1201] Native MoE kernels segfault during Qwen3.5 inference
- [Feature] 🆕 ⚠maintainer-authored [#32993](https://github.com/sgl-project/sglang/issues/32993) [Feature] Route per-tensor FP8 checkpoints to FlashInfer on SM89/SM90

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#50557](https://github.com/vllm-project/vllm/issues/50557) [Bug]: MiniMax-M3-NVFP4 illegal memory access

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#32968](https://github.com/sgl-project/sglang/issues/32968) [Bug][kimi-k3] Long-context [PAD] (id 163839) storms + DSPARK inf/nan asserts — NaN-contaminated logits; released kimi-k3 image predates #32477; pad not stopped/filtered; allowed_special="all" makes [PAD] injectable

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#50545](https://github.com/vllm-project/vllm/issues/50545) [Bug]: [XPU] Multi-GPU TP serving hangs on Intel Arc Pro B60 with torch 2.13 wheels (oneCCL 2022.x): warmup allreduce never returns, GuC timeouts, DEVICE_LOST`
- [Bug] 🆕 [#50477](https://github.com/vllm-project/vllm/issues/50477) [Bug]: gemma4 parser silently ignores named forced tool_choice on 0.26.0 (worked on 0.21.0)

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#32970](https://github.com/sgl-project/sglang/issues/32970) Kimi-K3 bug tracking
