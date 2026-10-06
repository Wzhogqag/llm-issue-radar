# LLM Serving Issue Radar

_Last run: 2026-10-06T13:33+00:00_

**12 issues** — sgl-project/sglang: 3, vllm-project/vllm: 9 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#42653](https://github.com/sgl-project/sglang/issues/42653) [Bug] `--enable-unified-memory` on a hybrid-SWA model kills the scheduler, `alloc_token_slots` raises "Out of memory"

### vllm-project/vllm

- [Bug] 🆕 [#60137](https://github.com/vllm-project/vllm/issues/60137) [Bug]: Paused streaming sessions deadlock the scheduler when the KV cache is full
- [Feature] 🆕 [#60184](https://github.com/vllm-project/vllm/issues/60184) [Feature]: vllm run-batch --resume to continue an interrupted batch

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#60205](https://github.com/vllm-project/vllm/issues/60205) [Bug]: [KV Offload][P2P] After a peer's EngineCore stalls ~45 s, P2P transfers to and from it fail permanently, although the control session reconnects
- [Bug] 🆕 [#60189](https://github.com/vllm-project/vllm/issues/60189) [Bug]: NIXL DCP config checks don't apply to NixlPullConnector
- [Bug] 🆕 [#60124](https://github.com/vllm-project/vllm/issues/60124) [Bug][KV Connector] MultiConnector on prefill silently disables the hybrid KV cache manager, so a NixlConnector decode rejects every transfer with an opaque "NIXL compatibility hash mismatch"

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#60174](https://github.com/vllm-project/vllm/issues/60174) [Bug] DFlash2/DSpark + prefix caching corrupt output after a cache hit on Qwen3.8-27B NVFP4 (compressed-tensors) on 0.30/0.31; 0.29, FP8 target and MTP are fine

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#42672](https://github.com/sgl-project/sglang/issues/42672) [Bug] NPU HiCache: MHATokenToKVPoolHost crashes when the device k_buffer is a single tensor (since #40326)

### vllm-project/vllm

- [Feature] 🆕 [#60138](https://github.com/vllm-project/vllm/issues/60138) [Feature]: Reload speculative draft model weights from a new checkpoint at runtime (online speculator updates)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#42752](https://github.com/sgl-project/sglang/issues/42752) [CI] Flaky tests and CI infrastructure failures seen while babysitting PRs

### vllm-project/vllm

- [Bug] 🆕 [#60212](https://github.com/vllm-project/vllm/issues/60212) [Bug]: DeepStream video backend raises ZeroDivisionError on MP4s with moov at the end, and truncates fragmented MP4s

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#60160](https://github.com/vllm-project/vllm/issues/60160) [Bug][ROCm] Qwen3.8-27B-FP8 (TP4, MI355X) accuracy collapses at high concurrency with `VLLM_ROCM_USE_AITER=1`; fine with AITER off
