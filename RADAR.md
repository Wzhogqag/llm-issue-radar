# LLM Serving Issue Radar

_Last run: 2026-09-13T13:24+00:00_

**10 issues** — sgl-project/sglang: 4, vllm-project/vllm: 6 — 🆕 **8 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [RFC] [#39192](https://github.com/sgl-project/sglang/issues/39192) [RFC] Contention-aware batching for dynamic EPLB expert migration

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#39302](https://github.com/sgl-project/sglang/issues/39302) [Bug] GLM-5.x NoPE MLA (qk_rope_head_dim=0) cannot run on SM120: every DSA sparse-MLA backend is unavailable

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#56699](https://github.com/vllm-project/vllm/issues/56699) [Bug][HiSparse] Decode engine dies with cudaErrorLaunchFailure in the host-mirror path under sustained P/D host imports
- [RFC] 🆕 [#56701](https://github.com/vllm-project/vllm/issues/56701) [RFC][KV Offload]: Align sliding-window restore coverage with MTP-retained history

## Attention Backend

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#39299](https://github.com/sgl-project/sglang/issues/39299) MoE deferred finalize is unreachable for models that supply their own routing (FLASHINFER_TRTLLM_ROUTED excluded)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#39226](https://github.com/sgl-project/sglang/issues/39226) [Bug] --moe-runner-backend deep_gemm accepted for DSV4.1 MXFP4 experts, then fails in CUDA graph capture (layout.hpp:108, sm_121)

### vllm-project/vllm

- [Performance] 🆕 [#56684](https://github.com/vllm-project/vllm/issues/56684) [Performance]: 3.4 s engine stalls from DeepGEMM compiling the o-projection kernel per prefill chunk size, DeepSeek-V4.1-Flash on 8x B200
- [other] 🆕 [#56700](https://github.com/vllm-project/vllm/issues/56700) [SM120] Field report: running DeepSeek-V4.1-Flash end-to-end on 8x RTX PRO 6000 — pitfall map + working configuration (1M context verified)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [RFC] [#56581](https://github.com/vllm-project/vllm/issues/56581) [RFC]: Streaming prompt prefill for overlapping upstream generation and downstream prefill

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#56696](https://github.com/vllm-project/vllm/issues/56696) [Bug]: --otlp-traces-endpoint initializes tracer but never sends spans (instrument_otel/manual_instrument_otel never invoked)
