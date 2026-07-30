# LLM Serving Issue Radar

_Last run: 2026-07-30T14:00+00:00_

**26 issues** — sgl-project/sglang: 5, vllm-project/vllm: 21 — 🆕 **26 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 6
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 6

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#50425](https://github.com/vllm-project/vllm/issues/50425) [Bug][PD][Mooncake] Client disconnect on decode node does not release prefill KV cache
- [no-prefix] 🆕 ⚠no-prefix [#50435](https://github.com/vllm-project/vllm/issues/50435) GSM8K accuracy regression: nightly (0.26.1rc1.dev77) drops ~5% vs latest (0.26.0) on GLM-5.2-FP8 P/D

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#32924](https://github.com/sgl-project/sglang/issues/32924) [Bug] Kimi-K3: repeated 'CUDA error: unspecified launch failure' in decode on the 07-29 kimi-k3 image (c6ad1f26), not on 74968e5653

### vllm-project/vllm

- [Bug] 🆕 [#50427](https://github.com/vllm-project/vllm/issues/50427) [Bug]: FlexAttention paged K/V offsets overflow int32 once `num_gpu_blocks ≥ 2**31 / (block_size · 2 · num_kv_heads · head_size)` — crash *or* silent wrong output
- [Bug] 🆕 [#50381](https://github.com/vllm-project/vllm/issues/50381) [Bug]: fp8/bfloat16 KV cache does a full NVML init+shutdown per attention layer per step
- [Bug] 🆕 [#50331](https://github.com/vllm-project/vllm/issues/50331) [Bug]: FlashInfer BatchPrefillWithPagedKVCache fails with "invalid resource handle" on SM121 (GB10) with head_dim 256 + FP8 KV cache
- [Bug] 🆕 [#50394](https://github.com/vllm-project/vllm/issues/50394) [Bug]: [Kimi K3] Warm up does not cover enough kernels
- [RFC] 🆕 ⚠maintainer-authored [#50324](https://github.com/vllm-project/vllm/issues/50324) [RFC]: Deprecate the FlexAttention backend

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32893](https://github.com/sgl-project/sglang/issues/32893) [Bug] v0.5.16 glm GLM-5.2 W4AFP8 + EAGLE + TP8 , MTP seed issue
- [Bug] 🆕 ⚠maintainer-authored [#32938](https://github.com/sgl-project/sglang/issues/32938) [Bug] FP8 KV cache slows down performance when DSPARK is enabled

### vllm-project/vllm

- [Bug] 🆕 [#50430](https://github.com/vllm-project/vllm/issues/50430) [Bug]: vllm hangs at using NCCL message on 8xB200
- [Performance] 🆕 [#50416](https://github.com/vllm-project/vllm/issues/50416) [Performance]: FlashInfer NVFP4 KV cache causal prefill is ~1.7-1.8x slower than FP8 on SM120
- [Bug] 🆕 [#50332](https://github.com/vllm-project/vllm/issues/50332) [Bug]: DeepGemm accuracy auto-disable (_DEEPGEMM_BLACKWELL_EXCLUDED_MODEL_TYPES) does not apply to the FP8 MoE path

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#50428](https://github.com/vllm-project/vllm/issues/50428) [Bug]: vLLM 0.26.0 incompatible with transformers 5.x (5.14.1) Qwen3.6-35B-A3B  config class renaming
- [Bug] 🆕 [#50413](https://github.com/vllm-project/vllm/issues/50413) [Bug]: RayExecutorV2 should sanitize inherited Ray runtime_env before creating model workers

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#50356](https://github.com/vllm-project/vllm/issues/50356) [Feature]: Support verbose_json for MOSS-Transcribe-Diarize
- [other] 🆕 [#50369](https://github.com/vllm-project/vllm/issues/50369) [Proposal] OpenEval Import/Export Support

## Sampling / Speculative Decoding

### vllm-project/vllm

- [RFC] 🆕 [#50438](https://github.com/vllm-project/vllm/issues/50438) [RFC]: Lookahead-aware prefix-cache hashing for EAGLE-style draft models
- [RFC] 🆕 [#50391](https://github.com/vllm-project/vllm/issues/50391) [RFC]: Support Speculative Decoding with Decode Context Parallelism

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#32907](https://github.com/sgl-project/sglang/issues/32907) [Bug] cutedsl_bf16_gemm 2-CTA TGV kernel: missing trailing cluster barrier → CUDBG_EXCEPTION_CLUSTER_BLOCK_NOT_PRESENT (SM103, PDL + CUDA graph)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#32855](https://github.com/sgl-project/sglang/issues/32855) [Bug] Kimi-K3 DSPARK: Xid 13 (CTA Not Present) crash at ~218k token context on B300

### vllm-project/vllm

- [Bug] 🆕 [#50436](https://github.com/vllm-project/vllm/issues/50436) [Bug]: ROCm tuned-config lookup keys off an unstable device name — shipped gfx1151 configs are unreachable
- [Performance] 🆕 [#50433](https://github.com/vllm-project/vllm/issues/50433) [Performance][MooncakeStoreConnector] Overlapping async cold-prefix loads cause duplicate Gets into distinct GPU blocks
- [Bug] 🆕 [#50337](https://github.com/vllm-project/vllm/issues/50337) [Bug]: JinaEmbeddingsV5Model fails on jina-embeddings-v5-text-nano: EuroBERT backbone misrouted to Qwen3 code path
- [Bug] 🆕 [#50399](https://github.com/vllm-project/vllm/issues/50399) [Bug]: tool_choice: "required" causes tool_calls to continuously output until the maximum token is reached with GLM-5.2 on vLLM 0.26.0
- [no-prefix] 🆕 ⚠no-prefix [#50348](https://github.com/vllm-project/vllm/issues/50348) Free MCP trust infrastructure for AI agents — Agent Trust Cards (Ed25519, 10-layer audit, $0)
