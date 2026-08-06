# LLM Serving Issue Radar

_Last run: 2026-08-06T14:00+00:00_

**32 issues** — sgl-project/sglang: 9, vllm-project/vllm: 23 — 🆕 **32 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 5
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 6
- [Uncategorized](#uncategorized) — 2

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#33789](https://github.com/sgl-project/sglang/issues/33789) [Bug] NIXL P/D stops serving after one role is replaced
- [Bug] 🆕 [#33740](https://github.com/sgl-project/sglang/issues/33740) [Bug] With PD Disaggregation, the router reports being healthy when the first prefill worker is still initializing

### vllm-project/vllm

- [Bug] 🆕 [#51163](https://github.com/vllm-project/vllm/issues/51163) [Bug]: cache_config_info reports block_size=4 despite --block-size 256, and num_gpu_blocks × block_size ≠ kv_cache_size_tokens (DeepSeek-V4, fp8_ds_mla)
- [Feature] 🆕 [#51234](https://github.com/vllm-project/vllm/issues/51234) [Feature]: per request kv cache write logic

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#33817](https://github.com/sgl-project/sglang/issues/33817) [Bug][Qwen3.5] Converted checkpoint cannot generate valid text, and FP8 output length increased significantly

### vllm-project/vllm

- [Bug] 🆕 [#51205](https://github.com/vllm-project/vllm/issues/51205) [Bug]:  Inkling-Small-NVFP4 wont start on 2 H200 GPUs.
- [Bug] 🆕 [#51188](https://github.com/vllm-project/vllm/issues/51188) [Bug]: compressed-tensors models with format: dense sparsity_config fail to load
- [Performance] 🆕 [#51197](https://github.com/vllm-project/vllm/issues/51197) [Performance]: Qwen3.6-35B-A3B (Qwen3_5MoeForConditionalGeneration) BF16 GDN backbone isn't quantized — ~80% of per-step reads, caps decode
- [RFC] 🆕 [#51214](https://github.com/vllm-project/vllm/issues/51214) [RFC]: ARK H2 Upstream Roadmap for vLLM INC Path XPU Inference

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#33867](https://github.com/sgl-project/sglang/issues/33867) [Bug] /v1/responses API fails with 400 when function_call_output output is an array

### vllm-project/vllm

- [Bug] 🆕 [#51200](https://github.com/vllm-project/vllm/issues/51200) [Bug]: `MiniMAXGemmaRMSNorm` unconditionally calls FlashInfer CUDA kernels, breaking MiniMax-M3 on every non-CUDA platform
- [RFC] 🆕 ⚠maintainer-authored [#51240](https://github.com/vllm-project/vllm/issues/51240) [RFC][kv_offload]: Tiering Admission Policy Design

## New Model Integration

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#33771](https://github.com/sgl-project/sglang/issues/33771) Question: content-based LoRA adapter selection (routing from the query, not the request)

### vllm-project/vllm

- [Bug] 🆕 [#51250](https://github.com/vllm-project/vllm/issues/51250) [Bug]: Prefix caching is ineffective on Mamba-2/GDN hybrid (Qwen3_5MoeForConditionalGeneration)
- [Bug] 🆕 [#51198](https://github.com/vllm-project/vllm/issues/51198) [Bug]: --enable-prefix-caching is a silent 0%-hit no-op on Mamba-2/GDN hybrids (Qwen3_5MoeForConditionalGeneration)
- [no-prefix] 🆕 ⚠no-prefix [#51211](https://github.com/vllm-project/vllm/issues/51211) Question: content-based LoRA adapter selection (routing from the query, not the request naming the adapter)
- [RFC] 🆕 ⚠maintainer-authored [#51220](https://github.com/vllm-project/vllm/issues/51220) [RFC][Rust Frontend] Complete RL control-plane endpoint parity

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#33782](https://github.com/sgl-project/sglang/issues/33782) [Bug][Ascend NPU] MTP (NEXTN) crashes on glm-ocr

### vllm-project/vllm

- [Bug] 🆕 [#51187](https://github.com/vllm-project/vllm/issues/51187) [Bug]: VLLM_BATCH_INVARIANT=1 returns non-identical logprobs across repeats of a byte-identical concurrent workload at ~44 co-resident sequences
- [RFC] 🆕 [#51212](https://github.com/vllm-project/vllm/issues/51212) [RFC]: Model Runner V2 Pluggable Design

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#33858](https://github.com/sgl-project/sglang/issues/33858) [Bug] Requests hang indefinitely on queue overflow with --tokenizer-worker-num 2
- [no-prefix] 🆕 ⚠no-prefix [#33828](https://github.com/sgl-project/sglang/issues/33828) MiniMax-H3 + DBCache: default residual_diff_threshold is inert, and T2VA cannot reach the documented quality bar

### vllm-project/vllm

- [Bug] 🆕 [#51266](https://github.com/vllm-project/vllm/issues/51266) [Bug][Anthropic] /v1/messages canonicalizes model aliases, causing Claude Code to strip thinking blocks during tool-use loops
- [Bug] 🆕 [#51164](https://github.com/vllm-project/vllm/issues/51164) [Bug]: Step3p5ReasoningParser strips the wrong newline once the discarded prefix is preserved (follow-up to #50918)

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#33846](https://github.com/sgl-project/sglang/issues/33846) [AMD/ROCm] Kimi-K3 KDA prefill occasional hang at c=1: chunk_kda_fwd → tolist() → hipMemcpy D2H never returns

### vllm-project/vllm

- [Bug] 🆕 [#51181](https://github.com/vllm-project/vllm/issues/51181) [Bug]: DeepSeekV4 DSpark CUDA graph capture failure on H100
- [other] 🆕 [#51232](https://github.com/vllm-project/vllm/issues/51232) [Rocm] Fix AITER_MLA issues for the kimik3-dspark model with Agentic workload
- [other] 🆕 [#51193](https://github.com/vllm-project/vllm/issues/51193) [Parity with CUDA vLLM]: ROCm Mooncake out of the box in prebuilt Docker
- [other] 🆕 [#51192](https://github.com/vllm-project/vllm/issues/51192) [Dependency]: Bump torchvision to a release containing the CVE-2026-65918 fix
- [RFC] 🆕 [#51186](https://github.com/vllm-project/vllm/issues/51186) [RFC]: Adopt otel genai semantic conventions for metrics

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#51264](https://github.com/vllm-project/vllm/issues/51264) [Feature]: Publish a standalone Rust frontend docker image
- [Feature] 🆕 [#51162](https://github.com/vllm-project/vllm/issues/51162) [Feature]: `vllm.utils.import_util._has_module` should not import modules
