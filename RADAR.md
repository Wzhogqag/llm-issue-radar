# LLM Serving Issue Radar

_Last run: 2026-07-14T08:35+00:00_

**25 issues** across 2 repos, uncategorized (Phase 3 output).

## vllm-project/vllm — 15 issues

- [Bug] [#48541](https://github.com/vllm-project/vllm/issues/48541) [Bug]: FlashInfer CUTLASS MoE selected on fp4-less builds (CUDA toolkit < 12.8); gpt-oss dies at engine start
- [RFC] [#48540](https://github.com/vllm-project/vllm/issues/48540) [RFC]: manylinux compatibility baseline for aarch64 binary dependencies
- [Bug] [#48518](https://github.com/vllm-project/vllm/issues/48518) [Bug]: Performance regression caused by high-priority L2 Cache Data Persisting from Server Startup
- [Bug] [#48508](https://github.com/vllm-project/vllm/issues/48508) [Bug]: humming is_layer_skipped ignores compressed-tensors "re:" patterns (ignored layers get quantized; real vs dummy load diverge)
- [RFC] [#48504](https://github.com/vllm-project/vllm/issues/48504) [RFC]: Read-only NIXL GDS connector for filesystem KV-cache loads
- [Bug] [#48503](https://github.com/vllm-project/vllm/issues/48503) [Bug]: Gemma 4 MTP speculative decoding crashes during CUDA graph capture (`_suppress_token_ids` is a Python list, not a device tensor)
- [RFC] [#48501](https://github.com/vllm-project/vllm/issues/48501) [RFC]: Session-centric KV-cache orchestration over typed session identity
- [Bug] [#48494](https://github.com/vllm-project/vllm/issues/48494) [Bug][Spec Decode] num_speculative_tokens_per_batch_size + MTP speculator fails full CUDA graph decode capture (InputBatch.make_dummy assert)
- [Bug] [#48493](https://github.com/vllm-project/vllm/issues/48493) [Bug]: `SWIGLUOAI_UNINTERLEAVE requires clamp_limit` blocks MiniMax-M3 AWQ/GPTQ INT4
- [Bug] [#48491](https://github.com/vllm-project/vllm/issues/48491) [Bug]: cuBLAS NVFP4 GEMM silently rejects M < 128, impacts speech model decode

## sgl-project/sglang — 10 issues

- [Bug] [#31133](https://github.com/sgl-project/sglang/issues/31133) [Bug] MiniMax sparse prefill: OOB GPU write when max_seqlen_k < seq_lens.max() (silent topk corruption / Xid 31 / NCCL watchdog kills)
- [Feature] [#31127](https://github.com/sgl-project/sglang/issues/31127) [Feature] any plan to support suffix decoding?
- [Bug] [#31120](https://github.com/sgl-project/sglang/issues/31120) [Bug] Significant Performance Degradation of Qwen3.5-4B on RTX 5090
- [no-prefix] ⚠no-prefix [#31116](https://github.com/sgl-project/sglang/issues/31116) DP attention + prefill CUDA graph + return_routed_experts (gated path): two fixes ready — is enabling it wanted?
- [Bug] [#31103](https://github.com/sgl-project/sglang/issues/31103) [Bug] qwen3.6-35b-a3b-fp8 still error with sglang 0.5.15
- [Bug] [#31093](https://github.com/sgl-project/sglang/issues/31093) [Bug] GLM-5.2 NVFP4 + EAGLE: CUDA illegal memory access during decode CUDA-graph capture on v0.5.15 and main (works on 2026-07-03 dev-glm52-nvfp4)
- [Bug] [#31084](https://github.com/sgl-project/sglang/issues/31084) [Bug] Dynamic LoRA loading is effectively unsupported with --tokenizer-worker-num > 1 (per-worker registry, no cross-worker sync)
- [Bug] [#31071](https://github.com/sgl-project/sglang/issues/31071) [Bug] EAGLE greedy verify lacks TP broadcast → ranks diverge on accepted tokens → collective deadlock (tp>1)
- [Bug] [#31046](https://github.com/sgl-project/sglang/issues/31046) [Bug] [Regression] DeepSeek-V4 serving crashes with ValueError: Unrecognized configuration class _DeepseekV4ConfigAlias in v0.5.15 (Works in v0.5.14)
- [Bug] [#31045](https://github.com/sgl-project/sglang/issues/31045) [Bug] glm-5.2-w4afp8 with sglang0.5.15 error
