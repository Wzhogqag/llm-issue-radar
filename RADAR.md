# LLM Serving Issue Radar

_Last run: 2026-09-05T13:23+00:00_

**21 issues** — sgl-project/sglang: 8, vllm-project/vllm: 13 — 🆕 **17 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 8
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#38022](https://github.com/sgl-project/sglang/issues/38022) [Bug] A single malformed multimodal request takes down the whole engine, and client retries spread it node-by-node across the cluster
- [Feature] 🆕 [#38069](https://github.com/sgl-project/sglang/issues/38069) [Feature] Per-request opt-out from prefix cache insertion (skip_cache_insert)

### vllm-project/vllm

- [Bug] 🆕 [#55381](https://github.com/vllm-project/vllm/issues/55381) [Bug]: Scheduler batch defaults silently fall back to smallest-GPU values inside MIG containers (NVML permission error swallowed), costing 28-53% throughput on H200 2g.35gb

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Performance] 🆕 [#55434](https://github.com/vllm-project/vllm/issues/55434) [Performance]: GLM-5.3 P/D on GB200 — NIXL issues up to ~112k KV descriptors per rank-transfer, making MNNVL/cuda_ipc slower than RDMA on this workload
- [Bug] 🆕 [#55428](https://github.com/vllm-project/vllm/issues/55428) [Bug]: KV cache offload crash-loops under NVIDIA Confidential Computing (TDX guest, H200 CC-On): cudaHostRegister is not allowed in CC mode (documented), and every built-in offload path depends on it
- [Feature] 🆕 [#55463](https://github.com/vllm-project/vllm/issues/55463) [Feature]: Zero-Copy In-Place KV-Cache Compactor via In-Situ Cycle Permutations (1.65x Speedup, 0 Bytes Aux VRAM)

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#55373](https://github.com/vllm-project/vllm/issues/55373) [Bug][ROCm] Sparse indexer clears the full max_model_len logits buffer every decode step: 17% throughput on a 1M context

## Quantization

### sgl-project/sglang

- [other] [#37993](https://github.com/sgl-project/sglang/issues/37993) [Playground] Verified cell: h200 / flash-official / fp4 / low-latency / single
- [RFC] ⚠maintainer-authored [#38004](https://github.com/sgl-project/sglang/issues/38004) [RFC] Quantization module layout: Config, Scheme, backend kernels

### vllm-project/vllm

- [Performance] 🆕 [#55462](https://github.com/vllm-project/vllm/issues/55462) [Performance]: AWQ CUDA GEMM kernel is heavily L1/Memory bound (Profiled on RTX 3070 Ti)
- [Bug] 🆕 [#55425](https://github.com/vllm-project/vllm/issues/55425) [Bug]: [XPU] Intel Arc Pro B70: Qwen3.8-27B MTP2 at 160K causes xe CCS timeout / BCS fault; MTP1 stable
- [Bug] 🆕 [#55406](https://github.com/vllm-project/vllm/issues/55406) [Bug]: Nemotron-3.5-Lightning-30B-A3B-NVFP4 dies with CUDA illegal memory access in cudagraph replay on SM110 (Jetson Thor); deterministic 5-request repro; --enforce-eager works around it
- [RFC] 🆕 [#55421](https://github.com/vllm-project/vllm/issues/55421) [RFC] RL Test Consolidation: File Ownership, Coverage Docstrings, and CI Integration
- [RFC] 🆕 [#55394](https://github.com/vllm-project/vllm/issues/55394) [RFC]: Tile-union QSA sparse attention for prefill (Qwen3.8-Flash-Next): share the K/V gather across neighbouring query rows, −4.7 % TTFT on GB10
- [no-prefix] 🆕 ⚠no-prefix [#55383](https://github.com/vllm-project/vllm/issues/55383) AOT compile cache key ignores the LoRA module tree, loading an incompatible artifact (`KeyError: 'weight'`)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#38031](https://github.com/sgl-project/sglang/issues/38031) [Bug] GLM-5.3-Flash (DSA): HiCache host-tier load-back corrupts generation even without speculative decoding — dropped tool calls, degenerate repetition loops (8×H100, TP8)
- [Bug] [#38009](https://github.com/sgl-project/sglang/issues/38009) [Bug] [DFlash2] Greedy output diverges from target-only Qwen3.8-27B when thinking is enabled

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#55382](https://github.com/vllm-project/vllm/issues/55382) [Feature]: Let `reasoning_effort` set a default `thinking_token_budget` via a server-side effort→budget map

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#55452](https://github.com/vllm-project/vllm/issues/55452) [Bug][ROCm] Startup aborts in CUDA graph capture with --max-num-seqs > 64: AITER split-K workspace is warmed on a different stream than capture uses

## Uncategorized

### sgl-project/sglang

- [Feature] 🆕 [#38075](https://github.com/sgl-project/sglang/issues/38075) [Feature] Implement the standard gRPC Health Checking Protocol
- [Bug] [#38013](https://github.com/sgl-project/sglang/issues/38013) [Bug]
