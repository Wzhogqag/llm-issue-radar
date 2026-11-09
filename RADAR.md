# LLM Serving Issue Radar

_Last run: 2026-11-09T13:22+00:00_

**10 issues** — sgl-project/sglang: 4, vllm-project/vllm: 6 — 🆕 **10 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#66556](https://github.com/vllm-project/vllm/issues/66556) [RFC]: Define an Optional In-Tree Integration Path for Hardware Backends
- [RFC] 🆕 ⚠maintainer-authored [#66570](https://github.com/vllm-project/vllm/issues/66570) [RFC]: Async CPU tier setup for OffloadingConnector

## Quantization

### sgl-project/sglang

- [Feature] 🆕 [#49296](https://github.com/sgl-project/sglang/issues/49296) [Feature] flashinfer: Split the extend into ragged and paged passes under full prefill CUDA graphs with an FP8 KV cache

### vllm-project/vllm

- [Bug] 🆕 [#66573](https://github.com/vllm-project/vllm/issues/66573) [Bug]: Qwen3.5 `qwen3_5.py` embedding drops `quant_config` — GGUF embeddings fall back to dense
- [RFC] 🆕 [#66491](https://github.com/vllm-project/vllm/issues/66491) [RFC]: Packed-weight INT4 GEMM (W4A16 / W4A8) for RDNA4 (gfx1200/gfx1201)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#49295](https://github.com/sgl-project/sglang/issues/49295) [Bug] Breakable prefill CUDA graphs return wrong, non-repeatable prompt logprobs for short prompts on Qwen3.8-2.4T-A95B-NVFP4 (B300)
- [no-prefix] 🆕 ⚠no-prefix [#49274](https://github.com/sgl-project/sglang/issues/49274) Silent deterministic output corruption: first token id 0 ("!") then [PAD] (id 163839) loop, spec accept-length pinned at 1.00, zero errors — Kimi-K3.1-Pro (hybrid mamba + DFlash2 draft) on AMD MI300X/AITER, fp8 KV, v0.5.23.dev20261104 (e67b2062e2)

## Performance / Memory / OOM

### sgl-project/sglang

- [Feature] 🆕 [#49257](https://github.com/sgl-project/sglang/issues/49257) [Feature][RFC] STANDALONE PD: homogeneous TP=2 handoff and rank-consistent seed rejection

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#66515](https://github.com/vllm-project/vllm/issues/66515) enable_gqa=True can be 2.59x slower than materializing the KV cache - silent MATH-backend fallback at decode

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#66525](https://github.com/vllm-project/vllm/issues/66525) [Bug]: Gemma4 suppression-token cache causes UnexpectedTracerError on TPU
