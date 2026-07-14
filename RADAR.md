# LLM Serving Issue Radar

_Last run: 2026-07-14T09:26+00:00_

**29 issues** — sgl-project/sglang: 12, vllm-project/vllm: 17 — 🆕 **29 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 8
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 ⚠maintainer-authored [#48485](https://github.com/vllm-project/vllm/issues/48485) [RFC]: Waiting-Queue-Informed LRU for Prefix Cache Eviction

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#48489](https://github.com/vllm-project/vllm/issues/48489) [Bug]: Deferred block-free path loses per-group eviction ordering for hybrid KV cache configs
- [RFC] 🆕 [#48504](https://github.com/vllm-project/vllm/issues/48504) [RFC]: Read-only NIXL GDS connector for filesystem KV-cache loads
- [RFC] 🆕 [#48501](https://github.com/vllm-project/vllm/issues/48501) [RFC]: Session-centric KV-cache orchestration over typed session identity

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31120](https://github.com/sgl-project/sglang/issues/31120) [Bug] Significant Performance Degradation of Qwen3.5-4B on RTX 5090
- [Bug] 🆕 [#31093](https://github.com/sgl-project/sglang/issues/31093) [Bug] GLM-5.2 NVFP4 + EAGLE: CUDA illegal memory access during decode CUDA-graph capture on v0.5.15 and main (works on 2026-07-03 dev-glm52-nvfp4)
- [Bug] 🆕 [#31045](https://github.com/sgl-project/sglang/issues/31045) [Bug] glm-5.2-w4afp8 with sglang0.5.15 error

### vllm-project/vllm

- [Bug] 🆕 [#48590](https://github.com/vllm-project/vllm/issues/48590) [Bug]: LoRA `lora_expand` Triton kernel outputs NaN on Hopper (sm_90) with `block_n=128`, producing garbled LoRA output
- [Bug] 🆕 [#48508](https://github.com/vllm-project/vllm/issues/48508) [Bug]: humming is_layer_skipped ignores compressed-tensors "re:" patterns (ignored layers get quantized; real vs dummy load diverge)
- [Bug] 🆕 [#48493](https://github.com/vllm-project/vllm/issues/48493) [Bug]: `SWIGLUOAI_UNINTERLEAVE requires clamp_limit` blocks MiniMax-M3 AWQ/GPTQ INT4
- [Bug] 🆕 [#48492](https://github.com/vllm-project/vllm/issues/48492) [Bug]: Missing quant_config in MTP eh_proj causes severe silent precision loss during W8A8 quantization
- [Bug] 🆕 [#48491](https://github.com/vllm-project/vllm/issues/48491) [Bug]: cuBLAS NVFP4 GEMM silently rejects M < 128, impacts speech model decode

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#31133](https://github.com/sgl-project/sglang/issues/31133) [Bug] MiniMax sparse prefill: OOB GPU write when max_seqlen_k < seq_lens.max() (silent topk corruption / Xid 31 / NCCL watchdog kills)
- [no-prefix] 🆕 ⚠no-prefix [#31116](https://github.com/sgl-project/sglang/issues/31116) DP attention + prefill CUDA graph + return_routed_experts (gated path): two fixes ready — is enabling it wanted?

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#48591](https://github.com/vllm-project/vllm/issues/48591) 还不支持[Usage]: vllm 0.25版本在tp=8并行的时候走dflash 和dspark 命中 attention后端的时候出现错误报错定位 CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_api.cpp:697): invalid configuration argument 8个worker(TP0-TP7)

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#31127](https://github.com/sgl-project/sglang/issues/31127) [Feature] any plan to support suffix decoding?
- [no-prefix] 🆕 ⚠no-prefix [#31175](https://github.com/sgl-project/sglang/issues/31175) Add native OLMo3 (Olmo3ForCausalLM) support by reusing the Olmo2 implementation

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#31178](https://github.com/sgl-project/sglang/issues/31178) [Bug] D node deployed with sglang glm 5.2 pd is throwing an error when using speculative decoding.
- [Bug] 🆕 [#31071](https://github.com/sgl-project/sglang/issues/31071) [Bug] EAGLE greedy verify lacks TP broadcast → ranks diverge on accepted tokens → collective deadlock (tp>1)

### vllm-project/vllm

- [Bug] 🆕 [#48592](https://github.com/vllm-project/vllm/issues/48592) [Bug]: v0.25.0 torchcodec not compatible with cu129 wheel
- [Bug] 🆕 [#48503](https://github.com/vllm-project/vllm/issues/48503) [Bug]: Gemma 4 MTP speculative decoding crashes during CUDA graph capture (`_suppress_token_ids` is a Python list, not a device tensor)
- [Bug] 🆕 [#48494](https://github.com/vllm-project/vllm/issues/48494) [Bug][Spec Decode] num_speculative_tokens_per_batch_size + MTP speculator fails full CUDA graph decode capture (InputBatch.make_dummy assert)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#31103](https://github.com/sgl-project/sglang/issues/31103) [Bug] qwen3.6-35b-a3b-fp8 still error with sglang 0.5.15
- [Bug] 🆕 ⚠maintainer-authored [#31084](https://github.com/sgl-project/sglang/issues/31084) [Bug] Dynamic LoRA loading is effectively unsupported with --tokenizer-worker-num > 1 (per-worker registry, no cross-worker sync)

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#31046](https://github.com/sgl-project/sglang/issues/31046) [Bug] [Regression] DeepSeek-V4 serving crashes with ValueError: Unrecognized configuration class _DeepseekV4ConfigAlias in v0.5.15 (Works in v0.5.14)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#48541](https://github.com/vllm-project/vllm/issues/48541) [Bug]: FlashInfer CUTLASS MoE selected on fp4-less builds (CUDA toolkit < 12.8); gpt-oss dies at engine start
- [Bug] 🆕 [#48518](https://github.com/vllm-project/vllm/issues/48518) [Bug]: Performance regression caused by high-priority L2 Cache Data Persisting from Server Startup
- [Bug] 🆕 [#48486](https://github.com/vllm-project/vllm/issues/48486) [Bug]: Hang in CUDA Graph replay with PyTorch symmetric-memory all-reduce when profiling with Nsight Systems
- [RFC] 🆕 [#48540](https://github.com/vllm-project/vllm/issues/48540) [RFC]: manylinux compatibility baseline for aarch64 binary dependencies
