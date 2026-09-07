# LLM Serving Issue Radar

_Last run: 2026-09-07T13:29+00:00_

**22 issues** — sgl-project/sglang: 5, vllm-project/vllm: 17 — 🆕 **22 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 4
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#38319](https://github.com/sgl-project/sglang/issues/38319) [Bug] Chunked Prefill + Radix Insert race corrupts KV pages (QSA, Qwen3.8-Flash-Next)

### vllm-project/vllm

- [RFC] 🆕 [#55639](https://github.com/vllm-project/vllm/issues/55639) [RFC][EPD] Avoid redundant encoder work when Prefill can reuse KV or embeddings

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#55729](https://github.com/vllm-project/vllm/issues/55729) [Bug][MooncakeConnector] Bootstrap registration timeout is fatal during slow rank-0 initialization
- [Feature] 🆕 [#55635](https://github.com/vllm-project/vllm/issues/55635) [Feature]: EFA vLLM image should work out of the box on AWS NVIDIA GPUs

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#55722](https://github.com/vllm-project/vllm/issues/55722) [Bug]: `fuse_attn_quant` without `use_inductor_graph_partition` drops all piecewise cudagraphs on backends that cannot do FULL (-38 % on ROCm sparse MLA)
- [Bug] 🆕 [#55720](https://github.com/vllm-project/vllm/issues/55720) [Bug]: `fuse_rope_kvcache` / `fuse_qk_norm_rope_kvcache` silently register zero patterns on MLA-only models, but their side effects are still paid
- [Bug] 🆕 [#55636](https://github.com/vllm-project/vllm/issues/55636) [Bug] DeepSeek V4 sparse MLA can index a nonexistent block-table row during CUDA-graph warmup
- [RFC] 🆕 [#55697](https://github.com/vllm-project/vllm/issues/55697) [RFC]: Application-Directed Prefix Checkpoints for Mamba / Hybrid Prefix Caching

## Quantization

### sgl-project/sglang

- [other] 🆕 [#38312](https://github.com/sgl-project/sglang/issues/38312) [Playground] Verified cell: h100 / flash-official / fp4 / high-throughput / single
- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#38300](https://github.com/sgl-project/sglang/issues/38300) TP2 hang with HiCache, breakable prefill CUDA graphs, and FlashInfer MNNVL on B300

### vllm-project/vllm

- [Bug] 🆕 [#55725](https://github.com/vllm-project/vllm/issues/55725) [Bug]: Weight loading error on GLM-5.3-Flash (`KeyError: 'layers.11.shared_transformer.self_attn.qkv_proj.weight'`) in 2-node setup
- [Bug] 🆕 [#55673](https://github.com/vllm-project/vllm/issues/55673) [Bug]: FlashInfer TensorRT-LLM NVFP4 KV cache produces invalid Qwen3.5-397B output on Blackwell
- [Bug] 🆕 [#55649](https://github.com/vllm-project/vllm/issues/55649) [Bug]: NVFP4 gated-MoE end-padding silently corrupts Gemma-4-26B at TP2 on B200 (SM100)
- [Bug] 🆕 [#55644](https://github.com/vllm-project/vllm/issues/55644) [Bug]: GLM-5.3-Flash video input: placeholder count (GLM-4.6V timestamp path) disagrees with the pixel path's frame sampling, engine core dies in _merge_multimodal_embeddings

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#55632](https://github.com/vllm-project/vllm/issues/55632) [Bug][ROCm] 15s EngineCore cleanup grace is defeated by MultiprocExecutor's 9s worker-kill budget; workers SIGKILLed mid-teardown

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#38291](https://github.com/sgl-project/sglang/issues/38291) [Bug] `fp8e4nv` not supported on A100 (SM80) when serving Qwen3.8-Flash-Next-FP8
- [RFC] 🆕 [#38334](https://github.com/sgl-project/sglang/issues/38334) [RFC] Gluon MegaMoE: SGLang Integration and Multi-Node Support

### vllm-project/vllm

- [Feature] 🆕 [#55683](https://github.com/vllm-project/vllm/issues/55683) [Feature]: LoRA support for deepseek v4 flash vision

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#55663](https://github.com/vllm-project/vllm/issues/55663) [Bug]: Sweep plots drop queued figures and hide worker failures
- [Bug] 🆕 [#55659](https://github.com/vllm-project/vllm/issues/55659) [Bug]: /v1/responses crashes on persisted additional_tools input items
- [Bug] 🆕 [#55633](https://github.com/vllm-project/vllm/issues/55633) [Bug]: legacy qwen3_xml streaming parser emits whitespace-only content before the first tool call

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#55689](https://github.com/vllm-project/vllm/issues/55689) [Bug]: GLM-5.3-Flash produces repetitive / off‑topic outputs in PD‑disaggregated deployment
