# LLM Serving Issue Radar

_Last run: 2026-11-21T13:22+00:00_

**7 issues** — sgl-project/sglang: 3, vllm-project/vllm: 4 — 🆕 **7 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#52040](https://github.com/sgl-project/sglang/issues/52040) SGLang: multimodal chunking parameters have no upper bound, enabling CPU and memory exhaustion from a single request

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#52079](https://github.com/sgl-project/sglang/issues/52079) [Bug] FA4 hd256 on SM90 copies the whole paged KV cache on every call when the cache is a strided view (unified-memory pool)

### vllm-project/vllm

- [Bug] 🆕 [#69038](https://github.com/vllm-project/vllm/issues/69038) [Bug]: After a KV connector loads the whole prompt, the recomputed last token is still reported as cached (cached_tokens == prompt_tokens, local_compute +0)
- [RFC] 🆕 [#69082](https://github.com/vllm-project/vllm/issues/69082) [RFC]: Partial-block prefix caching as the default path for every KV cache group

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#69130](https://github.com/vllm-project/vllm/issues/69130) [Bug]: merge_attn_states reads the wrong token from a head-sliced suffix in Triton and native CUDA

## Sampling / Speculative Decoding

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#52041](https://github.com/sgl-project/sglang/issues/52041) SGLang: stop_regex passes validation but a 24-byte pattern causes MemoryError that escapes the safety net and kills the scheduler

### vllm-project/vllm

- [Bug] 🆕 [#69047](https://github.com/vllm-project/vllm/issues/69047) [Bug]: Illegal memory access with Qwen3.5-family MTP (method=mtp, k=3) when two engines share one H200 under CUDA MPS (v0.33.0)
