# LLM Serving Issue Radar

_Last run: 2026-11-19T13:22+00:00_

**12 issues** — sgl-project/sglang: 2, vllm-project/vllm: 10 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#68610](https://github.com/vllm-project/vllm/issues/68610) [Bug]: With TP>1, `vllm:num_requests_waiting` briefly includes requests the scheduler hasn't seen yet (since #65466)
- [RFC] 🆕 [#68678](https://github.com/vllm-project/vllm/issues/68678) [RFC]: [KV Offload] Batched, serializable connector-manager interface

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#68668](https://github.com/vllm-project/vllm/issues/68668) [Bug]: [HiSparse] GLM-5.3-Flash with fp8_ds_mla KV fails at the first prefill on Hopper (AssertionError in HiSparseMLAIndexGroup._prefill_gather_plan)
- [no-prefix] 🆕 ⚠no-prefix [#68695](https://github.com/vllm-project/vllm/issues/68695) DFlash/LiLiCorr speculator CUDA-graph capture segfault on GB10 (sm_121)

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#68647](https://github.com/vllm-project/vllm/issues/68647) [Bug]: DSV4.1 Model weight memory increased from ~47 GiB to ~60 GiB per GPU between two nightlies (11.12 nightly and 11.18 nightly) H100

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#68595](https://github.com/vllm-project/vllm/issues/68595) [Bug]: `/resume` while the engine is asleep (sleep level 1) kills EngineCore: "ValueError: Pointer argument cannot be accessed from Triton (cpu tensor?)"

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#51531](https://github.com/sgl-project/sglang/issues/51531) [Bug] `--mamba-ssm-dtype bfloat16` costs ~8 points on long-reasoning MATH-500 with Qwen3.5-9B (float16 does not); GSM8K-style checks miss it

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#68619](https://github.com/vllm-project/vllm/issues/68619) [Bug]: null values in a --config YAML file are passed as the string "None"

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#51480](https://github.com/sgl-project/sglang/issues/51480) [Bug] sgl-deep-gemm PyPI wheels are built with CUDA 13.0, which compiles out DeepGEMM's CUDA >= 13.4 paths (in-CTA-norm Mega mHC on Rubin)

### vllm-project/vllm

- [Bug] 🆕 [#68692](https://github.com/vllm-project/vllm/issues/68692) [Bug]: Structured output does not see reasoning end at a tool-call opener for deepseek_v4 / deepseek_v41 (multi-token) and inkling
- [Bug] 🆕 [#68669](https://github.com/vllm-project/vllm/issues/68669) [Bug]: [HiSparse][P/D] HiSparse on the decode instance fails for hybrid models (GLM-5.3-Flash): Mixed-device KV registration is only supported for MLA models without Mamba layers
- [Bug] 🆕 [#68625](https://github.com/vllm-project/vllm/issues/68625) [Bug]: CPU offloading fails at startup with AttributeError: module 'os' has no attribute 'memfd_create' (uv-managed Python)
