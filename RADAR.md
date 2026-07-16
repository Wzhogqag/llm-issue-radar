# LLM Serving Issue Radar

_Last run: 2026-07-16T13:59+00:00_

**23 issues** — sgl-project/sglang: 6, vllm-project/vllm: 17 — 🆕 **23 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 8

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#31458](https://github.com/sgl-project/sglang/issues/31458) [Feature] RFC: SGLang KV Indexer for Distributed KV Cache Placement Metadata

### vllm-project/vllm

- [RFC] 🆕 [#48743](https://github.com/vllm-project/vllm/issues/48743) [RFC]: Return extracted hidden states in the generation response

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#48809](https://github.com/vllm-project/vllm/issues/48809) [Bug]: The Deepseek v4 model compiles kenrel during the inference process
- [Bug] 🆕 [#48803](https://github.com/vllm-project/vllm/issues/48803) [Bug]: "There are significant spike issues in TTFT" with Kimi-K2.6-NVFP4
- [Bug] 🆕 [#48752](https://github.com/vllm-project/vllm/issues/48752) [Bug]: sample_tokens RPC timeout with GLM-5.2-FP8 + DSpark speculative decoding, TP=8 across 2 nodes (Blackwell GB200)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#48827](https://github.com/vllm-project/vllm/issues/48827) [Bug]: enable_multithread_load silently disables EP weight filtering (local_expert_ids never reaches multi_thread_safetensors_weights_iterator)
- [Bug] 🆕 [#48801](https://github.com/vllm-project/vllm/issues/48801) [Bug]: vLLM+LMCache GLM-5.2 inference causes engine RPCTimeout

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#48747](https://github.com/vllm-project/vllm/issues/48747) [Feature]: Can we add base PCP support for hybrid attention?

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#31384](https://github.com/sgl-project/sglang/issues/31384) [Bug] glm5.2 tep dp=2 cause speculative eagle error

### vllm-project/vllm

- [Bug] 🆕 [#48848](https://github.com/vllm-project/vllm/issues/48848) [Bug]: Gemma4 MTP speculative decoding crashes at engine init on 0.25.1 — "a and b must have same reduction dim" (regression from 0.21.0)
- [Bug] 🆕 [#48749](https://github.com/vllm-project/vllm/issues/48749) [Bug]: [MRV2] MTP speculative decoding crashes with cudaErrorStreamCaptureUnsupported during CUDA graph capture

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#31459](https://github.com/sgl-project/sglang/issues/31459) [Bug] Model Gateway silently rewrites MCP tool_choice="required" to "auto"
- [Perf] 🆕 [#31424](https://github.com/sgl-project/sglang/issues/31424) [Perf] Speed up HiCache host buffer allocation: use `MAP_PRIVATE` + `madvise` instead of `MAP_SHARED | MAP_POPULATE`
- [no-prefix] 🆕 ⚠no-prefix [#31356](https://github.com/sgl-project/sglang/issues/31356) Provide a factory to build the OpenAI ASGI app bound to an in-process Engine

### vllm-project/vllm

- [Bug] 🆕 [#48753](https://github.com/vllm-project/vllm/issues/48753) [Bug]: Qwen3/Qwen3-Coder tool parser strips meaningful whitespace from string parameter values (breaks exact-match edit tools)

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#31347](https://github.com/sgl-project/sglang/issues/31347) JIT hadamard/DSA-indexer kernel compile races on shared NFS tvm-ffi cache — ESTALE link failure on multi-node cold start

### vllm-project/vllm

- [Bug] 🆕 [#48831](https://github.com/vllm-project/vllm/issues/48831) [Bug]: V1 Engine Produces Incorrect Scores for Qwen3-Reranker-0.6B on Long Sequences (>8K tokens)
- [Bug] 🆕 [#48823](https://github.com/vllm-project/vllm/issues/48823) [Bug]: Failed to initialize FlashInfer All Reduce workspace: CUDA driver error: invalid device ordinal
- [Bug] 🆕 [#48808](https://github.com/vllm-project/vllm/issues/48808) [Bug]: DP request distribution becomes imbalanced under long-context workload on H20 GPU
- [Bug] 🆕 [#48786](https://github.com/vllm-project/vllm/issues/48786) [Bug]: Qwen3.5-35B FP8 kv cache is slower than BF16 kv cache on SM90 (Hopper)
- [Bug] 🆕 [#48745](https://github.com/vllm-project/vllm/issues/48745) [Bug]: Spurious EngineDeadError traceback logged during graceful shutdown (AsyncLLM.shutdown cancels output_handler after engine teardown)
- [Bug] 🆕 [#48744](https://github.com/vllm-project/vllm/issues/48744) [Bug]: Gemma-4-26B-A4B-it MoE fails to deploy on XPU backend (vLLM v0.21.0)
- [Feature] 🆕 [#48826](https://github.com/vllm-project/vllm/issues/48826) [Feature]: Migration plan for ROCm 7.14 / TheRock production release (containers + wheels)
