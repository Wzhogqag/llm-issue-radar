# LLM Serving Issue Radar

_Last run: 2026-08-10T13:49+00:00_

**22 issues** — sgl-project/sglang: 8, vllm-project/vllm: 14 — 🆕 **22 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 5
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 ⚠maintainer-authored [#51608](https://github.com/vllm-project/vllm/issues/51608) [RFC]: Extensible Scheduler Plugin Framework for vLLM

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#51579](https://github.com/vllm-project/vllm/issues/51579) [Bug]: OffloadingConnector CPU tier leaks its /dev/shm mmap file on any unclean exit (including SIGKILL)
- [Bug] 🆕 [#51567](https://github.com/vllm-project/vllm/issues/51567) [Bug]: EPLB fails to transport E8M0 expert state
- [RFC] 🆕 [#51639](https://github.com/vllm-project/vllm/issues/51639) [RFC]: Generic Control RPC for KV Connectors

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#34260](https://github.com/sgl-project/sglang/issues/34260) [Bug] Kimi-K3 - sglang crash
- [Bug] 🆕 [#34259](https://github.com/sgl-project/sglang/issues/34259) [Bug] Kimi-K3 - cross prompt reasoning leakage

### vllm-project/vllm

- [Bug] 🆕 [#51658](https://github.com/vllm-project/vllm/issues/51658) [Bug]: attention backend probe in cuda.py catches only ImportError; non-ImportError side effects (e.g. cache PermissionError, CUDA runtime   mismatch) crash engine init instead of being recorded as unavailable

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#34192](https://github.com/sgl-project/sglang/issues/34192) [Bug] Llama4 NVFP4 MoE crashes on SM120/SM121: apply_router_weight_on_input is not supported for Flashinfer
- [no-prefix] 🆕 ⚠no-prefix [#34179](https://github.com/sgl-project/sglang/issues/34179) W4A4 MegaMoE FP4-acts on DeepSeek-V4-Flash-0731 (8x B200, SGLang v0.5.17): end-to-end TTFT unchanged on two serving shapes (scheduling-bound and GEMM-bound), plus bounded quality observations
- [RFC] 🆕 ⚠maintainer-authored [#34295](https://github.com/sgl-project/sglang/issues/34295) [RFC] Remove the torchao integration (`--torchao-config`)
- [no-prefix] 🆕 ⚠no-prefix [#34193](https://github.com/sgl-project/sglang/issues/34193) Where do CPU kernel patches go after sgl-kernel moved under sglang.kernels.aot?

### vllm-project/vllm

- [Bug] 🆕 [#51660](https://github.com/vllm-project/vllm/issues/51660) [Bug]: No viable structured-outputs backend for Kimi-K2.6 + EAGLE3 on v0.26.0: xgrammar bitmask desync kills the engine, outlines compile-timeout leaks threads until OOM, guidance rejects the slow tokenizer

## New Model Integration

### vllm-project/vllm

- [other] 🆕 [#51619](https://github.com/vllm-project/vllm/issues/51619) [New Model]: Support CrisperWhisper 2.0

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34239](https://github.com/sgl-project/sglang/issues/34239) [Bug] Qwen3.5-397B + NEXTN crashes with CUDA illegal memory access near 262144 context boundary on v0.5.16 (H800 TP8)
- [Bug] 🆕 [#34211](https://github.com/sgl-project/sglang/issues/34211) [Bug] [NPU] (v0.5.17)Eco-Tech/Qwen3.6-35B-A3B-w8a8 Model Served with four 910B: ValueError: Unsupported ModelSlim MoE schemes for layer mtp.layers.0.mlp.experts: W13='FLOAT', W2='FLOAT'

### vllm-project/vllm

- [Bug] 🆕 [#51571](https://github.com/vllm-project/vllm/issues/51571) [Bug]: Async MTP align mode reads accepted counts from mutable InputBatch rows

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#51679](https://github.com/vllm-project/vllm/issues/51679) [Bug]: qwen3_xml tool parser consumes `</think>`, merging reasoning into `content` with no way to split it
- [Bug] 🆕 [#51651](https://github.com/vllm-project/vllm/issues/51651) [Bug]: Missing `reasoning` on Some Turns in Multi-Turn Tool-Calling (DeepSeek-V4-Flash-0731)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#51677](https://github.com/vllm-project/vllm/issues/51677) [Bug]: NVML UUID resolution fails for NVIDIA's documented short-form CUDA_VISIBLE_DEVICES UUIDs
- [Bug] 🆕 [#51663](https://github.com/vllm-project/vllm/issues/51663) [Bug]: Massive output-token throughput regression since v0.24.0 with Qwen3.6-35B-A3B-FP8
- [Bug] 🆕 [#51580](https://github.com/vllm-project/vllm/issues/51580) [Bug]: [ROCm] v0.26.0 release image: NaN logits from AITER fused-MoE path on gfx942 (Qwen3.5-397B-A17B-FP8) — fixed on main, requesting 0.26.x backport
- [Bug] 🆕 [#51572](https://github.com/vllm-project/vllm/issues/51572) [Bug]:Anthropic Messages API: x-api-key authentication header not supported — only Authorization: Bearer works
