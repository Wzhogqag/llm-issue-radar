# LLM Serving Issue Radar

_Last run: 2026-09-29T13:35+00:00_

**29 issues** — sgl-project/sglang: 6, vllm-project/vllm: 23 — 🆕 **29 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 7
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#41653](https://github.com/sgl-project/sglang/issues/41653) [Bug][Simulator] SGLang Simulator cannot load hybrid GDN (qwen3_5) models: the CPU engine requires sgl_kernel CPU ops the CUDA wheel does not ship
- [RFC] 🆕 [#41576](https://github.com/sgl-project/sglang/issues/41576) [RFC] Dynamic Latent Consensus Governor for DeepSeek-R1 to Reduce KV-Cache Holding Time by 4.5x.

### vllm-project/vllm

- [Feature] 🆕 [#59210](https://github.com/vllm-project/vllm/issues/59210) [Feature]: Helm chart: add an optional ServiceMonitor with a configurable regex filter to reduce the number of exported metrics

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#41654](https://github.com/sgl-project/sglang/issues/41654) [Bug][Simulator] --max-total-tokens on a hybrid mamba/GDN model crashes with TypeError: NoneType // int — the mamba sizing step is skipped on that branch
- [Bug] 🆕 [#41617](https://github.com/sgl-project/sglang/issues/41617) [Bug] --strip-thinking-cache + retraction: release_kv_cache frees KV slots the radix tree still owns (double free)

### vllm-project/vllm

- [Bug] 🆕 [#59122](https://github.com/vllm-project/vllm/issues/59122) [Bug] ExampleHiddenStatesConnector does not support Hybrid KV Cache Manager
- [Bug] 🆕 [#59116](https://github.com/vllm-project/vllm/issues/59116) [Bug]: SMG MoRI-IO PD disagg
- [Bug] 🆕 [#59110](https://github.com/vllm-project/vllm/issues/59110) [Bug]: NixlConnector heterogeneous TP silently misreads KV pages with split K/V slots (ROCm AITER shuffle, ROCM_ATTN, B12X)
- [RFC] 🆕 [#59141](https://github.com/vllm-project/vllm/issues/59141) [RFC][KV Connector] NIXL support for shared in-flight prefix loads
- [RFC] 🆕 [#59111](https://github.com/vllm-project/vllm/issues/59111) [RFC]: NixlConnector: convert standard KV pages to ROCm AITER shuffled pages on the decode side

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#59203](https://github.com/vllm-project/vllm/issues/59203) [Bug]: DeepSeek-V4.1-Flash cannot run on SM120 (RTX PRO 6000): compressed-layer page_block_size=32 has no FlashInfer sparse-MLA decode kernel instantiation (only pbs=64)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#41609](https://github.com/sgl-project/sglang/issues/41609) [Bug] GLM-5.3-Flash-NVFP4 teacher-forced logprobs drift vs v0.5.20 on SM100 after 2026-09-18..09-21 (suspect #39688 KDA fusion gate)
- [Bug] 🆕 [#41606](https://github.com/sgl-project/sglang/issues/41606) [Bug] SM120: block-FP8 linears ignore scale_fmt "ue8m0" for activations (cutlass path uses FP32 amax/448 scales)

### vllm-project/vllm

- [other] 🆕 [#59151](https://github.com/vllm-project/vllm/issues/59151) [ROCm] mxfp4 MoE: TRITON_UNFUSED is never auto-selected, leaving pre-CDNA3 (gfx90a) with no working backend
- [other] 🆕 [#59219](https://github.com/vllm-project/vllm/issues/59219) [ROCm][Perf][Tracking Issue]: RedHatAI/gemma-4-31B-it-FP8-block

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#59189](https://github.com/vllm-project/vllm/issues/59189) [Bug]: GB200 DP4+EP serving crashes in NCCL symmetric reduce-scatter after #48247
- [Bug] 🆕 [#59181](https://github.com/vllm-project/vllm/issues/59181) [Bug] VLLM_BATCH_INVARIANT=1 is not batch-invariant for a pooling (cross-encoder) model on sm_120 — GEMMs fall to the cuBLAS-workspace branch
- [other] 🆕 [#59152](https://github.com/vllm-project/vllm/issues/59152) [ROCm][Bug] mimo_audio.py imports CUDA-only vllm.vllm_flash_attn, killing the engine core on audio input

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#59184](https://github.com/vllm-project/vllm/issues/59184) [Bug]: DFlash DCP slot mapping uses kernel block size for DCP ownership
- [Bug] 🆕 [#59161](https://github.com/vllm-project/vllm/issues/59161) [Bug]: Model Runner V2 maps lm_head LoRA per request instead of per logits row under speculative decoding (adapter has no effect / leaks to neighbouring requests)
- [Bug] 🆕 [#59115](https://github.com/vllm-project/vllm/issues/59115) [Bug]: GLM-5.3-Flash illegal memory access on long-context chucked prefill still reproduces on v 0.30.0 (B200, TP4+EP, MTP)
- [RFC] 🆕 [#59117](https://github.com/vllm-project/vllm/issues/59117) [RFC]: [Spec decode] KV-cache pool collapse when a draft model introduces a new cache spec type (hybrid GDN + DFlash): diagnosis, mitigation dead-ends, and a working dedicated-draft-pool POC

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#59222](https://github.com/vllm-project/vllm/issues/59222) [Bug]: Mistral pre-v11 tool parser fails the whole request on valid but unexpected tool call JSON
- [Bug] 🆕 [#59218](https://github.com/vllm-project/vllm/issues/59218) [Bug]: Engine-based parsers drop text after/between tool calls in non-streaming (streaming keeps it)
- [Feature] 🆕 [#59120](https://github.com/vllm-project/vllm/issues/59120) [Feature]: Add lifecycle management hooks for the worker extension class (--worker-extension-cls)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#59176](https://github.com/vllm-project/vllm/issues/59176) [Bug]: GLM-5.3-Flash with HiSparse has no compatible KV cache layout (LBHNC vs BLHNC)
- [Bug] 🆕 [#59154](https://github.com/vllm-project/vllm/issues/59154) [Bug]: rust vllm-bench result is quite different from vllm bench serve
- [Bug] 🆕 [#59114](https://github.com/vllm-project/vllm/issues/59114) [Bug]: MoRIIO WRITE: after the producer dies, decode requests hang until client timeout and KV usage stays elevated
- [Feature] 🆕 [#59155](https://github.com/vllm-project/vllm/issues/59155) [Feature]: [ROCm][AITER] Track relu2 (non-gated) MoE activation enablement (Tier 3, vLLM-side integration)
