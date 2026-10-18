# LLM Serving Issue Radar

_Last run: 2026-10-18T13:26+00:00_

**10 issues** — sgl-project/sglang: 7, vllm-project/vllm: 3 — 🆕 **9 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#62257](https://github.com/vllm-project/vllm/issues/62257) [RFC]: Add Single-Process In-Memory Engine Mode for Low-Tier Sandbox Environments (Colab T4 / Jupyter)

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#62283](https://github.com/vllm-project/vllm/issues/62283) [Feature][KV Offload]: Require canonical_layout when a secondary tier shares KV across TP sizes (direct layout silently corrupts)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#45000](https://github.com/sgl-project/sglang/issues/45000) [Bug] FP8 block-quantized checkpoint on SM86 (FP8 Marlin) intermittently gives wrong tokens with the overlap scheduler; exact without it
- [Bug] 🆕 [#44999](https://github.com/sgl-project/sglang/issues/44999) [Bug] Marlin MoE (AWQ W4A16) on SM86 intermittently returns wrong expert outputs, even for a single request; the Triton WNA16 kernel is exact
- [Bug] 🆕 [#44998](https://github.com/sgl-project/sglang/issues/44998) [Bug] NVFP4 Marlin fallback (SM80-SM90) garbles every output when the block scales are small (vllm-project/vllm#34577 not ported)

## New Model Integration

### sgl-project/sglang

- [Feature] [#44885](https://github.com/sgl-project/sglang/issues/44885) [Feature] kv-shard: Pass Q instead of KV for short prefills with long cached prefixes

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#45002](https://github.com/sgl-project/sglang/issues/45002) [Bug] Client-controlled RID prefix allows cross-request abort through disconnect cleanup
- [Bug] 🆕 [#44997](https://github.com/sgl-project/sglang/issues/44997) [Bug] NGRAM speculative decoding corrupts radix-cached KV with the overlap scheduler when requests end on a stop token (0.5.22)

### vllm-project/vllm

- [Bug] 🆕 [#62304](https://github.com/vllm-project/vllm/issues/62304) [Bug]: Hybrid GDN models (Qwen3.5) with n-gram speculative decoding: greedy outputs go wrong when drafts are partly accepted; the GDN state misses the last accepted token's update

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#44959](https://github.com/sgl-project/sglang/issues/44959) [NPU] Please keep publishing Docker images for Ascend 910B
