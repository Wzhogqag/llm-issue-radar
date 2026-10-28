# LLM Serving Issue Radar

_Last run: 2026-10-28T13:24+00:00_

**8 issues** — sgl-project/sglang: 5, vllm-project/vllm: 3 — 🆕 **8 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#47021](https://github.com/sgl-project/sglang/issues/47021) [RFC]: Quota and global-eviction contract for HiCache L3 when the backend is a shared filesystem
- [RFC] 🆕 [#47019](https://github.com/sgl-project/sglang/issues/47019) [RFC] Decouple Scheduler Control from Forward Submission
- [other] 🆕 ⚠maintainer-authored [#46952](https://github.com/sgl-project/sglang/issues/46952) [HiCache] write_back eviction blocks the scheduler for hundreds of ms per call under steady load, lowering the prefix-cache hit rate compared with write_through

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#64175](https://github.com/vllm-project/vllm/issues/64175) [RFC]: Serve requests on top of an externally computed KV cache (PrecomputedKVConnector)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#47069](https://github.com/sgl-project/sglang/issues/47069) [Bug] dumper.step() is advanced per forward, so one EAGLE speculation round spans several dump steps

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#64192](https://github.com/vllm-project/vllm/issues/64192) [Feature]: Add an NVIDIA RTX PRO 6000 Blackwell  deployment recipe for DeepSeek-V4.1-Flash

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#47039](https://github.com/sgl-project/sglang/issues/47039) [Bug] deepseekv4.1-flash-1017: The receiving length for data has decreased.

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#64226](https://github.com/vllm-project/vllm/issues/64226) [Bug]: Rust vllm-bench saves ramp-up runs as fixed-rate results
