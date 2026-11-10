# LLM Serving Issue Radar

_Last run: 2026-11-10T13:22+00:00_

**11 issues** — sgl-project/sglang: 6, vllm-project/vllm: 5 — 🆕 **11 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#49517](https://github.com/sgl-project/sglang/issues/49517) [Bug] diffusion_num_queue_reqs does not reflect requests pending in the ZMQ transport

### vllm-project/vllm

- [RFC] 🆕 [#66751](https://github.com/vllm-project/vllm/issues/66751) [RFC]: Draft Window KV: Dual-Boundary Recovery and Sparse P/D Page Fill

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#49449](https://github.com/sgl-project/sglang/issues/49449) [EFA Product Quality Control]: Nightly multi-node E2E functionality, accuracy & performance testing for EFA NIXL and EFA Mooncake Store, EFA DeepEP

### vllm-project/vllm

- [other] 🆕 [#66713](https://github.com/vllm-project/vllm/issues/66713) [EFA Product Quality Control]: Nightly multi-node E2E functionality, accuracy & performance testing for EFA NIXL and EFA Mooncake Store, EFA DeepEP

## Attention Backend

### sgl-project/sglang

- [other] 🆕 [#49454](https://github.com/sgl-project/sglang/issues/49454) [Feat] kda: run the Kimi-K3 fused FlashInfer decode on a BF16 SSM state (NVIDIA SM100/103)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#49493](https://github.com/sgl-project/sglang/issues/49493) [Bug] Qwen4-Exp PLE: BF16 n-gram shards are cast to FP8 with a unit scale when the checkpoint's config sets ple_embedding_dtype (primitive-ai/Qwen3.8-Flash-Next-NVFP4)

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#66727](https://github.com/vllm-project/vllm/issues/66727) [Feature]: Release whl for torch 2.15.0 and cu134

## Sampling / Speculative Decoding

### vllm-project/vllm

- [RFC] 🆕 [#66753](https://github.com/vllm-project/vllm/issues/66753) [RFC]: Tree speculative decoding in vLLM

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#49541](https://github.com/sgl-project/sglang/issues/49541) [Bug] FA3 SM90 FP8 two-level accumulation rebuild is ~2.6x slower for paged head_dim=256
- [Bug] 🆕 [#49494](https://github.com/sgl-project/sglang/issues/49494) [Bug] scheduler_0 crashes with exit code -3 (SIGQUIT) during normal decode operation — no Python exception logged, likely C++ layer crash

### vllm-project/vllm

- [Bug] 🆕 [#66806](https://github.com/vllm-project/vllm/issues/66806) [Bug]: Investigate DeepSeek V4.1 producer prefill graph and replay output differences
