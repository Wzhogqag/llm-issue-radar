# LLM Serving Issue Radar

_Last run: 2026-07-27T14:02+00:00_

**26 issues** — sgl-project/sglang: 8, vllm-project/vllm: 18 — 🆕 **22 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#32433](https://github.com/sgl-project/sglang/issues/32433) Question: unit mismatch in evict_from_tree_cache for SWATokenToKVPoolAllocator?

### vllm-project/vllm

- [Bug] 🆕 [#49902](https://github.com/vllm-project/vllm/issues/49902) [Bug]: Tiered KV offload promotes every waiting request (which fills primary DRAM pool)

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#32521](https://github.com/sgl-project/sglang/issues/32521) [Bug] [MLX] Hunyuan cannot be served: auto_map fails in kv_cache_builder.resolve_transformers_arch

### vllm-project/vllm

- [Bug] 🆕 [#49920](https://github.com/vllm-project/vllm/issues/49920) [Bug]: DiffusionGemma - Unconditional minimax_m3 warmup import in kernel_warmup() crashes engine startup for unrelated models (Triton JIT fails to parse index_topk kernel)

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#49980](https://github.com/vllm-project/vllm/issues/49980) [Bug]: FlashInfer builder ValueError 'provided out is the wrong size for the accumulation' with Llama-4 chunked local attention when a prefill exceeds attention_chunk_size and max_num_seqs is small
- [Bug] 🆕 [#49886](https://github.com/vllm-project/vllm/issues/49886) [Bug]: GLM-5.2-NVFP4 produces garbled/incorrect output and hits NotImplementedError in forward_mha on GB10 (SM121a) with FLASHINFER_MLA_SPARSE_SM120

## Quantization

### sgl-project/sglang

- [Bug] [#32426](https://github.com/sgl-project/sglang/issues/32426) [Bug] In version v0.5.16, the sakamakismile/Ornith-1.0-35B-NVFP4 model generates garbled characters.

### vllm-project/vllm

- [Bug] 🆕 [#49981](https://github.com/vllm-project/vllm/issues/49981) [Bug]: tool_choice: "required" causes xgrammar FSM crash / infinite hang with GLM-5.2-NVFP4 on vLLM 0.24.0
- [Bug] 🆕 [#49926](https://github.com/vllm-project/vllm/issues/49926) [Bug]: EngineDeadError NVFP4 marlin
- [Bug] 🆕 [#49893](https://github.com/vllm-project/vllm/issues/49893) [Bug]: SpeculativeConfig method="draft_model" cannot load mixed-precision compressed-tensors checkpoints (config_groups)
- [Feature] 🆕 [#49905](https://github.com/vllm-project/vllm/issues/49905) [Feature]: DeepGEMM kernels are never warmed — only 2 of 24 entry points, so fp8_einsum JIT-loads during serving

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#32470](https://github.com/sgl-project/sglang/issues/32470) [Bug]  CUDA illegal memory access during compact ragged-verify graph capture (c128 plan kernel race)

### vllm-project/vllm

- [Bug] 🆕 [#49983](https://github.com/vllm-project/vllm/issues/49983) [Bug]: /metrics returns 500 when PROMETHEUS_MULTIPROC_DIR resolves to a network-backed/mounted volume (TP>1)
- [Perf] 🆕 [#49921](https://github.com/vllm-project/vllm/issues/49921) [Perf] BF16x3 router GEMM gated off family-120 Blackwell (GB10 / DGX Spark, sm_121) — the only barrier for DeepSeek-V4-Flash's fp32 router

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#49973](https://github.com/vllm-project/vllm/issues/49973) [Feature]: Support ubuntu 26.04 runtime container

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#32527](https://github.com/sgl-project/sglang/issues/32527) [BUG] EAGLE + DP Attention + PD Disaggregation: Deadlock when `index_share_for_mtp_iteration` is enabled for GLM-5.2

### vllm-project/vllm

- [Perf] 🆕 [#49927](https://github.com/vllm-project/vllm/issues/49927) [Perf] #48137 costs ~10.6% spec-decode acceptance and #48660 shifts output distributions on DeepSeek-V4-Flash — isolated via #48660-only arm on a production 2-node deployment
- [Bug] 🆕 [#49918](https://github.com/vllm-project/vllm/issues/49918) [Bug]: Prefill with prompt length == 1 + num_speculative_tokens misclassified as uniform decode → FULL spec-verify cudagraph skips GDN/hybrid recurrent-state write → deterministic garbage (any spec method incl. ngram; v0.25.1 & v0.26.0)
- [Bug] 🆕 [#49896](https://github.com/vllm-project/vllm/issues/49896) [Bug] DeepSeek-V4 on SM12x: NaN MQA logits drive top_k_per_row_prefill to emit uninitialized smem as indices -> illegal memory access

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#32536](https://github.com/sgl-project/sglang/issues/32536) [Bug] poolside_v1 reasoning parser doesn't separate reasoning for Laguna-S-2.1 (thinking-on template default)

### vllm-project/vllm

- [Bug] 🆕 [#49922](https://github.com/vllm-project/vllm/issues/49922) [Bug]: [Regression] Assertion res == CUresult::CUDA_SUCCESS failed in FlashMLA (phase1.cuh) for DeepSeek-V4 on v0.26.0 (Works in v0.25.0)

## Performance / Memory / OOM

### sgl-project/sglang

- [RFC] [#32432](https://github.com/sgl-project/sglang/issues/32432) [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for Dynamic CUDA Graph Replay

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49924](https://github.com/vllm-project/vllm/issues/49924) [Bug][XPU]: GDN attention silently corrupts memory under load — fix merged in vllm-xpu-kernels but requirements/xpu.txt pins a release that predates it
- [other] 🆕 [#49955](https://github.com/vllm-project/vllm/issues/49955) [Regression] Trailing <turn|> token appearing at the end of generated text in vLLM 0.26.0
- [Bug] [#49878](https://github.com/vllm-project/vllm/issues/49878) [Bug]: Dramatic KV cache size increase (~40%) for Gemma4 from v0.25.1 to v0.26

## Uncategorized

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#32519](https://github.com/sgl-project/sglang/issues/32519) [WIP]
