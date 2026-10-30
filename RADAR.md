# LLM Serving Issue Radar

_Last run: 2026-10-30T13:24+00:00_

**10 issues** — sgl-project/sglang: 2, vllm-project/vllm: 8 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#47397](https://github.com/sgl-project/sglang/issues/47397) SGLANG_JIT_DEEPGEMM_FAST_WARMUP on DeepSeek-V4.1: 3-5x faster cold start, no runtime degradation detectable at chunked-prefill 16384

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#64680](https://github.com/vllm-project/vllm/issues/64680) [Bug]: ROCM_AITER_FA crashes with draft_model/EAGLE drafters in extend_forward (None prefix in merge_attn_states; cp_mha_gather_cache illegal address)
- [Bug] 🆕 [#64639](https://github.com/vllm-project/vllm/issues/64639) [Bug]: 0.30.0 kimi-k3 PD分离  使用MLA-Block5草稿模型版本接收率基本为0

## Quantization

### vllm-project/vllm

- [RFC] 🆕 [#64725](https://github.com/vllm-project/vllm/issues/64725) [RFC]: Integrating LeapQuant into vLLM — INT8 Quantization of GDN/KDA Linear Attention Recurrent States
- [other] 🆕 ⚠maintainer-authored [#64632](https://github.com/vllm-project/vllm/issues/64632) [Tracking] Muse Spark Open Improvement

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#64713](https://github.com/vllm-project/vllm/issues/64713) [Feature]: Add an NVIDIA RTX PRO 6000 Blackwell deployment recipe for DeepSeek-V4-Flash-Vision-Exp

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#64679](https://github.com/vllm-project/vllm/issues/64679) [Bug]: fuse_rope_kvcache breaks draft_model/EAGLE spec decode when the drafter's attention shape differs from the target's (ROCm)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#47399](https://github.com/sgl-project/sglang/issues/47399) [Bug] [NPU] 图模式下走Fia v2算子，torch_npu.npu_fused_infer_attention_score_v2函数入参错误

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#64714](https://github.com/vllm-project/vllm/issues/64714) [Bug]:
- [Bug] 🆕 [#64664](https://github.com/vllm-project/vllm/issues/64664) [Bug][ROCm] vLLM fails to detect AMD GPU in WSL when AMDSMI cannot initialize
