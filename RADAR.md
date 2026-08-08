# LLM Serving Issue Radar

_Last run: 2026-08-08T13:34+00:00_

**25 issues** — sgl-project/sglang: 9, vllm-project/vllm: 16 — 🆕 **23 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 6
- [New Model Integration](#new-model-integration) — 4
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#34112](https://github.com/sgl-project/sglang/issues/34112) [Bug] Cancelling the tail request in a chunked-prefill batch still leaks one visible token and leaves negative scheduler output ids
- [Bug] 🆕 [#34003](https://github.com/sgl-project/sglang/issues/34003) [Bug] [NPU] Qwen3.5 model does not work in dynamic CPP scenario with radix cache

### vllm-project/vllm

- [RFC] 🆕 [#51439](https://github.com/vllm-project/vllm/issues/51439) [RFC]: [TieredOffloading][Performance] Tiered Lookup Resolution

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#51401](https://github.com/vllm-project/vllm/issues/51401) [Bug]: VLLM silently ignores falsey yaml configuration options
- [RFC] 🆕 [#51428](https://github.com/vllm-project/vllm/issues/51428) [RFC]: Programmatic Session-Aware KV Cache Management

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#34111](https://github.com/sgl-project/sglang/issues/34111) [Bug] A cancelled grammar-constrained overlap request can still emit visible text before abort
- [Bug] 🆕 [#33985](https://github.com/sgl-project/sglang/issues/33985) [Bug] DSpark speculative decoding cannot start on SM120: decode-dsv4 has no topk=192 instantiation, so verify falls through to the prefill kernel's num_tokens > 64 assert

### vllm-project/vllm

- [Bug] 🆕 [#51386](https://github.com/vllm-project/vllm/issues/51386) [Bug]: MooncakeStoreConnector produces N× write amplification under DCP for MLA models

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#34110](https://github.com/sgl-project/sglang/issues/34110) [Bug] MiniMax-H3 Ref2VA consistently produces snow/noise on SGLang 0.5.17 with L40S offload
- [Bug] [#33978](https://github.com/sgl-project/sglang/issues/33978) [Bug]

### vllm-project/vllm

- [Performance] 🆕 [#51494](https://github.com/vllm-project/vllm/issues/51494) [Performance] MiniMax-M3-NVFP4 on 8x B200, first numbers after the #48929 correctness fix: 1M real-prose envelope, EAGLE3 2.1-2.3x decode
- [Bug] 🆕 [#51456](https://github.com/vllm-project/vllm/issues/51456) [Bug]: online FP8 (--quantization fp8) produces corrupted, non-EOS-terminating output on Qwen2.5-1.5B-Instruct
- [Performance] 🆕 [#51454](https://github.com/vllm-project/vllm/issues/51454) [Performance] DP8 vs TP8 for single-KV-head MLA: 7.7x KV, 3.7x faster 1M TTFT at c=8 (DeepSeek-V4-Flash-0731, 8x B200, vLLM v0.25.0)
- [Bug] 🆕 [#51441](https://github.com/vllm-project/vllm/issues/51441) [Bug]: Hybrid sparse attention + Eagle results in full cache miss for certain prompt lengths

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#34092](https://github.com/sgl-project/sglang/issues/34092) [Feature] Support config.json from transformers > 4.57 for DeepSeek V4

### vllm-project/vllm

- [Bug] 🆕 [#51405](https://github.com/vllm-project/vllm/issues/51405) [Bug]: Inkling (InklingForConditionalGeneration) fails on SM120 — tml_fa4 attention lacks paged-KV support
- [Bug] 🆕 [#51396](https://github.com/vllm-project/vllm/issues/51396) [Bug]: cpu_offload_gb silently no-ops on Model Runner V2 — offloader never installed, model loads fully on-GPU with no warning
- [other] 🆕 [#51497](https://github.com/vllm-project/vllm/issues/51497) [New Model]: nvidia/LocateAnything-3B (slow autoregressive mode first)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34113](https://github.com/sgl-project/sglang/issues/34113) [Bug] Stock `/abort_request` returns HTTP 200 even though the later abort path fails with `AttributeError`
- [Bug] 🆕 [#34000](https://github.com/sgl-project/sglang/issues/34000) [Bug] Multi-output diffusion rollout: per-sample trajectories collapse to output 0, grouped forward AttributeError, provided latents skip packing

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#51465](https://github.com/vllm-project/vllm/issues/51465) [Bug]: Kimi K3 usage.prompt_tokens over-counts trailing channel-open stub (+3)
- [Bug] 🆕 [#51399](https://github.com/vllm-project/vllm/issues/51399) [Bug]: Kimi K3 tool parser streams the raw <|close|>message<|sep|> marker into content
- [Bug] 🆕 [#51387](https://github.com/vllm-project/vllm/issues/51387) [Bug]: Inkling: trailing <|end_message|> leaks into content on plain-text turns when tools are enabled (every post-tool-result synthesis turn)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#51467](https://github.com/vllm-project/vllm/issues/51467) [Bug]: DeepSeek-V4-Flash-0731 `response_format` (structured output) crashes the vLLM EngineCore — `apply_grammar_bitmask` tensor size mismatch (4040 vs 4041)
- [Bug] [#51376](https://github.com/vllm-project/vllm/issues/51376) [Bug]: Qwen3-ASR `/v1/realtime` returns previous transcription on silence/noise under KV reuse
