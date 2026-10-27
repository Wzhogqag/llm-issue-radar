# LLM Serving Issue Radar

_Last run: 2026-10-27T13:36+00:00_

**16 issues** — sgl-project/sglang: 6, vllm-project/vllm: 10 — 🆕 **16 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#64048](https://github.com/vllm-project/vllm/issues/64048) [Bug]: NixlConnector P/D on GH200 returns garbage when the KV cache base is 4 GiB-aligned (dma-buf MR wraps); UCX_CUDA_COPY_DMABUF=no avoids it
- [Bug] 🆕 [#64005](https://github.com/vllm-project/vllm/issues/64005) [Bug][MRV2] Qwen3-32B BF16 TP=2 emits only token ID 0 on v0.28.0; MRV1 works
- [Bug] 🆕 [#63997](https://github.com/vllm-project/vllm/issues/63997) [Bug]: NixlConnector fails at startup with "KV cache view cannot be partitioned into NIXL regions" when KV cache groups have different block sizes (Gemma 4)
- [Feature] 🆕 [#63968](https://github.com/vllm-project/vllm/issues/63968) [Feature] Per-request KV block visibility (deny list) for role-scoped RAG

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#46798](https://github.com/sgl-project/sglang/issues/46798) [Bug] [SM120]DeepSeek v4.1 flash Unstable FullTopK index order in C1 and C2 decode

### vllm-project/vllm

- [Performance] 🆕 [#64058](https://github.com/vllm-project/vllm/issues/64058) [Performance]: FA3 runs long decodes without split-KV whenever a prefill chunk shares the batch
- [Performance] 🆕 [#63958](https://github.com/vllm-project/vllm/issues/63958) [Performance]: SM120 FP8 KV cache prefill: widening the referenced pages to BF16 once and running BF16 FA2 is about 1.5× faster than FlashInfer's FP8-K/V FA2 path

## Quantization

### vllm-project/vllm

- [other] 🆕 [#64018](https://github.com/vllm-project/vllm/issues/64018) [ROCm][AMD] Muse Spark Open PTPC-FP8 gfx942 Performance Optimization
- [RFC] 🆕 [#64002](https://github.com/vllm-project/vllm/issues/64002) [RFC] [DSV4.1] [Engram]: Share immutable host-backed Engram tables across independent instances

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#63983](https://github.com/vllm-project/vllm/issues/63983) [Bug]: FunctionGemma tool parser drops every non-string argument (numbers, booleans, arrays, objects)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#46803](https://github.com/sgl-project/sglang/issues/46803) [Bug] FlashInfer `cascade` module JIT-compiles inside the first prefixed request (~4.5 s) on pip installs
- [Bug] 🆕 [#46752](https://github.com/sgl-project/sglang/issues/46752) [Bug] DSPARK/DFLASH speculative decoding silently ignores repetition_penalty / frequency_penalty / presence_penalty
- [Bug] 🆕 [#46742](https://github.com/sgl-project/sglang/issues/46742) [Bug] qwen3.8-27b says "let me look at the file" but emits no tool call, then concludes without evidence (thinking-only / tool-call dropped)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#64012](https://github.com/vllm-project/vllm/issues/64012) [Bug]: v0.19.0 qwen3_xml corrupts separate tool calls across chunk boundaries (legacy/backport)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#46831](https://github.com/sgl-project/sglang/issues/46831) [Bug] ROCm DCP-PD allocator reserve growth precedes HIP resource aborts under burst load
- [Bug] 🆕 [#46829](https://github.com/sgl-project/sglang/issues/46829) [Bug] ROCm absorb-BMM hand config aborts Triton compilation at M=256 on gfx950
