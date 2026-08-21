# LLM Serving Issue Radar

_Last run: 2026-08-21T13:34+00:00_

**22 issues** — sgl-project/sglang: 12, vllm-project/vllm: 10 — 🆕 **22 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 10
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#35808](https://github.com/sgl-project/sglang/issues/35808) [Feature] Enhanced KV Cache Observability: Full-Lifecycle Metrics and Diagnostics

### vllm-project/vllm

- [Performance] 🆕 [#53237](https://github.com/vllm-project/vllm/issues/53237) [Performance] MooncakeConnector emits one RDMA descriptor per (layer, block) — but with the unified paged KV layout a block's layers are contiguous; page-level descriptors give up to 19x faster PD transfers

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#35772](https://github.com/sgl-project/sglang/issues/35772) [Bug] Qwen3-VL vision features diverge from Transformers/vLLM in v0.5.17 on fine-grained grounding

### vllm-project/vllm

- [RFC] 🆕 [#53208](https://github.com/vllm-project/vllm/issues/53208) [RFC]: Opt-out control for individual startup kernel warmups

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#35797](https://github.com/sgl-project/sglang/issues/35797) [Bug] Qwen3.5 MTP weights silently dropped on compressed-tensors checkpoints (accept len pinned at 1.0)
- [other] 🆕 [#35860](https://github.com/sgl-project/sglang/issues/35860) [Playground] Verified cell: Qwen3.8-27B / dgx-spark / nvfp4 / DFLASH2 / single
- [no-prefix] 🆕 ⚠no-prefix [#35851](https://github.com/sgl-project/sglang/issues/35851) # Breakable CUDA graph: per-layer break dominates GDN prefill time on hybrid models (Qwen3.5/3.6)
- [no-prefix] 🆕 ⚠no-prefix [#35777](https://github.com/sgl-project/sglang/issues/35777) Qwen3.8-27B NVFP4 on RTX 5090: cookbook mem-fraction OOMs at decode-graph capture (~5GB) and torch.compile + decode graph is a 6x regression

### vllm-project/vllm

- [Bug] 🆕 [#53254](https://github.com/vllm-project/vllm/issues/53254) [Bug]: LoRA + Muse-Glimmer-30B: AssertionError in lora_shrink (token_lora_mapping.size(0) == M) at startup profiling, on stock nightly and regardless of adapter targets
- [Performance] 🆕 [#53215](https://github.com/vllm-project/vllm/issues/53215) [Performance]: MTP acceptance metrics fluctuate within a benchmark run for GLM-5.2-FP8 on 8×H200 with vLLM v0.24.0
- [Bug] 🆕 [#53211](https://github.com/vllm-project/vllm/issues/53211) [Bug][XPU]: AutoRound int4 models silently emit garbage under concurrent requests; ARK WOQ backend is auto-selected with no opt-out
- [Bug] 🆕 [#53181](https://github.com/vllm-project/vllm/issues/53181) [Bug] Xgrammar "Failed to advance FSM" still fires after #52805 (0.27.2rc1.dev256+geac636a7f) — follow-up to #52852
- [Bug] 🆕 [#53180](https://github.com/vllm-project/vllm/issues/53180) [Bug]: TurboQuant k8v4 + MTP speculative decoding silently produces degenerate output on hybrid GDN models (v0.27.1, stock)
- [RFC] 🆕 [#53192](https://github.com/vllm-project/vllm/issues/53192) [RFC]: V1/V2 Weight Reload with Streaming Quantization Units

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#35743](https://github.com/sgl-project/sglang/issues/35743) [Bug] A global --attention-backend kills the server when a non-DiT component does not declare it (MiniMax-H3 audio_vae)
- [Feature] 🆕 [#35752](https://github.com/sgl-project/sglang/issues/35752) [Feature] Support Prometheus name[] filtering for multiprocess metrics

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#35822](https://github.com/sgl-project/sglang/issues/35822) [Bug] EAGLE speculative decoding (native Qwen3.5/3.8 MTP) hangs in tree_speculative_sampling_target_only on Ampere (2x A2, TP=2, 100% GPU util / low power)
- [no-prefix] 🆕 ⚠no-prefix [#35765](https://github.com/sgl-project/sglang/issues/35765) Support sampling masks without finite top-k

### vllm-project/vllm

- [Bug] 🆕 [#53257](https://github.com/vllm-project/vllm/issues/53257) [Bug] DeepSeek-V4-Flash: non-deterministic output at temperature=0, rate scales with concurrency

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#35811](https://github.com/sgl-project/sglang/issues/35811) [Bug] Using hicache in the main branch of deepseekv4-flash will result in illegal memory access.

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#53216](https://github.com/vllm-project/vllm/issues/53216) [Performance]: Best practices for preventing GPU OOM in production

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#35785](https://github.com/sgl-project/sglang/issues/35785) Triton version mismatch
