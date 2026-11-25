# LLM Serving Issue Radar

_Last run: 2026-11-25T13:24+00:00_

**14 issues** — sgl-project/sglang: 3, vllm-project/vllm: 11 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#69888](https://github.com/vllm-project/vllm/issues/69888) [RFC]: CPU Offloading Tier: Best-Effort KV Hint Retention
- [RFC] 🆕 [#69844](https://github.com/vllm-project/vllm/issues/69844) [RFC][Multimodal]: Preemptible vision encoding via zero-cross-frame micro-chunking and layer-boundary yields on colocated GPUs

## Quantization

### sgl-project/sglang

- [other] 🆕 [#53062](https://github.com/sgl-project/sglang/issues/53062) [Refactor] WIP features in PR50205

### vllm-project/vllm

- [RFC] 🆕 [#69876](https://github.com/vllm-project/vllm/issues/69876) [RFC]: Memory-neutral NVFP4 x FP8 MoE on Hopper: on-the-fly decode from Marlin tensors
- [RFC] 🆕 [#69854](https://github.com/vllm-project/vllm/issues/69854) [RFC]: Low-Rank Recurrent State Compression for Mamba2 Hybrid Models (SPARE)

## New Model Integration

### vllm-project/vllm

- [RFC] 🆕 [#69827](https://github.com/vllm-project/vllm/issues/69827) [RFC]: Extend automatic NUMA binding to additional accelerator platforms

## Sampling / Speculative Decoding

### vllm-project/vllm

- [other] 🆕 [#69832](https://github.com/vllm-project/vllm/issues/69832) [Doc/UX] The --async-scheduling x speculative-decoding restriction is undocumented and its two failure modes are asymmetric
- [RFC] 🆕 [#69895](https://github.com/vllm-project/vllm/issues/69895) [RFC]: Qwen3.6-27B DMTP speculative decoding with native MTP and DFlash2

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#69791](https://github.com/vllm-project/vllm/issues/69791) [Bug]: Malformed message-level input on the DeepSeek-V4 and V4.1 chat encoders returns HTTP 500 instead of 400

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#69902](https://github.com/vllm-project/vllm/issues/69902) [Bug]: I'm using the CPU version of vLLM, and the memory usage keeps growing continuously. Has anyone else encountered this issue
- [Bug] 🆕 [#69897](https://github.com/vllm-project/vllm/issues/69897) [Bug][XPU] Memory query remains free == total after allocations on WSL2, inflating KV cache budget
- [Bug] 🆕 [#69839](https://github.com/vllm-project/vllm/issues/69839) [Bug][ROCm] num_compute_units() is half the card's CU count on gfx1201, so grid-sized ops run at half occupancy (4.3x measured)

## Uncategorized

### sgl-project/sglang

- [other] 🆕 [#53122](https://github.com/sgl-project/sglang/issues/53122) [Question] Public kernel and benchmark for Strata Figure 5 (H200 GPU-assisted KV I/O)
- [Feature] 🆕 [#53066](https://github.com/sgl-project/sglang/issues/53066) [Feature] Discover individual workers from headless Service DNS in sgl-router
