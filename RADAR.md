# LLM Serving Issue Radar

_Last run: 2026-08-16T13:30+00:00_

**33 issues** — sgl-project/sglang: 12, vllm-project/vllm: 21 — 🆕 **22 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 7
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 5
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 7
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] [#34941](https://github.com/sgl-project/sglang/issues/34941) [Bug] DSA sparse-MLA prefill silently computes no attention at all for a single extend > 65535 tokens (trtllm-gen gridDim.z limit is still unguarded on the non-DP path)

### vllm-project/vllm

- [Bug] 🆕 [#52475](https://github.com/vllm-project/vllm/issues/52475) [Bug]: MTP speculative decoding produces repetition collapse with turboquant_* KV cache on sm120 (Qwen3.8-27B hybrid GDN)
- [other] [#52408](https://github.com/vllm-project/vllm/issues/52408) [Docs/Robustness] NIXL connector: the block_len_per_layer == seen_base_addresses assert is load-bearing for hybrid-Mamba descriptor IDs
- [no-prefix] ⚠no-prefix ⚠maintainer-authored [#52409](https://github.com/vllm-project/vllm/issues/52409) EPD Tracker

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#34972](https://github.com/sgl-project/sglang/issues/34972) [Bug] HiCache host-pool memory check (psutil.virtual_memory().available) does not account for reserved HugePages, causing false "Not enough host memory" failures
- [Bug] 🆕 [#34969](https://github.com/sgl-project/sglang/issues/34969) [Bug] HF3FS HiCache hits ZeroDivisionError with DeepSeek-V4 logical KV anchor

## Quantization

### sgl-project/sglang

- [Perf] 🆕 [#35019](https://github.com/sgl-project/sglang/issues/35019) [Perf] No MMQ kernel for I-quant GGUF: 4-6x slower prefill than llama.cpp on the same weights (measured)
- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#35003](https://github.com/sgl-project/sglang/issues/35003) AMD Development Roadmap (2026 Q3)
- [other] [#34918](https://github.com/sgl-project/sglang/issues/34918) [Playground] Verified cell: rtx6000 / default / nvfp4 / balanced / single

### vllm-project/vllm

- [Bug] 🆕 [#52480](https://github.com/vllm-project/vllm/issues/52480) [Bug]: qwen3_5_mtp fails to load at tensor-parallel-size >= 2 (drafter weight shape mismatch)
- [Bug] 🆕 [#52454](https://github.com/vllm-project/vllm/issues/52454) [Bug]: Qwen 3.8 quark int4 loading failed.
- [Bug] 🆕 [#52407](https://github.com/vllm-project/vllm/issues/52407) [Bug]: VLLM_BATCH_INVARIANT=1 crashes NVFP4 models: emulation break_fp4_bytes device mismatch (lookup table on CPU, indices on GPU)
- [Feature] [#52447](https://github.com/vllm-project/vllm/issues/52447) [Feature]: Support NVFP4 DeepSeek-V4-Flash-0731 with FP4 KV cache + DSpark speculative decoding on SM121 (DGX Spark)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] [#34920](https://github.com/sgl-project/sglang/issues/34920) [Bug] Kimi K3 decode crash: DSPARK target_verify + DCP → cumsum(extend_prefix_lens=None) in layers/dcp/planner.py

### vllm-project/vllm

- [Bug] 🆕 [#52504](https://github.com/vllm-project/vllm/issues/52504) [Bug] Cross-node TP CUDA-graph replay deadlocks with NCCL 2.28.9 (fixed by NCCL 2.30.4) — watchdog "RPC call to sample_tokens timed out"

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34974](https://github.com/sgl-project/sglang/issues/34974) [Bug] --enable-eplb + --speculative-algorithm DSPARK crashes during draft CUDA graph capture: on_select_experts scatter_add_ dimension mismatch (layer_idx=None)
- [Bug] 🆕 [#34959](https://github.com/sgl-project/sglang/issues/34959) [Bug] DSPARK silently corrupts identifiers on DeepSeek-V4-Flash, making speculative decoding unsafe
- [Bug] [#34943](https://github.com/sgl-project/sglang/issues/34943) [Bug] Stopping the by-stage profiler under speculative decoding freezes the scheduler for ~25 s (synchronous trace export on the scheduler thread), and the stop condition leaks into later requests
- [no-prefix] ⚠no-prefix [#34942](https://github.com/sgl-project/sglang/issues/34942) --profile-by-stage with speculative decoding: profiler never stops on decode batches (TARGET_VERIFY counted as prefill); deferred stop + synchronous trace export freeze the server for ~25 s inside later unrelated requests

### vllm-project/vllm

- [Bug] 🆕 [#52461](https://github.com/vllm-project/vllm/issues/52461) [Bug]: Under async scheduling, stateful logits processors that read output_token_ids values see -1 placeholders — logitsprocs_need_output_token_ids only counts CLI custom processors

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#52443](https://github.com/vllm-project/vllm/issues/52443) [Bug]: Harmony browser.* streaming emits both MCP and web-search events
- [Bug] 🆕 [#52410](https://github.com/vllm-project/vllm/issues/52410) [Bug]: Gemma4 parser defaults omitted enable_thinking to true while the template defaults false
- [no-prefix] 🆕 ⚠no-prefix [#52471](https://github.com/vllm-project/vllm/issues/52471) Streaming input: per-chunk arrival cost is O(cumulative prompt), making long multimodal sessions quadratic

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#52457](https://github.com/vllm-project/vllm/issues/52457) [Bug]: 0.27.1 crashes in custom_all_reduce (illegal memory access) during CUDA graph capture on Hopper TP=4; identical config works on 0.26.0
- [Bug] 🆕 ⚠maintainer-authored [#52511](https://github.com/vllm-project/vllm/issues/52511) [Bug]: FlashInfer TRT-LLM bf16 MoE weight-conversion OOM recurs post-#45589 at TP2 (120B MoE, GB200) — cumem MemPool still doesn't reclaim under pressure

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#52435](https://github.com/vllm-project/vllm/issues/52435) [Bug]: AssertionError: n_physical_experts=256 must be divisible by ep_size=3. Adjust num_redundant_experts.
- [Bug] 🆕 [#52416](https://github.com/vllm-project/vllm/issues/52416) [Bug] XPU qnorm/rope kernel: int32 overflow in the address computation past 2^31 q elements
- [Bug] 🆕 [#52453](https://github.com/vllm-project/vllm/issues/52453) [Bug]: the issues about install vllm with cuda 12.6, Why hasn't anyone answered this question?
- [Bug] 🆕 ⚠maintainer-authored [#52413](https://github.com/vllm-project/vllm/issues/52413) [Bug]: Alignment specialization on causal_conv1d metadata pointers forces inference-time JIT compiles; raced shared-cache writes produced silent all-NaN outputs
- [Bug] [#52434](https://github.com/vllm-project/vllm/issues/52434) [Bug]: AttributeError: 'ParallelLMHead' object has no attribute 'output_size_per_partition'
- [Bug] [#52415](https://github.com/vllm-project/vllm/issues/52415) [Bug] XPU qnorm/rope kernel: overlapping stores in one program corrupt the KV cache nondeterministically
- [Bug] [#52442](https://github.com/vllm-project/vllm/issues/52442) [Bug][ROCm] Kimi-K3 a8w4 SiTU MoE: AITER_SITUV2_A8W4 without VLLM_ROCM_USE_AITER_MOE_SITUV2_A8W4 silently produces garbage

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#35012](https://github.com/sgl-project/sglang/issues/35012) [Bug] The timeout setting is invalid in can_terminate_prefetch when pool_transfers_done is false
