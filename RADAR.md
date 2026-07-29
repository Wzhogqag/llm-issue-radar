# LLM Serving Issue Radar

_Last run: 2026-07-29T14:00+00:00_

**19 issues** — sgl-project/sglang: 7, vllm-project/vllm: 12 — 🆕 **19 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 8
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#32777](https://github.com/sgl-project/sglang/issues/32777) TX PFC / NIC pause frames during Mooncake L3 cache prefetch — NIC→host-memory intra-node bottleneck

### vllm-project/vllm

- [Bug] 🆕 [#50235](https://github.com/vllm-project/vllm/issues/50235) [Bug]: Kimi-K3 prefix cache miss when prompt length is exactly a 1536-token boundary

## Attention Backend

### vllm-project/vllm

- [other] 🆕 [#50255](https://github.com/vllm-project/vllm/issues/50255) [Kernel][Model] Gemma4: optimize FA4 mm_prefix range lookup and CuTe JIT stability

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32781](https://github.com/sgl-project/sglang/issues/32781) [Bug] DeepSeek-V4-Pro fails to load with Marlin TP16 on v0.5.16
- [Bug] 🆕 [#32669](https://github.com/sgl-project/sglang/issues/32669) [Bug] DeepSeek-V4 non-EP TBO uses TP-wide metadata and combine for attention-TP > 1
- [Feature] 🆕 [#32712](https://github.com/sgl-project/sglang/issues/32712) [Feature] [RFC] SharedEP: a zerocopy execution model for MoE Expert Parallelism

### vllm-project/vllm

- [Bug] 🆕 [#50269](https://github.com/vllm-project/vllm/issues/50269) [Bug]: Host memory is not reducing after the model is loaded into Intel XPU
- [Performance] 🆕 [#50264](https://github.com/vllm-project/vllm/issues/50264) [Performance]: On RDNA, hybrid-Mamba models fall back to Triton paged attention and decode collapses at long context
- [Bug] 🆕 [#50189](https://github.com/vllm-project/vllm/issues/50189) [Bug]: Xid 31 MMU fault (illegal write) with flashinfer_b12x MoE backend under concurrent chunked prefill (SM120, Qwen3.5-122B-A10B-NVFP4)
- [Bug] 🆕 [#50188](https://github.com/vllm-project/vllm/issues/50188) [Bug]: Explicit --enable-prefix-caching with MTP spec decode + tool calling corrupts tool-call emission on repeated identical prompts
- [other] 🆕 [#50206](https://github.com/vllm-project/vllm/issues/50206) [New Model]: Support GLM-5.2-Vision-NVFP4

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#32751](https://github.com/sgl-project/sglang/issues/32751) [Bug] `create_custom_parallel_group` calls `all_gather_object` without explicit `group`, causing non-deterministic device selection and CUDA errors on non-NVIDIA backends
- [other] 🆕 [#32774](https://github.com/sgl-project/sglang/issues/32774) [Roadmap] Integrate NCCL 2.30 Features into SGLang

### vllm-project/vllm

- [Bug] 🆕 [#50179](https://github.com/vllm-project/vllm/issues/50179) [Bug]: Multicast check disables the symmetric memory two-shot all-reduce path, which never uses multicast

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#32750](https://github.com/sgl-project/sglang/issues/32750) [Feature] PP Support PD + DSpark

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#50258](https://github.com/vllm-project/vllm/issues/50258) [Bug]: Kimi K3 parser leaks truncated reasoning into content with speculative decoding

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#50271](https://github.com/vllm-project/vllm/issues/50271) [Bug]:  Rust HF benchmark hard-codes the Dataset Viewer endpoint and can stall when it is unreachable
- [Bug] 🆕 [#50249](https://github.com/vllm-project/vllm/issues/50249) [Bug]: CUDA error: no kernel image is available for execution on the device when running Kimi-K3 on Ampere (A100) with vllm/vllm-openai:kimi-k3

## Uncategorized

### vllm-project/vllm

- [Bug] 🆕 [#50203](https://github.com/vllm-project/vllm/issues/50203) [Bug]: vllm-k3-toolcall repeat and repeat error
