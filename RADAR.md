# LLM Serving Issue Radar

_Last run: 2026-10-20T13:32+00:00_

**11 issues** — sgl-project/sglang: 4, vllm-project/vllm: 7 — 🆕 **11 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#45357](https://github.com/sgl-project/sglang/issues/45357) [Bug] PD prefill PP8 + HiCache cache mode hangs: PP0–PP3 blocked in the HiCache PP-sync drain
- [Perf] 🆕 [#45351](https://github.com/sgl-project/sglang/issues/45351) [Perf] HiCache PP-sync drain makes the PP prefill scheduler lock-step across ranks

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#62697](https://github.com/vllm-project/vllm/issues/62697) [Bug][ROCm] `ROCM_ATTN` returns wrong attention (and can fault the GPU) on RDNA for head size ≥ 96 with KV block size ≠ 16, and for MHA with head size 192/256

## Quantization

### sgl-project/sglang

- [other] 🆕 [#45373](https://github.com/sgl-project/sglang/issues/45373) [Tracking] GLM-5.3-Flash performance optimization on Hopper (SM90)

### vllm-project/vllm

- [Bug] 🆕 [#62609](https://github.com/vllm-project/vllm/issues/62609) [Bug]: A100 run Bolt (nv-community/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) throw :B12X NVFP4 kernels require a Blackwell 12x device

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Feature] 🆕 [#62694](https://github.com/vllm-project/vllm/issues/62694) [Feature]: [Spec Decode] Support model-based drafters (target hidden states) via custom_class
- [RFC] 🆕 [#62640](https://github.com/vllm-project/vllm/issues/62640) [RFC]: Improve MTP configuration warning

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#62598](https://github.com/vllm-project/vllm/issues/62598) [Bug][Rust Frontend] Long conversations fail with HTTP 500 (chat template fuel limit)

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#45370](https://github.com/sgl-project/sglang/issues/45370) [Roadmap] Beam Development & Optimization

### vllm-project/vllm

- [Bug] 🆕 [#62639](https://github.com/vllm-project/vllm/issues/62639) [Bug]: Responses API: tool_choice=allowed_tools does not work
- [Bug] 🆕 [#62606](https://github.com/vllm-project/vllm/issues/62606) [Bug][ROCm]: ROCM_AITER_UNIFIED_ATTN gives wrong output on gfx950 when a layer's KV cache is 2–4 GiB
