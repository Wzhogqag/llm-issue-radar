# LLM Serving Issue Radar

_Last run: 2026-11-14T13:22+00:00_

**21 issues** — sgl-project/sglang: 18, vllm-project/vllm: 3 — 🆕 **21 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#50416](https://github.com/sgl-project/sglang/issues/50416) [Bug] Muse Spark: the hook's `SGLANG_OPT_UNIFIED_CACHE_FREE_OUT_OF_WINDOW_SLOTS=False` default collapses the prefix cache when SWA memory is tight
- [Feature] 🆕 [#50479](https://github.com/sgl-project/sglang/issues/50479) [Feature][MeetUp][NPU][Docs][Qwen3.8-27B] Add long-context memory tuning guidance for Qwen3.8-27B on Ascend 910B
- [other] 🆕 [#50478](https://github.com/sgl-project/sglang/issues/50478) [MeetUp][Docs][NPU] Qwen3.8-27B BF16 and W8A8 Test Results on Ascend 910B

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#50405](https://github.com/sgl-project/sglang/issues/50405) [Feature] Receive requests during model forward to overlap DFS KV prefetch
- [other] 🆕 [#50461](https://github.com/sgl-project/sglang/issues/50461) [MeetUp][Docs][NPU] Qwen3.8-27B MeetUp Test Results for BF16&W8A8 on Ascend 910B

## Attention Backend

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#50499](https://github.com/sgl-project/sglang/issues/50499) dspark_accept SoftmaxTemp.execute (flashinfer branch) returns NaN rows on GB10 in 6/17 cold starts — cross-ref flashinfer#9486

### vllm-project/vllm

- [Bug] 🆕 [#67630](https://github.com/vllm-project/vllm/issues/67630) [Bug][Perf]: flashinfer_autotune / _dummy_run never calls compute_logits, leaving FP8 LM-head GEMM un-autotuned

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#50429](https://github.com/sgl-project/sglang/issues/50429) [Bug] Weight updates crash the scheduler for dense Marlin layers (GPTQ, AWQ, compressed-tensors W4A16, FP8 on sm86)
- [Feature] 🆕 [#50421](https://github.com/sgl-project/sglang/issues/50421) [Feature]  [MeetUp][NPU] Qwen3.8-27B（virtual machine）Meetup Task
- [other] 🆕 [#50488](https://github.com/sgl-project/sglang/issues/50488) [NPU][Qwen3.8-27B] Docs: Add A2 (910B3) deployment guidance, 128K prefix-cache best practice, and fix testing instructions

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Feature] 🆕 [#50497](https://github.com/sgl-project/sglang/issues/50497) [Feature] EAGLE tree verify without per-node state snapshots for GDN layers
- [Feature] 🆕 [#50411](https://github.com/sgl-project/sglang/issues/50411) [Feature] [MeetUp][NPU] DeepSeek-V4-Flash: document reproducible shared-prefix TPOT evaluation
- [other] 🆕 [#50450](https://github.com/sgl-project/sglang/issues/50450) [MeetUp][NPU][Docs] Qwen3.8-27B on Ascend A2: consolidated deployment and evaluation findings
- [other] 🆕 [#50423](https://github.com/sgl-project/sglang/issues/50423) [MeetUp][NPU][DeepSeek-V4-Flash-0731]  Add DeepSeek-V4-Flash 950PR/DT performance recipe

### vllm-project/vllm

- [Feature] 🆕 [#67552](https://github.com/vllm-project/vllm/issues/67552) [Feature]: Carry repetition_detection and extra_args on vllm.Inference GenerateRequest

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#50516](https://github.com/sgl-project/sglang/issues/50516) [Bug] Forward the upstream Retry-After header in OpenAI gateway responses
- [Bug] 🆕 [#50424](https://github.com/sgl-project/sglang/issues/50424) [Bug] Native serving benchmark counts a context-length stream error as a successful request
- [Bug] 🆕 [#50422](https://github.com/sgl-project/sglang/issues/50422) [Bug] Spark2.5 rounds large integer tool arguments
- [Feature] 🆕 [#50408](https://github.com/sgl-project/sglang/issues/50408) [Feature] glm-5.3: Encode message content as ordinary text in the built-in GLM-5.3 chat template

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#50443](https://github.com/sgl-project/sglang/issues/50443) [Bug] [NPU][MeetUp][Qwen3.8-27B] Output silently truncated to 1 token when KV pool is smaller than input length (hybrid model, 128K on A2 32GB)

### vllm-project/vllm

- [Feature] 🆕 [#67551](https://github.com/vllm-project/vllm/issues/67551) [Feature]: Enable libtorch-ABI-stable vLLM ROCm wheels
