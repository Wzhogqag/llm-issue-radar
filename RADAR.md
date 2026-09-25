# LLM Serving Issue Radar

_Last run: 2026-09-25T13:29+00:00_

**16 issues** — sgl-project/sglang: 2, vllm-project/vllm: 14 — 🆕 **15 new** since last run

## Contents

- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 5
- [Uncategorized](#uncategorized) — 1

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#58627](https://github.com/vllm-project/vllm/issues/58627) [Bug][DSA] Complete sparse top-k output after DeepSelect detects a NaN
- [no-prefix] 🆕 ⚠no-prefix [#58616](https://github.com/vllm-project/vllm/issues/58616) vllm serve segfaults deterministically right after weight loading (single L4 GPU, V1 engine) — only avoided by VLLM_TRACE_FUNCTION=1

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#58636](https://github.com/vllm-project/vllm/issues/58636) [Bug]: GLM-5.x sparse indexer: the replicated key norm is autotuned per rank, so TP ranks can select different candidates and greedy completions change from launch to launch

## New Model Integration

### sgl-project/sglang

- [Feature] [#41129](https://github.com/sgl-project/sglang/issues/41129) [Feature] Support configurable retention for request log files

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#58694](https://github.com/vllm-project/vllm/issues/58694) [Bug]: Guidance feature gate mistakes property names and literal data for `patternProperties`
- [Bug] 🆕 [#58692](https://github.com/vllm-project/vllm/issues/58692) [Bug]: Dynamic SD (num_speculative_tokens_per_batch_size) + MTP on V2 runner crashes with ZeroDivisionError in SpeculatorCudaGraphManager._init_candidates
- [other] 🆕 [#58644](https://github.com/vllm-project/vllm/issues/58644) [CI] test_mtp_sharded_sampling_equivalence diverges intermittently (2 failures on 2026-09-24)
- [no-prefix] 🆕 ⚠no-prefix [#58677](https://github.com/vllm-project/vllm/issues/58677) Speculative-decoding draft model (EAGLE/MTP head) compile cache key flips between two values with byte-identical startup args — shared `VllmConfig` mutated in-place during main-model full-compile startup (v0.27.1; deterministic on 0.29)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#58640](https://github.com/vllm-project/vllm/issues/58640) [Bug]: When using the V4 parser in vLLM to parse outputs from DeepSeek V4.1 Flash, the leading extra space in V4.1 DSML tags breaks state machine matching and parameter regex, filters arg deltas, and prevents streaming return of tool call arguments.

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#58624](https://github.com/vllm-project/vllm/issues/58624) [Performance]: MoE decode ~15% slower on SM12x since #56876 (DeepGEMM contiguous-layout alignment 128 instead of 64)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#41192](https://github.com/sgl-project/sglang/issues/41192) [Bug] Diffusion Qwen-Image-2.1: TP=2 output corrupted with dense chroma speckle (single-GPU clean; vLLM-Omni TP=2 shows the identical corruption)

### vllm-project/vllm

- [Bug] 🆕 [#58688](https://github.com/vllm-project/vllm/issues/58688) [Bug][ROCm]: Qwen3.8-Flash-Next-FP8 cannot load on ROCm, the AMD Qwen4ExpNGramEmbedding has no FP8 weight_scale
- [Performance] 🆕 [#58639](https://github.com/vllm-project/vllm/issues/58639) [Performance][ROCm] V2 runner PP side streams make gfx1201 (RDNA4) forward ~2× slower; main-stream option fixes it
- [RFC] 🆕 [#58697](https://github.com/vllm-project/vllm/issues/58697) [RFC]: Shared JSON Schema structure for structured-output checks and transformations
- [other] 🆕 [#58606](https://github.com/vllm-project/vllm/issues/58606) [ROCm][Perf][Tracking Issue]: Hy4-Preview

## Uncategorized

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#58657](https://github.com/vllm-project/vllm/issues/58657) Use-case proposal: payment-gated self-hosted vLLM for agents (HTTP 402 + Nano)
