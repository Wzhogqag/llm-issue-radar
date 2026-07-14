# LLM Serving Issue Radar

_Last run: 2026-07-14T13:59+00:00_

**22 issues** — sgl-project/sglang: 10, vllm-project/vllm: 12 — 🆕 **2 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 4

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] [#48504](https://github.com/vllm-project/vllm/issues/48504) [RFC]: Read-only NIXL GDS connector for filesystem KV-cache loads
- [RFC] [#48501](https://github.com/vllm-project/vllm/issues/48501) [RFC]: Session-centric KV-cache orchestration over typed session identity

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 [#48613](https://github.com/vllm-project/vllm/issues/48613) [Feature]: [Batch-Invariant-Kernels] GDN_ATTN does not support batch-invariant mode for Qwen3.5/Qwen3.6 GDN models

## Quantization

### sgl-project/sglang

- [Bug] [#31120](https://github.com/sgl-project/sglang/issues/31120) [Bug] Significant Performance Degradation of Qwen3.5-4B on RTX 5090
- [Bug] [#31093](https://github.com/sgl-project/sglang/issues/31093) [Bug] GLM-5.2 NVFP4 + EAGLE: CUDA illegal memory access during decode CUDA-graph capture on v0.5.15 and main (works on 2026-07-03 dev-glm52-nvfp4)

### vllm-project/vllm

- [Bug] [#48590](https://github.com/vllm-project/vllm/issues/48590) [Bug]: LoRA `lora_expand` Triton kernel outputs NaN on Hopper (sm_90) with `block_n=128`, producing garbled LoRA output
- [Bug] [#48508](https://github.com/vllm-project/vllm/issues/48508) [Bug]: humming is_layer_skipped ignores compressed-tensors "re:" patterns (ignored layers get quantized; real vs dummy load diverge)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] [#31133](https://github.com/sgl-project/sglang/issues/31133) [Bug] MiniMax sparse prefill: OOB GPU write when max_seqlen_k < seq_lens.max() (silent topk corruption / Xid 31 / NCCL watchdog kills)
- [no-prefix] ⚠no-prefix [#31116](https://github.com/sgl-project/sglang/issues/31116) DP attention + prefill CUDA graph + return_routed_experts (gated path): two fixes ready — is enabling it wanted?

### vllm-project/vllm

- [no-prefix] ⚠no-prefix [#48591](https://github.com/vllm-project/vllm/issues/48591) 还不支持[Usage]: vllm 0.25版本在tp=8并行的时候走dflash 和dspark 命中 attention后端的时候出现错误报错定位 CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_api.cpp:697): invalid configuration argument 8个worker(TP0-TP7)

## New Model Integration

### sgl-project/sglang

- [Feature] [#31127](https://github.com/sgl-project/sglang/issues/31127) [Feature] any plan to support suffix decoding?
- [no-prefix] ⚠no-prefix [#31175](https://github.com/sgl-project/sglang/issues/31175) Add native OLMo3 (Olmo3ForCausalLM) support by reusing the Olmo2 implementation

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] [#31178](https://github.com/sgl-project/sglang/issues/31178) [Bug] D node deployed with sglang glm 5.2 pd is throwing an error when using speculative decoding.
- [Bug] [#31071](https://github.com/sgl-project/sglang/issues/31071) [Bug] EAGLE greedy verify lacks TP broadcast → ranks diverge on accepted tokens → collective deadlock (tp>1)

### vllm-project/vllm

- [Bug] [#48592](https://github.com/vllm-project/vllm/issues/48592) [Bug]: v0.25.0 torchcodec not compatible with cu129 wheel
- [Bug] [#48503](https://github.com/vllm-project/vllm/issues/48503) [Bug]: Gemma 4 MTP speculative decoding crashes during CUDA graph capture (`_suppress_token_ids` is a Python list, not a device tensor)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] [#31103](https://github.com/sgl-project/sglang/issues/31103) [Bug] qwen3.6-35b-a3b-fp8 still error with sglang 0.5.15
- [Bug] ⚠maintainer-authored [#31084](https://github.com/sgl-project/sglang/issues/31084) [Bug] Dynamic LoRA loading is effectively unsupported with --tokenizer-worker-num > 1 (per-worker registry, no cross-worker sync)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#48602](https://github.com/vllm-project/vllm/issues/48602) [Bug]: DeepSeekv4 flash on RTXpro6000 vllm benchmark input 8192 output 1024 encounter a err
- [Bug] [#48541](https://github.com/vllm-project/vllm/issues/48541) [Bug]: FlashInfer CUTLASS MoE selected on fp4-less builds (CUDA toolkit < 12.8); gpt-oss dies at engine start
- [Bug] [#48518](https://github.com/vllm-project/vllm/issues/48518) [Bug]: Performance regression caused by high-priority L2 Cache Data Persisting from Server Startup
- [RFC] [#48540](https://github.com/vllm-project/vllm/issues/48540) [RFC]: manylinux compatibility baseline for aarch64 binary dependencies
