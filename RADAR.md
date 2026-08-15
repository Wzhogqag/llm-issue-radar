# LLM Serving Issue Radar

_Last run: 2026-08-15T13:30+00:00_

**21 issues** — sgl-project/sglang: 7, vllm-project/vllm: 14 — 🆕 **19 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 5
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Build / Install / Platform](#build--install--platform) — 7

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#52360](https://github.com/vllm-project/vllm/issues/52360) [Bug][MooncakeStoreConnector]: Preemption frees GPU blocks while async store jobs are still reading them, storing KV that does not belong to the key

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#34941](https://github.com/sgl-project/sglang/issues/34941) [Bug] DSA sparse-MLA prefill silently computes no attention at all for a single extend > 65535 tokens (trtllm-gen gridDim.z limit is still unguarded on the non-DP path)

### vllm-project/vllm

- [other] 🆕 [#52359](https://github.com/vllm-project/vllm/issues/52359) [Refactor] Refactor EPD
- [other] 🆕 [#52408](https://github.com/vllm-project/vllm/issues/52408) [Docs/Robustness] NIXL connector: the block_len_per_layer == seen_base_addresses assert is load-bearing for hybrid-Mamba descriptor IDs
- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#52409](https://github.com/vllm-project/vllm/issues/52409) EPD Tracker
- [Bug] [#52339](https://github.com/vllm-project/vllm/issues/52339) [Bug]: DeepSeek-V4 FlashMLA sparse prefill phase1.cuh:614 on H20-3e TP8 at ~161K context

## Quantization

### sgl-project/sglang

- [other] 🆕 [#34918](https://github.com/sgl-project/sglang/issues/34918) [Playground] Verified cell: rtx6000 / default / nvfp4 / balanced / single

### vllm-project/vllm

- [Bug] 🆕 [#52393](https://github.com/vllm-project/vllm/issues/52393) [Bug]: Client stop strings match inside the reasoning segment for think-in-prompt models, truncating CoT and yielding content=None
- [Feature] 🆕 [#52447](https://github.com/vllm-project/vllm/issues/52447) [Feature]: Support NVFP4 DeepSeek-V4-Flash-0731 with FP4 KV cache + DSpark speculative decoding on SM121 (DGX Spark)
- [Feature] [#52347](https://github.com/vllm-project/vllm/issues/52347) [Feature]: Native OCP MXFP6 execution on NVIDIA SM120

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#34920](https://github.com/sgl-project/sglang/issues/34920) [Bug] Kimi K3 decode crash: DSPARK target_verify + DCP → cumsum(extend_prefix_lens=None) in layers/dcp/planner.py

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34943](https://github.com/sgl-project/sglang/issues/34943) [Bug] Stopping the by-stage profiler under speculative decoding freezes the scheduler for ~25 s (synchronous trace export on the scheduler thread), and the stop condition leaks into later requests
- [no-prefix] 🆕 ⚠no-prefix [#34942](https://github.com/sgl-project/sglang/issues/34942) --profile-by-stage with speculative decoding: profiler never stops on decode batches (TARGET_VERIFY counted as prefill); deferred stop + synchronous trace export freeze the server for ~25 s inside later unrelated requests

### vllm-project/vllm

- [Bug] 🆕 [#52448](https://github.com/vllm-project/vllm/issues/52448) [Bug]: DeepSeek-V4-Flash think-until-cap / empty turn under concurrent DSpark + breakable CUDA graphs

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#34861](https://github.com/sgl-project/sglang/issues/34861) [Bug] [NPU] Router GEMM output should always be fp32
- [Bug] 🆕 ⚠maintainer-authored [#34857](https://github.com/sgl-project/sglang/issues/34857) [Bug] [ROCm] Router GEMM output should always be fp32, and the expert correction bias should not be cast to bf16

### vllm-project/vllm

- [Bug] 🆕 [#52434](https://github.com/vllm-project/vllm/issues/52434) [Bug]: AttributeError: 'ParallelLMHead' object has no attribute 'output_size_per_partition'
- [Bug] 🆕 [#52415](https://github.com/vllm-project/vllm/issues/52415) [Bug] XPU qnorm/rope kernel: overlapping stores in one program corrupt the KV cache nondeterministically
- [Bug] 🆕 [#52404](https://github.com/vllm-project/vllm/issues/52404) [Bug]: 4 B200 GPU ，DP 4 + EP（or TP 4 + EP），Deepseek V4 Flash 0731 , simultaneously processing hundreds of text extraction tasks, outputting garbled characters.
- [Bug] 🆕 [#52386](https://github.com/vllm-project/vllm/issues/52386) [Bug]: XPU worker fails to start with world_size=1 when oneCCL cannot initialize
- [Bug] 🆕 [#52442](https://github.com/vllm-project/vllm/issues/52442) [Bug][ROCm] Kimi-K3 a8w4 SiTU MoE: AITER_SITUV2_A8W4 without VLLM_ROCM_USE_AITER_MOE_SITUV2_A8W4 silently produces garbage
