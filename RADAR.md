# LLM Serving Issue Radar

_Last run: 2026-10-31T13:21+00:00_

**13 issues** — sgl-project/sglang: 2, vllm-project/vllm: 11 — 🆕 **13 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 4

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#64790](https://github.com/vllm-project/vllm/issues/64790) [Bug]: In-tree LMCache integration can't be imported with lmcache >= 0.5.6

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#64874](https://github.com/vllm-project/vllm/issues/64874) [Bug]: [ROCm][GLM-5.3-Flash]: "Workspace is locked" AssertionError in rocm_fp8_paged_mqa_logits under high decode concurrency (glm5next AMD indexer reserves decode logits via torch.empty, not the workspace)

## Quantization

### sgl-project/sglang

- [RFC] 🆕 [#47624](https://github.com/sgl-project/sglang/issues/47624) [RFC] NPU RL Test Consolidation: File Ownership, Coverage Docstrings, and CI Integration (Ascend)

### vllm-project/vllm

- [Bug] 🆕 [#64814](https://github.com/vllm-project/vllm/issues/64814) [Bug]: MooncakeStoreConnector: one TP rank stalls (its GPU idle, peers spinning) on Kimi-K3 under agentic load

## Distributed / TP / PP / EP

### vllm-project/vllm

- [RFC] 🆕 [#64780](https://github.com/vllm-project/vllm/issues/64780) [RFC]: DBO support for FlashInfer NVLink all-to-all backends (single-node H200/B200 first)
- [RFC] 🆕 [#64776](https://github.com/vllm-project/vllm/issues/64776) [RFC]: Single Batch Overlap (down GEMM ↔ combine) for DeepEP LL

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#64845](https://github.com/vllm-project/vllm/issues/64845) [Bug]: EmbeddingGemma 2 rejects `dimensions` by default although the model supports Matryoshka (128/256/512/768)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#64789](https://github.com/vllm-project/vllm/issues/64789) [Bug]: Responses API rejects `input_text` content for Mistral Large 4 with --tokenizer-mode mistral
- [Bug] 🆕 [#64778](https://github.com/vllm-project/vllm/issues/64778) [Bug]: Non-streaming `/v1/chat/completions/derender` and `/v1/completions/derender` report `usage.prompt_tokens: 0` when the request omits `prompt_tokens`, ignoring `generate_response.usage`

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#47562](https://github.com/sgl-project/sglang/issues/47562) [AITER-Upgrade] PR readiness gfx1250 (MI45x)

### vllm-project/vllm

- [Bug] 🆕 [#64809](https://github.com/vllm-project/vllm/issues/64809) [Bug]: `raw_logprobs` are computed after the structured-output grammar mask
- [Performance] 🆕 [#64791](https://github.com/vllm-project/vllm/issues/64791) [Performance][ROCm]: set HSA_SCRATCH_SINGLE_LIMIT in the ROCm image: per-dispatch scratch allocation costs ~130 us before large RCCL all-reduces on MI355X
- [Feature] 🆕 [#64866](https://github.com/vllm-project/vllm/issues/64866) [Feature]: [CI] Restore Ascend interface compatibility checks with locked test dependencies
