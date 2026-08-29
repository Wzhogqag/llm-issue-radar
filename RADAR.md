# LLM Serving Issue Radar

_Last run: 2026-08-29T13:22+00:00_

**18 issues** — sgl-project/sglang: 4, vllm-project/vllm: 14 — 🆕 **17 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [other] 🆕 [#36935](https://github.com/sgl-project/sglang/issues/36935) [Prefix Cache / Hybrid] Branch reuse silently collapses under LRU pressure when (kv_pool_tokens / chunked_prefill_size) > max_mamba_cache_size

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#37022](https://github.com/sgl-project/sglang/issues/37022) [Bug] Prefill transfer failed with exception KVTransferError Decode instance could be dead, remote mooncake session ...:port is not alive

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#54317](https://github.com/vllm-project/vllm/issues/54317) [Bug]: GLM-5.3-Flash (glm5next) — recurring CUDA illegal memory access on 4xB200, surfacing in three unrelated kernels (KDA linear-attention, MHC TileLang, TRT-LLM fused MoE)
- [Bug] 🆕 [#54305](https://github.com/vllm-project/vllm/issues/54305) [Bug]: Direct DCP A2A crashes on GLM sparse-MLA strided output
- [Bug] 🆕 [#54300](https://github.com/vllm-project/vllm/issues/54300) [Bug]: [Regression 0.27→0.28]: GlmMoeDsa (GLM-5.3) + decode-context-parallel crashes: 'FlashInferMLASparseMetadata' object has no attribute 'decode' — with or without spec decode, both runners, both cudagraph modes

## Quantization

### sgl-project/sglang

- [other] 🆕 [#36941](https://github.com/sgl-project/sglang/issues/36941) [GB10] Long prefill (>40k tokens) exhausts unified memory and silently kills the worker rank — no traceback, no OOM record; cross-stack control passes at 54k

### vllm-project/vllm

- [Bug] 🆕 [#54350](https://github.com/vllm-project/vllm/issues/54350) [Bug]: [XPU] moe_wna16 AWQ fallback compares CUDA device_capability, always -1 on XPU
- [Bug] 🆕 [#54349](https://github.com/vllm-project/vllm/issues/54349) [Bug]: [XPU] AWQ MoE selector (check_moe_marlin_supports_config) ignores XPU platform, crashes on Marlin path
- [Bug] 🆕 [#54331](https://github.com/vllm-project/vllm/issues/54331) [Bug]: sm_120 hybrid-GDN NVFP4 dies under sustained load whenever CUDA graphs are on — persists 0.26.0 → 0.28.0, clean on 0.24.0; PIECEWISE and TRITON_ATTN both fail, only enforce_eager survives
- [Bug] 🆕 [#54304](https://github.com/vllm-project/vllm/issues/54304) [Bug]: Quantized embeddings fail on many model types
- [Bug] [#54237](https://github.com/vllm-project/vllm/issues/54237) [Bug]: 0.28.0 consume all host memory at start and freeze (OK with 0.27.1)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#36943](https://github.com/sgl-project/sglang/issues/36943) [Bug] --enable-symm-mem: all TP schedulers deadlock silently in ncclCommWindowRegister (blocking UDS recvmsg, no timeout) when the symmetric-memory pool grows at runtime

### vllm-project/vllm

- [Bug] 🆕 [#54259](https://github.com/vllm-project/vllm/issues/54259) [Bug]: intermittent ShmRingBuffer race on cold boot with TP=2 over Ray (sm_121 / unified memory)

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#54318](https://github.com/vllm-project/vllm/issues/54318) [Bug]: Qwen3.8-Flash-Next-FP8 fails to start on 4x NVIDIA A100 due to fp8e4nv unsupported in SM80
- [Bug] 🆕 [#54256](https://github.com/vllm-project/vllm/issues/54256) [Bug]: Gemma4 parser drops tool calls when transitioning out of reasoning channel (<channel|>call:...)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#54337](https://github.com/vllm-project/vllm/issues/54337) [Bug]: Assistant `content=null` + `tool_calls` renders literal "None" into chat template context — degenerate outputs in agent workloads
- [Feature] 🆕 [#54340](https://github.com/vllm-project/vllm/issues/54340) [Feature]: In the framework, there are many assert statements. How can we optimize the issue of service processes crashing due to asserts?

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#54243](https://github.com/vllm-project/vllm/issues/54243) [Bug]: batch-invariant M buckets collapse under `torch.compile` (0.28.0)
