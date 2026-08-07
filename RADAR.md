# LLM Serving Issue Radar

_Last run: 2026-08-07T13:46+00:00_

**11 issues** — sgl-project/sglang: 4, vllm-project/vllm: 7 — 🆕 **11 new** since last run

## Contents

- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33943](https://github.com/sgl-project/sglang/issues/33943) [Bug] DeepSeek-V4 DSpark draft crashes on SM120 because topk=192 misses FlashInfer decode dispatch
- [Bug] 🆕 [#33915](https://github.com/sgl-project/sglang/issues/33915) [Bug] FlashInfer backend drops attn_logit_softcapping: the cap is passed to the deprecated forward() instead of plan(), so gemma-2 and grok-1 run uncapped
- [Bug] 🆕 [#33967](https://github.com/sgl-project/sglang/issues/33967) [Bug] It is defined as int32 in SGLang, but the kernel within `ascend_backend` reads it as int64, leading to incorrect memory‑address access.

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#33978](https://github.com/sgl-project/sglang/issues/33978) [Bug]

### vllm-project/vllm

- [Bug] 🆕 [#51326](https://github.com/vllm-project/vllm/issues/51326) [Bug]: DeepSeek-V4-Flash-0731 produces corrupted output on H100 TP8+EP with vLLM 0.26.0
- [Bug] 🆕 [#51297](https://github.com/vllm-project/vllm/issues/51297) [Bug]: Qwen3.5 122b a10 model RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#51340](https://github.com/vllm-project/vllm/issues/51340) [Bug]: kernel_warmup() has no inter-rank synchronization between stages that issue real TP/EP collectives, causing startup hangs on multi-node deployments

## Sampling / Speculative Decoding

### vllm-project/vllm

- [other] 🆕 ⚠maintainer-authored [#51303](https://github.com/vllm-project/vllm/issues/51303) [Tracking][Spec Decode] Adaptive DSpark Bring-Up Tracker

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#51376](https://github.com/vllm-project/vllm/issues/51376) [Bug]: Qwen3-ASR `/v1/realtime` returns previous transcription on silence/noise under KV reuse
- [Bug] 🆕 [#51374](https://github.com/vllm-project/vllm/issues/51374) [Bug]: Qwen3-ASR `/v1/realtime` second utterance copies previous transcription under KV reuse
- [Bug] 🆕 [#51286](https://github.com/vllm-project/vllm/issues/51286) [Bug]: FA4 SM100 split-KV kernels fail to compile with `TYPE_UNSTABLE_JOIN` (nvidia-cutlass-dsl 4.6.0 pin) — crashes Kimi-K3 startup during CuTeDSL warmup
