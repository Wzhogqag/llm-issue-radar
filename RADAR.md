# LLM Serving Issue Radar

_Last run: 2026-07-21T13:59+00:00_

**25 issues** — sgl-project/sglang: 12, vllm-project/vllm: 13 — 🆕 **25 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 8
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#31833](https://github.com/sgl-project/sglang/issues/31833) [Bug] NemotronH --mamba-scheduler-strategy extra_buffer accuracy drop on AIME26 (Nemotron-3-Super-120B)

### vllm-project/vllm

- [Bug] 🆕 [#49317](https://github.com/vllm-project/vllm/issues/49317) [Bug]: [Performance] AsyncLLM `add_request` runs multimodal `process_inputs` (HF processor) synchronously on the event-loop thread, serializing per-request image preprocessing and starving the GPU under concurrent multi-image requests
- [Bug] 🆕 [#49276](https://github.com/vllm-project/vllm/issues/49276) [Bug]: cuMemcpyBatchAsync segfaults or hangs on large/repeated compact scatter submissions

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 [#31842](https://github.com/sgl-project/sglang/issues/31842) [Enhancement] [LMCache] MP mode: non-blocking store on request finish

### vllm-project/vllm

- [Bug] 🆕 [#49250](https://github.com/vllm-project/vllm/issues/49250) [Bug]: kv_load_failure_policy="recompute" gives wrong output when a KV connector rejects a synchronous load (V2 runner)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31938](https://github.com/sgl-project/sglang/issues/31938) [Bug] DSV4-Flash BF16 model + A2 dual machine，start failed, error is "socVersion [ascend910b] does not support opType [HcPre]"
- [Bug] 🆕 [#31864](https://github.com/sgl-project/sglang/issues/31864) [Bug] GLM-5.2-NVFP4 disaggregated prefill crashes in FlashInfer TRTLLM MoE batched GEMM with sm100f kernel
- [Bug] 🆕 [#31827](https://github.com/sgl-project/sglang/issues/31827) [Bug] MiniMax-M3 NVFP4 fails to load: fused MoE falls back to UnquantizedFusedMoEMethod (6144 vs 3072) and MXFP8 linear scales are dropped

### vllm-project/vllm

- [Bug] 🆕 [#49259](https://github.com/vllm-project/vllm/issues/49259) [Bug]: [Performance]: Qwen3-VL-32B-FP8 throughput collapses on v0.25.1 (v0.24.0 fine)
- [Bug] 🆕 [#49248](https://github.com/vllm-project/vllm/issues/49248) [Bug]: glm47 tool parser silently returns empty arguments when the model omits the opening <arg_value> tag
- [no-prefix] 🆕 ⚠no-prefix [#49239](https://github.com/vllm-project/vllm/issues/49239) Malformed /v1/responses request returns a >100MB validation-error body (full input echoed per error)
- [no-prefix] 🆕 ⚠no-prefix [#49237](https://github.com/vllm-project/vllm/issues/49237) POST /wake_up fails with AttributeError: 'list' object has no attribute 'zero_' in init_fp8_kv_scales, wedging the engine (health stays green, completions hang)
- [RFC] 🆕 [#49232](https://github.com/vllm-project/vllm/issues/49232) [RFC]: ReplaySSM: cache SSM inputs instead of state for faster standard and speculative decode (Mamba2 + GDN)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#31929](https://github.com/sgl-project/sglang/issues/31929) [Bug] _fwd_kernel_ep_scatter_1 may lead to illegal memory access.

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#31894](https://github.com/sgl-project/sglang/issues/31894) [Feature] Feature LoRA support for the CPU engine (Intel Xeon) —  pin_memory=True  hardcoded in lora/layers.py crashes on CPU-only systems
- [Feature] 🆕 [#31828](https://github.com/sgl-project/sglang/issues/31828) [Feature] Support pre-sampled video input to decouple decoding from mm preprocessor/encoder

## Sampling / Speculative Decoding

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#31858](https://github.com/sgl-project/sglang/issues/31858) Potential issue about the numerical precision of Qwen3.5 Router GEMM

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#31915](https://github.com/sgl-project/sglang/issues/31915) Tool-call parsers lose or corrupt data at streaming chunk boundaries (multiple detectors)
- [no-prefix] 🆕 ⚠no-prefix [#31912](https://github.com/sgl-project/sglang/issues/31912) ReDoS in PythonicDetector: a truncated tool call pins a worker CPU (catastrophic regex backtracking)

### vllm-project/vllm

- [RFC] 🆕 [#49288](https://github.com/vllm-project/vllm/issues/49288) [RFC]: Multimodal Asynchronous Collaborative Architecture Sidecar

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#49224](https://github.com/vllm-project/vllm/issues/49224) [Bug]: Model Runner V2 (now default for dense models) skips CUDA graph memory reservation — `profile_cudagraph_memory()` returns 0, causing OOM during `capture_model()`

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#31862](https://github.com/sgl-project/sglang/issues/31862) Checklist: CUDA PyTorch stack upgrade to 2.13 (#28836)

### vllm-project/vllm

- [Bug] 🆕 [#49311](https://github.com/vllm-project/vllm/issues/49311) [Bug]: v0.25.0 regression - Qwen3.5 FP8 on H200 crashes during CUDA graph capture with CUDA illegal memory access
- [Bug] 🆕 [#49254](https://github.com/vllm-project/vllm/issues/49254) [Bug]: nvidia/Gemma-4-26B-A4B-NVFP4 model tool parser issue
- [Bug] 🆕 [#49238](https://github.com/vllm-project/vllm/issues/49238) [Bug]: Decode instance segfaults on NIXL `loadRemoteMD` after prefill pod restarts in P/D disaggregation
