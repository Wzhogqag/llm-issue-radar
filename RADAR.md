# LLM Serving Issue Radar

_Last run: 2026-08-18T13:32+00:00_

**20 issues** — sgl-project/sglang: 5, vllm-project/vllm: 15 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#35241](https://github.com/sgl-project/sglang/issues/35241) [Bug] PrefillDelayer can enter a persistent mixed-state feedback loop and collapse prefill progress under DP Attention + chunked prefill

### vllm-project/vllm

- [Bug] 🆕 [#52693](https://github.com/vllm-project/vllm/issues/52693) [Bug] Streaming input: zero-token continuation crashes EngineCore (Invalid request status: RUNNING) — client-triggerable via temperature>0 chat sessions
- [Feature] 🆕 [#52727](https://github.com/vllm-project/vllm/issues/52727) [Feature]: Low-overhead asynchronous early-exit checks & KV-cache reclamation for Continuous Batching

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#35229](https://github.com/sgl-project/sglang/issues/35229) [Bug] Anthropic /v1/messages drops PD bootstrap fields during AnthropicMessagesRequest → ChatCompletionRequest conversion

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#35242](https://github.com/sgl-project/sglang/issues/35242) [Bug] qwen3.8-27b toolcall error

### vllm-project/vllm

- [Bug] 🆕 [#52768](https://github.com/vllm-project/vllm/issues/52768) [Bug]: Gemma4 crashes at startup in v0.27.1 with `AmbiguousGlobalPerLayerAttributeError`
- [Bug] 🆕 [#52732](https://github.com/vllm-project/vllm/issues/52732) [Bug] DeepseekV4 cannot start on sm_121 (GB10): unguarded DeepGEMM call, and CutlassScaledMM.is_supported() ignores compute capability
- [Bug] 🆕 [#52715](https://github.com/vllm-project/vllm/issues/52715) [Bug]: Weight-only int8 MoE fails at every group_size under --quantization moe_wna16
- [Bug] 🆕 [#52714](https://github.com/vllm-project/vllm/issues/52714) [Bug]: CompressedTensorsWNA16MoEMethod rejects grouped int8 MoE checkpoints (regression)
- [Bug] 🆕 [#52682](https://github.com/vllm-project/vllm/issues/52682) [Bug]: Qwen3.8-27B-FP8 hangs indefinitely at startup during CUDA-graph capture on Ampere (RTX A5000, TP=4) — fixed by --enforce-eager

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#52710](https://github.com/vllm-project/vllm/issues/52710) [Bug]: Missing `has_cutedsl()` guard in `DeepseekCompressor` (head_dim == 512 path)
- [Bug] 🆕 [#52667](https://github.com/vllm-project/vllm/issues/52667) [Bug][PaliGemma] Image embeddings remain inverse-scaled after Gemma input scaling change
- [Performance] 🆕 [#52744](https://github.com/vllm-project/vllm/issues/52744) [Performance]: DeepEP v2 (ElasticBuffer) finalize_async runs combine synchronously — the shared-expert overlap window is never used

## New Model Integration

### vllm-project/vllm

- [RFC] 🆕 [#52689](https://github.com/vllm-project/vllm/issues/52689) [RFC]: support rl feature : weight checker

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#35324](https://github.com/sgl-project/sglang/issues/35324) [Bug] Intermittent CUDA device-side crash with DSPARK speculative decoding on DeepSeek-V4-Flash-0731

### vllm-project/vllm

- [Bug] 🆕 [#52767](https://github.com/vllm-project/vllm/issues/52767) [Bug]: MTP spec decode still advances the grammar matcher after termination when a structural tag is built (residual after #44297)
- [Bug] 🆕 [#52735](https://github.com/vllm-project/vllm/issues/52735) [Bug]: OffloadingConnector stores but never serves when MTP/EAGLE speculative decoding is enabled (hybrid GDN model, XPU)
- [Feature] 🆕 [#52673](https://github.com/vllm-project/vllm/issues/52673) [Feature]: Detect and break exact repeating loops inside reasoning sections (spec-decode-aware ThinkingLoopBreaker)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#52761](https://github.com/vllm-project/vllm/issues/52761) [Bug]: deepseek-v4-flash-0731: Pipeline parallelism is not supported for this model.

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#35301](https://github.com/sgl-project/sglang/issues/35301) https://github.com/sgl-project/sglang/issues/10038[Bug]
