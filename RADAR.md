# LLM Serving Issue Radar

_Last run: 2026-08-12T13:51+00:00_

**20 issues** — sgl-project/sglang: 4, vllm-project/vllm: 16 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 5

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#34513](https://github.com/sgl-project/sglang/issues/34513) [RFC] Agent-aware session affinity without routing keys: a router policy

### vllm-project/vllm

- [Bug] 🆕 [#51921](https://github.com/vllm-project/vllm/issues/51921) [Bug] v0.27.0 engine permanently stalls after ~1 min idle on 4-node TP=4 (GB10/sm_121, aarch64): shm_broadcast writer starves, requests never reach scheduler

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 [#34510](https://github.com/sgl-project/sglang/issues/34510) [Tracking] PD disaggregation shared-protocol unification

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#51964](https://github.com/vllm-project/vllm/issues/51964) [Bug]:amd mi308x gpu, vllm 0.27.0~0.27.1, rocm 7.2.3, Kimi-K2.7-Coder start fails:AssertionError: mla_gluon requires gfx950 (CDNA4), got gfx942
- [Bug] 🆕 [#51920](https://github.com/vllm-project/vllm/issues/51920) [Bug] FlashInferMLASparseSM120Impl missing masked_mha_available: engine crash on sm_121 (GB10) at startup

## Quantization

### sgl-project/sglang

- [other] 🆕 [#34559](https://github.com/sgl-project/sglang/issues/34559) [NPU][Tracking] Ascend A5 MXFP8/MXFP4 Capability and Model Coverage

### vllm-project/vllm

- [Bug] 🆕 [#51971](https://github.com/vllm-project/vllm/issues/51971) [Bug]: Qwen3 MoE GPTQ `qzeros` shape mismatch on ROCm gfx1201
- [Bug] 🆕 [#51884](https://github.com/vllm-project/vllm/issues/51884) [Bug]: FP8 block-scaled weights fail on sm120 (RTX 5090) — DeepGEMM "Unknown SF transformation" during process_weights_after_loading

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#51929](https://github.com/vllm-project/vllm/issues/51929) [Feature]: Built-in watermarking support for EU AI Act Article 50(2)
- [RFC] 🆕 [#51940](https://github.com/vllm-project/vllm/issues/51940) [RFC]: Per-request activation of multiple LoRA adapters with static scales

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#51916](https://github.com/vllm-project/vllm/issues/51916) [Bug][DSV4-Flash][DSpark] v0.27 weight loader regressed — KeyError routed_experts.w13_weight_scale (v0.26 gracefully skipped)
- [Bug] 🆕 [#51902](https://github.com/vllm-project/vllm/issues/51902) [Bug]: H100 FA3 violates batch invariance when an unrelated prefill changes tiling

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#51912](https://github.com/vllm-project/vllm/issues/51912) [Feature]: Allow logging model output text without output token IDs
- [RFC] 🆕 [#51963](https://github.com/vllm-project/vllm/issues/51963) [RFC]: Report characters/second alongside tokens/second in vllm bench serve
- [RFC] 🆕 [#51948](https://github.com/vllm-project/vllm/issues/51948) [RFC]: Bounded-memory video sessions — KV retention for long-running streaming-input requests

## Build / Install / Platform

### sgl-project/sglang

- [RFC] 🆕 [#34562](https://github.com/sgl-project/sglang/issues/34562) [RFC] HIP/ROCm - Provide a bit-exact SWA prefix reuse for DeepSeek-V4 with unified_kv atten backend

### vllm-project/vllm

- [Bug] 🆕 [#51993](https://github.com/vllm-project/vllm/issues/51993) [Bug]: security: bump minimum setuptools version in requirements/common.txt
- [Bug] 🆕 [#51986](https://github.com/vllm-project/vllm/issues/51986) [Bug]: mnnvl allreduce workspace init hangs 30s and leaks GPU memory on IB-only multi-node
- [Bug] 🆕 [#51977](https://github.com/vllm-project/vllm/issues/51977) [Bug]: openai_harmony.HarmonyError: unexpected tokens remaining in message header on v0.26.0 (gpt-oss-120b)
- [Bug] 🆕 [#51975](https://github.com/vllm-project/vllm/issues/51975) [Bug]: Bugs in kimi-k3 docker image
