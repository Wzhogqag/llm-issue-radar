# LLM Serving Issue Radar

_Last run: 2026-07-15T13:59+00:00_

**31 issues** — sgl-project/sglang: 14, vllm-project/vllm: 17 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 11
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 4
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 4
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#31327](https://github.com/sgl-project/sglang/issues/31327) [Feature] Add token-weighted prefix cache hit rate panel to Grafana dashboard

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] [#31252](https://github.com/sgl-project/sglang/issues/31252) [Bug] HiCache draft KV pool backup crashes with cudaMemcpyBatchAsync invalid argument in PD disaggregation

### vllm-project/vllm

- [Bug] 🆕 [#48656](https://github.com/vllm-project/vllm/issues/48656) [Bug]: #48036 auto-enables sequence-parallel MoE on TP+EP without DP — −19% throughput, −24% KV cache, and no way to opt out

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#31310](https://github.com/sgl-project/sglang/issues/31310) [Bug] fa3 backend slow with mla page-size 64 for H20

### vllm-project/vllm

- [Bug] [#48650](https://github.com/vllm-project/vllm/issues/48650) [Bug]: Runtime-varying tl.constexpr params force Triton kernel recompiles on the serving path (unified attention MAX_MM_RANGES et al.)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#31295](https://github.com/sgl-project/sglang/issues/31295) [Bug] [PD][NIXL] Qwen3.5 TP1-attention prefill -> TP4 decode fails in prepXferDlist with NIXL_ERR_NOT_FOUND
- [Bug] [#31236](https://github.com/sgl-project/sglang/issues/31236) [Bug] 'Gemma4ForConditionalGeneration' object has no attribute 'get_embed_and_head' when modelopt_fp4
- [Bug] [#31283](https://github.com/sgl-project/sglang/issues/31283) [Bug] _mxfp8_block_scaled_matmul_kernel declares M (token count) as tl.constexpr — full GEMM recompile per 128-token batch bucket
- [Feature] [#31248](https://github.com/sgl-project/sglang/issues/31248) [Feature] Support CompressedTensorsW4A16Sparse24
- [Feature] [#31235](https://github.com/sgl-project/sglang/issues/31235) [Feature] Support serialized static-FP8 MXFP4 MoE on the resident FlashInfer backend (SM120/SM121)
- [no-prefix] ⚠no-prefix [#31224](https://github.com/sgl-project/sglang/issues/31224) Misleading "FP8 KV cache but no scaling factors provided" warning fires even when per-layer ModelOpt/compressed-tensors KV scales are present and loaded

### vllm-project/vllm

- [Performance] 🆕 [#48732](https://github.com/vllm-project/vllm/issues/48732) [Performance]: Qwen3-Omni MoE decode 3-6x slower on RTX 5090 (sm_120) — no fused-MoE tuned configs for GeForce Blackwell
- [Bug] 🆕 [#48718](https://github.com/vllm-project/vllm/issues/48718) [Bug]: Qwen3.6 35B-A3B NVFP4 2-3x slower on B300s with v0.25.0
- [no-prefix] 🆕 ⚠no-prefix [#48652](https://github.com/vllm-project/vllm/issues/48652) transformers backend: tensor reshape error during profile run with GLM MoE architecture
- [no-prefix] 🆕 ⚠no-prefix [#48651](https://github.com/vllm-project/vllm/issues/48651) transformers backend: per_token_group_quant_8bit not implemented for Float8_e4m3fn (FP8 MoE models)
- [Bug] [#48689](https://github.com/vllm-project/vllm/issues/48689) [Bug]: GLM-5.2 nvpf4 quantization not loading with TP

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#31336](https://github.com/sgl-project/sglang/issues/31336) [Bug] [AMD] Qwen3.5-397B-A17B-FP8 + MoRI + dp-attention crashes at init: FusedMoE shared-expert slot assertion (num_experts - num_shared_slots) % moe_ep_size
- [Bug] [#31243](https://github.com/sgl-project/sglang/issues/31243) [Bug] can't deploy Mimo V2.5

### vllm-project/vllm

- [Bug] 🆕 [#48707](https://github.com/vllm-project/vllm/issues/48707) [Bug]:  vLLM 0.25.0 crashed
- [no-prefix] ⚠no-prefix [#48661](https://github.com/vllm-project/vllm/issues/48661) Expose public get_layer_params(config) helper for Gemma4 per-layer attention/FFN params

## New Model Integration

### sgl-project/sglang

- [Feature] [#31261](https://github.com/sgl-project/sglang/issues/31261) [Feature] Support Deterministic Inference for Qwen3_5ForConditionalGeneration

### vllm-project/vllm

- [Feature] [#48644](https://github.com/vllm-project/vllm/issues/48644) [Feature]: Support fast weight updates from disk

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#48733](https://github.com/vllm-project/vllm/issues/48733) [Bug]: Qwen3-Omni video prompt_tokens ~65% higher than HF processor semantics for identical sampling config (online path)
- [Bug] 🆕 [#48700](https://github.com/vllm-project/vllm/issues/48700) [Bug]: EAGLE speculative decoding crashes for multimodal wrapper architectures — load_eagle_model resolves lm_head from target_model instead of target_language_model

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#31271](https://github.com/sgl-project/sglang/issues/31271) Can not load gpt-oss-20b model specific tokenizer

### vllm-project/vllm

- [Feature] [#48635](https://github.com/vllm-project/vllm/issues/48635) [Feature][KV-offloading]: Relax Offloading Block Size asserts

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#31293](https://github.com/sgl-project/sglang/issues/31293) [Bug] Adding the --moe-a2a-backend deepep parameter causes the program to freeze; it runs without it. Does the system require any environment configuration?

### vllm-project/vllm

- [Bug] 🆕 [#48723](https://github.com/vllm-project/vllm/issues/48723) [Bug]: [ROCm][gfx1201] AITER update in v0.25.0 generates unified-attention kernel exceeding LDS limit
- [Bug] [#48645](https://github.com/vllm-project/vllm/issues/48645) [Bug]: deepseek_v4 parser: reply without </think> routes the whole answer to reasoning_content (content empty), trailing EOS not stripped
- [no-prefix] ⚠no-prefix [#48667](https://github.com/vllm-project/vllm/issues/48667) Idefics3/SmolVLM: num_patches=0 for non-tiled images mis-sizes pixel_values while the prompt still reserves image_seq_len placeholder tokens

## Uncategorized

### vllm-project/vllm

- [no-prefix] ⚠no-prefix [#48662](https://github.com/vllm-project/vllm/issues/48662) Serving note: pairing vLLM with BGPT evidence MCP for science agents
