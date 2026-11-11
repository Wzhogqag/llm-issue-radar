# LLM Serving Issue Radar

_Last run: 2026-11-11T13:22+00:00_

**11 issues** — sgl-project/sglang: 1, vllm-project/vllm: 10 — 🆕 **11 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Feature] 🆕 [#66990](https://github.com/vllm-project/vllm/issues/66990) [Feature]: EC events: publish encoder cache presence and eviction from the EC connector

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#66947](https://github.com/vllm-project/vllm/issues/66947) [Feature]: [KV Connector] Configure Mooncake Mamba snapshot write intervals
- [RFC] 🆕 [#66949](https://github.com/vllm-project/vllm/issues/66949) [RFC]: DWDP: Distributed Weight Data Parallelism for MoE Prefill
- [RFC] 🆕 [#66942](https://github.com/vllm-project/vllm/issues/66942) [RFC]: KV Trace monitoring

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#67028](https://github.com/vllm-project/vllm/issues/67028) [Bug][KV Offload]: canonical_layout refuses to start with FlashInfer on pre-Blackwell GPUs: kernel-split blocks fail the canonical shape check
- [Feature] 🆕 [#66960](https://github.com/vllm-project/vllm/issues/66960) [Feature]: Sparse-MLA (DSA) attention on SM80/Ampere (A100): no selectable backend since the Triton fallback removal — SM80 DSA models hard-fail at engine init

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#66939](https://github.com/vllm-project/vllm/issues/66939) [Bug]: kimi_k2 truncated tool-call markers corrupt arguments and function names, and leak into content
- [RFC] 🆕 [#66974](https://github.com/vllm-project/vllm/issues/66974) [RFC]: Shared stream conformance cases for `vllm bench serve` and `vllm-bench`

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#49796](https://github.com/sgl-project/sglang/issues/49796) [Bug] Qwen-VL image preprocessing OOMs on GPU: 2.87x peak from torch.cat(processed_images) plus a cache that never returns memory

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#67012](https://github.com/vllm-project/vllm/issues/67012) Weight loading: warn (optionally fail) when a single-file checkpoint coexists with an index/shard set in a local directory

## Uncategorized

### vllm-project/vllm

- [Bug] 🆕 [#67017](https://github.com/vllm-project/vllm/issues/67017) [Bug]: The hard judgment of IMAGE_PLACEHOLDER is not elegant enough in Deepseekv4.1-flash on version of 0.33.0
