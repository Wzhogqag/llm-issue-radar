# Weekly Trends — 2026-07-19

Window: 2026-07-14 → 2026-07-19 (11 snapshots)

**Totals:** 27 → 19  (19 appeared, 27 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 0 | 1 | +1 | 1 | 0 |
| Build / Install / Platform | 4 | 0 | -4 | 0 | 4 |
| Distributed / TP / PP / EP | 2 | 1 | -1 | 1 | 2 |
| KV Cache / Connector / PD Disagg | 3 | 3 | 0 | 3 | 3 |
| New Model Integration | 1 | 0 | -1 | 0 | 1 |
| Performance / Memory / OOM | 1 | 1 | 0 | 1 | 1 |
| Quantization | 9 | 10 | +1 | 10 | 9 |
| Sampling / Speculative Decoding | 3 | 2 | -1 | 2 | 3 |
| Scheduler / Batching | 2 | 1 | -1 | 1 | 2 |
| Serving / OpenAI API / Streaming | 2 | 0 | -2 | 0 | 2 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#31594](https://github.com/sgl-project/sglang/issues/31594) [Bug] [AMD] Qwen3.5 GatedDeltaNet + dp-attention on ROCm/MoRI: HIP "invalid configuration argument" (linear-attn/Mamba state path); process hangs in chunk_gated_delta_rule_fwd under kernel serialization

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#49004](https://github.com/vllm-project/vllm/issues/49004) [Bug]: DBRX MoE weight loading crashes with KeyError after FusedMoE/MoERunner inversion refactor (#41184) — dbrx.py missed by follow-up fix #45054

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#31640](https://github.com/sgl-project/sglang/issues/31640) [Bug] FA4 decode passes unsupported descale tensors on FP8 nemotron_h; forward_decode lacks the FA4 guard used by forward_extend
- [Bug] [vllm-project/vllm#49049](https://github.com/vllm-project/vllm/issues/49049) [Bug] Inkling on sm_121a (GB10): unclamped q-row in rel-bias score-mod gather causes deterministic illegal address (coredump evidence); + aux-stream KV-write race in fused_qkvr_prep
- [other] [vllm-project/vllm#49064](https://github.com/vllm-project/vllm/issues/49064) [Usability] Engine fails to start when available Mamba cache blocks < max_num_seqs (hybrid models + LoRA) — suggest auto-clamping with a warning

### Performance / Memory / OOM

- [Perf] [vllm-project/vllm#49013](https://github.com/vllm-project/vllm/issues/49013) [Perf] ~2x decode throughput regression for structured outputs since #45424: apply_grammar_bitmask staging rewrite (bisected to commit, file, and hunk)

### Quantization

- [Bug] [sgl-project/sglang#31600](https://github.com/sgl-project/sglang/issues/31600) [Bug] glm-5.2-w4afp8 +l2(hicache)+l3(mooncake) kvcache dram cluster ,cache hit is slower than prefill+ decoder
- [Bug] [vllm-project/vllm#49005](https://github.com/vllm-project/vllm/issues/49005) [Bug]: Minimax MSA - AttributeError: module 'cutlass.cute.core' has no attribute 'ThrMma'
- [Bug] [vllm-project/vllm#49010](https://github.com/vllm-project/vllm/issues/49010) [Bug]: XQA decode under FULL cudagraph capture silently corrupts attention output (fp8 and nvfp4 KV)
- [Feature] [vllm-project/vllm#49011](https://github.com/vllm-project/vllm/issues/49011) [Feature]: nvfp4 KV cache on SM120 — flashinfer ships the kernels, vLLM isn't wired to them (working prototype, 245K ctx on a 5090)
- [Bug] [vllm-project/vllm#49012](https://github.com/vllm-project/vllm/issues/49012) [Bug]: nvfp4 reshape_and_cache_flash assumes NHD layout — silently mis-swizzles HND caches when num_kv_heads % 4 == 0
- [Bug] [vllm-project/vllm#49031](https://github.com/vllm-project/vllm/issues/49031) [Bug]:  FlashInfer B12x W4A16 runtime repacking retains original and packed MoE weights, causing startup OOM
- [Bug] [vllm-project/vllm#49070](https://github.com/vllm-project/vllm/issues/49070) [Bug]: MiniMax-M3 NVFP4 produces garbage output + CUDA illegal memory access on Hopper (sm90) via Marlin FP4-MoE
- [Bug] [vllm-project/vllm#49076](https://github.com/vllm-project/vllm/issues/49076) [Bug]:  --linear-backend=flashinfer_b12x crashes on Qwen3.6-35B-A3B-NVFP4 — no kernel for FP8-quantized GDN QKVZ layer
- [Bug] [vllm-project/vllm#49079](https://github.com/vllm-project/vllm/issues/49079) [Bug]: --moe-backend flashinfer_b12x roughly doubles peak activation memory vs default, cutting available KV cache ~55%
- [RFC] [vllm-project/vllm#49090](https://github.com/vllm-project/vllm/issues/49090) [RFC][SpecDecode] Move MTP completeness validation to the weight-update transaction boundary

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#31711](https://github.com/sgl-project/sglang/issues/31711) [Bug] XGrammar rollback copies the full token history during EAGLE constrained decoding
- [Bug] [vllm-project/vllm#49002](https://github.com/vllm-project/vllm/issues/49002) [Bug]: Speculative Decoding + Structured Output（tool call）组合下，decode 阶段出现秒级卡顿

### Scheduler / Batching

- [Bug] [vllm-project/vllm#49089](https://github.com/vllm-project/vllm/issues/49089) [Bug]: assert req_id in self.requests in Scheduler._update_from_kv_xfer_finished kills the engine on late KV xfer-finished for an already-failed request

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [Bug] [vllm-project/vllm#48486](https://github.com/vllm-project/vllm/issues/48486) [Bug]: Hang in CUDA Graph replay with PyTorch symmetric-memory all-reduce when profiling with Nsight Systems
- [Bug] [vllm-project/vllm#48518](https://github.com/vllm-project/vllm/issues/48518) [Bug]: Performance regression caused by high-priority L2 Cache Data Persisting from Server Startup
- [RFC] [vllm-project/vllm#48540](https://github.com/vllm-project/vllm/issues/48540) [RFC]: manylinux compatibility baseline for aarch64 binary dependencies
- [Bug] [vllm-project/vllm#48541](https://github.com/vllm-project/vllm/issues/48541) [Bug]: FlashInfer CUTLASS MoE selected on fp4-less builds (CUDA toolkit < 12.8); gpt-oss dies at engine start

### Distributed / TP / PP / EP

- [no-prefix] [sgl-project/sglang#31116](https://github.com/sgl-project/sglang/issues/31116) DP attention + prefill CUDA graph + return_routed_experts (gated path): two fixes ready — is enabling it wanted?
- [Bug] [sgl-project/sglang#31133](https://github.com/sgl-project/sglang/issues/31133) [Bug] MiniMax sparse prefill: OOB GPU write when max_seqlen_k < seq_lens.max() (silent topk corruption / Xid 31 / NCCL watchdog kills)

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#48489](https://github.com/vllm-project/vllm/issues/48489) [Bug]: Deferred block-free path loses per-group eviction ordering for hybrid KV cache configs
- [RFC] [vllm-project/vllm#48501](https://github.com/vllm-project/vllm/issues/48501) [RFC]: Session-centric KV-cache orchestration over typed session identity
- [RFC] [vllm-project/vllm#48504](https://github.com/vllm-project/vllm/issues/48504) [RFC]: Read-only NIXL GDS connector for filesystem KV-cache loads

### New Model Integration

- [Feature] [sgl-project/sglang#31127](https://github.com/sgl-project/sglang/issues/31127) [Feature] any plan to support suffix decoding?

### Performance / Memory / OOM

- [Bug] [sgl-project/sglang#31046](https://github.com/sgl-project/sglang/issues/31046) [Bug] [Regression] DeepSeek-V4 serving crashes with ValueError: Unrecognized configuration class _DeepseekV4ConfigAlias in v0.5.15 (Works in v0.5.14)

### Quantization

- [Bug] [sgl-project/sglang#31045](https://github.com/sgl-project/sglang/issues/31045) [Bug] glm-5.2-w4afp8 with sglang0.5.15 error
- [Bug] [sgl-project/sglang#31093](https://github.com/sgl-project/sglang/issues/31093) [Bug] GLM-5.2 NVFP4 + EAGLE: CUDA illegal memory access during decode CUDA-graph capture on v0.5.15 and main (works on 2026-07-03 dev-glm52-nvfp4)
- [Bug] [sgl-project/sglang#31120](https://github.com/sgl-project/sglang/issues/31120) [Bug] Significant Performance Degradation of Qwen3.5-4B on RTX 5090
- [Bug] [vllm-project/vllm#48477](https://github.com/vllm-project/vllm/issues/48477) [Bug]: Qwen3.5-122B-A10B-FP8 serve crashes on nightly/0.25 (CUBLAS_STATUS_EXECUTION_FAILED at profile_run); no version serves FP8 hybrid GDN + DFlash together
- [RFC] [vllm-project/vllm#48480](https://github.com/vllm-project/vllm/issues/48480) [RFC]: Make Triton kernel unit tests hardware-agnostic and cover untested kernels
- [Bug] [vllm-project/vllm#48491](https://github.com/vllm-project/vllm/issues/48491) [Bug]: cuBLAS NVFP4 GEMM silently rejects M < 128, impacts speech model decode
- [Bug] [vllm-project/vllm#48493](https://github.com/vllm-project/vllm/issues/48493) [Bug]: `SWIGLUOAI_UNINTERLEAVE requires clamp_limit` blocks MiniMax-M3 AWQ/GPTQ INT4
- [Bug] [vllm-project/vllm#48508](https://github.com/vllm-project/vllm/issues/48508) [Bug]: humming is_layer_skipped ignores compressed-tensors "re:" patterns (ignored layers get quantized; real vs dummy load diverge)
- [Bug] [vllm-project/vllm#48590](https://github.com/vllm-project/vllm/issues/48590) [Bug]: LoRA `lora_expand` Triton kernel outputs NaN on Hopper (sm_90) with `block_n=128`, producing garbled LoRA output

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#31071](https://github.com/sgl-project/sglang/issues/31071) [Bug] EAGLE greedy verify lacks TP broadcast → ranks diverge on accepted tokens → collective deadlock (tp>1)
- [Bug] [vllm-project/vllm#48494](https://github.com/vllm-project/vllm/issues/48494) [Bug][Spec Decode] num_speculative_tokens_per_batch_size + MTP speculator fails full CUDA graph decode capture (InputBatch.make_dummy assert)
- [Bug] [vllm-project/vllm#48503](https://github.com/vllm-project/vllm/issues/48503) [Bug]: Gemma 4 MTP speculative decoding crashes during CUDA graph capture (`_suppress_token_ids` is a Python list, not a device tensor)

### Scheduler / Batching

- [RFC] [vllm-project/vllm#48478](https://github.com/vllm-project/vllm/issues/48478) [RFC] Fail-Closed Graph Storage Contract for Weight Reload
- [RFC] [vllm-project/vllm#48485](https://github.com/vllm-project/vllm/issues/48485) [RFC]: Waiting-Queue-Informed LRU for Prefix Cache Eviction

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#31084](https://github.com/sgl-project/sglang/issues/31084) [Bug] Dynamic LoRA loading is effectively unsupported with --tokenizer-worker-num > 1 (per-worker registry, no cross-worker sync)
- [Bug] [sgl-project/sglang#31103](https://github.com/sgl-project/sglang/issues/31103) [Bug] qwen3.6-35b-a3b-fp8 still error with sglang 0.5.15
