# LLM Serving Issue Radar

_Last run: 2026-11-07T13:21+00:00_

**19 issues** — sgl-project/sglang: 3, vllm-project/vllm: 16 — 🆕 **19 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Performance] 🆕 ⚠maintainer-authored [#49055](https://github.com/sgl-project/sglang/issues/49055) [Performance][Non-blocking] Rust server stack #48815 follow-ups

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#66231](https://github.com/vllm-project/vllm/issues/66231) [RFC]: P/D disaggregation for continuous RL rollouts (S1): order-free, seconds-long weight-update pauses

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#66232](https://github.com/vllm-project/vllm/issues/66232) [Bug][Perf]: W4A16 HummingLinearKernel is non-deterministic across processes and faster than the default Machete on H100 (sm_90)

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#66211](https://github.com/vllm-project/vllm/issues/66211) [Bug]: Compressed-tensors NVFP4/MXFP4 row-parallel layers load with other groups' block scales when the TP split cuts a scale group (Gemma-4-26B-A4B NVFP4 at TP=8: GSM8K 24% -> 1.4%)
- [Bug] 🆕 [#66193](https://github.com/vllm-project/vllm/issues/66193) [Bug]: Extensible KV cache reserves the one-off FlashInfer autotune peak as a serving transient, cutting KV 2.4x under an explicit --gpu-memory-utilization (regression from #56492)
- [no-prefix] 🆕 ⚠no-prefix [#66218](https://github.com/vllm-project/vllm/issues/66218) GLM-5.3-Flash FP4-Local in production on 2x RTX PRO 6000 (SM120): what's missing for a full community-main base?

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Feature] 🆕 [#66170](https://github.com/vllm-project/vllm/issues/66170) [Feature]: Enable and validate pipeline parallelism for Domyn Edge

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#49065](https://github.com/sgl-project/sglang/issues/49065) [Bug] ComfyUI SGLD loader: Fun ControlNet on Qwen-Image 2.1 fails with AttributeError

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#48964](https://github.com/sgl-project/sglang/issues/48964) [Bug] GLM-5.3-Flash: engine state corrupted after a 1M-token request on v0.5.23 (MTP accept rate 0.00, all subsequent requests degenerate); v0.5.22 clean

### vllm-project/vllm

- [Bug] 🆕 [#66250](https://github.com/vllm-project/vllm/issues/66250) [Bug]: phi-2 crashes with CUDA illegal memory access during compile/warmup at size 32
- [Bug] 🆕 [#66244](https://github.com/vllm-project/vllm/issues/66244) [Bug]: Qwen2.5-0.5B crashes with CUDA illegal memory access during initialization warmup

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#66182](https://github.com/vllm-project/vllm/issues/66182) [Bug]: Step3ReasoningParser.extract_content_ids excludes think_end_token at last index
- [Bug] 🆕 [#66180](https://github.com/vllm-project/vllm/issues/66180) [Bug]: xLAM non-streaming tool parser drops single tool call object in <tool_call> tags
- [Bug] 🆕 [#66178](https://github.com/vllm-project/vllm/issues/66178) [Bug]: Granite20bFCToolParser streaming misses tool calls when preceded by content
- [Bug] 🆕 [#66173](https://github.com/vllm-project/vllm/issues/66173) [Bug]: Pythonic tool parsers silently drop calls with Python reserved keywords as parameter names

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#66242](https://github.com/vllm-project/vllm/issues/66242) [Bug]:  Phi-2 crashes with CUDA illegal memory access during compile/warmup at size 32
- [Bug] 🆕 [#66239](https://github.com/vllm-project/vllm/issues/66239) [Bug][KV Offload] FS tier reports EIO instead of ENOSPC when the disk fills
- [Bug] 🆕 [#66195](https://github.com/vllm-project/vllm/issues/66195) [Bug]: Block-FP8 Triton fused_moe_kernel fails to compile with Triton 3.9 since #64760 (`too many indices for tensor of rank 0` at `b_scale[None, :]`)
- [Bug] 🆕 [#66192](https://github.com/vllm-project/vllm/issues/66192) [Bug]: SM100 default prefill CUDA-graph grid (up to 8192 tokens, #63406) adds ~5 GiB/GPU graph memory and breaks max_model_len=256000 startup for Qwen3.8-2.4T-A95B-FP8 TP16 on GB200
