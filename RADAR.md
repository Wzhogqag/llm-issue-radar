# LLM Serving Issue Radar

_Last run: 2026-09-02T13:29+00:00_

**23 issues** — sgl-project/sglang: 9, vllm-project/vllm: 14 — 🆕 **23 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#37590](https://github.com/sgl-project/sglang/issues/37590) [Bug] DP-attention scheduler crashes (NoneType len) when attn_tp_size>1 and attn_cp_size>1: request-broadcast source rank has work_reqs=None

### vllm-project/vllm

- [RFC] 🆕 [#54864](https://github.com/vllm-project/vllm/issues/54864) [RFC]: Truncate mode for `thinking_token_budget`
- [no-prefix] 🆕 ⚠no-prefix [#54919](https://github.com/vllm-project/vllm/issues/54919) `[Performance]: Qwen3.8-Flash-Next long-prefill workload periodically starves active decode for 3-7 minutes on 2-node DGX Spark TP2`

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#54926](https://github.com/vllm-project/vllm/issues/54926) [Bug]: Gemma 4 MTP + NIXL PD disaggregation — draft model KV not transferred, MTP ineffective
- [Bug] 🆕 [#54877](https://github.com/vllm-project/vllm/issues/54877) [Bug]: padded KV page reshape uses a spec-page stride against a kernel-block size, so as_strided over-requests storage by the split ratio
- [Bug] 🆕 [#54870](https://github.com/vllm-project/vllm/issues/54870) [Bug]: `MooncakeStoreScheduler` fatal assert "Missing current block table for store request" when a KV load failure recovery (#19330) reschedules the request

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#37608](https://github.com/sgl-project/sglang/issues/37608) [Bug] --tool-call-parser auto selects glm45 instead of spark25 for Spark-X2.5

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#37559](https://github.com/sgl-project/sglang/issues/37559) [Bug] CUDA_ERROR_ILLEGAL_ADDRESS crash with --moe-a2a-backend megamoe on B300 (SM100) after sgl-deep-gemm 0.1.7 bump
- [other] 🆕 [#37519](https://github.com/sgl-project/sglang/issues/37519) [Roadmap][Feature] Support T-Head PPU

### vllm-project/vllm

- [Bug] 🆕 [#54900](https://github.com/vllm-project/vllm/issues/54900) [Bug]: GLM-5.3 Quark MXFP4 Loading Issue
- [other] 🆕 [#54966](https://github.com/vllm-project/vllm/issues/54966) [CI][Refactor] Comprehensive `AiterExperts` test coverage and possible split
- [other] 🆕 [#54959](https://github.com/vllm-project/vllm/issues/54959) [Refactor] Complete the MOE oracle / linear kernel migration

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#37609](https://github.com/sgl-project/sglang/issues/37609) [Bug] Spark2.5 MLP uses tanh-approximate GELU instead of reference GELU
- [Bug] 🆕 [#37579](https://github.com/sgl-project/sglang/issues/37579) [Bug] GLM-V (glm4v processor): stray multimodal placeholder strings in message text cause 500 "Mismatch: More IMAGE tokens found than corresponding data provided"

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#54866](https://github.com/vllm-project/vllm/issues/54866) DP engine startup stuck >50 min in MoE triton JIT warmup (MoEPrepareAndFinalizeNaiveDPEPModular) vs ~3 min single-node

## New Model Integration

### vllm-project/vllm

- [other] 🆕 [#54961](https://github.com/vllm-project/vllm/issues/54961) [Refactor] Standardize `benchmarks/kernels/` and support multi-device tuning

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#37561](https://github.com/sgl-project/sglang/issues/37561) [Bug] Kimi-K3 multi-node MegaMoE sparse-DP prefill CUDA graph deadlocks after PR #33871
- [other] 🆕 [#37548](https://github.com/sgl-project/sglang/issues/37548) [GLM-5.3-Flash] NextN/MTP crashes on the first request: Glm5NextForConditionalGenerationNextN inherits DeepSeek's draft forward, embedding gather goes out of bounds at TP8

### vllm-project/vllm

- [Bug] 🆕 [#54906](https://github.com/vllm-project/vllm/issues/54906) [Bug]: thinking_token_budget ignored by Model Runner V2 with Qwen3.8 NVFP4 + MTP

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#54914](https://github.com/vllm-project/vllm/issues/54914) [Bug]: KV Cache Offloading AssertionError after several days of uptime with DeepSeek-V4-Pro on 3×8 H100 (TP8+DP3)
- [Feature] 🆕 [#54937](https://github.com/vllm-project/vllm/issues/54937) [Feature]: Tokenized Prompt as Input for Chat and Messages Endpoints when serving

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#54928](https://github.com/vllm-project/vllm/issues/54928) [Bug][SpecDecode] DFlash2 changes greedy Qwen3.8 thinking output at token 30, including K=1 and --enforce-eager

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#37524](https://github.com/sgl-project/sglang/issues/37524) GLM-5.3-Flash bug tracking
