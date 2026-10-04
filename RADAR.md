# LLM Serving Issue Radar

_Last run: 2026-10-04T15:00+00:00_

**13 issues** — sgl-project/sglang: 7, vllm-project/vllm: 6 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 4
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#42508](https://github.com/sgl-project/sglang/issues/42508) [Bug] Scheduler aborts with `double free or corruption` inside the idle-loop invariant check (`session_held_tokens` walk); server hangs permanently afterwards

### vllm-project/vllm

- [Bug] 🆕 [#59907](https://github.com/vllm-project/vllm/issues/59907) [Bug]: Priority scheduling can un-schedule a request it already scheduled in the same step (encoder cache miss, prefix hits on unwritten KV, priority inversion)

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#59956](https://github.com/vllm-project/vllm/issues/59956) [Bug]: NIXL: `remove_remote_agent` does not release UCX endpoints, so each `engine_ttl` eviction + re-handshake leaks until handshakes fail

## Quantization

### sgl-project/sglang

- [Feature] 🆕 [#42511](https://github.com/sgl-project/sglang/issues/42511) [Feature] server-level control over GPU image decoding
- [no-prefix] 🆕 ⚠no-prefix [#42473](https://github.com/sgl-project/sglang/issues/42473) Test issue (deprecated)

### vllm-project/vllm

- [Bug] 🆕 [#59946](https://github.com/vllm-project/vllm/issues/59946) [Bug]: gemma4 loader requires k_proj/v_proj/k_norm for KV-shared layers that transformers 5.5.4 never saves; any transformers-saved gemma4 checkpoint is refused
- [other] [#59868](https://github.com/vllm-project/vllm/issues/59868) [Qwen4Exp] PLE pinned-host FP8 lookup will not compile on sm_86, so --engram-config cpu_offload is unusable on consumer Ampere

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#42510](https://github.com/sgl-project/sglang/issues/42510) [Bug] EAGLE/MTP same-checkpoint draft keeps redundant embed_tokens/lm_head copies resident during KV pool sizing → under-sized pool, startup OOM
- [no-prefix] 🆕 ⚠no-prefix [#42415](https://github.com/sgl-project/sglang/issues/42415) fix(mlx): repeated chat returns unrelated text after native generation

### vllm-project/vllm

- [Bug] 🆕 [#59933](https://github.com/vllm-project/vllm/issues/59933) [Bug]: RecoverSSM align mode commits the final SSM state to an unwritten block at exact block boundaries (floor vs ceil-1)
- [Bug] 🆕 [#59926](https://github.com/vllm-project/vllm/issues/59926) [Bug] DeepSeek-V4-Flash tool-call format failures associated with prefix-cache reuse; worst for short cached head + long uncached suffix; `cache_salt` reduces failures but is confounded with hit shape (v0.27.1, fp8 KV, MTP)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#42465](https://github.com/sgl-project/sglang/issues/42465) [Bug] DeepSeek-V4 + HiCache write_through: TP ranks deadlock under concurrent long prefills (scheduler and detokenizer go silent, /health 503)

## Build / Install / Platform

### sgl-project/sglang

- [Feature] 🆕 [#42459](https://github.com/sgl-project/sglang/issues/42459) [Feature] Upgrade Nsight Compute bundled by the CUDA devel base image
