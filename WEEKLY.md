# Weekly Trends — 2026-11-22

Window: 2026-11-16 → 2026-11-22 (7 snapshots)

**Totals:** 22 → 14  (14 appeared, 22 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 2 | +1 | 2 | 1 |
| Build / Install / Platform | 1 | 1 | 0 | 1 | 1 |
| Distributed / TP / PP / EP | 1 | 1 | 0 | 1 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 1 | -1 | 1 | 2 |
| New Model Integration | 1 | 0 | -1 | 0 | 1 |
| Performance / Memory / OOM | 1 | 0 | -1 | 0 | 1 |
| Quantization | 7 | 3 | -4 | 3 | 7 |
| Sampling / Speculative Decoding | 1 | 3 | +2 | 3 | 1 |
| Scheduler / Batching | 4 | 0 | -4 | 0 | 4 |
| Serving / OpenAI API / Streaming | 2 | 2 | 0 | 2 | 2 |
| Uncategorized | 1 | 1 | 0 | 1 | 1 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#52274](https://github.com/sgl-project/sglang/issues/52274) [Bug] gemma4: Vision attention ignores the padding mask on fa3 / fa4 / triton_attn
- [Bug] [vllm-project/vllm#69228](https://github.com/vllm-project/vllm/issues/69228) [Bug]: Intermittent CUDA OOM in DCP a2a combine fallback (`_dcp_a2a_send_recv_buffers`) at high concurrency with short prompts — Kimi-K3.1-Pro, TP8 + DCP8, `gpu-memory-utilization 0.97`

### Build / Install / Platform

- [Bug] [sgl-project/sglang#52191](https://github.com/sgl-project/sglang/issues/52191) [Bug] Diffusion orchestrator: deeply nested result frame escapes per-request handler and stops routing loop

### Distributed / TP / PP / EP

- [Perf] [sgl-project/sglang#52213](https://github.com/sgl-project/sglang/issues/52213) [Perf] hicache: unconditional _all_reduce_attn_groups in the drain collective when the linker is idle

### KV Cache / Connector / PD Disagg

- [Feature] [vllm-project/vllm#69237](https://github.com/vllm-project/vllm/issues/69237) [Feature]: Process checkpoint support for the native CPU KV offload connector (OffloadingConnector)

### Quantization

- [Bug] [sgl-project/sglang#52318](https://github.com/sgl-project/sglang/issues/52318) [Bug] Qwen3-Omni: vision and audio layers are built under names the quantization ignore list never matches, so cyankiwi/Qwen3-Omni-30B-A3B-Instruct-AWQ-4bit fails to start
- [Feature] [vllm-project/vllm#69156](https://github.com/vllm-project/vllm/issues/69156) [Feature]: Inkling 2 Mini on Ampere/Ada (SM80/86/89)
- [Bug] [vllm-project/vllm#69183](https://github.com/vllm-project/vllm/issues/69183) [Bug]: compressed-tensors W4A8 int (CompressedTensorsWNA8Int) serves W4A16 on SM86: Marlin takes the layer, and with Humming forced, the groupwise fallback drops the int8 input

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#52215](https://github.com/sgl-project/sglang/issues/52215) [Bug][CP] DeepSeek-V4.1-Flash pre_from_prev + CP8: vision MoE router input_ids shape mismatch in moe_fused_gate (a2a=none)
- [Performance] [vllm-project/vllm#69152](https://github.com/vllm-project/vllm/issues/69152) [Performance]: Fused CUDA GDN MTP decode kernel stores a full recurrent state per draft token
- [Bug] [vllm-project/vllm#69154](https://github.com/vllm-project/vllm/issues/69154) [Bug]: GLM-5.3-Flash + MTP + prefix caching on v0.34.0 (B200, TP4): silent constant-token degeneration ("locklock…"), MTP acceptance collapses to 0, persists for requests sharing the prefix

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#69161](https://github.com/vllm-project/vllm/issues/69161) [Bug]: olmo3 tool parser: text before <function_calls> is dropped (stream=false) or the tool call is lost (stream=true)
- [Bug] [vllm-project/vllm#69241](https://github.com/vllm-project/vllm/issues/69241) [Bug]: Parser engine tool parsers (granite, llama3_json, inkling): arguments sent as a JSON-encoded string stream as '' but are returned without streaming

### Uncategorized

- [Bug] [vllm-project/vllm#69173](https://github.com/vllm-project/vllm/issues/69173) [Bug]: hy_v4 tool parser returns an argument as a string when its schema uses allOf

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [sgl-project/sglang#50715](https://github.com/sgl-project/sglang/issues/50715) [Bug] [NPU] RMSNorm ignores explicit cast_x_before_out_mul=True

### Build / Install / Platform

- [other] [sgl-project/sglang#50754](https://github.com/sgl-project/sglang/issues/50754) [NPU] [Roadmap] SGLang Diffusion Integration with MindIE-SD

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#67911](https://github.com/vllm-project/vllm/issues/67911) [Bug]: MiniMax-M3.1-Flash fails on nightly with transformers 5.23.0: 'MiniMaxM3VLTextConfig' object has no attribute 'sparse_attention_config'

### KV Cache / Connector / PD Disagg

- [Feature] [vllm-project/vllm#67829](https://github.com/vllm-project/vllm/issues/67829) [Feature]: Add GetLoad RPC to the Rust frontend gRPC Control service
- [RFC] [vllm-project/vllm#67874](https://github.com/vllm-project/vllm/issues/67874) [RFC][HiSparse] On-Demand KV Gather and Layerwise Two-Slot Reuse for Sparse-MLA (DSA) Prefill

### New Model Integration

- [Bug] [sgl-project/sglang#50780](https://github.com/sgl-project/sglang/issues/50780) [Bug] fused_hc_mix can hang on repeated calls from separate CUDA streams

### Performance / Memory / OOM

- [Feature] [sgl-project/sglang#50761](https://github.com/sgl-project/sglang/issues/50761) [Feature] fused MoE tuner: tuned configs can regress at the batch sizes between tuned keys

### Quantization

- [Bug] [vllm-project/vllm#67834](https://github.com/vllm-project/vllm/issues/67834) [Bug]: FlexAttention fails on recent hybrid models and SM89 (recompile limit, 576 block size, shared memory)
- [Bug] [vllm-project/vllm#67862](https://github.com/vllm-project/vllm/issues/67862) [Bug]: MiniMax-M3.1-Flash NVFP4 packed routed experts fail to load with TP8 / TP4+PP2 on v0.33.0 (192 vs 384 in RoutedExperts._load_w13)
- [RFC] [vllm-project/vllm#67865](https://github.com/vllm-project/vllm/issues/67865) [RFC]: Opt-in online quantization of the target model LM head
- [other] [vllm-project/vllm#67876](https://github.com/vllm-project/vllm/issues/67876) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)
- [Feature] [vllm-project/vllm#67901](https://github.com/vllm-project/vllm/issues/67901) [Feature][ROCm]: MI308X (gfx942, 80 CUs) cannot use --monokernel; MXFP4 MoE experts fall back to Triton W4A16 — lossless FP8 128x128 repack doubles decode throughput
- [Bug] [vllm-project/vllm#67914](https://github.com/vllm-project/vllm/issues/67914) [Bug]: flashinfer_b12x NVFP4 MoE returns garbage on SM120 since #64692 (the DeepGEMM warmup overwrites its FC2 input scale)
- [RFC] [vllm-project/vllm#67922](https://github.com/vllm-project/vllm/issues/67922) [RFC]: PLE Connector for Disaggregated Embedding Serving

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#67831](https://github.com/vllm-project/vllm/issues/67831) [Bug]: Draft-model drafted-token metrics inflated when dynamic speculative decoding picks K=1

### Scheduler / Batching

- [other] [sgl-project/sglang#50700](https://github.com/sgl-project/sglang/issues/50700) [Roadmap] Hybrid State Cache Management for Agentic Workloads (FlashStates)
- [RFC] [sgl-project/sglang#50756](https://github.com/sgl-project/sglang/issues/50756) [RFC] Elastic KV tail: lend idle co-tenant VRAM to the KV cache and give it back on demand (HIP VMM, ROCm)
- [RFC] [vllm-project/vllm#67892](https://github.com/vllm-project/vllm/issues/67892) [RFC] Declarative metrics hooks, metric levels, and a runtime level control plane
- [RFC] [vllm-project/vllm#67909](https://github.com/vllm-project/vllm/issues/67909) [RFC]: Offloading cache lifecycle metrics

### Serving / OpenAI API / Streaming

- [no-prefix] [vllm-project/vllm#67851](https://github.com/vllm-project/vllm/issues/67851) Race in auto NUMA binding when workers start concurrently: AssertionError in _mp_set_executable
- [Bug] [vllm-project/vllm#67923](https://github.com/vllm-project/vllm/issues/67923) [Bug]: Rust qwen3_coder parser keeps the next <parameter=...> tag in the value when </parameter> is missing

### Uncategorized

- [Feature] [vllm-project/vllm#67929](https://github.com/vllm-project/vllm/issues/67929) [Feature]: EPLB and beyond
