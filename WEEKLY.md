# Weekly Trends — 2026-08-30

Window: 2026-08-24 → 2026-08-30 (7 snapshots)

**Totals:** 19 → 27  (27 appeared, 19 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 2 | +1 | 2 | 1 |
| Build / Install / Platform | 2 | 2 | 0 | 2 | 2 |
| KV Cache / Connector / PD Disagg | 6 | 4 | -2 | 4 | 6 |
| New Model Integration | 1 | 2 | +1 | 2 | 1 |
| Performance / Memory / OOM | 1 | 0 | -1 | 0 | 1 |
| Quantization | 3 | 6 | +3 | 6 | 3 |
| Sampling / Speculative Decoding | 2 | 6 | +4 | 6 | 2 |
| Scheduler / Batching | 3 | 2 | -1 | 2 | 3 |
| Serving / OpenAI API / Streaming | 0 | 2 | +2 | 2 | 0 |
| Uncategorized | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#37105](https://github.com/sgl-project/sglang/issues/37105) [Bug] GLM-5.3-Flash on RTX PRO 6000 (sm_120): two DSA backend blockers after the deep_gemm NameError
- [Bug] [vllm-project/vllm#54317](https://github.com/vllm-project/vllm/issues/54317) [Bug]: GLM-5.3-Flash (glm5next) — recurring CUDA illegal memory access on 4xB200, surfacing in three unrelated kernels (KDA linear-attention, MHC TileLang, TRT-LLM fused MoE)

### Build / Install / Platform

- [Bug] [sgl-project/sglang#37111](https://github.com/sgl-project/sglang/issues/37111) [Bug] Qwen3.8-Flash-Next QSA + NEXTN decode graph silently corrupts output on GB10 TP2
- [Bug] [vllm-project/vllm#54385](https://github.com/vllm-project/vllm/issues/54385) [Bug]: DeepSeek V4 DSpark TP=2 on 2× GB10 hits dual-rank Xid 31 at the inferred T=16 PIECEWISE warmup

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#37022](https://github.com/sgl-project/sglang/issues/37022) [Bug] Prefill transfer failed with exception KVTransferError Decode instance could be dead, remote mooncake session ...:port is not alive
- [Feature] [vllm-project/vllm#54354](https://github.com/vllm-project/vllm/issues/54354) [Feature]: cannot budget KV cache per GPU when one card of a DP group is shared with another process
- [no-prefix] [vllm-project/vllm#54383](https://github.com/vllm-project/vllm/issues/54383) First boot of a new `(max-num-batched-tokens, max-num-seqs)` shape is granted a ~5% smaller KV cache than subsequent identical boots
- [RFC] [vllm-project/vllm#54426](https://github.com/vllm-project/vllm/issues/54426) [RFC] Qwen3.8-Flash-Next: fp8_e4m3 KV cache on the QSA path — working patch, one machine, looking for corroboration

### New Model Integration

- [Bug] [vllm-project/vllm#54318](https://github.com/vllm-project/vllm/issues/54318) [Bug]: Qwen3.8-Flash-Next-FP8 fails to start on 4x NVIDIA A100 due to fp8e4nv unsupported in SM80
- [Bug] [vllm-project/vllm#54415](https://github.com/vllm-project/vllm/issues/54415) [Bug][Feature][KV-offloading]: shared-mmap CPU region assumes all ranks on one host — multi-node engines hang at init; node-local disk tier reference implementation

### Quantization

- [Bug] [sgl-project/sglang#37052](https://github.com/sgl-project/sglang/issues/37052) [Bug] Qwen3.8-Flash-Next + NEXTN full decode graph: repeated dual-rank invalid-probability asserts on GB10
- [Bug] [sgl-project/sglang#37089](https://github.com/sgl-project/sglang/issues/37089) [Bug] Qwen3.8-Flash-Next W4A16 on A100 TP4: Marlin MoE invalid thread config; Triton MoE then hits QSA FA-CuTe capture failure
- [Bug] [vllm-project/vllm#54311](https://github.com/vllm-project/vllm/issues/54311) [Bug]: Cutlass int8 kernel never declines on SM120, making the Triton int8 fallback unreachable
- [Bug] [vllm-project/vllm#54331](https://github.com/vllm-project/vllm/issues/54331) [Bug]: sm_120 hybrid-GDN NVFP4 dies under sustained load whenever CUDA graphs are on — persists 0.26.0 → 0.28.0, clean on 0.24.0; PIECEWISE and TRITON_ATTN both fail, only enforce_eager survives
- [Bug] [vllm-project/vllm#54349](https://github.com/vllm-project/vllm/issues/54349) [Bug]: [XPU] AWQ MoE selector (check_moe_marlin_supports_config) ignores XPU platform, crashes on Marlin path
- [Bug] [vllm-project/vllm#54350](https://github.com/vllm-project/vllm/issues/54350) [Bug]: [XPU] moe_wna16 AWQ fallback compares CUDA device_capability, always -1 on XPU

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#37128](https://github.com/sgl-project/sglang/issues/37128) [Bug] Spec V2 paths no longer emit speculative-decoding OpenTelemetry spans
- [RFC] [vllm-project/vllm#54333](https://github.com/vllm-project/vllm/issues/54333) [RFC]: Reduced sampling for tensor-parallel decoding
- [Bug] [vllm-project/vllm#54360](https://github.com/vllm-project/vllm/issues/54360) [Bug]: Speculative decoding (mtp and dflash) silently disables prefix-cache hits for hybrid GDN models on nightly; worked on v0.24.0
- [Bug] [vllm-project/vllm#54392](https://github.com/vllm-project/vllm/issues/54392) [Bug]: PD-admitted Mamba request is spec-padded before prefill completes, then align split truncates the 8-token window to 5
- [Feature] [vllm-project/vllm#54414](https://github.com/vllm-project/vllm/issues/54414) [Feature][KV-offloading]: recent-window state groups can never participate in restores — per-group offload exclusion + hit-boundary rollback (GLM-5.3 tail_cache)
- [Bug] [vllm-project/vllm#54425](https://github.com/vllm-project/vllm/issues/54425) [Bug]: V2 sampler warmup misses explicit-seed native path when FlashInfer is enabled

### Scheduler / Batching

- [RFC] [vllm-project/vllm#54363](https://github.com/vllm-project/vllm/issues/54363) [RFC]: Data integrity and I/O liveness for the filesystem KV offload tier
- [Feature] [vllm-project/vllm#54413](https://github.com/vllm-project/vllm/issues/54413) [Feature][KV-offloading]: OffloadingConnector rejects hybrid models whose KV groups have blocks smaller than one hash unit (GLM-5.3-Flash) — per-group blocks_per_chunk implementation attached

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#37097](https://github.com/sgl-project/sglang/issues/37097) [Bug] Pretokenized image requests can crash GLM MRoPE with a stale retokenized mask
- [Feature] [vllm-project/vllm#54340](https://github.com/vllm-project/vllm/issues/54340) [Feature]: In the framework, there are many assert statements. How can we optimize the issue of service processes crashing due to asserts?

### Uncategorized

- [Feature] [vllm-project/vllm#54389](https://github.com/vllm-project/vllm/issues/54389) [Feature]: Tencent/WeMM-Embedding

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#53573](https://github.com/vllm-project/vllm/issues/53573) [Bug]: [PCP+DCP][MLA] Rank-local PCP context metadata causes divergent DCP KV-gather collectives

### Build / Install / Platform

- [Bug] [vllm-project/vllm#53480](https://github.com/vllm-project/vllm/issues/53480) [Bug][XPU]: Silent persistent output corruption (endless "!" / token 0) under sustained concurrent decode on Arc Pro B70, W4A16 27B head_dim 256
- [Bug] [vllm-project/vllm#53481](https://github.com/vllm-project/vllm/issues/53481) [Bug]: FLASHINFER backend produces degenerate output for Mistral3 (Ministral-3-3B) on sm_120 with ANY kv-cache dtype; TRITON_ATTN and FLASH_ATTN correct

### KV Cache / Connector / PD Disagg

- [Feature] [sgl-project/sglang#36083](https://github.com/sgl-project/sglang/issues/36083) [Feature] Extend cross-layer index-topk reuse (dsa_layer_skips_topk) to DeepSeek-V4
- [Bug] [sgl-project/sglang#36140](https://github.com/sgl-project/sglang/issues/36140) [Bug] DFLASH speculative decoding is not supported under PD disaggregation: spec_info None crash, then watchdog self-kill
- [RFC] [vllm-project/vllm#53484](https://github.com/vllm-project/vllm/issues/53484) [RFC]: Generalize Connector Metrics
- [Bug] [vllm-project/vllm#53505](https://github.com/vllm-project/vllm/issues/53505) [Bug]: [SpecDecode] Hybrid Mamba (align) corrupts under speculative decoding when a KV connector is attached — even with zero retrieved tokens
- [Performance] [vllm-project/vllm#53548](https://github.com/vllm-project/vllm/issues/53548) [Performance]: higher Mooncake Store tail latency with all-HCA registration on 4-TP / 4-RNIC hosts
- [Bug] [vllm-project/vllm#53569](https://github.com/vllm-project/vllm/issues/53569) [Bug][KV Offload] OffloadingConnector fs tier: multi-group MLA+DSA (DeepSeek-V4) TP=2 lookup fully misses across restart; single-group MHA hits 99.6%

### New Model Integration

- [Feature] [sgl-project/sglang#36174](https://github.com/sgl-project/sglang/issues/36174) [Feature] Support deterministic inference for DeepSeek-V4

### Performance / Memory / OOM

- [Performance] [vllm-project/vllm#53472](https://github.com/vllm-project/vllm/issues/53472) [Performance]: v0.23→v0.26: ~20% decode ITL regression on non-gated (relu2) BF16 MoE (SM100) — TRTLLM-gen backend swap (#43853) adds per-call host cost; --moe-backend flashinfer_cutlass recovers ~90%

### Quantization

- [Bug] [sgl-project/sglang#36118](https://github.com/sgl-project/sglang/issues/36118) [Bug] Qwen3.8 DFlash2 TTFT regresses 3.1% from db2eb475 to 95f5ecd3 on RTX PRO 6000 Blackwell
- [Bug] [sgl-project/sglang#36181](https://github.com/sgl-project/sglang/issues/36181) [Bug] DSV4 indexer weights_proj CUBLAS_STATUS_EXECUTION_FAILED / cudaErrorIllegalAddress under multi-turn hicache load
- [RFC] [vllm-project/vllm#53563](https://github.com/vllm-project/vllm/issues/53563) [RFC]: SM90 Exact Fused DSA Prefill Indexer

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#53477](https://github.com/vllm-project/vllm/issues/53477) [Bug]: DFLASH2 force reprocesses context every reply
- [Performance] [vllm-project/vllm#53504](https://github.com/vllm-project/vllm/issues/53504) [Performance]: MTP first repeat misses prefix cache on a hybrid Mamba/GDN model

### Scheduler / Batching

- [Bug] [sgl-project/sglang#36179](https://github.com/sgl-project/sglang/issues/36179) [Bug] When using hicache to enable L2/L3 storage in DeepSeek V4, token loop repetition occurs very frequently
- [RFC] [vllm-project/vllm#53485](https://github.com/vllm-project/vllm/issues/53485) [RFC]: Reconcile Backpressure Admission
- [RFC] [vllm-project/vllm#53486](https://github.com/vllm-project/vllm/issues/53486) [RFC]: Secondary Tier Usage Metrics
