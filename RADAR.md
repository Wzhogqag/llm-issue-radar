# LLM Serving Issue Radar

_Last run: 2026-08-03T14:04+00:00_

**26 issues** — sgl-project/sglang: 11, vllm-project/vllm: 15 — 🆕 **25 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 4
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 5

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#33393](https://github.com/sgl-project/sglang/issues/33393) [Bug]  dsv4-flash-0731 watchdog timeout under 0.5.16

### vllm-project/vllm

- [RFC] 🆕 [#50853](https://github.com/vllm-project/vllm/issues/50853) [RFC]: Balance request admission across Model Runner V2 pipeline-parallel batches

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#33385](https://github.com/sgl-project/sglang/issues/33385) [Bug] DeepSeekV4TokenToKVPool (SWA/HiSparse) has no get_cpu_copy() → decode-mode retract crashes with NotImplementedError (offload is unconditional, not gated on --disaggregation-decode-enable-offload-kvcache)
- [RFC] 🆕 [#33394](https://github.com/sgl-project/sglang/issues/33394) [RFC][sgl-router] Recoverable KV Placement State with Snapshots and Event Replay
- [Bug] [#33268](https://github.com/sgl-project/sglang/issues/33268) [Bug] HiCache storage keys omit kv_cache_dtype — silent cross-run cache collisions

### vllm-project/vllm

- [Bug] 🆕 [#50765](https://github.com/vllm-project/vllm/issues/50765) [Bug][P/D]: NIXL handshake failure with asymmetric TP in PD disaggregation (pTP2 + dTP4)

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33283](https://github.com/sgl-project/sglang/issues/33283) [Bug]  sglang hangs before server readiness when launched under Nsight Systems process-tree profiling

### vllm-project/vllm

- [Bug] 🆕 [#50774](https://github.com/vllm-project/vllm/issues/50774) [Bug]: FLASHMLA_SPARSE_DSV4 backend crashes with "swa_metadata missing tile_sched entry for compress_ratio=1" on DeepSeek-V4-Flash-0731

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#50842](https://github.com/vllm-project/vllm/issues/50842) [Bug]: DSpark speculative decoding causes FlashMLA kernel assertion errors on DeepSeek-V4-Pro with both TP=8 and DP=8+EP
- [Bug] 🆕 [#50821](https://github.com/vllm-project/vllm/issues/50821) [Bug]: Native CPU offloading can compute inconsistent num_cpu_blocks across PP ranks
- [Bug] 🆕 [#50772](https://github.com/vllm-project/vllm/issues/50772) [Bug]: --load_format fastsafetensors produces corrupted/incoherent generation for DeepSeek-V4-Flash-0731 with TP+EP (works with default loader)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#33289](https://github.com/sgl-project/sglang/issues/33289) [Bug] Multi-node TP rank-divergence deadlock: one rank wedges in NCCL proxy append (logits all-gather), peer idles at request broadcast — DeepSeek-V4 + DSpark on 2× DGX Spark (GB10)

### vllm-project/vllm

- [Bug] 🆕 [#50877](https://github.com/vllm-project/vllm/issues/50877) [Bug]: DSpark speculative decoding triggers FlashInfer MNNVL allreduce "buffer size insufficient" via draft model's embed_input_ids (TP8, GB200 NVL72)
- [Bug] 🆕 [#50835](https://github.com/vllm-project/vllm/issues/50835) [Bug]: Generation Hang after a while when using RayExecutorV2 cross two nodes with VLLM v0.24.0
- [RFC] 🆕 [#50834](https://github.com/vllm-project/vllm/issues/50834) [RFC]:  Unify the Tensor Type for Device-Pointer Storage to `torch.uint64`

## Sampling / Speculative Decoding

### sgl-project/sglang

- [other] 🆕 [#33383](https://github.com/sgl-project/sglang/issues/33383) [AMD] EAGLE3 spec-decode unsupported for MiniMax-M3: minimax_sparse_backend has no decode-shaped forward path (extend_seq_lens=None)
- [other] 🆕 [#33357](https://github.com/sgl-project/sglang/issues/33357) [Temp][diffusion] model: Support MiniMax-H3 on Ascend A2/A3 Temporary Quick-Start Guide

### vllm-project/vllm

- [Bug] 🆕 [#50837](https://github.com/vllm-project/vllm/issues/50837) [Bug]: Qwen3.5 DFlash speculative decoding produces repetitive/degenerate output
- [Bug] 🆕 [#50767](https://github.com/vllm-project/vllm/issues/50767) [Bug]: override-generation-config silently ignores presence_penalty / frequency_penalty (missing from available_params whitelist)

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#33356](https://github.com/sgl-project/sglang/issues/33356) [Bug] DSpark large decode CUDA-Graph capture can hit non-deterministic illegal memory on TP8 (v0.5.16)
- [Feature] 🆕 [#33322](https://github.com/sgl-project/sglang/issues/33322) [Feature]  Make diffusion LLM serving usable for RL rollout and high-throughput workloads

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#33360](https://github.com/sgl-project/sglang/issues/33360) [Bug] DeepSeek-V4-Flash-0731 abnormal accuracy output when dp < tp

### vllm-project/vllm

- [Bug] 🆕 [#50850](https://github.com/vllm-project/vllm/issues/50850) [Bug]: Qwen/Qwen3.6-35B-A3B and Qwen/Qwen3.6-35B-A3B-FP8 issue while inferencing on Intel XPU (4xB70)
- [Bug] 🆕 [#50780](https://github.com/vllm-project/vllm/issues/50780) [Bug]: CUDA graph memory profiler charges an mnbt-linear profiling transient as "graph memory" → KV cache pool −18–24% on hybrid GDN models since v0.26.0 (the real FULL graphs cost ~24 MiB each)
- [Bug] 🆕 [#50773](https://github.com/vllm-project/vllm/issues/50773) [Bug]: fuse_norm_quant/fuse_act_quant custom fusions produce garbled token output on SM120 (GB10) for DeepSeek-V4-Flash-0731
- [Bug] 🆕 [#50768](https://github.com/vllm-project/vllm/issues/50768) [Bug]: Responses API Returns Raw Malformed Kimi Tool Marker as Assistant Text Instead of function_call
