# LLM Serving Issue Radar

_Last run: 2026-10-26T14:47+00:00_

**15 issues** — sgl-project/sglang: 7, vllm-project/vllm: 8 — 🆕 **15 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Uncategorized](#uncategorized) — 2

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#63693](https://github.com/vllm-project/vllm/issues/63693) [Bug]: P/D disaggregation (NixlConnector): decode output differs from a non-disaggregated run whenever repetition_penalty != 1.0

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 [#63743](https://github.com/vllm-project/vllm/issues/63743) [Feature]: [Case Study] Agent Context Compaction Breaks RadixAttention Prefix Caching (10.1% -> 99.6% Hit Rate)

## Quantization

### sgl-project/sglang

- [other] 🆕 [#46588](https://github.com/sgl-project/sglang/issues/46588) [Roadmap] TDX/CC Prefill–Decode Disaggregation
- [other] 🆕 [#46579](https://github.com/sgl-project/sglang/issues/46579) [Roadmap] Humming integration maintenance
- [RFC] 🆕 [#46520](https://github.com/sgl-project/sglang/issues/46520) [RFC] [XPU] paged-experts: Intel XPU support with Lookahead Expert Scheduling (LES) and an SSD tier for iGPU, single-GPU MoE offload

### vllm-project/vllm

- [Bug] 🆕 [#63732](https://github.com/vllm-project/vllm/issues/63732) [Bug]: Gemma 4 + online --quantization fp8: image requests crash since v0.23.0 (FP8-cast pixel values reach quantized patch_embedder.input_proj); v0.22.0 works

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Performance] 🆕 [#63705](https://github.com/vllm-project/vllm/issues/63705) [Performance]: MiniMax-M2.7 throughput regression on TP4+EP in vLLM 0.29 0.31 0.32

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#46598](https://github.com/sgl-project/sglang/issues/46598) [Feature] Support reasoning and content continuation through model renderers/encoders
- [other] 🆕 [#46550](https://github.com/sgl-project/sglang/issues/46550) [MUSA][help]

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#46508](https://github.com/sgl-project/sglang/issues/46508) [Bug][MUSA] fa3: scheduler metadata is computed from the draft backend under speculative decoding, hanging when the radix cache hits

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#46566](https://github.com/sgl-project/sglang/issues/46566) [Bug] MiMoDetector: string "null" becomes None, invalid booleans become false, and text around tool calls is dropped

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#63751](https://github.com/vllm-project/vllm/issues/63751) [Bug]: IndexError in _create_chat_logprobs / _create_completion_logprobs (top_logprobs shorter than token_ids) causes 500s
- [RFC] 🆕 [#63734](https://github.com/vllm-project/vllm/issues/63734) [RFC]: Define a graceful-draining contract for external Kubernetes controllers

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#63744](https://github.com/vllm-project/vllm/issues/63744) [Feature]: [RFC / Performance] How LLM Agent Context Compaction Collapses Automatic Prefix Caching (APC)
- [other] 🆕 [#63741](https://github.com/vllm-project/vllm/issues/63741) [RFC / Performance] How LLM Agent Context Compaction Collapses Automatic Prefix Caching (APC)
