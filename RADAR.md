# LLM Serving Issue Radar

_Last run: 2026-09-19T13:25+00:00_

**13 issues** — sgl-project/sglang: 2, vllm-project/vllm: 11 — 🆕 **13 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Attention Backend](#attention-backend) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#57691](https://github.com/vllm-project/vllm/issues/57691) [Bug]: Task cancellation during _commit_scale_down_elastic_ep corrupts cluster state without rollback
- [Bug] 🆕 [#57596](https://github.com/vllm-project/vllm/issues/57596) [Bug]: With a KV connector, prompt_logprobs requests are counted as full external prefix cache misses

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#40286](https://github.com/sgl-project/sglang/issues/40286) [Bug] GLM-5.3-Flash has no usable DSA attention backend on SM121 (DGX Spark): trtllm SM100-only, tilelang exceeds dynamic smem, triton ROCm-only, flashinfer_sparse_mla gated to GlmMoeDsa archs

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#40320](https://github.com/sgl-project/sglang/issues/40320) [Bug] FlashInfer autotune cache is discarded every boot under MoE expert parallelism (EP>1): per-rank shapes never agree, so the fused-MoE tactic is re-drawn each start

### vllm-project/vllm

- [RFC] 🆕 [#57649](https://github.com/vllm-project/vllm/issues/57649) [RFC]: Declarative cross-platform capability negotiation and effective configuration reporting

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#57671](https://github.com/vllm-project/vllm/issues/57671) [Bug]: collect-env is not supported in MAC
- [no-prefix] 🆕 ⚠no-prefix [#57631](https://github.com/vllm-project/vllm/issues/57631) GLM-OCR MTP broken by two defects: loader drops model.language_model.layers.* MTP weights before prefix rewrite; MTP forward not CUDA-graph safe

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Feature] 🆕 [#57608](https://github.com/vllm-project/vllm/issues/57608) [Feature][Spec Decode]: host-context hook between draft proposal and verify for out-of-graph per-layer caches

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#57593](https://github.com/vllm-project/vllm/issues/57593) [Feature]: Share non-streaming chat message assembly between `OpenAIServingChat` and batch derender

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#57680](https://github.com/vllm-project/vllm/issues/57680) [Bug]: Decode throughput drops ~3.3x from 0.26.0 to 0.29.0 on H100 (Qwen3.6-35B-A3B-FP8, same config, same backends)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#57614](https://github.com/vllm-project/vllm/issues/57614) [Bug]: [ROCm][gfx1151] Navi paged attention silently accepts unsupported ALiBi and block size 32
- [Feature] 🆕 [#57588](https://github.com/vllm-project/vllm/issues/57588) [Feature][ROCm][Perf]: Add AITER gluon sparse MLA for rope-free BF16 (GLM-5.3-Flash, gfx950)
- [other] 🆕 [#57684](https://github.com/vllm-project/vllm/issues/57684) [Question] Support path for platform plugins that cannot install Triton (MRV2 requires it)
