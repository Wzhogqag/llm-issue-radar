# LLM Serving Issue Radar

_Last run: 2026-07-20T14:00+00:00_

**24 issues** — sgl-project/sglang: 7, vllm-project/vllm: 17 — 🆕 **24 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 5

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#31779](https://github.com/sgl-project/sglang/issues/31779) [RFC] An NPU-Native, Sparsity-Driven KV Offloading SubSystem for Efficient LLM Decoding

### vllm-project/vllm

- [Bug] 🆕 [#49097](https://github.com/vllm-project/vllm/issues/49097) [Bug]: PRIORITY scheduling can silently skip a running request for a full step when the preemption victim was already deferred earlier in the same schedule() call

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#31774](https://github.com/sgl-project/sglang/issues/31774) [RFC] Backend, KV dtype and platform compatibility is checked case by case, and the responses are inconsistent

### vllm-project/vllm

- [Bug] 🆕 [#49125](https://github.com/vllm-project/vllm/issues/49125) [Bug]: Stale partial prefix-cache hash resurrected into the cache after full-block promotion

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31740](https://github.com/sgl-project/sglang/issues/31740) [Bug] Error in starting kimi-k2.6 nvfp4 model in release v0.5.15: CUBLAS_STATUS_EXECUTION_FAILED.
- [Bug] 🆕 [#31720](https://github.com/sgl-project/sglang/issues/31720) [Bug] Qwen3.6-27B (hybrid GDN) + AWQ degenerates on few-shot / multi-turn prompts at temperature 0; same checkpoint is clean on vLLM
- [other] 🆕 ⚠maintainer-authored [#31783](https://github.com/sgl-project/sglang/issues/31783) [Roadmap] Quantization 2026 H2

### vllm-project/vllm

- [Bug] 🆕 [#49200](https://github.com/vllm-project/vllm/issues/49200) [Bug]: Kimi-K2.5 (compressed-tensors/int4) crashes with `ValueError: Mismatched mO.strides[0]` in FA4 CuTe MLA prefill context-chunk on Blackwell (long context)
- [Bug] 🆕 [#49165](https://github.com/vllm-project/vllm/issues/49165) [Bug] Deepseek-V4-Pro corruption: H100 multi-rank startup can select a FlashInfer block-FP8 path with a cold JIT cache race
- [Feature] 🆕 [#49198](https://github.com/vllm-project/vllm/issues/49198) [Feature]: Recency-based progressive mixed-precision KV cache

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#49101](https://github.com/vllm-project/vllm/issues/49101) [Bug]: Failed: Cuda error /workspace/csrc/custom_all_reduce.cuh:455 'invalid argument'
- [Bug] 🆕 [#49105](https://github.com/vllm-project/vllm/issues/49105) [Bug]: inkling bf16 h20*2 start failed with vllm/vllm-openai:inkling

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#31766](https://github.com/sgl-project/sglang/issues/31766) [Bug] fd exhaustion on the prefill side

### vllm-project/vllm

- [Bug] 🆕 [#49197](https://github.com/vllm-project/vllm/issues/49197) [Bug]: Beam Search is slower by a factor of 1000
- [Bug] 🆕 [#49112](https://github.com/vllm-project/vllm/issues/49112) [Bug]: Speculative decoding with a hybrid draft model (LFM2/LFM2.5 short_conv) fails — drafter requires all draft layers in one KV cache group

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#49205](https://github.com/vllm-project/vllm/issues/49205) [Bug]: StreamingParserEngine leaks a bare tag fragment (e.g. '<tool_') into content when a PreLexedTerminal supersedes a buffered text-token prefix of the same tag
- [Bug] 🆕 [#49116](https://github.com/vllm-project/vllm/issues/49116) [Bug]: Transcription streaming uses Chat Completions SSE format instead of OpenAI transcript events
- [Bug] 🆕 [#49103](https://github.com/vllm-project/vllm/issues/49103) [Bug]: Latest vllm is incompatible with `openai<2.25.0`

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#49182](https://github.com/vllm-project/vllm/issues/49182) [Bug]: vLLM serving Qwen3.6-27B with multimodal inputs causes InternalServerError due to CUDA OOM despite sufficient GPU memory

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#31763](https://github.com/sgl-project/sglang/issues/31763) How should I configure the service to make the model return tool calls that comply with the OpenAI standard instead of XML format?

### vllm-project/vllm

- [Bug] 🆕 [#49203](https://github.com/vllm-project/vllm/issues/49203) [Bug]: Qwen3.6-35B-A3B (GDN hybrid) intermittently livelocks under load on GB10/SM121 — GPU 96% util, 0 tok/s, no crash, no Xid
- [Bug] 🆕 [#49141](https://github.com/vllm-project/vllm/issues/49141) [Bug]: Fused_moe dimension mismatch for Qwen mxfp4 model on ROCM
- [Bug] 🆕 [#49122](https://github.com/vllm-project/vllm/issues/49122) [Bug]: AriaForConditionalGeneration produces incoherent garbage output at tensor-parallel size > 1 (reproduces on CPU, no GPU/accelerator needed)
- [Bug] 🆕 [#49106](https://github.com/vllm-project/vllm/issues/49106) [Bug]: False positive warning "Unexpected gate/up projection names" for non-gated MoE (Nemotron 3 Ultra / Nemotron H)
