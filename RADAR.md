# LLM Serving Issue Radar

_Last run: 2026-11-24T13:22+00:00_

**12 issues** — sgl-project/sglang: 4, vllm-project/vllm: 8 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 4
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#52854](https://github.com/sgl-project/sglang/issues/52854) [Bug] Scheduler deadlocks silently on VLM request admission with --mm-feature-transport cuda_ipc (TP>1): permanent engine hang, health-check restart
- [Bug] 🆕 [#52761](https://github.com/sgl-project/sglang/issues/52761) [Bug] [Diffusion] MiniMax-H3-Image does not start on a 24 GB GPU + 32 GB host (plain command and derived 4090 recipe)

### vllm-project/vllm

- [Bug] 🆕 [#69612](https://github.com/vllm-project/vllm/issues/69612) [Bug]: MoRIIO WRITE producer: preempted request's deferred write submits reallocated blocks
- [RFC] 🆕 [#69635](https://github.com/vllm-project/vllm/issues/69635) [RFC]: Engine-side time-to-first-token forecast for routers

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#52823](https://github.com/sgl-project/sglang/issues/52823) [Feature] HiCache: choose between L3 fetch and prefill from estimated completion times

### vllm-project/vllm

- [other] 🆕 [#69662](https://github.com/vllm-project/vllm/issues/69662) [KVConnector] Fall back to legacy IPC when the extensible KV cache is unavailable

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#69657](https://github.com/vllm-project/vllm/issues/69657) [Bug] rotary_embedding crashes the process with SIGFPE when num_tokens == 0 (0/0 at pos_encoding_kernels.cu:144)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [RFC] 🆕 [#69568](https://github.com/vllm-project/vllm/issues/69568) [RFC]: Grammar-as-a-Drafter (GaaD): Composing Grammar-Forced Tokens with Speculative Decoding

## Performance / Memory / OOM

### sgl-project/sglang

- [Feature] 🆕 [#52762](https://github.com/sgl-project/sglang/issues/52762) [Feature] diffusion: Q4 roadmap proposal: fast MiniMax-H3 image ↔ video switching on consumer GPUs

### vllm-project/vllm

- [RFC] 🆕 [#69590](https://github.com/vllm-project/vllm/issues/69590) [RFC] Fault Tolerance for RL Workloads in vLLM

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#69663](https://github.com/vllm-project/vllm/issues/69663) [Bug]: activation/gating ops accept non-contiguous inputs and silently compute wrong results; strided outputs leave unwritten cells and corrupt the parent buffer
- [Bug] 🆕 [#69661](https://github.com/vllm-project/vllm/issues/69661) [Bug]: --otlp-traces-endpoint sends no spans when another integration owns the global tracer provider
