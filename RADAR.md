# LLM Serving Issue Radar

_Last run: 2026-08-30T13:23+00:00_

**27 issues** — sgl-project/sglang: 7, vllm-project/vllm: 20 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 6
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 6
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Feature] 🆕 [#54413](https://github.com/vllm-project/vllm/issues/54413) [Feature][KV-offloading]: OffloadingConnector rejects hybrid models whose KV groups have blocks smaller than one hash unit (GLM-5.3-Flash) — per-group blocks_per_chunk implementation attached
- [RFC] 🆕 [#54363](https://github.com/vllm-project/vllm/issues/54363) [RFC]: Data integrity and I/O liveness for the filesystem KV offload tier

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] [#37022](https://github.com/sgl-project/sglang/issues/37022) [Bug] Prefill transfer failed with exception KVTransferError Decode instance could be dead, remote mooncake session ...:port is not alive

### vllm-project/vllm

- [Feature] 🆕 [#54354](https://github.com/vllm-project/vllm/issues/54354) [Feature]: cannot budget KV cache per GPU when one card of a DP group is shared with another process
- [RFC] 🆕 [#54426](https://github.com/vllm-project/vllm/issues/54426) [RFC] Qwen3.8-Flash-Next: fp8_e4m3 KV cache on the QSA path — working patch, one machine, looking for corroboration
- [no-prefix] 🆕 ⚠no-prefix [#54383](https://github.com/vllm-project/vllm/issues/54383) First boot of a new `(max-num-batched-tokens, max-num-seqs)` shape is granted a ~5% smaller KV cache than subsequent identical boots

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#37105](https://github.com/sgl-project/sglang/issues/37105) [Bug] GLM-5.3-Flash on RTX PRO 6000 (sm_120): two DSA backend blockers after the deep_gemm NameError

### vllm-project/vllm

- [Bug] [#54317](https://github.com/vllm-project/vllm/issues/54317) [Bug]: GLM-5.3-Flash (glm5next) — recurring CUDA illegal memory access on 4xB200, surfacing in three unrelated kernels (KDA linear-attention, MHC TileLang, TRT-LLM fused MoE)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#37089](https://github.com/sgl-project/sglang/issues/37089) [Bug] Qwen3.8-Flash-Next W4A16 on A100 TP4: Marlin MoE invalid thread config; Triton MoE then hits QSA FA-CuTe capture failure
- [Bug] 🆕 [#37052](https://github.com/sgl-project/sglang/issues/37052) [Bug] Qwen3.8-Flash-Next + NEXTN full decode graph: repeated dual-rank invalid-probability asserts on GB10

### vllm-project/vllm

- [Bug] 🆕 [#54311](https://github.com/vllm-project/vllm/issues/54311) [Bug]: Cutlass int8 kernel never declines on SM120, making the Triton int8 fallback unreachable
- [Bug] [#54350](https://github.com/vllm-project/vllm/issues/54350) [Bug]: [XPU] moe_wna16 AWQ fallback compares CUDA device_capability, always -1 on XPU
- [Bug] [#54349](https://github.com/vllm-project/vllm/issues/54349) [Bug]: [XPU] AWQ MoE selector (check_moe_marlin_supports_config) ignores XPU platform, crashes on Marlin path
- [Bug] [#54331](https://github.com/vllm-project/vllm/issues/54331) [Bug]: sm_120 hybrid-GDN NVFP4 dies under sustained load whenever CUDA graphs are on — persists 0.26.0 → 0.28.0, clean on 0.24.0; PIECEWISE and TRITON_ATTN both fail, only enforce_eager survives

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#54415](https://github.com/vllm-project/vllm/issues/54415) [Bug][Feature][KV-offloading]: shared-mmap CPU region assumes all ranks on one host — multi-node engines hang at init; node-local disk tier reference implementation
- [Bug] [#54318](https://github.com/vllm-project/vllm/issues/54318) [Bug]: Qwen3.8-Flash-Next-FP8 fails to start on 4x NVIDIA A100 due to fp8e4nv unsupported in SM80

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#37128](https://github.com/sgl-project/sglang/issues/37128) [Bug] Spec V2 paths no longer emit speculative-decoding OpenTelemetry spans

### vllm-project/vllm

- [Bug] 🆕 [#54425](https://github.com/vllm-project/vllm/issues/54425) [Bug]: V2 sampler warmup misses explicit-seed native path when FlashInfer is enabled
- [Bug] 🆕 [#54392](https://github.com/vllm-project/vllm/issues/54392) [Bug]: PD-admitted Mamba request is spec-padded before prefill completes, then align split truncates the 8-token window to 5
- [Bug] 🆕 [#54360](https://github.com/vllm-project/vllm/issues/54360) [Bug]: Speculative decoding (mtp and dflash) silently disables prefix-cache hits for hybrid GDN models on nightly; worked on v0.24.0
- [Feature] 🆕 [#54414](https://github.com/vllm-project/vllm/issues/54414) [Feature][KV-offloading]: recent-window state groups can never participate in restores — per-group offload exclusion + hit-boundary rollback (GLM-5.3 tail_cache)
- [RFC] 🆕 [#54333](https://github.com/vllm-project/vllm/issues/54333) [RFC]: Reduced sampling for tensor-parallel decoding

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#37097](https://github.com/sgl-project/sglang/issues/37097) [Bug] Pretokenized image requests can crash GLM MRoPE with a stale retokenized mask

### vllm-project/vllm

- [Feature] [#54340](https://github.com/vllm-project/vllm/issues/54340) [Feature]: In the framework, there are many assert statements. How can we optimize the issue of service processes crashing due to asserts?

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#37111](https://github.com/sgl-project/sglang/issues/37111) [Bug] Qwen3.8-Flash-Next QSA + NEXTN decode graph silently corrupts output on GB10 TP2

### vllm-project/vllm

- [Bug] 🆕 [#54385](https://github.com/vllm-project/vllm/issues/54385) [Bug]: DeepSeek V4 DSpark TP=2 on 2× GB10 hits dual-rank Xid 31 at the inferred T=16 PIECEWISE warmup

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#54389](https://github.com/vllm-project/vllm/issues/54389) [Feature]: Tencent/WeMM-Embedding
