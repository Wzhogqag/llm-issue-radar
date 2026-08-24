# LLM Serving Issue Radar

_Last run: 2026-08-24T13:37+00:00_

**19 issues** — sgl-project/sglang: 6, vllm-project/vllm: 13 — 🆕 **18 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 6
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#36179](https://github.com/sgl-project/sglang/issues/36179) [Bug] When using hicache to enable L2/L3 storage in DeepSeek V4, token loop repetition occurs very frequently

### vllm-project/vllm

- [RFC] 🆕 [#53486](https://github.com/vllm-project/vllm/issues/53486) [RFC]: Secondary Tier Usage Metrics
- [RFC] 🆕 [#53485](https://github.com/vllm-project/vllm/issues/53485) [RFC]: Reconcile Backpressure Admission

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#36140](https://github.com/sgl-project/sglang/issues/36140) [Bug] DFLASH speculative decoding is not supported under PD disaggregation: spec_info None crash, then watchdog self-kill
- [Feature] [#36083](https://github.com/sgl-project/sglang/issues/36083) [Feature] Extend cross-layer index-topk reuse (dsa_layer_skips_topk) to DeepSeek-V4

### vllm-project/vllm

- [Bug] 🆕 [#53569](https://github.com/vllm-project/vllm/issues/53569) [Bug][KV Offload] OffloadingConnector fs tier: multi-group MLA+DSA (DeepSeek-V4) TP=2 lookup fully misses across restart; single-group MHA hits 99.6%
- [Performance] 🆕 [#53548](https://github.com/vllm-project/vllm/issues/53548) [Performance]: higher Mooncake Store tail latency with all-HCA registration on 4-TP / 4-RNIC hosts
- [Bug] 🆕 [#53505](https://github.com/vllm-project/vllm/issues/53505) [Bug]: [SpecDecode] Hybrid Mamba (align) corrupts under speculative decoding when a KV connector is attached — even with zero retrieved tokens
- [RFC] 🆕 [#53484](https://github.com/vllm-project/vllm/issues/53484) [RFC]: Generalize Connector Metrics

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#53573](https://github.com/vllm-project/vllm/issues/53573) [Bug]: [PCP+DCP][MLA] Rank-local PCP context metadata causes divergent DCP KV-gather collectives

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36181](https://github.com/sgl-project/sglang/issues/36181) [Bug] DSV4 indexer weights_proj CUBLAS_STATUS_EXECUTION_FAILED / cudaErrorIllegalAddress under multi-turn hicache load
- [Bug] 🆕 [#36118](https://github.com/sgl-project/sglang/issues/36118) [Bug] Qwen3.8 DFlash2 TTFT regresses 3.1% from db2eb475 to 95f5ecd3 on RTX PRO 6000 Blackwell

### vllm-project/vllm

- [RFC] 🆕 [#53563](https://github.com/vllm-project/vllm/issues/53563) [RFC]: SM90 Exact Fused DSA Prefill Indexer

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#36174](https://github.com/sgl-project/sglang/issues/36174) [Feature] Support deterministic inference for DeepSeek-V4

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Performance] 🆕 [#53504](https://github.com/vllm-project/vllm/issues/53504) [Performance]: MTP first repeat misses prefix cache on a hybrid Mamba/GDN model
- [Bug] 🆕 [#53477](https://github.com/vllm-project/vllm/issues/53477) [Bug]: DFLASH2 force reprocesses context every reply

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#53472](https://github.com/vllm-project/vllm/issues/53472) [Performance]: v0.23→v0.26: ~20% decode ITL regression on non-gated (relu2) BF16 MoE (SM100) — TRTLLM-gen backend swap (#43853) adds per-call host cost; --moe-backend flashinfer_cutlass recovers ~90%

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#53481](https://github.com/vllm-project/vllm/issues/53481) [Bug]: FLASHINFER backend produces degenerate output for Mistral3 (Ministral-3-3B) on sm_120 with ANY kv-cache dtype; TRITON_ATTN and FLASH_ATTN correct
- [Bug] 🆕 [#53480](https://github.com/vllm-project/vllm/issues/53480) [Bug][XPU]: Silent persistent output corruption (endless "!" / token 0) under sustained concurrent decode on Arc Pro B70, W4A16 27B head_dim 256
