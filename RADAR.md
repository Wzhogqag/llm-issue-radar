# LLM Serving Issue Radar

_Last run: 2026-07-17T13:57+00:00_

**24 issues** — sgl-project/sglang: 8, vllm-project/vllm: 16 — 🆕 **23 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 11
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#31473](https://github.com/sgl-project/sglang/issues/31473) Optimistic prefill can reach a cross-stage capacity stall

## Attention Backend

### sgl-project/sglang

- [Feature] 🆕 [#31578](https://github.com/sgl-project/sglang/issues/31578) [Feature] Native SM120 (Blackwell) support for flash_mla_sparse_fwd (DeepSeek-V4 sparse-attention prefill)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31490](https://github.com/sgl-project/sglang/issues/31490) [Bug] GSM8K accuracy regression on DeepSeek-V4-Flash-FP8 (dp8ep8, gfx950) traced to #29275 "Fix gfx95 bpreshuffle FP8 activation scale layout"
- [Feature] 🆕 [#31570](https://github.com/sgl-project/sglang/issues/31570) [Feature] [NPU] Implement CI test for different quantization prefixes (w1/2/3; gate/up/down_proj)
- [other] 🆕 ⚠maintainer-authored [#31504](https://github.com/sgl-project/sglang/issues/31504) [Proposal] Fuse static FP8 activation quantization into producer kernels (norm / activation / allreduce epilogue)

### vllm-project/vllm

- [Bug] 🆕 [#48946](https://github.com/vllm-project/vllm/issues/48946) [Bug][XPU]: gpt-oss-120b (MXFP4 MoE, TP=2) corrupt under piecewise XPU graph capture on Data Center GPU Max 1100 (PVC); compile-mode correct
- [Bug] 🆕 [#48904](https://github.com/vllm-project/vllm/issues/48904) [Bug]: VLLM_MARLIN_INPUT_DTYPE=int8 silently ignored for auto-round (INC) checkpoints
- [Bug] 🆕 [#48898](https://github.com/vllm-project/vllm/issues/48898) [Bug]: ModelOpt NVFP4 dense model outputs garbage on SM120 (RTX 6000D/RTX PRO 6000): FlashInferCutlass and native Cutlass NVFP4 kernels both incorrect, only Marlin correct
- [Bug] 🆕 [#48895](https://github.com/vllm-project/vllm/issues/48895) [Bug]: moe_wna16_marlin_gemm applies wrong per-row topk weights (mul_topk_weights=True) at gpt-oss NVFP4 MoE shapes — corrupt output
- [Bug] 🆕 [#48945](https://github.com/vllm-project/vllm/issues/48945) [Bug]: Ministral is broken with --kv-cache-dtype fp8 in 0.25.1
- [Feature] 🆕 [#48921](https://github.com/vllm-project/vllm/issues/48921) [Feature]: FlashInfer-CUTLASS NVFP4 MoE lacks SWIGLUSTEP activation (blocks Step-3.7-Flash-NVFP4 at TP=8)
- [RFC] 🆕 [#48941](https://github.com/vllm-project/vllm/issues/48941) [RFC] Recursive Tensor Collector: Fix CUDA Graph Invalidation After Weight Reload
- [no-prefix] 🆕 ⚠no-prefix [#48862](https://github.com/vllm-project/vllm/issues/48862) LoRA Triton kernel crashes with NVFP4 (modelopt_fp4) quantization - CUDA illegal memory access

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#31568](https://github.com/sgl-project/sglang/issues/31568) [Bug] Unused/unnecessary tl.constexpr params causing Triton cache-key pollution in KV-cache and FLA kernels

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#48919](https://github.com/vllm-project/vllm/issues/48919) [Bug]: CPU offloading fails with block_size=256 + speculative decoding due to eagle group block_size mismatch
- [Bug] 🆕 [#48894](https://github.com/vllm-project/vllm/issues/48894) [Bug]: EAGLE-3 + prompts >2048 tokens: device-side assert (Triton `index < 2048`) in inductor-compiled eagle_head kernels; eager works, cudagraph_mode=NONE still crashes (v0.24.0)
- [Bug] 🆕 [#48853](https://github.com/vllm-project/vllm/issues/48853) [Bug]: FastIncrementalDetokenizer leaks full prompt text into streamed output when prompt ends with an incomplete UTF-8 token
- [Bug] [#48848](https://github.com/vllm-project/vllm/issues/48848) [Bug]: Gemma4 MTP speculative decoding crashes at engine init on 0.25.1 — "a and b must have same reduction dim" (regression from 0.21.0)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#48931](https://github.com/vllm-project/vllm/issues/48931) [Bug] DeepSeek-V4 tool-call parser leaks raw DSML into content when the model omits the `<｜DSML｜tool_calls>` START token (long context)
- [Bug] 🆕 [#48874](https://github.com/vllm-project/vllm/issues/48874) [Bug]: Anthropic /v1/messages renders system-role messages inside `messages` positionally into the chat template (breaks Claude Code >=2.1.2xx tool calling)
- [no-prefix] 🆕 ⚠no-prefix [#48863](https://github.com/vllm-project/vllm/issues/48863) reasoning: null content when include_reasoning=False + json_schema response_format (introduced v0.23.1)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#31545](https://github.com/sgl-project/sglang/issues/31545) [Bug][ROCm] MI355X: CUDA-graph decode kernels are captured but async-deferred into one post-marker burst — per-step timing unrecoverable (torch profiler)

### vllm-project/vllm

- [Bug] 🆕 [#48840](https://github.com/vllm-project/vllm/issues/48840) [Bug]: AssertionError: graph_pool_id is not set under graph capture when VLLM_USE_NCCL_SYMM_MEM=1 with ModelRunner V2

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#31505](https://github.com/sgl-project/sglang/issues/31505) [Bug] how to use hicache l2(dram) to muti host(muti inference instances ,not pd ) share kvcache offload ?
