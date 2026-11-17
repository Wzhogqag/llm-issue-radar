# LLM Serving Issue Radar

_Last run: 2026-11-17T13:22+00:00_

**13 issues** — sgl-project/sglang: 7, vllm-project/vllm: 6 — 🆕 **13 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#50920](https://github.com/sgl-project/sglang/issues/50920) Idle-burst prefill: first request waits for the next batch (consecutive prefill overlap) and bursts are split 1+N

### vllm-project/vllm

- [RFC] 🆕 [#68079](https://github.com/vllm-project/vllm/issues/68079) [RFC]: Keep agent KV in the CPU offload tier across tool calls, using client hints

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#68156](https://github.com/vllm-project/vllm/issues/68156) [Feature]: Add a synchronization hook for indexer cache loading before sparse top-k execution
- [other] 🆕 [#68123](https://github.com/vllm-project/vllm/issues/68123) [Discussion] Separate Mamba state pool from the paged KV pool for hybrid models (directional proposal)

## Quantization

### sgl-project/sglang

- [other] 🆕 [#50943](https://github.com/sgl-project/sglang/issues/50943) [Roadmap] Unified weight snapshot loading: weight cache, R-Fork and stores
- [RFC] 🆕 [#51018](https://github.com/sgl-project/sglang/issues/51018) [RFC] [NPU] MoE expert offloading through Paged Experts

### vllm-project/vllm

- [other] 🆕 [#68104](https://github.com/vllm-project/vllm/issues/68104) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#50915](https://github.com/sgl-project/sglang/issues/50915) [Bug] macOS: --device cpu fails with RuntimeError running 'lscpu' (get_cpu_ids_by_node)

### vllm-project/vllm

- [Feature] 🆕 [#68069](https://github.com/vllm-project/vllm/issues/68069) [Feature]: vllm prefetch plugin hook independently to accelerate model loading, 2.x faster than none prefetch, 1.x faster than inside prefetch

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#51009](https://github.com/sgl-project/sglang/issues/51009) [Bug] Qwen3.8-Flash-Next QSA: a verify window crossing a 4-token group overwrites the pending index-key ring (MTP 1-3 affected)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [other] 🆕 [#50927](https://github.com/sgl-project/sglang/issues/50927) [CI] [NPU] Test-only changes need an isolated validation track after #50560

### vllm-project/vllm

- [Bug] 🆕 [#68137](https://github.com/vllm-project/vllm/issues/68137) [Bug]: Qwen3 Python parser treats trailing reasoning whitespace as answer text

## Performance / Memory / OOM

### sgl-project/sglang

- [other] 🆕 [#51007](https://github.com/sgl-project/sglang/issues/51007) [CI] NPU base CI was disabled
