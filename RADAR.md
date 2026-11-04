# LLM Serving Issue Radar

_Last run: 2026-11-04T13:22+00:00_

**12 issues** — sgl-project/sglang: 4, vllm-project/vllm: 8 — 🆕 **12 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#48344](https://github.com/sgl-project/sglang/issues/48344) [RFC] mem_cache: Cross-branch KV page splicing and cursor fork/rewind for hybrid models (Qwen3.5 / GDN)

## Quantization

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#48311](https://github.com/sgl-project/sglang/issues/48311) [CI] diffusion: perf checks depend on which runner a job lands on, and in-job retries can't fix a slow host

### vllm-project/vllm

- [RFC] 🆕 [#65650](https://github.com/vllm-project/vllm/issues/65650) [RFC]: Using Backend-Owned KV Cache Runtime Shapes

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Feature] 🆕 [#48346](https://github.com/sgl-project/sglang/issues/48346) [Feature] dp-attention: the per-step H2D transfer of global_num_tokens_gpu is overwritten before anything reads it

### vllm-project/vllm

- [Performance] 🆕 [#65569](https://github.com/vllm-project/vllm/issues/65569) [Performance]: Batch-invariant mode on Hopper/Blackwell routes Linear layers to Triton although cuBLAS is already batch-invariant under the mode's settings

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#65632](https://github.com/vllm-project/vllm/issues/65632) [Bug]: vLLM Kimi k3 KVV AMD GPU product quality issue (DeepSWE & BEAM)
- [Feature] 🆕 [#65653](https://github.com/vllm-project/vllm/issues/65653) [Feature]: Support simultaneous Tool Calling and Structured Output via Grammar Union / Prefix Tree

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#65644](https://github.com/vllm-project/vllm/issues/65644) [Bug]: Streaming final usage chunk intermittently omits metrics.speculative_decoding while spec-decode Prometheus counters advance
- [Bug] 🆕 [#65592](https://github.com/vllm-project/vllm/issues/65592) [Bug]: /inference/v1/generate with "max_tokens": null bypasses default/override/platform output-token caps

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#65662](https://github.com/vllm-project/vllm/issues/65662) [Bug]: v0.33.0 GitHub Release incorrectly points to v0.33.0rc3 tag

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#65564](https://github.com/vllm-project/vllm/issues/65564) [Bug]: Qwen3.5-9B forced named tool choice is ~11x slower on A100 with v0.27.1 than v0.31.0

## Uncategorized

### sgl-project/sglang

- [Feature] 🆕 [#48348](https://github.com/sgl-project/sglang/issues/48348) [Feature]
