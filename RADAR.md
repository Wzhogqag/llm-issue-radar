# LLM Serving Issue Radar

_Last run: 2026-10-10T13:29+00:00_

**20 issues** — sgl-project/sglang: 4, vllm-project/vllm: 16 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 4
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### sgl-project/sglang

- [other] 🆕 [#43557](https://github.com/sgl-project/sglang/issues/43557) [PD] Runtime role switch: engine launched with --disaggregation-mode decode crashes with illegal memory access after decode -> prefill -> decode

### vllm-project/vllm

- [Bug] 🆕 [#60905](https://github.com/vllm-project/vllm/issues/60905) [Bug]: DeepSeek-V4-Pro returns wrong answers on long prompts (>~380k tokens) when --long-prefill-token-threshold=256 is set (v0.30.0)
- [Feature] 🆕 [#60947](https://github.com/vllm-project/vllm/issues/60947) [Feature]: Allow pooling tasks (token_embed / token_classify) to reuse prefix cache while returning full hidden-state sequences
- [RFC] 🆕 [#60986](https://github.com/vllm-project/vllm/issues/60986) [RFC]: Scheduler-owned KV transfer obligations: release blocks only after both recv and send complete

## Quantization

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#43526](https://github.com/sgl-project/sglang/issues/43526) [AMD][Bug] Accuracy issue with gfx942 block-FP8 linear AITER CK blockscale GEMM

### vllm-project/vllm

- [Bug] 🆕 [#60914](https://github.com/vllm-project/vllm/issues/60914) [Bug]: compressed-tensors MXFP4 MoE (`CutlassExpertsMxfp4`) crashes with an illegal memory access on GB200 (SM100) on main
- [Feature] 🆕 [#60944](https://github.com/vllm-project/vllm/issues/60944) [Feature]: Explicitly trust a selected preload daemon to avoid checkpoint rescans on engine restart
- [RFC] 🆕 [#60932](https://github.com/vllm-project/vllm/issues/60932) [RFC]: Peer-device expert tier: run a subset of routed experts on a second GPU in the same host (out-of-tree plugin first, then a small seam in RoutedExperts)
- [no-prefix] 🆕 ⚠no-prefix [#60931](https://github.com/vllm-project/vllm/issues/60931) WIP [RFC]: SupportsReload, a single post-load contract and reload verifier (follow-up to #59502)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#60928](https://github.com/vllm-project/vllm/issues/60928) [Bug]: Exception on a non-output TP rank is logged and the worker dequeues the next RPC, so ranks desync and collectives mispair (cross-node deadlock)
- [RFC] 🆕 [#60965](https://github.com/vllm-project/vllm/issues/60965) [RFC]: Support Internally Managed Elastic EP with the MP DP Backend

## New Model Integration

### sgl-project/sglang

- [other] 🆕 [#43519](https://github.com/sgl-project/sglang/issues/43519) [Roadmap][NPU][Multimodal] Model support and serving features (2026 Q4)

### vllm-project/vllm

- [other] 🆕 ⚠maintainer-authored [#60935](https://github.com/vllm-project/vllm/issues/60935) [Draft] [RFC]: Support dispatcher-native token dropping for MoE expert capacity

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#60981](https://github.com/vllm-project/vllm/issues/60981) [Bug]: ngram_gpu crashes with num_speculative_tokens_per_batch_size (assert num_speculative_tokens == self.k)
- [Bug] 🆕 [#60897](https://github.com/vllm-project/vllm/issues/60897) [Bug]: token_indices_to_sample underflows past the request's query start with PP > 1 spec decode
- [Bug] 🆕 [#60929](https://github.com/vllm-project/vllm/issues/60929) [Bug][Spec Decode]: DeepGEMM warm-up covers only the target model; speculator GEMMs JIT-load in the serving hot path

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#43486](https://github.com/sgl-project/sglang/issues/43486) [Bug]  DSV4.1 Flash + DSPARK: CUDA caching allocator exhausts GPU memory under sustained max-batch decode (OOM crash every 15–25 min), KV pool only 29% used

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#60985](https://github.com/vllm-project/vllm/issues/60985) [Performance]: Resize video frames while decoding to skip full-resolution copies

## Build / Install / Platform

### vllm-project/vllm

- [other] 🆕 [#60964](https://github.com/vllm-project/vllm/issues/60964) [Installation]:
- [RFC] 🆕 [#60904](https://github.com/vllm-project/vllm/issues/60904) [RFC]: A standard for MonoKernels in vllm/models
