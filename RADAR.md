# LLM Serving Issue Radar

_Last run: 2026-08-25T13:36+00:00_

**23 issues** — sgl-project/sglang: 6, vllm-project/vllm: 17 — 🆕 **23 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 5
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#36326](https://github.com/sgl-project/sglang/issues/36326) [Bug] --config rejects canonical mamba-radix-cache-strategy due to DeprecatedAliasStoreAction
- [RFC] 🆕 ⚠maintainer-authored [#36224](https://github.com/sgl-project/sglang/issues/36224) [RFC] First-Class, Versioned KV Hint Envelope for SGLang

### vllm-project/vllm

- [Bug] 🆕 [#53658](https://github.com/vllm-project/vllm/issues/53658) [Bug]: FULL cudagraph dummy runs set seq_lens > max_model_len, overrunning the block table (TRITON_ATTN illegal memory access; FLEX_ATTENTION shape error)
- [Bug] 🆕 [#53655](https://github.com/vllm-project/vllm/issues/53655) [Bug]: model_hosting_container_standards changes a shared root/vllm handler to ERROR and suppresses vLLM startup logs
- [RFC] 🆕 [#53703](https://github.com/vllm-project/vllm/issues/53703) [RFC]: Progressive block handoff for NIXL Push

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#53706](https://github.com/vllm-project/vllm/issues/53706) [Bug]: Mamba N-1 truncation after a full local prefix-cache hit makes num_new_tokens zero and crashes the prefill EngineCore

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#53691](https://github.com/vllm-project/vllm/issues/53691) [Performance]: DSA indexer is computed redundantly on every TP rank (NVIDIA / CUDA)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36302](https://github.com/sgl-project/sglang/issues/36302) [Bug] sglang-kernel JIT: HiCache L3 segfault on first backup with nvcc 12.8 + CUDA 13 runtime (compile-time vs runtime cudaMemcpyBatchAsync ABI in staged_write_back.cuh)
- [no-prefix] 🆕 ⚠no-prefix [#36291](https://github.com/sgl-project/sglang/issues/36291) --enable-deterministic-inference accepted and reported enabled, but has no effect on an NVFP4 W4A4 + hybrid-Mamba checkpoint with a DFlash2 drafter (GB10 / sm_121)

### vllm-project/vllm

- [Performance] 🆕 [#53687](https://github.com/vllm-project/vllm/issues/53687) [Performance]: Add native layer-fused MoE parameter loading for weight reload
- [Bug] 🆕 [#53635](https://github.com/vllm-project/vllm/issues/53635) [Bug][DSV4][Blackwell SM12x] Indexer decode paged MQA logits broken when DeepGEMM is available: 2-state compress pages vs kernels templated for block_kv 32/64
- [RFC] 🆕 [#53714](https://github.com/vllm-project/vllm/issues/53714) [RFC]: PCP-Sharded O-Projection Weights
- [RFC] 🆕 [#53629](https://github.com/vllm-project/vllm/issues/53629) [RFC]: Apply MoE weight transformations at disk streaming time instead of materializing raw tensor

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#53718](https://github.com/vllm-project/vllm/issues/53718) [Bug]: Named shared memory may be closed before peer ranks open it
- [RFC] 🆕 [#53684](https://github.com/vllm-project/vllm/issues/53684) [RFC]: Allow the DSA Indexer to Use Context Parallelism Independently

## New Model Integration

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#53626](https://github.com/vllm-project/vllm/issues/53626) Unsupported tool_choice in Responses API (Harmony/gpt-oss) returns HTTP 501, should be 4xx

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#36276](https://github.com/sgl-project/sglang/issues/36276) [Bug] qwen3.6-35b-a3b repeat bug

### vllm-project/vllm

- [Bug] 🆕 [#53620](https://github.com/vllm-project/vllm/issues/53620) [Bug]: test_spec_decode_logprobs never runs on NVIDIA CI, and is ill-defined at top-k ties when it does
- [no-prefix] 🆕 ⚠no-prefix [#53726](https://github.com/vllm-project/vllm/issues/53726) Silent CUDA IMA (exit 0) in hybrid GDN + MTP k=3 + async scheduling on RTX 3090; persists through #50021/#45100/#53613-class fixes
- [RFC] 🆕 ⚠maintainer-authored [#53673](https://github.com/vllm-project/vllm/issues/53673) [RFC]: Decouple draft-model parallelism from the target model (PCP/DCP + speculative decoding)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Performance] 🆕 [#36226](https://github.com/sgl-project/sglang/issues/36226) [Performance] Multiple potential avoidable scheduler, sampling, and streaming overheads identified

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#53717](https://github.com/vllm-project/vllm/issues/53717) [Bug]: MedGemma 27B model:  Repetitive newline-token generation loop
- [Bug] 🆕 [#53665](https://github.com/vllm-project/vllm/issues/53665) [Bug]: min_tokens + structured output can empty the token mask and return HTTP 500
