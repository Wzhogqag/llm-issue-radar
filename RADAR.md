# LLM Serving Issue Radar

_Last run: 2026-09-17T13:28+00:00_

**10 issues** — sgl-project/sglang: 4, vllm-project/vllm: 6 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#39963](https://github.com/sgl-project/sglang/issues/39963) # [RFC] Asymmetric P/D deployment for DeepSeek-V4.1 Flash

### vllm-project/vllm

- [RFC] 🆕 [#57383](https://github.com/vllm-project/vllm/issues/57383) [RFC]: Asymmetric P/D Deployment for DeepSeek-V4.1 Flash

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#57324](https://github.com/vllm-project/vllm/issues/57324) [Bug]: Claude Code tool search: first request of every session rejected with 400 (tool_addition content blocks not accepted by /v1/messages)
- [Feature] 🆕 [#57345](https://github.com/vllm-project/vllm/issues/57345) [Feature]: [CPU][GLM5Next] Add native sparse MLA / KeyPool indexer support for GLM-5.3-Flash

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#39850](https://github.com/sgl-project/sglang/issues/39850) [Bug] GLM-5.3-Flash (glm5_next): image requests render a no-multimodal reminder instead of the image placeholder — model never sees the image
- [other] 🆕 [#39971](https://github.com/sgl-project/sglang/issues/39971) [KDA] Fused intra-chunk prefill path (`chunk_kda_fwd_intra(fuse_diagonal=True)`) collapses for strong per-channel decays because of the ±126 clamp in the exp2 factorization

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Performance] 🆕 [#57350](https://github.com/vllm-project/vllm/issues/57350) [Performance]: Streaming derender bypasses renderer thread pool and blocks the event loop

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#39922](https://github.com/sgl-project/sglang/issues/39922) [Bug] /v1/messages never reports cache_creation_input_tokens, so cache writes are billed as plain input

### vllm-project/vllm

- [Bug] 🆕 [#57276](https://github.com/vllm-project/vllm/issues/57276) [Bug]: MRV2不支持anthropic?
- [Feature] 🆕 [#57346](https://github.com/vllm-project/vllm/issues/57346) [Feature]: [CPU][GLM5Next][KDA] Add CPU KDA backend for GLM-5.3-Flash
