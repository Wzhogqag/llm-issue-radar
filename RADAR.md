# LLM Serving Issue Radar

_Last run: 2026-08-17T13:32+00:00_

**25 issues** — sgl-project/sglang: 5, vllm-project/vllm: 20 — 🆕 **24 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 9

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#35129](https://github.com/sgl-project/sglang/issues/35129) [Bug] DeepSeek-V4-Flash-0731 + dsv4 + DSPARK + HiCache: long agentic sessions get #cached-token: 0 every turn despite stable 50%+ prefix (short requests hit ~98%)

### vllm-project/vllm

- [Bug] 🆕 [#52520](https://github.com/vllm-project/vllm/issues/52520) [Bug]: hybrid Mamba + `--mamba-cache-mode align`: a request near the KV-pool ceiling is admitted, prefilled to 98.9 %, requeued, and re-prefilled forever with zero output tokens and zero preemption accounting

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#52617](https://github.com/vllm-project/vllm/issues/52617) [Bug]: vLLM 0.26.0 LMCache P/D receiver reports a full KV-cache hit but decoding diverges from the monolithic baseline at token 0
- [Bug] 🆕 [#52591](https://github.com/vllm-project/vllm/issues/52591) [Bug]: two logger calls have mismatched %-args, so the log record is dropped

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#52585](https://github.com/vllm-project/vllm/issues/52585) [Performance][ROCm] gfx1100 long-prefill: unified attention BLOCK_M=16 default leaves ~2x on the table; BLOCK_M=64 gives 1.1-1.3x TTFT on latest main

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#35148](https://github.com/sgl-project/sglang/issues/35148) [Bug] Qwen3.8-27B-FP8 reasoning content does not parse correctly in rust sgl-model-gateway

### vllm-project/vllm

- [Bug] 🆕 [#52613](https://github.com/vllm-project/vllm/issues/52613) [Bug]: MiniMax-M3 (MXFP8) streaming: generation stops (empty delta, finish_reason=stop) right after reasoning closes, whenever a tool call should follow — non-streaming with identical payload succeeds
- [Bug] 🆕 [#52540](https://github.com/vllm-project/vllm/issues/52540) [Bug]: ModelOpt NVFP4 on SM120 dies or wedges under sustained load with CUDA graphs (not the NVFP4 GEMM backend)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#52590](https://github.com/vllm-project/vllm/issues/52590) [Bug]: num_blocks division is a no-op in get_moe_wna16_block_config because block_size_k is reassigned first

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#35080](https://github.com/sgl-project/sglang/issues/35080) [Bug] Flashinfer backend is not supported on Blackwell GPUs

### vllm-project/vllm

- [RFC] 🆕 [#52567](https://github.com/vllm-project/vllm/issues/52567) [RFC]: First-class agentic inference support in vLLM

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#35150](https://github.com/sgl-project/sglang/issues/35150) [Bug] Qwen3.8 DSpark forced-reject is not lossless: accumulated GDN state drift vs Base decode
- [Bug] 🆕 [#35144](https://github.com/sgl-project/sglang/issues/35144) [Bug] EAGLE/NEXTN TP=2 hangs at warmup on Intel XPU after #34238 moved the verify-decision TP broadcast out of the sampling branch

### vllm-project/vllm

- [Feature] 🆕 [#52536](https://github.com/vllm-project/vllm/issues/52536) [Feature] Allow random dataset to use --dataset-path for realistic token sampling

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#52586](https://github.com/vllm-project/vllm/issues/52586) [Bug]: when setting dp=2 dsv4f0731 ,console log and metric running-request can not see both grafana and console log

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] ⚠maintainer-authored [#52511](https://github.com/vllm-project/vllm/issues/52511) [Bug]: FlashInfer TRT-LLM bf16 MoE weight-conversion OOM recurs post-#45589 at TP2 (120B MoE, GB200) — cumem MemPool still doesn't reclaim under pressure

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#52620](https://github.com/vllm-project/vllm/issues/52620) [Bug]: `ngram_gpu` speculative decoding with xgrammar returns HTTP 500 under concurrent structured-output requests
- [Bug] 🆕 [#52614](https://github.com/vllm-project/vllm/issues/52614) [Bug]: lm-format-enforcer 0.11.3 integration is incompatible with vLLM 0.26.0 due to stale MistralTokenizer import path
- [Bug] 🆕 [#52594](https://github.com/vllm-project/vllm/issues/52594) [Bug]: muse_glimmer cannot combine reasoning with structured outputs — schema is silently skipped when enable_in_reasoning=False
- [Bug] 🆕 [#52583](https://github.com/vllm-project/vllm/issues/52583) [Bug]: Prefix Caching hangs with large multimodal inputs (Qwen3.8-VL) – CPU-bound hash alignment blocks prefill
- [Bug] 🆕 [#52551](https://github.com/vllm-project/vllm/issues/52551) [Bug]: Qwen3.6-27B (dense Gated-DeltaNet) permanently hard-wedges the V1 engine — two reproducible modes (2 large images; long multi-turn text), possibly related
- [Bug] 🆕 [#52544](https://github.com/vllm-project/vllm/issues/52544) [Bug]: VLLM_USE_PRECOMPILED can fall back across CUDA variants without compatibility validation
- [Bug] 🆕 [#52531](https://github.com/vllm-project/vllm/issues/52531) [Bug]:  Kimi-K3 CUDA graph capture silently corrupts output at batch=1; three distinct failure modes across cudagraph modes.
- [Bug] 🆕 [#52525](https://github.com/vllm-project/vllm/issues/52525) [Bug]: Marlin MoE output depends on equivalent within-expert token ordering
- [Bug] 🆕 [#52589](https://github.com/vllm-project/vllm/issues/52589) [Bug]:Is it possible to install vllm >= 0.18.0 on Ubuntu 20, CUDA 12.6, and Torch 2.11?
