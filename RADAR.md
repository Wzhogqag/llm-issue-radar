# LLM Serving Issue Radar

_Last run: 2026-11-03T13:22+00:00_

**18 issues** — sgl-project/sglang: 3, vllm-project/vllm: 15 — 🆕 **18 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 5
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#48145](https://github.com/sgl-project/sglang/issues/48145) [Bug] Mooncake HiCache backup fails for Qwen3.8-Flash-Next-FP8

### vllm-project/vllm

- [Bug] 🆕 [#65378](https://github.com/vllm-project/vllm/issues/65378) [Bug]: Extensible KV cache undersizes the KV cache on integrated (UMA) GPUs, down to 0 blocks: free memory read with raw cudaMemGetInfo
- [Bug] 🆕 [#65325](https://github.com/vllm-project/vllm/issues/65325) [Bug]: Requests queued during level-2 sleep run before `reload_weights` and return wrong output with HTTP 200
- [Bug] 🆕 [#65324](https://github.com/vllm-project/vllm/issues/65324) [Bug]: Requests queued during level-2 sleep run before `reload_weights` and return wrong output with HTTP 200
- [other] 🆕 [#65327](https://github.com/vllm-project/vllm/issues/65327) [Core]: DRY BlockPool.get_new_blocks with caching + metrics on/off variable factored out of the loop

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#48141](https://github.com/sgl-project/sglang/issues/48141) [Bug] MiniMax H3 cookbook silently downscales 1440p video requests to 768p

### vllm-project/vllm

- [Bug] 🆕 [#65387](https://github.com/vllm-project/vllm/issues/65387) [Bug]: TP workers wedge permanently in Triton kernel launch (GDN layer_norm_fwd) with idle GPUs; Qwen3.5 + MTP, v0.29.0
- [other] 🆕 [#65359](https://github.com/vllm-project/vllm/issues/65359) [Proposal][Perf] Wire flashinfer's PcieIpcAllGatherWorkspace into CudaCommunicator.all_gather for latency-bound TP gathers

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#48150](https://github.com/sgl-project/sglang/issues/48150) [Bug] fused_marlin_moe is not run-to-run deterministic on sm_90+ (atomic adds, moe_align_block_size token order); --enable-deterministic-inference does not cover it

## Distributed / TP / PP / EP

### vllm-project/vllm

- [other] 🆕 [#65358](https://github.com/vllm-project/vllm/issues/65358) [Feature request] DeepGEMM MegaMoE: support SM120 (Blackwell workstation) GPUs

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#65401](https://github.com/vllm-project/vllm/issues/65401) [Bug]: get_top_k_tokens applies scaling and soft capping in the wrong order
- [Bug] 🆕 [#65385](https://github.com/vllm-project/vllm/issues/65385) [Bug]: GDN Triton/FLA prefill gives wrong, non-deterministic results on Hopper (H20) with triton 3.6: `chunk_scaled_dot_kkt_fwd` autotune configs with BK < K and num_warps >= 4 are broken
- [Bug] 🆕 [#65332](https://github.com/vllm-project/vllm/issues/65332) [Bug]: Large `n` (parallel sampling) in /v1/chat/completions causes severe cross-request latency
- [no-prefix] 🆕 ⚠no-prefix [#65312](https://github.com/vllm-project/vllm/issues/65312) High-concurrency MTP on GLM-5.3 (H20 x8, batch 256): static K loses 10x; per-batch-size K table recovers it

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#65328](https://github.com/vllm-project/vllm/issues/65328) [Bug]: shared streaming helper synthesizes delta_token_ids that serving never sends, changing engine behavior

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#65391](https://github.com/vllm-project/vllm/issues/65391) [Bug]: Resolve Triton kernel block sizes per platform instead of hardcoding them
- [other] 🆕 [#65390](https://github.com/vllm-project/vllm/issues/65390) [ROCm] A text-only model needs torchvision, and you find out 15 minutes into JIT compilation

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#65348](https://github.com/vllm-project/vllm/issues/65348) [Feature]: Rust frontend: allow fetching multimodal media from private/internal hosts
