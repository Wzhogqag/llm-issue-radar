# LLM Serving Issue Radar

_Last run: 2026-07-26T13:53+00:00_

**24 issues** — sgl-project/sglang: 10, vllm-project/vllm: 14 — 🆕 **13 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#32433](https://github.com/sgl-project/sglang/issues/32433) Question: unit mismatch in evict_from_tree_cache for SWATokenToKVPoolAllocator?
- [Bug] [#32356](https://github.com/sgl-project/sglang/issues/32356) [Bug] DeepSeek-V4 DSpark TP=8 can permanently stall under HiCache long-prefix load

### vllm-project/vllm

- [Bug] [#49809](https://github.com/vllm-project/vllm/issues/49809) [Bug][KV Offload][P2P] EngineCore crash reconnecting to peer: stale dead ZmqConnection remains registered

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] [#32309](https://github.com/sgl-project/sglang/issues/32309) [Feature] --enable-dsa-cache-layer-split support single deploy
- [RFC] [#32321](https://github.com/sgl-project/sglang/issues/32321) [RFC] Make BaseTpWorker the explicit framework-to-backend boundary - MLX runner-stub redesign

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#49851](https://github.com/vllm-project/vllm/issues/49851) [Bug]: Multimodal models fail to load on ROCm/RDNA4 (gfx1201) — `CUDA error: invalid argument` in `vit_torch_sdpa_wrapper` encoder attention
- [Bug] 🆕 [#49810](https://github.com/vllm-project/vllm/issues/49810) [Bug]: PCP (#46570) broken for non-compress models (GLM-5.2, compress_ratio=1) — multiple crash paths

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32426](https://github.com/sgl-project/sglang/issues/32426) [Bug] In version v0.5.16, the sakamakismile/Ornith-1.0-35B-NVFP4 model generates garbled characters.
- [Bug] [#32378](https://github.com/sgl-project/sglang/issues/32378) [Bug] mooncake with sglang:dev with glm-5.2-w4afp8 with pd error
- [Bug] [#32311](https://github.com/sgl-project/sglang/issues/32311) [Bug] deepseek v4 flash hang on 4rtx 6000 pro with limited host ram

### vllm-project/vllm

- [Bug] 🆕 [#49844](https://github.com/vllm-project/vllm/issues/49844) [Bug]: PP=2 + GlmMoeDsa: inductor compile combined with CUDA-graph capture produces garbage output; either alone is clean (v0.24 & v0.26)
- [Bug] 🆕 [#49783](https://github.com/vllm-project/vllm/issues/49783) [Bug]: DeepGEMM 2.6.x UE8M0 assert - vLLM passes uninitialized FP32 scale-factor padding to the packing kernel

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#49826](https://github.com/vllm-project/vllm/issues/49826) [Bug]: Cross-node Pipeline Parallelism (PP) fails with "invalid device ordinal" at PyNccl warmup on ROCm (AMD RDNA4 / R9700), reproducible on first inference even after context-corruption workaround

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#49816](https://github.com/vllm-project/vllm/issues/49816) [Feature]: per gpu gpu-memory-utilization
- [RFC] [#49752](https://github.com/vllm-project/vllm/issues/49752) [RFC]: vLLM Agentic Coding Readiness Survey

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#49874](https://github.com/vllm-project/vllm/issues/49874) [Bug]: vllm+tilert+glm-5.1 error
- [Feature] 🆕 [#49848](https://github.com/vllm-project/vllm/issues/49848) [Feature]: MTP speculative decoding under pipeline parallelism — one real blocker (PP+async single-token assumption), everything else is guards

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Feature] [#32312](https://github.com/sgl-project/sglang/issues/32312) [Feature] [Kernel] cursor warp decode kernel for low latency small batch MOE inference

### vllm-project/vllm

- [RFC] [#49765](https://github.com/vllm-project/vllm/issues/49765) [RFC]: Native Disaggregated Pull-Based Queue Worker Interface and Heuristic Pull Router

## Performance / Memory / OOM

### sgl-project/sglang

- [RFC] 🆕 [#32432](https://github.com/sgl-project/sglang/issues/32432) [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for Dynamic CUDA Graph Replay

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49878](https://github.com/vllm-project/vllm/issues/49878) [Bug]: Dramatic KV cache size increase (~40%) for Gemma4 from v0.25.1 to v0.26
- [Bug] 🆕 [#49778](https://github.com/vllm-project/vllm/issues/49778) [Bug]: gpt-oss-120b fails for ROCm on gfx950 with Triton 3.7.1

## Uncategorized

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#32355](https://github.com/sgl-project/sglang/issues/32355) Add REFUTE scientific critique + calibration benchmark

### vllm-project/vllm

- [no-prefix] ⚠no-prefix [#49769](https://github.com/vllm-project/vllm/issues/49769) Add REFUTE scientific critique + calibration benchmark
