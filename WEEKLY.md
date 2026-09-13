# Weekly Trends — 2026-09-13

Window: 2026-09-07 → 2026-09-13 (7 snapshots)

**Totals:** 22 → 10  (10 appeared, 22 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 4 | 1 | -3 | 1 | 4 |
| Build / Install / Platform | 1 | 1 | 0 | 1 | 1 |
| Distributed / TP / PP / EP | 1 | 0 | -1 | 0 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 3 | +1 | 3 | 2 |
| New Model Integration | 3 | 0 | -3 | 0 | 3 |
| Quantization | 6 | 3 | -3 | 3 | 6 |
| Scheduler / Batching | 2 | 1 | -1 | 1 | 2 |
| Serving / OpenAI API / Streaming | 3 | 1 | -2 | 1 | 3 |

## Appeared this week

### Attention Backend

- [no-prefix] [sgl-project/sglang#39299](https://github.com/sgl-project/sglang/issues/39299) MoE deferred finalize is unreachable for models that supply their own routing (FLASHINFER_TRTLLM_ROUTED excluded)

### Build / Install / Platform

- [Bug] [vllm-project/vllm#56696](https://github.com/vllm-project/vllm/issues/56696) [Bug]: --otlp-traces-endpoint initializes tracer but never sends spans (instrument_otel/manual_instrument_otel never invoked)

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#39302](https://github.com/sgl-project/sglang/issues/39302) [Bug] GLM-5.x NoPE MLA (qk_rope_head_dim=0) cannot run on SM120: every DSA sparse-MLA backend is unavailable
- [Bug] [vllm-project/vllm#56699](https://github.com/vllm-project/vllm/issues/56699) [Bug][HiSparse] Decode engine dies with cudaErrorLaunchFailure in the host-mirror path under sustained P/D host imports
- [RFC] [vllm-project/vllm#56701](https://github.com/vllm-project/vllm/issues/56701) [RFC][KV Offload]: Align sliding-window restore coverage with MTP-retained history

### Quantization

- [Bug] [sgl-project/sglang#39226](https://github.com/sgl-project/sglang/issues/39226) [Bug] --moe-runner-backend deep_gemm accepted for DSV4.1 MXFP4 experts, then fails in CUDA graph capture (layout.hpp:108, sm_121)
- [Performance] [vllm-project/vllm#56684](https://github.com/vllm-project/vllm/issues/56684) [Performance]: 3.4 s engine stalls from DeepGEMM compiling the o-projection kernel per prefill chunk size, DeepSeek-V4.1-Flash on 8x B200
- [other] [vllm-project/vllm#56700](https://github.com/vllm-project/vllm/issues/56700) [SM120] Field report: running DeepSeek-V4.1-Flash end-to-end on 8x RTX PRO 6000 — pitfall map + working configuration (1M context verified)

### Scheduler / Batching

- [RFC] [sgl-project/sglang#39192](https://github.com/sgl-project/sglang/issues/39192) [RFC] Contention-aware batching for dynamic EPLB expert migration

### Serving / OpenAI API / Streaming

- [RFC] [vllm-project/vllm#56581](https://github.com/vllm-project/vllm/issues/56581) [RFC]: Streaming prompt prefill for overlapping upstream generation and downstream prefill

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#55636](https://github.com/vllm-project/vllm/issues/55636) [Bug] DeepSeek V4 sparse MLA can index a nonexistent block-table row during CUDA-graph warmup
- [RFC] [vllm-project/vllm#55697](https://github.com/vllm-project/vllm/issues/55697) [RFC]: Application-Directed Prefix Checkpoints for Mamba / Hybrid Prefix Caching
- [Bug] [vllm-project/vllm#55720](https://github.com/vllm-project/vllm/issues/55720) [Bug]: `fuse_rope_kvcache` / `fuse_qk_norm_rope_kvcache` silently register zero patterns on MLA-only models, but their side effects are still paid
- [Bug] [vllm-project/vllm#55722](https://github.com/vllm-project/vllm/issues/55722) [Bug]: `fuse_attn_quant` without `use_inductor_graph_partition` drops all piecewise cudagraphs on backends that cannot do FULL (-38 % on ROCm sparse MLA)

### Build / Install / Platform

- [Bug] [vllm-project/vllm#55689](https://github.com/vllm-project/vllm/issues/55689) [Bug]: GLM-5.3-Flash produces repetitive / off‑topic outputs in PD‑disaggregated deployment

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#55632](https://github.com/vllm-project/vllm/issues/55632) [Bug][ROCm] 15s EngineCore cleanup grace is defeated by MultiprocExecutor's 9s worker-kill budget; workers SIGKILLed mid-teardown

### KV Cache / Connector / PD Disagg

- [Feature] [vllm-project/vllm#55635](https://github.com/vllm-project/vllm/issues/55635) [Feature]: EFA vLLM image should work out of the box on AWS NVIDIA GPUs
- [Bug] [vllm-project/vllm#55729](https://github.com/vllm-project/vllm/issues/55729) [Bug][MooncakeConnector] Bootstrap registration timeout is fatal during slow rank-0 initialization

### New Model Integration

- [Bug] [sgl-project/sglang#38291](https://github.com/sgl-project/sglang/issues/38291) [Bug] `fp8e4nv` not supported on A100 (SM80) when serving Qwen3.8-Flash-Next-FP8
- [RFC] [sgl-project/sglang#38334](https://github.com/sgl-project/sglang/issues/38334) [RFC] Gluon MegaMoE: SGLang Integration and Multi-Node Support
- [Feature] [vllm-project/vllm#55683](https://github.com/vllm-project/vllm/issues/55683) [Feature]: LoRA support for deepseek v4 flash vision

### Quantization

- [no-prefix] [sgl-project/sglang#38300](https://github.com/sgl-project/sglang/issues/38300) TP2 hang with HiCache, breakable prefill CUDA graphs, and FlashInfer MNNVL on B300
- [other] [sgl-project/sglang#38312](https://github.com/sgl-project/sglang/issues/38312) [Playground] Verified cell: h100 / flash-official / fp4 / high-throughput / single
- [Bug] [vllm-project/vllm#55644](https://github.com/vllm-project/vllm/issues/55644) [Bug]: GLM-5.3-Flash video input: placeholder count (GLM-4.6V timestamp path) disagrees with the pixel path's frame sampling, engine core dies in _merge_multimodal_embeddings
- [Bug] [vllm-project/vllm#55649](https://github.com/vllm-project/vllm/issues/55649) [Bug]: NVFP4 gated-MoE end-padding silently corrupts Gemma-4-26B at TP2 on B200 (SM100)
- [Bug] [vllm-project/vllm#55673](https://github.com/vllm-project/vllm/issues/55673) [Bug]: FlashInfer TensorRT-LLM NVFP4 KV cache produces invalid Qwen3.5-397B output on Blackwell
- [Bug] [vllm-project/vllm#55725](https://github.com/vllm-project/vllm/issues/55725) [Bug]: Weight loading error on GLM-5.3-Flash (`KeyError: 'layers.11.shared_transformer.self_attn.qkv_proj.weight'`) in 2-node setup

### Scheduler / Batching

- [Bug] [sgl-project/sglang#38319](https://github.com/sgl-project/sglang/issues/38319) [Bug] Chunked Prefill + Radix Insert race corrupts KV pages (QSA, Qwen3.8-Flash-Next)
- [RFC] [vllm-project/vllm#55639](https://github.com/vllm-project/vllm/issues/55639) [RFC][EPD] Avoid redundant encoder work when Prefill can reuse KV or embeddings

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#55633](https://github.com/vllm-project/vllm/issues/55633) [Bug]: legacy qwen3_xml streaming parser emits whitespace-only content before the first tool call
- [Bug] [vllm-project/vllm#55659](https://github.com/vllm-project/vllm/issues/55659) [Bug]: /v1/responses crashes on persisted additional_tools input items
- [Bug] [vllm-project/vllm#55663](https://github.com/vllm-project/vllm/issues/55663) [Bug]: Sweep plots drop queued figures and hide worker failures
