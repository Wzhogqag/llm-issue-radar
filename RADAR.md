# LLM Serving Issue Radar

_Last run: 2026-09-12T13:24+00:00_

**6 issues** — sgl-project/sglang: 1, vllm-project/vllm: 5 — 🆕 **6 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#39192](https://github.com/sgl-project/sglang/issues/39192) [RFC] Contention-aware batching for dynamic EPLB expert migration

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#56564](https://github.com/vllm-project/vllm/issues/56564) [Performance]: GLM-5.3-Flash on H100: auto-selected FLASHINFER_MLA_SPARSE_SM90 is 36-70% slower than FLASH_ATTN_MLA_SPARSE

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [RFC] 🆕 [#56581](https://github.com/vllm-project/vllm/issues/56581) [RFC]: Streaming prompt prefill for overlapping upstream generation and downstream prefill

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#56605](https://github.com/vllm-project/vllm/issues/56605) [Bug]: GLM-5.3-Flash degenerates into repeated-token "word salad" in multi-turn agentic use
- [Bug] 🆕 [#56521](https://github.com/vllm-project/vllm/issues/56521) [Bug][ROCm]: Intermittent worker segfault in libhsa-runtime64 — ROCPROFILER_QUEUE_INTERPOSITION=0 forces an unfixed ROCr heap overflow
- [Bug] 🆕 [#56540](https://github.com/vllm-project/vllm/issues/56540) [Bug]: ROCm Stack DeepSeekv4.1 Flash Issue spamming logs with GLUON backend not available. Using TRITON backend!!!
