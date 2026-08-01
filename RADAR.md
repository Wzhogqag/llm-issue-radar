# LLM Serving Issue Radar

_Last run: 2026-08-01T13:53+00:00_

**13 issues** — sgl-project/sglang: 7, vllm-project/vllm: 6 — 🆕 **13 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#50630](https://github.com/vllm-project/vllm/issues/50630) No capability flag declares which KV-cache kinds may be peeked past a candidate boundary — each margin implementation excludes Mamba by hand

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33134](https://github.com/sgl-project/sglang/issues/33134) [Bug] DeepSeek-V4-Flash-0731 DSPARK on 2x DGX Spark (sm_121, TP=2): sparse-MLA prefill rejects topk=192 (config index_topk=512; kernel buckets 128/512/1024/2048)

### vllm-project/vllm

- [Bug] 🆕 [#50603](https://github.com/vllm-project/vllm/issues/50603) [Bug]: gfx1100 (RDNA3): first-call non-determinism + long-seq corruption from Triton paged-attention fallback (ROCm 7.14)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#33163](https://github.com/sgl-project/sglang/issues/33163) [Bug] deepseek-v4-flash toolcall error runner_backend from marlin to  flashinfer_mxfp4

### vllm-project/vllm

- [Bug] 🆕 [#50679](https://github.com/vllm-project/vllm/issues/50679) [Bug]: fused_qk_rmsnorm compile error on rocm

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#33181](https://github.com/sgl-project/sglang/issues/33181) [Bug] Inkling reasoning parser leaks the tool name into visible content when a turn opens with a tool call

## New Model Integration

### vllm-project/vllm

- [other] 🆕 [#50672](https://github.com/vllm-project/vllm/issues/50672) [Installation]:vllm-openai:kimi-k3 cpuoffloadgb not support?

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#50615](https://github.com/vllm-project/vllm/issues/50615) [Bug]: DSpark spec decode dies in profile_run — forward_mqa warmup asserts topk_indices_buffer, which a drafter never has (regression from #50298)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#33185](https://github.com/sgl-project/sglang/issues/33185) [Bug] DeepSeek-V4-Flash-0731: reasoning_effort mapped one level off — `high` is a no-op and vendor `max` is unreachable

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#33194](https://github.com/sgl-project/sglang/issues/33194) [Bug] DeepSeek-V4-Flash-0731 on Ampere (8x A800, SM80, TP=8): three further blockers after the deep_gemm NameError
- [other] 🆕 [#33187](https://github.com/sgl-project/sglang/issues/33187) [Bug/Design] `SGLANG_SANITIZE_NAN_LOGITS`: a fully-NaN logits row becomes a uniform-random sample — garbage streamed to clients as normal output; proposal: opt-in per-request abort

### vllm-project/vllm

- [other] 🆕 ⚠maintainer-authored [#50682](https://github.com/vllm-project/vllm/issues/50682) [ROCm][AMD] Kimi-K3 Gap and Roadmap Tracking

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#33180](https://github.com/sgl-project/sglang/issues/33180) @copilot resolve the merge conflicts on this branch.
