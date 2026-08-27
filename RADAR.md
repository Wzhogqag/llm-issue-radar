# LLM Serving Issue Radar

_Last run: 2026-08-27T17:01+00:00_

**21 issues** — sgl-project/sglang: 9, vllm-project/vllm: 12 — 🆕 **21 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#36702](https://github.com/sgl-project/sglang/issues/36702) [Bug] Kimi-K3 + DCP: all TP ranks wedge in filter_dcp_local_kv_indices (nonzero → cudaStreamSynchronize) on long chunked prefill; 300s watchdog, memory free

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#36698](https://github.com/sgl-project/sglang/issues/36698) [Bug] DeepSeek-V4-Flash-0731 fails to stop at stop sequence when preceded by Chinese text
- [other] 🆕 ⚠maintainer-authored [#36633](https://github.com/sgl-project/sglang/issues/36633) [CPU] FP8 KV store: keep fused decode path, stop using Python index_put

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#36711](https://github.com/sgl-project/sglang/issues/36711) [Bug] GLM-5.3-Flash (glm5_next) crashes on startup with --moe-runner-backend flashinfer_trtllm: IndexError index 288 out of bounds in logical_to_all_physical
- [Bug] 🆕 [#36690](https://github.com/sgl-project/sglang/issues/36690) [Bug] gemma-3n-E2B-it/E4B-it: degenerate output (fa3/flashinfer) or crash (triton) in multimodal serving, 0% vision accuracy

### vllm-project/vllm

- [other] 🆕 [#54059](https://github.com/vllm-project/vllm/issues/54059) [Model]: GLM-5.3-Flash (glm5_next): no sparse-MLA attention path on Ada (sm_89, RTX 4090)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36597](https://github.com/sgl-project/sglang/issues/36597) [Bug] NVFP4 MoE + EP>1: globally-loaded input scales not sliced to local experts in non-CuteDSL branch (_compute_gemm1_alphas shape mismatch)

### vllm-project/vllm

- [Bug] 🆕 [#54047](https://github.com/vllm-project/vllm/issues/54047) [Bug]: GraniteMoeHybrid cannot load per-expert quantized checkpoints — KeyError: 'layers.0.block_sparse_moe.experts.w2_weight'

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#36678](https://github.com/sgl-project/sglang/issues/36678) [Feature] Expose opt-in per-request metrics in OpenAI-compatible responses

### vllm-project/vllm

- [Bug] 🆕 [#54062](https://github.com/vllm-project/vllm/issues/54062) [Bug]: GLM-5.3-Flash - attention archiecture Glm5NextTextLinearAttention not supported
- [Bug] 🆕 [#53975](https://github.com/vllm-project/vllm/issues/53975) [Bug]: legacy guided_json is silently ignored - request returns 200 with unconstrained free-form text

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#54027](https://github.com/vllm-project/vllm/issues/54027) [Bug]: DFlash2 + YaRN identical 1.04M prompt gets zero prefix-cache reuse while target-only reuses ~1.039M tokens
- [Bug] 🆕 [#54011](https://github.com/vllm-project/vllm/issues/54011) [Bug][Spec Decode] DSpark adaptive verification on SM90 (H20): draft acceptance collapse + hang during batch drain (sample_tokens RPC timeout)
- [Bug] 🆕 [#53983](https://github.com/vllm-project/vllm/issues/53983) [Bug]: ROCm spec-decode attention-metadata allowlist is enumerated by hand and has now been patched at least three times; consider letting backends declare support
- [Bug] 🆕 [#53982](https://github.com/vllm-project/vllm/issues/53982) [Bug]: _compute_slot_mapping_kernel reads block_table out of bounds for cache groups whose block table is narrower than the sequence
- [other] 🆕 [#54039](https://github.com/vllm-project/vllm/issues/54039) [Question] async scheduling defaults to on for ROCm + MTP speculative decoding, while vLLM's own ROCm CI disables that combination (#32275) — was the hang root-caused, and should the default resolution encode it?

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#36675](https://github.com/sgl-project/sglang/issues/36675) [Bug]

### vllm-project/vllm

- [Bug] 🆕 [#54002](https://github.com/vllm-project/vllm/issues/54002) [Bug]: crashed engine leaks /dev/shm/vllm_offload_*.mmap, making every in-place container restart fail at SharedOffloadRegion init

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#36669](https://github.com/sgl-project/sglang/issues/36669) [Bug] GLM-5.3-Flash thinking output degenerates into repeated '!' under multi-tool agentic prompts

### vllm-project/vllm

- [Bug] 🆕 [#54003](https://github.com/vllm-project/vllm/issues/54003) [Bug]: JSON/GRAMMAR structured-output schema compilation has no timeout (regex does); deeply-nested schemas cause unbounded compile time
- [Bug] 🆕 [#53973](https://github.com/vllm-project/vllm/issues/53973) [Bug]: PyAV video backend deadlocks under serving concurrency — unbounded SLICE threading in decode_frames
