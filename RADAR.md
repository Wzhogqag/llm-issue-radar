# LLM Serving Issue Radar

_Last run: 2026-09-27T13:26+00:00_

**13 issues** — sgl-project/sglang: 5, vllm-project/vllm: 8 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#41372](https://github.com/sgl-project/sglang/issues/41372) [Bug]: scheduler Req.decoded_text is never written: dead stop-string fallback at schedule_batch.py:1846 and empty DecodeStatus seed on eviction re-init

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 [#58882](https://github.com/vllm-project/vllm/issues/58882) [Feature]: Allow LBNHC/NHD for ROCM_AITER_UNIFIED_ATTN where supported
- [other] 🆕 [#58858](https://github.com/vllm-project/vllm/issues/58858) [Question][ROCm] GLM-5.3-Flash kpool indexer: does the 640-token block table reach 32-pool pages on gfx942/gfx950 too?

## Quantization

### vllm-project/vllm

- [Performance] [#58799](https://github.com/vllm-project/vllm/issues/58799) [Performance]: Suboptimal SM90 FP8 CUTLASS MoE dispatch on H20 EP8 — upstream fix proposed

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#41449](https://github.com/sgl-project/sglang/issues/41449) [Bug] DSpark + TP: grammar-constrained request batched with any other request deadlocks all ranks (overlap and non-overlap), GPUs spin in a collective

### vllm-project/vllm

- [Bug] 🆕 [#58850](https://github.com/vllm-project/vllm/issues/58850) [Bug]: Intermittent Xid 31 MMU fault in pynccl all_reduce during CUDA graph

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] [#41351](https://github.com/sgl-project/sglang/issues/41351) [Bug] Potential hybrid GDN Radix-cache selected-logprob drift on repeated branch scoring

### vllm-project/vllm

- [Bug] 🆕 [#58899](https://github.com/vllm-project/vllm/issues/58899) [Bug]: Greedy output changes between restarts, also with VLLM_BATCH_INVARIANT=1: the q/k-norm + RoPE combo kernel picks its reduction config by timing

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [other] 🆕 [#41363](https://github.com/sgl-project/sglang/issues/41363) [CI] ltx_2_3_hq_pipeline perf checks fail on most diffusion PRs (load / decode / denoise variance)

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#41385](https://github.com/sgl-project/sglang/issues/41385) EvalPort: portable interchange for BenchmarkResult

### vllm-project/vllm

- [Bug] 🆕 [#58902](https://github.com/vllm-project/vllm/issues/58902) [Bug]: Qwen3-Omni: M-RoPE positions silently misaligned for every multimodal request (offset double-counts the modality-start token)
- [Performance] 🆕 [#58849](https://github.com/vllm-project/vllm/issues/58849) [Performance]: WSL2: `VLLM_WSL2_ENABLE_PIN_MEMORY=1` makes the default V2 runner ~12% faster per decode step
- [Performance] [#58804](https://github.com/vllm-project/vllm/issues/58804) [Performance][Bug]: Tiered Offloading
