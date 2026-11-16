# LLM Serving Issue Radar

_Last run: 2026-11-16T13:45+00:00_

**22 issues** — sgl-project/sglang: 6, vllm-project/vllm: 16 — 🆕 **22 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 4
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 7
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#50756](https://github.com/sgl-project/sglang/issues/50756) [RFC] Elastic KV tail: lend idle co-tenant VRAM to the KV cache and give it back on demand (HIP VMM, ROCm)
- [other] 🆕 [#50700](https://github.com/sgl-project/sglang/issues/50700) [Roadmap] Hybrid State Cache Management for Agentic Workloads (FlashStates)

### vllm-project/vllm

- [RFC] 🆕 [#67892](https://github.com/vllm-project/vllm/issues/67892) [RFC] Declarative metrics hooks, metric levels, and a runtime level control plane
- [RFC] 🆕 ⚠maintainer-authored [#67909](https://github.com/vllm-project/vllm/issues/67909) [RFC]: Offloading cache lifecycle metrics

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#67829](https://github.com/vllm-project/vllm/issues/67829) [Feature]: Add GetLoad RPC to the Rust frontend gRPC Control service
- [RFC] 🆕 [#67874](https://github.com/vllm-project/vllm/issues/67874) [RFC][HiSparse] On-Demand KV Gather and Layerwise Two-Slot Reuse for Sparse-MLA (DSA) Prefill

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#50715](https://github.com/sgl-project/sglang/issues/50715) [Bug] [NPU] RMSNorm ignores explicit cast_x_before_out_mul=True

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#67914](https://github.com/vllm-project/vllm/issues/67914) [Bug]: flashinfer_b12x NVFP4 MoE returns garbage on SM120 since #64692 (the DeepGEMM warmup overwrites its FC2 input scale)
- [Bug] 🆕 [#67862](https://github.com/vllm-project/vllm/issues/67862) [Bug]: MiniMax-M3.1-Flash NVFP4 packed routed experts fail to load with TP8 / TP4+PP2 on v0.33.0 (192 vs 384 in RoutedExperts._load_w13)
- [Bug] 🆕 [#67834](https://github.com/vllm-project/vllm/issues/67834) [Bug]: FlexAttention fails on recent hybrid models and SM89 (recompile limit, 576 block size, shared memory)
- [Feature] 🆕 [#67901](https://github.com/vllm-project/vllm/issues/67901) [Feature][ROCm]: MI308X (gfx942, 80 CUs) cannot use --monokernel; MXFP4 MoE experts fall back to Triton W4A16 — lossless FP8 128x128 repack doubles decode throughput
- [other] 🆕 [#67876](https://github.com/vllm-project/vllm/issues/67876) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)
- [RFC] 🆕 [#67922](https://github.com/vllm-project/vllm/issues/67922) [RFC]: PLE Connector for Disaggregated Embedding Serving
- [RFC] 🆕 [#67865](https://github.com/vllm-project/vllm/issues/67865) [RFC]: Opt-in online quantization of the target model LM head

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#67911](https://github.com/vllm-project/vllm/issues/67911) [Bug]: MiniMax-M3.1-Flash fails on nightly with transformers 5.23.0: 'MiniMaxM3VLTextConfig' object has no attribute 'sparse_attention_config'

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#50780](https://github.com/sgl-project/sglang/issues/50780) [Bug] fused_hc_mix can hang on repeated calls from separate CUDA streams

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#67831](https://github.com/vllm-project/vllm/issues/67831) [Bug]: Draft-model drafted-token metrics inflated when dynamic speculative decoding picks K=1

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#67923](https://github.com/vllm-project/vllm/issues/67923) [Bug]: Rust qwen3_coder parser keeps the next <parameter=...> tag in the value when </parameter> is missing
- [no-prefix] 🆕 ⚠no-prefix [#67851](https://github.com/vllm-project/vllm/issues/67851) Race in auto NUMA binding when workers start concurrently: AssertionError in _mp_set_executable

## Performance / Memory / OOM

### sgl-project/sglang

- [Feature] 🆕 [#50761](https://github.com/sgl-project/sglang/issues/50761) [Feature] fused MoE tuner: tuned configs can regress at the batch sizes between tuned keys

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#50754](https://github.com/sgl-project/sglang/issues/50754) [NPU] [Roadmap] SGLang Diffusion Integration with MindIE-SD

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#67929](https://github.com/vllm-project/vllm/issues/67929) [Feature]: EPLB and beyond
