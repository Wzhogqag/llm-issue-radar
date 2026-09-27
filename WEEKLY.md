# Weekly Trends — 2026-09-27

Window: 2026-09-21 → 2026-09-27 (7 snapshots)

**Totals:** 15 → 13  (13 appeared, 15 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 2 | +1 | 2 | 1 |
| Build / Install / Platform | 1 | 4 | +3 | 4 | 1 |
| Distributed / TP / PP / EP | 1 | 2 | +1 | 2 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 0 | -2 | 0 | 2 |
| New Model Integration | 1 | 0 | -1 | 0 | 1 |
| Performance / Memory / OOM | 3 | 0 | -3 | 0 | 3 |
| Quantization | 3 | 1 | -2 | 1 | 3 |
| Sampling / Speculative Decoding | 3 | 2 | -1 | 2 | 3 |
| Scheduler / Batching | 0 | 1 | +1 | 1 | 0 |
| Serving / OpenAI API / Streaming | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Attention Backend

- [other] [vllm-project/vllm#58858](https://github.com/vllm-project/vllm/issues/58858) [Question][ROCm] GLM-5.3-Flash kpool indexer: does the 640-token block table reach 32-pool pages on gfx942/gfx950 too?
- [Feature] [vllm-project/vllm#58882](https://github.com/vllm-project/vllm/issues/58882) [Feature]: Allow LBNHC/NHD for ROCM_AITER_UNIFIED_ATTN where supported

### Build / Install / Platform

- [no-prefix] [sgl-project/sglang#41385](https://github.com/sgl-project/sglang/issues/41385) EvalPort: portable interchange for BenchmarkResult
- [Performance] [vllm-project/vllm#58804](https://github.com/vllm-project/vllm/issues/58804) [Performance][Bug]: Tiered Offloading
- [Performance] [vllm-project/vllm#58849](https://github.com/vllm-project/vllm/issues/58849) [Performance]: WSL2: `VLLM_WSL2_ENABLE_PIN_MEMORY=1` makes the default V2 runner ~12% faster per decode step
- [Bug] [vllm-project/vllm#58902](https://github.com/vllm-project/vllm/issues/58902) [Bug]: Qwen3-Omni: M-RoPE positions silently misaligned for every multimodal request (offset double-counts the modality-start token)

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#41449](https://github.com/sgl-project/sglang/issues/41449) [Bug] DSpark + TP: grammar-constrained request batched with any other request deadlocks all ranks (overlap and non-overlap), GPUs spin in a collective
- [Bug] [vllm-project/vllm#58850](https://github.com/vllm-project/vllm/issues/58850) [Bug]: Intermittent Xid 31 MMU fault in pynccl all_reduce during CUDA graph

### Quantization

- [Performance] [vllm-project/vllm#58799](https://github.com/vllm-project/vllm/issues/58799) [Performance]: Suboptimal SM90 FP8 CUTLASS MoE dispatch on H20 EP8 — upstream fix proposed

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#41351](https://github.com/sgl-project/sglang/issues/41351) [Bug] Potential hybrid GDN Radix-cache selected-logprob drift on repeated branch scoring
- [Bug] [vllm-project/vllm#58899](https://github.com/vllm-project/vllm/issues/58899) [Bug]: Greedy output changes between restarts, also with VLLM_BATCH_INVARIANT=1: the q/k-norm + RoPE combo kernel picks its reduction config by timing

### Scheduler / Batching

- [Bug] [sgl-project/sglang#41372](https://github.com/sgl-project/sglang/issues/41372) [Bug]: scheduler Req.decoded_text is never written: dead stop-string fallback at schedule_batch.py:1846 and empty DecodeStatus seed on eviction re-init

### Serving / OpenAI API / Streaming

- [other] [sgl-project/sglang#41363](https://github.com/sgl-project/sglang/issues/41363) [CI] ltx_2_3_hq_pipeline perf checks fail on most diffusion PRs (load / decode / denoise variance)

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#57932](https://github.com/vllm-project/vllm/issues/57932) [Bug]: SM120 / RTX PRO 6000 Blackwell: GLM-5.3-Flash fails with FlashInfer attention backend

### Build / Install / Platform

- [Bug] [vllm-project/vllm#57927](https://github.com/vllm-project/vllm/issues/57927) [Bug]: Chunked embeddings break dot-product scoring with `use_activation=true

### Distributed / TP / PP / EP

- [Feature] [vllm-project/vllm#57837](https://github.com/vllm-project/vllm/issues/57837) [Feature]: [WideEP][CPU]: Add a CPU-only Wide Expert Parallelism well-lit path

### KV Cache / Connector / PD Disagg

- [RFC] [sgl-project/sglang#40522](https://github.com/sgl-project/sglang/issues/40522) [RFC] Decouple the SWA sidecar page size from the full-attention page size (DSv4, Hybrid Models)
- [Bug] [vllm-project/vllm#57938](https://github.com/vllm-project/vllm/issues/57938) [Bug]: AssertionError in _update_from_kv_xfer_finished when LMCache KV load fails on heterogeneous attention models

### New Model Integration

- [Bug] [vllm-project/vllm#57839](https://github.com/vllm-project/vllm/issues/57839) [Bug] [watermarking]: reference detection server does not support dual_key_gumbel; detector alpha default disagrees with generation default

### Performance / Memory / OOM

- [Bug] [sgl-project/sglang#40562](https://github.com/sgl-project/sglang/issues/40562) [Bug][Diffusion] Warmup request finalization reloads offloaded components and triggers OOM on Wan2.2 A14B
- [Bug] [vllm-project/vllm#57890](https://github.com/vllm-project/vllm/issues/57890) [Bug]: HunYuan Dense V1 fails CUDA graph capture on v0.29 — HF dynamic RoPE does a host-side sync during capture
- [Bug] [vllm-project/vllm#57936](https://github.com/vllm-project/vllm/issues/57936) [Bug]: --kv-cache-memory suggestion double-counts CUDAGraph memory (regression of #37426, reintroduced by #49208)

### Quantization

- [Bug] [sgl-project/sglang#40558](https://github.com/sgl-project/sglang/issues/40558) [Bug] sm_120 - tvm.error.InternalError: Error in function 'TllmGenFmhaRunner' at sglang/lib/python3.12/site-packages/flashinfer/data/include/flashinfer/trtllm/fmha/fmhaRunner.cuh:37: Unsupported architecture
- [Bug] [vllm-project/vllm#57838](https://github.com/vllm-project/vllm/issues/57838) [Bug]: RowWiseTorchFP8ScaledMMLinearKernel is selected on RDNA4 (gfx1201) from v0.28 and costs 5-24% decode
- [RFC] [vllm-project/vllm#57895](https://github.com/vllm-project/vllm/issues/57895) [RFC]: Stable runtime tensor lifecycle for sleep and live weight reload

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#57929](https://github.com/vllm-project/vllm/issues/57929) [Bug]: `/v1/completions/derender` drops requested `prompt_logprobs`
- [Bug] [vllm-project/vllm#57935](https://github.com/vllm-project/vllm/issues/57935) [Bug]: `/v1/chat/completions/batch` leaks hidden reasoning through logprobs and token IDs when `include_reasoning=false`
- [Bug] [vllm-project/vllm#57941](https://github.com/vllm-project/vllm/issues/57941) [Bug]: Spec decode hits illegal memory access when the draft model's context is shorter than the target's
