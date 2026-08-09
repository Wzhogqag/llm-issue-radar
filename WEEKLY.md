# Weekly Trends — 2026-08-09

Window: 2026-08-03 → 2026-08-09 (7 snapshots)

**Totals:** 26 → 16  (16 appeared, 26 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 2 | 1 | -1 | 1 | 2 |
| Build / Install / Platform | 5 | 2 | -3 | 2 | 5 |
| Distributed / TP / PP / EP | 4 | 2 | -2 | 2 | 4 |
| KV Cache / Connector / PD Disagg | 4 | 1 | -3 | 1 | 4 |
| New Model Integration | 0 | 2 | +2 | 2 | 0 |
| Performance / Memory / OOM | 2 | 0 | -2 | 0 | 2 |
| Quantization | 3 | 5 | +2 | 5 | 3 |
| Sampling / Speculative Decoding | 4 | 2 | -2 | 2 | 4 |
| Scheduler / Batching | 2 | 0 | -2 | 0 | 2 |
| Serving / OpenAI API / Streaming | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#34111](https://github.com/sgl-project/sglang/issues/34111) [Bug] A cancelled grammar-constrained overlap request can still emit visible text before abort

### Build / Install / Platform

- [Bug] [vllm-project/vllm#51467](https://github.com/vllm-project/vllm/issues/51467) [Bug]: DeepSeek-V4-Flash-0731 `response_format` (structured output) crashes the vLLM EngineCore — `apply_grammar_bitmask` tensor size mismatch (4040 vs 4041)
- [no-prefix] [vllm-project/vllm#51521](https://github.com/vllm-project/vllm/issues/51521) DeepSeek-V4 (deepseek_v4): fused topk_softplus_sqrt router rejects non-standard expert counts on CUDA (REAP 144-expert ckpts); torch fallback is XPU-gated

### Distributed / TP / PP / EP

- [RFC] [vllm-project/vllm#51513](https://github.com/vllm-project/vllm/issues/51513) [RFC]: Unify functional P2P gating — one veto-only verdict for all P2P consumers (NCCL, custom allreduce, symm-mem)
- [other] [vllm-project/vllm#51533](https://github.com/vllm-project/vllm/issues/51533) [Installation]: Worker processes hang in CPU deadloop after NCCL initialization when loading DeepSeek-V4-Flash-0731 with vLLM V1 engine on H100

### KV Cache / Connector / PD Disagg

- [no-prefix] [vllm-project/vllm#51518](https://github.com/vllm-project/vllm/issues/51518) MooncakeConnector P/D: NVLink fallback transfer fails "Requested address not found" (fp8 MLA, v0.25.0)

### New Model Integration

- [other] [vllm-project/vllm#51497](https://github.com/vllm-project/vllm/issues/51497) [New Model]: nvidia/LocateAnything-3B (slow autoregressive mode first)
- [no-prefix] [vllm-project/vllm#51522](https://github.com/vllm-project/vllm/issues/51522) deepseek_v4: decode runs unfused (breakable CUDA graph) — DeepseekV4ForCausalLM lacks @support_torch_compile; fullgraph capture blocked by inline deep_gemm/tilelang pybinds

### Quantization

- [Bug] [sgl-project/sglang#34155](https://github.com/sgl-project/sglang/issues/34155) [Bug] 1M-token prefill kills the engine with CUDA OOM in DSV4 indexer fp8_mqa_logits (nonpaged path) under --tp 8 + MegaMoE on 8x B200 (v0.5.17); equivalent request serves under tp8/dp8 dp-attention
- [Performance] [vllm-project/vllm#51454](https://github.com/vllm-project/vllm/issues/51454) [Performance] DP8 vs TP8 for single-KV-head MLA: 7.7x KV, 3.4x faster 1M TTFT at c=8 (DeepSeek-V4-Flash-0731, 8x B200, vLLM v0.25.0)
- [Bug] [vllm-project/vllm#51456](https://github.com/vllm-project/vllm/issues/51456) [Bug]: online FP8 (--quantization fp8) produces corrupted, non-EOS-terminating output on Qwen2.5-1.5B-Instruct
- [Performance] [vllm-project/vllm#51494](https://github.com/vllm-project/vllm/issues/51494) [Performance] MiniMax-M3-NVFP4 on 8x B200, first numbers after the #48929 correctness fix: 1M real-prose envelope, EAGLE3 2.1-2.3x decode
- [other] [vllm-project/vllm#51541](https://github.com/vllm-project/vllm/issues/51541) [ROCm][AITER] Port FlyDSL int4 MoE integration to AITER fused_moe API

### Sampling / Speculative Decoding

- [RFC] [vllm-project/vllm#51472](https://github.com/vllm-project/vllm/issues/51472) [RFC] Raw multimodal input for /generate endpoint (RL workloads)
- [Bug] [vllm-project/vllm#51510](https://github.com/vllm-project/vllm/issues/51510) [Bug][Spec Decode] MRV2 AutoRegressiveSpeculator ignores dynamic K from scheduler — DSD non-functional on MRV2

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#51465](https://github.com/vllm-project/vllm/issues/51465) [Bug]: Kimi K3 usage.prompt_tokens over-counts trailing channel-open stub (+3)

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [sgl-project/sglang#33283](https://github.com/sgl-project/sglang/issues/33283) [Bug]  sglang hangs before server readiness when launched under Nsight Systems process-tree profiling
- [Bug] [vllm-project/vllm#50774](https://github.com/vllm-project/vllm/issues/50774) [Bug]: FLASHMLA_SPARSE_DSV4 backend crashes with "swa_metadata missing tile_sched entry for compress_ratio=1" on DeepSeek-V4-Flash-0731

### Build / Install / Platform

- [Bug] [sgl-project/sglang#33360](https://github.com/sgl-project/sglang/issues/33360) [Bug] DeepSeek-V4-Flash-0731 abnormal accuracy output when dp < tp
- [Bug] [vllm-project/vllm#50768](https://github.com/vllm-project/vllm/issues/50768) [Bug]: Responses API Returns Raw Malformed Kimi Tool Marker as Assistant Text Instead of function_call
- [Bug] [vllm-project/vllm#50773](https://github.com/vllm-project/vllm/issues/50773) [Bug]: fuse_norm_quant/fuse_act_quant custom fusions produce garbled token output on SM120 (GB10) for DeepSeek-V4-Flash-0731
- [Bug] [vllm-project/vllm#50780](https://github.com/vllm-project/vllm/issues/50780) [Bug]: CUDA graph memory profiler charges an mnbt-linear profiling transient as "graph memory" → KV cache pool −18–24% on hybrid GDN models since v0.26.0 (the real FULL graphs cost ~24 MiB each)
- [Bug] [vllm-project/vllm#50850](https://github.com/vllm-project/vllm/issues/50850) [Bug]: Qwen/Qwen3.6-35B-A3B and Qwen/Qwen3.6-35B-A3B-FP8 issue while inferencing on Intel XPU (4xB70)

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#33289](https://github.com/sgl-project/sglang/issues/33289) [Bug] Multi-node TP rank-divergence deadlock: one rank wedges in NCCL proxy append (logits all-gather), peer idles at request broadcast — DeepSeek-V4 + DSpark on 2× DGX Spark (GB10)
- [RFC] [vllm-project/vllm#50834](https://github.com/vllm-project/vllm/issues/50834) [RFC]:  Unify the Tensor Type for Device-Pointer Storage to `torch.uint64`
- [Bug] [vllm-project/vllm#50835](https://github.com/vllm-project/vllm/issues/50835) [Bug]: Generation Hang after a while when using RayExecutorV2 cross two nodes with VLLM v0.24.0
- [Bug] [vllm-project/vllm#50877](https://github.com/vllm-project/vllm/issues/50877) [Bug]: DSpark speculative decoding triggers FlashInfer MNNVL allreduce "buffer size insufficient" via draft model's embed_input_ids (TP8, GB200 NVL72)

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#33268](https://github.com/sgl-project/sglang/issues/33268) [Bug] HiCache storage keys omit kv_cache_dtype — silent cross-run cache collisions
- [Bug] [sgl-project/sglang#33385](https://github.com/sgl-project/sglang/issues/33385) [Bug] DeepSeekV4TokenToKVPool (SWA/HiSparse) has no get_cpu_copy() → decode-mode retract crashes with NotImplementedError (offload is unconditional, not gated on --disaggregation-decode-enable-offload-kvcache)
- [RFC] [sgl-project/sglang#33394](https://github.com/sgl-project/sglang/issues/33394) [RFC][sgl-router] Recoverable KV Placement State with Snapshots and Event Replay
- [Bug] [vllm-project/vllm#50765](https://github.com/vllm-project/vllm/issues/50765) [Bug][P/D]: NIXL handshake failure with asymmetric TP in PD disaggregation (pTP2 + dTP4)

### Performance / Memory / OOM

- [Feature] [sgl-project/sglang#33322](https://github.com/sgl-project/sglang/issues/33322) [Feature]  Make diffusion LLM serving usable for RL rollout and high-throughput workloads
- [Bug] [sgl-project/sglang#33356](https://github.com/sgl-project/sglang/issues/33356) [Bug] DSpark large decode CUDA-Graph capture can hit non-deterministic illegal memory on TP8 (v0.5.16)

### Quantization

- [Bug] [vllm-project/vllm#50772](https://github.com/vllm-project/vllm/issues/50772) [Bug]: --load_format fastsafetensors produces corrupted/incoherent generation for DeepSeek-V4-Flash-0731 with TP+EP (works with default loader)
- [Bug] [vllm-project/vllm#50821](https://github.com/vllm-project/vllm/issues/50821) [Bug]: Native CPU offloading can compute inconsistent num_cpu_blocks across PP ranks
- [Bug] [vllm-project/vllm#50842](https://github.com/vllm-project/vllm/issues/50842) [Bug]: DSpark speculative decoding causes FlashMLA kernel assertion errors on DeepSeek-V4-Pro with both TP=8 and DP=8+EP

### Sampling / Speculative Decoding

- [other] [sgl-project/sglang#33357](https://github.com/sgl-project/sglang/issues/33357) [Temp][diffusion] model: Support MiniMax-H3 on Ascend A2/A3 Temporary Quick-Start Guide
- [other] [sgl-project/sglang#33383](https://github.com/sgl-project/sglang/issues/33383) [AMD] EAGLE3 spec-decode unsupported for MiniMax-M3: minimax_sparse_backend has no decode-shaped forward path (extend_seq_lens=None)
- [Bug] [vllm-project/vllm#50767](https://github.com/vllm-project/vllm/issues/50767) [Bug]: override-generation-config silently ignores presence_penalty / frequency_penalty (missing from available_params whitelist)
- [Bug] [vllm-project/vllm#50837](https://github.com/vllm-project/vllm/issues/50837) [Bug]: Qwen3.5 DFlash speculative decoding produces repetitive/degenerate output

### Scheduler / Batching

- [Bug] [sgl-project/sglang#33393](https://github.com/sgl-project/sglang/issues/33393) [Bug]  dsv4-flash-0731 watchdog timeout under 0.5.16
- [RFC] [vllm-project/vllm#50853](https://github.com/vllm-project/vllm/issues/50853) [RFC]: Balance request admission across Model Runner V2 pipeline-parallel batches
