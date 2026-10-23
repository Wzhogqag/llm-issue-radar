# LLM Serving Issue Radar

_Last run: 2026-10-23T13:30+00:00_

**3 issues** — sgl-project/sglang: 1, vllm-project/vllm: 2 — 🆕 **3 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#45989](https://github.com/sgl-project/sglang/issues/45989) [Bug] HiCache `buffer_only` + Mooncake L3: scheduler admits a chunked prefill it cannot finish, then crashes with "Prefill out of memory" (evictable 0, every radix node locked)

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#63331](https://github.com/vllm-project/vllm/issues/63331) Anthropic /v1/messages: inline system messages are merged into the leading system prompt, so every Claude Code turn misses the prefix cache after that point

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#63276](https://github.com/vllm-project/vllm/issues/63276) [Bug]: DS V4.1 Flash1017 outputs incorrect numbers
