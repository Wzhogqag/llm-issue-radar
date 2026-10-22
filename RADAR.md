# LLM Serving Issue Radar

_Last run: 2026-10-22T13:33+00:00_

**13 issues** — sgl-project/sglang: 5, vllm-project/vllm: 8 — 🆕 **13 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#63037](https://github.com/vllm-project/vllm/issues/63037) [Bug][KV Offload] Reused OffloadKey can lose metadata from delayed BlockStored events

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#63058](https://github.com/vllm-project/vllm/issues/63058) [Feature]: keep_tags for CuMemAllocator.sleep so selected allocations (e.g. kv_cache) stay mapped
- [Feature] 🆕 [#63056](https://github.com/vllm-project/vllm/issues/63056) [Feature]: expose --sleep-mode-backend on the CLI (ModelConfig.sleep_mode_backend has no EngineArgs flag)

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#63043](https://github.com/vllm-project/vllm/issues/63043) [Bug]: Native FlashInfer produces garbage output with BF16 Q and non-unit q_scale

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#45755](https://github.com/sgl-project/sglang/issues/45755) [Bug] Kimi-K3 on SM90: `flashinfer_mxfp4` silently computes GPT-OSS SwiGLU instead of SiTU

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#45786](https://github.com/sgl-project/sglang/issues/45786) [Bug] GB300 aarch64/MNNVL: NCCL initialization fails under Nsight Systems in v0.5.22 stack

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#45777](https://github.com/sgl-project/sglang/issues/45777) [Feature] Add Host Offloading and Asynchronous Prefetching for DeepSeek V4.1 Engram

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#45781](https://github.com/sgl-project/sglang/issues/45781) [Bug] GLM-5.3 FP8 inference hangs after sustained workload with KV cache full (TP8, EAGLE, H200)

### vllm-project/vllm

- [Bug] 🆕 [#63128](https://github.com/vllm-project/vllm/issues/63128) [Bug][Spec Decode] MTP draft from a draft-only checkpoint runs with an uninitialised embedding under pipeline parallelism (no error; acceptance collapses)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [RFC] 🆕 [#45816](https://github.com/sgl-project/sglang/issues/45816) [RFC] Complete migration to the shared api.v1 backend API

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#63121](https://github.com/vllm-project/vllm/issues/63121) [Bug]: `torchcodec` is unpinned and resolves to a CUDA-13 wheel in CUDA-12.9 builds, breaking `vllm serve` on `vllm/vllm-openai:v0.32.0-cu129`
- [Bug] 🆕 [#63052](https://github.com/vllm-project/vllm/issues/63052) [Bug]: Breakable PIECEWISE capture (model runner V2) leaves warmup activations cached on the discarded capture stream
- [Bug] 🆕 [#63026](https://github.com/vllm-project/vllm/issues/63026) [Bug]: EngineCore CPU memory growth on Ascend associated with SHM notification mailbox accumulation
