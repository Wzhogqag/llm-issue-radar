# LLM Serving Issue Radar

_Last run: 2026-11-23T13:24+00:00_

**13 issues** — sgl-project/sglang: 5, vllm-project/vllm: 8 — 🆕 **13 new** since last run

## Contents

- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Quantization

### sgl-project/sglang

- [other] 🆕 [#52523](https://github.com/sgl-project/sglang/issues/52523) [NPU] [Roadmap] Optimization of GLM-5.2 (DSA / sparse-MLA) inference on Ascend NPU
- [other] 🆕 [#52574](https://github.com/sgl-project/sglang/issues/52574) [NPU] [Roadmap] DeepSeek-V4.1 Ascend Development & Optimization
- [no-prefix] 🆕 ⚠no-prefix [#52506](https://github.com/sgl-project/sglang/issues/52506) DSPARK draft MoE crashes on SM120: HybridFp8NvFp4Config unconditionally uses TRT-LLM-gen (sm100-only cubins) for MTP layers

### vllm-project/vllm

- [Bug] 🆕 [#69377](https://github.com/vllm-project/vllm/issues/69377) [Bug][XPU][INC] ARK weight post-processing fragments the allocator (~9.5 GiB reserved, unused); Qwen3.6-27B-int4-AutoRound cannot boot on one 32 GB B70

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#69320](https://github.com/vllm-project/vllm/issues/69320) [Bug]: Transformers backend: OmniASR fails at startup because `padding_mask` is kept on CPU but forwarded to `get_audio_features`

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#69417](https://github.com/vllm-project/vllm/issues/69417) [Feature]: Support RWKV-7 (Goose) as a model plugin via the V1 Mamba state cache
- [Feature] 🆕 [#69391](https://github.com/vllm-project/vllm/issues/69391) [Feature]: Add native block-diffusion support for Clover-35B-A3B-Preview

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#52543](https://github.com/sgl-project/sglang/issues/52543) [Bug] multimodal_gen: Unfiltered `diffusers_kwargs` in `POST /v1/videos` allows validation bypass and GPU OOM

### vllm-project/vllm

- [Performance] 🆕 [#69418](https://github.com/vllm-project/vllm/issues/69418) [Performance]: Synchronized attention-page growth causes decode preemption on Qwen3.5 without MTP
- [Performance] 🆕 [#69408](https://github.com/vllm-project/vllm/issues/69408) [Performance]: Parallel sampling (n>1) is 10–14% slower in v0.34.0 than v0.28.0; n=1 unchanged
- [Perf] 🆕 [#69375](https://github.com/vllm-project/vllm/issues/69375) [Perf][Spec Decode] Support draft windows above 8 tokens in GDN/KDA spec-decode kernels (T=9 for DSpark, T=16 for DFlash/DSpine)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#69350](https://github.com/vllm-project/vllm/issues/69350) [Bug]: FlashInfer 0.7.6rc1 compatibility blocked by cuDNN Frontend <1.33 cap

## Uncategorized

### sgl-project/sglang

- [Feature] 🆕 [#52555](https://github.com/sgl-project/sglang/issues/52555) [Feature] How to use DeepEP transfer Engram fragments likely DeepInfer?
