# Weekly Trends — 2026-08-16

Window: 2026-08-10 → 2026-08-16 (7 snapshots)

**Totals:** 22 → 33  (33 appeared, 22 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 3 | 2 | -1 | 2 | 3 |
| Build / Install / Platform | 4 | 7 | +3 | 7 | 4 |
| Distributed / TP / PP / EP | 0 | 2 | +2 | 2 | 0 |
| KV Cache / Connector / PD Disagg | 3 | 4 | +1 | 4 | 3 |
| New Model Integration | 1 | 0 | -1 | 0 | 1 |
| Performance / Memory / OOM | 0 | 2 | +2 | 2 | 0 |
| Quantization | 5 | 7 | +2 | 7 | 5 |
| Sampling / Speculative Decoding | 3 | 5 | +2 | 5 | 3 |
| Scheduler / Batching | 1 | 0 | -1 | 0 | 1 |
| Serving / OpenAI API / Streaming | 2 | 3 | +1 | 3 | 2 |
| Uncategorized | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#34969](https://github.com/sgl-project/sglang/issues/34969) [Bug] HF3FS HiCache hits ZeroDivisionError with DeepSeek-V4 logical KV anchor
- [Bug] [sgl-project/sglang#34972](https://github.com/sgl-project/sglang/issues/34972) [Bug] HiCache host-pool memory check (psutil.virtual_memory().available) does not account for reserved HugePages, causing false "Not enough host memory" failures

### Build / Install / Platform

- [Bug] [vllm-project/vllm#52413](https://github.com/vllm-project/vllm/issues/52413) [Bug]: Alignment specialization on causal_conv1d metadata pointers forces inference-time JIT compiles; raced shared-cache writes produced silent all-NaN outputs
- [Bug] [vllm-project/vllm#52415](https://github.com/vllm-project/vllm/issues/52415) [Bug] XPU qnorm/rope kernel: overlapping stores in one program corrupt the KV cache nondeterministically
- [Bug] [vllm-project/vllm#52416](https://github.com/vllm-project/vllm/issues/52416) [Bug] XPU qnorm/rope kernel: int32 overflow in the address computation past 2^31 q elements
- [Bug] [vllm-project/vllm#52434](https://github.com/vllm-project/vllm/issues/52434) [Bug]: AttributeError: 'ParallelLMHead' object has no attribute 'output_size_per_partition'
- [Bug] [vllm-project/vllm#52435](https://github.com/vllm-project/vllm/issues/52435) [Bug]: AssertionError: n_physical_experts=256 must be divisible by ep_size=3. Adjust num_redundant_experts.
- [Bug] [vllm-project/vllm#52442](https://github.com/vllm-project/vllm/issues/52442) [Bug][ROCm] Kimi-K3 a8w4 SiTU MoE: AITER_SITUV2_A8W4 without VLLM_ROCM_USE_AITER_MOE_SITUV2_A8W4 silently produces garbage
- [Bug] [vllm-project/vllm#52453](https://github.com/vllm-project/vllm/issues/52453) [Bug]: the issues about install vllm with cuda 12.6, Why hasn't anyone answered this question?

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#34920](https://github.com/sgl-project/sglang/issues/34920) [Bug] Kimi K3 decode crash: DSPARK target_verify + DCP → cumsum(extend_prefix_lens=None) in layers/dcp/planner.py
- [Bug] [vllm-project/vllm#52504](https://github.com/vllm-project/vllm/issues/52504) [Bug] Cross-node TP CUDA-graph replay deadlocks with NCCL 2.28.9 (fixed by NCCL 2.30.4) — watchdog "RPC call to sample_tokens timed out"

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#34941](https://github.com/sgl-project/sglang/issues/34941) [Bug] DSA sparse-MLA prefill silently computes no attention at all for a single extend > 65535 tokens (trtllm-gen gridDim.z limit is still unguarded on the non-DP path)
- [other] [vllm-project/vllm#52408](https://github.com/vllm-project/vllm/issues/52408) [Docs/Robustness] NIXL connector: the block_len_per_layer == seen_base_addresses assert is load-bearing for hybrid-Mamba descriptor IDs
- [no-prefix] [vllm-project/vllm#52409](https://github.com/vllm-project/vllm/issues/52409) EPD Tracker
- [Bug] [vllm-project/vllm#52475](https://github.com/vllm-project/vllm/issues/52475) [Bug]: MTP speculative decoding produces repetition collapse with turboquant_* KV cache on sm120 (Qwen3.8-27B hybrid GDN)

### Performance / Memory / OOM

- [Bug] [vllm-project/vllm#52457](https://github.com/vllm-project/vllm/issues/52457) [Bug]: 0.27.1 crashes in custom_all_reduce (illegal memory access) during CUDA graph capture on Hopper TP=4; identical config works on 0.26.0
- [Bug] [vllm-project/vllm#52511](https://github.com/vllm-project/vllm/issues/52511) [Bug]: FlashInfer TRT-LLM bf16 MoE weight-conversion OOM recurs post-#45589 at TP2 (120B MoE, GB200) — cumem MemPool still doesn't reclaim under pressure

### Quantization

- [other] [sgl-project/sglang#34918](https://github.com/sgl-project/sglang/issues/34918) [Playground] Verified cell: rtx6000 / default / nvfp4 / balanced / single
- [no-prefix] [sgl-project/sglang#35003](https://github.com/sgl-project/sglang/issues/35003) AMD Development Roadmap (2026 Q3)
- [Perf] [sgl-project/sglang#35019](https://github.com/sgl-project/sglang/issues/35019) [Perf] No MMQ kernel for I-quant GGUF: 4-6x slower prefill than llama.cpp on the same weights (measured)
- [Bug] [vllm-project/vllm#52407](https://github.com/vllm-project/vllm/issues/52407) [Bug]: VLLM_BATCH_INVARIANT=1 crashes NVFP4 models: emulation break_fp4_bytes device mismatch (lookup table on CPU, indices on GPU)
- [Feature] [vllm-project/vllm#52447](https://github.com/vllm-project/vllm/issues/52447) [Feature]: Support NVFP4 DeepSeek-V4-Flash-0731 with FP4 KV cache + DSpark speculative decoding on SM121 (DGX Spark)
- [Bug] [vllm-project/vllm#52454](https://github.com/vllm-project/vllm/issues/52454) [Bug]: Qwen 3.8 quark int4 loading failed.
- [Bug] [vllm-project/vllm#52480](https://github.com/vllm-project/vllm/issues/52480) [Bug]: qwen3_5_mtp fails to load at tensor-parallel-size >= 2 (drafter weight shape mismatch)

### Sampling / Speculative Decoding

- [no-prefix] [sgl-project/sglang#34942](https://github.com/sgl-project/sglang/issues/34942) --profile-by-stage with speculative decoding: profiler never stops on decode batches (TARGET_VERIFY counted as prefill); deferred stop + synchronous trace export freeze the server for ~25 s inside later unrelated requests
- [Bug] [sgl-project/sglang#34943](https://github.com/sgl-project/sglang/issues/34943) [Bug] Stopping the by-stage profiler under speculative decoding freezes the scheduler for ~25 s (synchronous trace export on the scheduler thread), and the stop condition leaks into later requests
- [Bug] [sgl-project/sglang#34959](https://github.com/sgl-project/sglang/issues/34959) [Bug] DSPARK silently corrupts identifiers on DeepSeek-V4-Flash, making speculative decoding unsafe
- [Bug] [sgl-project/sglang#34974](https://github.com/sgl-project/sglang/issues/34974) [Bug] --enable-eplb + --speculative-algorithm DSPARK crashes during draft CUDA graph capture: on_select_experts scatter_add_ dimension mismatch (layer_idx=None)
- [Bug] [vllm-project/vllm#52461](https://github.com/vllm-project/vllm/issues/52461) [Bug]: Under async scheduling, stateful logits processors that read output_token_ids values see -1 placeholders — logitsprocs_need_output_token_ids only counts CLI custom processors

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#52410](https://github.com/vllm-project/vllm/issues/52410) [Bug]: Gemma4 parser defaults omitted enable_thinking to true while the template defaults false
- [Bug] [vllm-project/vllm#52443](https://github.com/vllm-project/vllm/issues/52443) [Bug]: Harmony browser.* streaming emits both MCP and web-search events
- [no-prefix] [vllm-project/vllm#52471](https://github.com/vllm-project/vllm/issues/52471) Streaming input: per-chunk arrival cost is O(cumulative prompt), making long multimodal sessions quadratic

### Uncategorized

- [Bug] [sgl-project/sglang#35012](https://github.com/sgl-project/sglang/issues/35012) [Bug] The timeout setting is invalid in can_terminate_prefetch when pool_transfers_done is false

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [sgl-project/sglang#34259](https://github.com/sgl-project/sglang/issues/34259) [Bug] Kimi-K3 - cross prompt reasoning leakage
- [Bug] [sgl-project/sglang#34260](https://github.com/sgl-project/sglang/issues/34260) [Bug] Kimi-K3 - sglang crash
- [Bug] [vllm-project/vllm#51658](https://github.com/vllm-project/vllm/issues/51658) [Bug]: attention backend probe in cuda.py catches only ImportError; non-ImportError side effects (e.g. cache PermissionError, CUDA runtime   mismatch) crash engine init instead of being recorded as unavailable

### Build / Install / Platform

- [Bug] [vllm-project/vllm#51572](https://github.com/vllm-project/vllm/issues/51572) [Bug]:Anthropic Messages API: x-api-key authentication header not supported — only Authorization: Bearer works
- [Bug] [vllm-project/vllm#51580](https://github.com/vllm-project/vllm/issues/51580) [Bug]: [ROCm] v0.26.0 release image: NaN logits from AITER fused-MoE path on gfx942 (Qwen3.5-397B-A17B-FP8) — fixed on main, requesting 0.26.x backport
- [Bug] [vllm-project/vllm#51663](https://github.com/vllm-project/vllm/issues/51663) [Bug]: Massive output-token throughput regression since v0.24.0 with Qwen3.6-35B-A3B-FP8
- [Bug] [vllm-project/vllm#51677](https://github.com/vllm-project/vllm/issues/51677) [Bug]: NVML UUID resolution fails for NVIDIA's documented short-form CUDA_VISIBLE_DEVICES UUIDs

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#51567](https://github.com/vllm-project/vllm/issues/51567) [Bug]: EPLB fails to transport E8M0 expert state
- [Bug] [vllm-project/vllm#51579](https://github.com/vllm-project/vllm/issues/51579) [Bug]: OffloadingConnector CPU tier leaks its /dev/shm mmap file on any unclean exit (including SIGKILL)
- [RFC] [vllm-project/vllm#51639](https://github.com/vllm-project/vllm/issues/51639) [RFC]: Generic Control RPC for KV Connectors

### New Model Integration

- [other] [vllm-project/vllm#51619](https://github.com/vllm-project/vllm/issues/51619) [New Model]: Support CrisperWhisper 2.0

### Quantization

- [no-prefix] [sgl-project/sglang#34179](https://github.com/sgl-project/sglang/issues/34179) W4A4 MegaMoE FP4-acts on DeepSeek-V4-Flash-0731 (8x B200, SGLang v0.5.17): end-to-end TTFT unchanged on two serving shapes (scheduling-bound and GEMM-bound), plus bounded quality observations
- [Bug] [sgl-project/sglang#34192](https://github.com/sgl-project/sglang/issues/34192) [Bug] Llama4 NVFP4 MoE crashes on SM120/SM121: apply_router_weight_on_input is not supported for Flashinfer
- [no-prefix] [sgl-project/sglang#34193](https://github.com/sgl-project/sglang/issues/34193) Where do CPU kernel patches go after sgl-kernel moved under sglang.kernels.aot?
- [RFC] [sgl-project/sglang#34295](https://github.com/sgl-project/sglang/issues/34295) [RFC] Remove the torchao integration (`--torchao-config`)
- [Bug] [vllm-project/vllm#51660](https://github.com/vllm-project/vllm/issues/51660) [Bug]: No viable structured-outputs backend for Kimi-K2.6 + EAGLE3 on v0.26.0: xgrammar bitmask desync kills the engine, outlines compile-timeout leaks threads until OOM, guidance rejects the slow tokenizer

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#34211](https://github.com/sgl-project/sglang/issues/34211) [Bug] [NPU] (v0.5.17)Eco-Tech/Qwen3.6-35B-A3B-w8a8 Model Served with four 910B: ValueError: Unsupported ModelSlim MoE schemes for layer mtp.layers.0.mlp.experts: W13='FLOAT', W2='FLOAT'
- [Bug] [sgl-project/sglang#34239](https://github.com/sgl-project/sglang/issues/34239) [Bug] Qwen3.5-397B + NEXTN crashes with CUDA illegal memory access near 262144 context boundary on v0.5.16 (H800 TP8)
- [Bug] [vllm-project/vllm#51571](https://github.com/vllm-project/vllm/issues/51571) [Bug]: Async MTP align mode reads accepted counts from mutable InputBatch rows

### Scheduler / Batching

- [RFC] [vllm-project/vllm#51608](https://github.com/vllm-project/vllm/issues/51608) [RFC]: Extensible Scheduler Plugin Framework for vLLM

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#51651](https://github.com/vllm-project/vllm/issues/51651) [Bug]: Missing `reasoning` on Some Turns in Multi-Turn Tool-Calling (DeepSeek-V4-Flash-0731)
- [Bug] [vllm-project/vllm#51679](https://github.com/vllm-project/vllm/issues/51679) [Bug]: qwen3_xml tool parser consumes `</think>`, merging reasoning into `content` with no way to split it
