# LLM Serving Issue Radar

_Last run: 2026-10-05T13:39+00:00_

**13 issues** — sgl-project/sglang: 8, vllm-project/vllm: 5 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 5
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#42544](https://github.com/sgl-project/sglang/issues/42544) [Bug] /update_weights_from_disk: is_async / keep_pause / token_step have no effect, num_paused_requests is always 0
- [Bug] [#42508](https://github.com/sgl-project/sglang/issues/42508) [Bug] Scheduler aborts with `double free or corruption` inside the idle-loop invariant check (`session_held_tokens` walk); server hangs permanently afterwards

### vllm-project/vllm

- [Bug] 🆕 [#60019](https://github.com/vllm-project/vllm/issues/60019) [Bug]: P2P KV offload tier runs NIXL peer registration synchronously inside the scheduler step, stalling all requests on the rank
- [Bug] 🆕 [#60007](https://github.com/vllm-project/vllm/issues/60007) [Bug]: TRITON_MLA is not batch invariant under chunked prefill with `VLLM_BATCH_INVARIANT=1` (DeepSeek-V2-Lite, DeepSeek-V3.1)
- [Feature] 🆕 [#60044](https://github.com/vllm-project/vllm/issues/60044) [Feature]: Per-request prefix-cache miss attribution (prompt divergence vs. eviction)

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#59971](https://github.com/vllm-project/vllm/issues/59971) [Bug]: NIXL pull: one wedged connection repeatedly strands decode KV blocks (production log analysis)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#42530](https://github.com/sgl-project/sglang/issues/42530) [Bug] big prefill blocks other requests on 2xRTX3090  for qwen3.8 27b
- [no-prefix] ⚠no-prefix [#42473](https://github.com/sgl-project/sglang/issues/42473) Development Roadmap (2026 Q4)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#42568](https://github.com/sgl-project/sglang/issues/42568) [Bug] `chain_speculative_sampling_triton` rejects every draft whose q rounds just above 1.0 (since #37134)
- [Feature] 🆕 [#42559](https://github.com/sgl-project/sglang/issues/42559) [Feature] Support Whisper speech translation (task="translate" / /v1/audio/translations)
- [Bug] [#42510](https://github.com/sgl-project/sglang/issues/42510) [Bug] EAGLE/MTP same-checkpoint draft keeps redundant embed_tokens/lm_head copies resident during KV pool sizing → under-sized pool, startup OOM

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#60059](https://github.com/vllm-project/vllm/issues/60059) [Bug]: `/inference/v1/generate` doesn't pass `reasoning_ended` or `reasoning_parser_kwargs`, so structured outputs start later than on `/v1/chat/completions`

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#42564](https://github.com/sgl-project/sglang/issues/42564) [Bug][ROCm] FLUX.2-dev fails on gfx1151: NVIDIA PTX inline assembly in residual_gate_add kernel
