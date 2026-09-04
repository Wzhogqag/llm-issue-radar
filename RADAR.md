# LLM Serving Issue Radar

_Last run: 2026-09-04T13:27+00:00_

**22 issues** — sgl-project/sglang: 8, vllm-project/vllm: 14 — 🆕 **22 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 8
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#55265](https://github.com/vllm-project/vllm/issues/55265) [RFC] Length-aware batch composition for admission scheduling — experimental evidence, fairness fix, and where it breaks

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#37983](https://github.com/sgl-project/sglang/issues/37983) [Bug] VisionTritonAttention drops MiMo-style window attention and sinks

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#37931](https://github.com/sgl-project/sglang/issues/37931) [Bug] DeepSeek-V4-Flash-Vision-Exp on 2x DGX Spark: scheduler OOM-killed during weight load (cookbook cell dgx-spark|flash-vision|fp4)
- [other] 🆕 [#37993](https://github.com/sgl-project/sglang/issues/37993) [Playground] Verified cell: h200 / flash-official / fp4 / low-latency / single
- [RFC] 🆕 ⚠maintainer-authored [#38004](https://github.com/sgl-project/sglang/issues/38004) [RFC] Quantization module layout: Config, Scheme, backend kernels

### vllm-project/vllm

- [Bug] 🆕 [#55291](https://github.com/vllm-project/vllm/issues/55291) [Bug]: Qwen3.6-27B-FP8 eventually collapses into repeated ! tokens, affecting all subsequent requests
- [Bug] 🆕 [#55281](https://github.com/vllm-project/vllm/issues/55281) [Bug]: Whisper segment timestamps collapse under `prompt` — the reference timestamp decoding rules are not applied
- [Bug] 🆕 [#55250](https://github.com/vllm-project/vllm/issues/55250) [Bug]: DFlash2 draft gets 0% acceptance with --dtype float16 on XPU (bf16 works) — Qwen3.8-27B + incoai/Qwen3.8-27B-DFlash2
- [RFC] 🆕 [#55259](https://github.com/vllm-project/vllm/issues/55259) [RFC]: Optional native startup self-benchmarking for forward-pass performance characterization
- [RFC] 🆕 [#55339](https://github.com/vllm-project/vllm/issues/55339) [RFC]: Unify ModelOpt MoE methods (mirror of #49381)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#55336](https://github.com/vllm-project/vllm/issues/55336) [Bug]: Model Runner V2 never locks the workspace, so post-capture growth silently invalidates captured CUDA graphs
- [Feature] 🆕 [#55261](https://github.com/vllm-project/vllm/issues/55261) [Feature]: Benchmark and integrate CUTLASS Lamport GEMM + AllReduce into vLLM

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#38009](https://github.com/sgl-project/sglang/issues/38009) [Bug] [DFlash2] Greedy output diverges from target-only Qwen3.8-27B when thinking is enabled

### vllm-project/vllm

- [Bug] 🆕 [#55323](https://github.com/vllm-project/vllm/issues/55323) [Bug]: num_speculative_tokens cannot default from the draft config's n_predict for MTP models (TypeError in SpeculativeConfig MTP auto-detection)
- [Bug] 🆕 [#55322](https://github.com/vllm-project/vllm/issues/55322) [Bug]: Qwen3.5/3.6 MTP resolves n_predict=None for multimodal-wrapper checkpoints (mtp_num_hidden_layers is read from the wrapper, not text_config)
- [Bug] 🆕 [#55313](https://github.com/vllm-project/vllm/issues/55313) [Bug]: Qwen3.8 + DSpark + streaming json_schema can desync XGrammar and emit 250k trailing spaces with HTTP 200
- [Bug] 🆕 [#55279](https://github.com/vllm-project/vllm/issues/55279) [Bug]: DFlash2 (dflash method) deterministic cumulative OOB — engine dies with CUDA IMA / Xid 31 after ~11k decode steps under sampling load (sm_80, v0.27.1)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#37919](https://github.com/sgl-project/sglang/issues/37919) The initial CI workflows were stopped by the PR gate because the `run-ci` label is missing, so no tests were executed.

## Performance / Memory / OOM

### sgl-project/sglang

- [Feature] 🆕 [#37944](https://github.com/sgl-project/sglang/issues/37944) [Feature] Dynamic Prefill Context Parallelism

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#55238](https://github.com/vllm-project/vllm/issues/55238) [Bug]: gemma-4-26B-A4B-it produces different greedy output with CUDA graphs than with enforce_eager
- [other] 🆕 [#55327](https://github.com/vllm-project/vllm/issues/55327) [ROCm] gfx950 top-k policy is gated on topK==1024, leaving index_topk=2048 models (GLM-5.x) on the generic 10-way split

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#38013](https://github.com/sgl-project/sglang/issues/38013) [Bug]
