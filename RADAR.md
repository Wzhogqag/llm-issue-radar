# LLM Serving Issue Radar

_Last run: 2026-09-23T13:29+00:00_

**16 issues** — sgl-project/sglang: 6, vllm-project/vllm: 10 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#40865](https://github.com/sgl-project/sglang/issues/40865) [RFC] Explicit, budgeted tail-replay for Mamba/GDN state in UnifiedRadixCache

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 [#40877](https://github.com/sgl-project/sglang/issues/40877) [SM120] Field report: DeepSeek-V4.1-Flash in production on 8x RTX PRO 6000 (PCIe, no NVLink) - working config, measured throughput, rejected topologies

### vllm-project/vllm

- [Feature] 🆕 [#58263](https://github.com/vllm-project/vllm/issues/58263) [Feature]: Bind batch-invariant mode into KV-offload namespaces and KV-connector compatibility checks
- [RFC] 🆕 [#58329](https://github.com/vllm-project/vllm/issues/58329) [RFC]: KVPP (KV pipeline parallel, LayerSplit) for vLLM

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#40903](https://github.com/sgl-project/sglang/issues/40903) [Bug] DeepSeek chunked-prefix prefill merges base-2 LSE into a natural-log merge_state_v2 (silent accuracy loss on every prefix-cache hit)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#40843](https://github.com/sgl-project/sglang/issues/40843) [Bug] Severe repetition and degenerate loops in reasoning/output when serving GLM-5.3 with DFLASH speculative decoding

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#58365](https://github.com/vllm-project/vllm/issues/58365) [Bug] `ep_gather` output store overflows int32 with DeepEP v2 expanded layout (IMA in `_fwd_kernel_ep_gather`)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#58353](https://github.com/vllm-project/vllm/issues/58353) [Bug]: Qwen2-VL video sampling divides by zero after rounding a one-frame clip to zero frames
- [other] 🆕 [#58303](https://github.com/vllm-project/vllm/issues/58303) [Bug/Perf]: the dense default chosen for Mamba + EAGLE reverts to 0% prefix reuse under interleaved long conversations

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#40809](https://github.com/sgl-project/sglang/issues/40809) [Bug] v0.5.19 tokenizer hang
- [Bug] 🆕 [#40808](https://github.com/sgl-project/sglang/issues/40808) [Bug] v0.5.19 can't decode image

### vllm-project/vllm

- [Bug] 🆕 [#58315](https://github.com/vllm-project/vllm/issues/58315) [Bug]: GLM required tool-call grammar accepts split marker tokens that the streaming parser treats as content
- [Performance] 🆕 [#58266](https://github.com/vllm-project/vllm/issues/58266) [Performance]: multimodal preprocessing is single-threaded per API server; a wider thread pool does not help (GIL) — process pool for _mm_executor?

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#58290](https://github.com/vllm-project/vllm/issues/58290) [Bug]: Multi-node TP=8 (2 nodes x 4 H200) hangs in ncclCommInitRank during startup — even local_rank ranks complete Init COMPLETE, odd ranks block in graph-connect phase
- [Feature] 🆕 [#58313](https://github.com/vllm-project/vllm/issues/58313) [Feature]: Request observer hook for the Rust frontend
- [other] 🆕 [#58270](https://github.com/vllm-project/vllm/issues/58270) [Installation]:  v0.30.0 CPU wheels now require manylinux_2_39 (glibc 2.39), breaking installation on Ubuntu 22.04/Rhel9
