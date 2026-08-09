# LLM Serving Issue Radar

_Last run: 2026-08-09T13:36+00:00_

**16 issues** — sgl-project/sglang: 2, vllm-project/vllm: 14 — 🆕 **9 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#51518](https://github.com/vllm-project/vllm/issues/51518) MooncakeConnector P/D: NVLink fallback transfer fails "Requested address not found" (fp8 MLA, v0.25.0)

## Attention Backend

### sgl-project/sglang

- [Bug] [#34111](https://github.com/sgl-project/sglang/issues/34111) [Bug] A cancelled grammar-constrained overlap request can still emit visible text before abort

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#34155](https://github.com/sgl-project/sglang/issues/34155) [Bug] 1M-token prefill kills the engine with CUDA OOM in DSV4 indexer fp8_mqa_logits (nonpaged path) under --tp 8 + MegaMoE on 8x B200 (v0.5.17); equivalent request serves under tp8/dp8 dp-attention

### vllm-project/vllm

- [other] 🆕 [#51541](https://github.com/vllm-project/vllm/issues/51541) [ROCm][AITER] Port FlyDSL int4 MoE integration to AITER fused_moe API
- [Performance] [#51494](https://github.com/vllm-project/vllm/issues/51494) [Performance] MiniMax-M3-NVFP4 on 8x B200, first numbers after the #48929 correctness fix: 1M real-prose envelope, EAGLE3 2.1-2.3x decode
- [Performance] [#51454](https://github.com/vllm-project/vllm/issues/51454) [Performance] DP8 vs TP8 for single-KV-head MLA: 7.7x KV, 3.4x faster 1M TTFT at c=8 (DeepSeek-V4-Flash-0731, 8x B200, vLLM v0.25.0)
- [Bug] [#51456](https://github.com/vllm-project/vllm/issues/51456) [Bug]: online FP8 (--quantization fp8) produces corrupted, non-EOS-terminating output on Qwen2.5-1.5B-Instruct

## Distributed / TP / PP / EP

### vllm-project/vllm

- [other] 🆕 [#51533](https://github.com/vllm-project/vllm/issues/51533) [Installation]: Worker processes hang in CPU deadloop after NCCL initialization when loading DeepSeek-V4-Flash-0731 with vLLM V1 engine on H100
- [RFC] 🆕 [#51513](https://github.com/vllm-project/vllm/issues/51513) [RFC]: Unify functional P2P gating — one veto-only verdict for all P2P consumers (NCCL, custom allreduce, symm-mem)

## New Model Integration

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#51522](https://github.com/vllm-project/vllm/issues/51522) deepseek_v4: decode runs unfused (breakable CUDA graph) — DeepseekV4ForCausalLM lacks @support_torch_compile; fullgraph capture blocked by inline deep_gemm/tilelang pybinds
- [other] [#51497](https://github.com/vllm-project/vllm/issues/51497) [New Model]: nvidia/LocateAnything-3B (slow autoregressive mode first)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#51510](https://github.com/vllm-project/vllm/issues/51510) [Bug][Spec Decode] MRV2 AutoRegressiveSpeculator ignores dynamic K from scheduler — DSD non-functional on MRV2
- [RFC] 🆕 ⚠maintainer-authored [#51472](https://github.com/vllm-project/vllm/issues/51472) [RFC] Raw multimodal input for /generate endpoint (RL workloads)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] [#51465](https://github.com/vllm-project/vllm/issues/51465) [Bug]: Kimi K3 usage.prompt_tokens over-counts trailing channel-open stub (+3)

## Build / Install / Platform

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#51521](https://github.com/vllm-project/vllm/issues/51521) DeepSeek-V4 (deepseek_v4): fused topk_softplus_sqrt router rejects non-standard expert counts on CUDA (REAP 144-expert ckpts); torch fallback is XPU-gated
- [Bug] [#51467](https://github.com/vllm-project/vllm/issues/51467) [Bug]: DeepSeek-V4-Flash-0731 `response_format` (structured output) crashes the vLLM EngineCore — `apply_grammar_bitmask` tensor size mismatch (4040 vs 4041)
