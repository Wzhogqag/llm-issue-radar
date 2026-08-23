# Weekly Trends — 2026-08-23

Window: 2026-08-17 → 2026-08-23 (7 snapshots)

**Totals:** 25 → 24  (24 appeared, 25 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 1 | 0 | 1 | 1 |
| Build / Install / Platform | 9 | 4 | -5 | 4 | 9 |
| Distributed / TP / PP / EP | 1 | 1 | 0 | 1 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 4 | +2 | 4 | 2 |
| New Model Integration | 2 | 2 | 0 | 2 | 2 |
| Performance / Memory / OOM | 1 | 1 | 0 | 1 | 1 |
| Quantization | 3 | 3 | 0 | 3 | 3 |
| Sampling / Speculative Decoding | 3 | 4 | +1 | 4 | 3 |
| Scheduler / Batching | 2 | 1 | -1 | 1 | 2 |
| Serving / OpenAI API / Streaming | 1 | 3 | +2 | 3 | 1 |

## Appeared this week

### Attention Backend

- [Bug] [vllm-project/vllm#53413](https://github.com/vllm-project/vllm/issues/53413) [Bug]: GLM-5.2 FP8 on 8×H200 dies with runtime CUDA OOM in sparse_decode_fwd

### Build / Install / Platform

- [Bug] [sgl-project/sglang#36058](https://github.com/sgl-project/sglang/issues/36058) [Bug] /usr/bin/ld: cannot find -lcuda: No such file or directory collect2: error: ld returned 1 exit status ninja: build stopped: subcommand failed.
- [Bug] [vllm-project/vllm#53359](https://github.com/vllm-project/vllm/issues/53359) [Bug]: tool_call_parser_invocations_total no longer increments for engine-backed parsers (regression after ParserEngine refactor)
- [Bug] [vllm-project/vllm#53411](https://github.com/vllm-project/vllm/issues/53411) [Bug]: DeepSeek v4 Pro Base - The default MoE backend selection produces incorrect output and inflated logprobs (FlashInfer TRTLLM vs deep_gemm)
- [Bug] [vllm-project/vllm#53434](https://github.com/vllm-project/vllm/issues/53434) [Bug]: Long term continuous operation leads to an increase in model output illusion

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#36018](https://github.com/sgl-project/sglang/issues/36018) [Bug] Kimi-K3 crash in v0.5.18 release

### KV Cache / Connector / PD Disagg

- [other] [sgl-project/sglang#36033](https://github.com/sgl-project/sglang/issues/36033) [PD] Inconsistent prefill→decode failure notification across transfer backends; NIXL has none
- [Feature] [sgl-project/sglang#36083](https://github.com/sgl-project/sglang/issues/36083) [Feature] Extend cross-layer index-topk reuse (dsa_layer_skips_topk) to DeepSeek-V4
- [Feature] [vllm-project/vllm#53368](https://github.com/vllm-project/vllm/issues/53368) [Feature]: Expose CPU vs P2P attribution for multi-tier KV restores
- [RFC] [vllm-project/vllm#53371](https://github.com/vllm-project/vllm/issues/53371) [RFC]: Optimization: Take over a partial-hit block instead of CoW copy when ref_cnt == 1

### New Model Integration

- [Feature] [vllm-project/vllm#53445](https://github.com/vllm-project/vllm/issues/53445) [Feature]: Native support for Granite Switch (GraniteSwitchForCausalLM)
- [Feature] [vllm-project/vllm#53455](https://github.com/vllm-project/vllm/issues/53455) [Feature]: Optional torch.compile support for NVIDIA DeepSeek-V4

### Performance / Memory / OOM

- [Perf] [vllm-project/vllm#53459](https://github.com/vllm-project/vllm/issues/53459) [Perf] Indexer score GEMM uses fp32 accumulate on DeepSeek-V4; bf16 may be sufficient

### Quantization

- [Bug] [sgl-project/sglang#36048](https://github.com/sgl-project/sglang/issues/36048) [Bug] Qwen3.8-27B AWQ has no usable fast path on single Ada SM89 32GB: CUDA graph hangs and native MTP cannot allocate requests
- [Bug] [vllm-project/vllm#53387](https://github.com/vllm-project/vllm/issues/53387) [Bug]: Qwen3.5-family native MTP crashes with compressed-tensors WNA16 checkpoints (unquantized mtp.fc)
- [Bug] [vllm-project/vllm#53390](https://github.com/vllm-project/vllm/issues/53390) [Bug]: int32 token-offset overflow in silu_and_mul_per_block_quant (act_quant fusion) — illegal memory access above ~2^31/(2*intermediate_size) batched tokens

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#53363](https://github.com/vllm-project/vllm/issues/53363) [Bug]: tool_choice="required" not enforced with gemma4 tool parser — prose-only response returned with finish_reason="tool_calls" and empty tool_calls
- [Bug] [vllm-project/vllm#53366](https://github.com/vllm-project/vllm/issues/53366) [Bug]: torch.compile cache key does not include num_speculative_tokens, causing compiled-graph collision across different speculative-token counts
- [Bug] [vllm-project/vllm#53391](https://github.com/vllm-project/vllm/issues/53391) [Bug][DSV4-Flash][DSpark] Startup dies in kernel warmup with "ragged spec decode batch: 7 tokens over 2 requests"
- [Bug] [vllm-project/vllm#53436](https://github.com/vllm-project/vllm/issues/53436) [Bug]: Run-to-run performance non-determinism with speculative decoding at temperature=0 (fixed seed) on DeepSeek-V4-Flash / Blackwell SM120

### Scheduler / Batching

- [RFC] [vllm-project/vllm#53401](https://github.com/vllm-project/vllm/issues/53401) [RFC]: Experimental Recirculation for causal decoders

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#36081](https://github.com/sgl-project/sglang/issues/36081) [Bug] DSV4F0731+DSPARK ERROR IN SGLANG 0.5.18
- [Feature] [vllm-project/vllm#53349](https://github.com/vllm-project/vllm/issues/53349) [Feature]: Opt-in omission of unset vLLM-specific extension fields from /v1/chat/completions responses
- [Bug] [vllm-project/vllm#53393](https://github.com/vllm-project/vllm/issues/53393) [Bug][Frontend]: Anthropic system-turn handling (merge or in-place) breaks prefix caching for clients that append a system turn every turn; in-place re-role to user satisfies all constraints

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Performance] [vllm-project/vllm#52585](https://github.com/vllm-project/vllm/issues/52585) [Performance][ROCm] gfx1100 long-prefill: unified attention BLOCK_M=16 default leaves ~2x on the table; BLOCK_M=64 gives 1.1-1.3x TTFT on latest main

### Build / Install / Platform

- [Bug] [vllm-project/vllm#52525](https://github.com/vllm-project/vllm/issues/52525) [Bug]: Marlin MoE output depends on equivalent within-expert token ordering
- [Bug] [vllm-project/vllm#52531](https://github.com/vllm-project/vllm/issues/52531) [Bug]:  Kimi-K3 CUDA graph capture silently corrupts output at batch=1; three distinct failure modes across cudagraph modes.
- [Bug] [vllm-project/vllm#52544](https://github.com/vllm-project/vllm/issues/52544) [Bug]: VLLM_USE_PRECOMPILED can fall back across CUDA variants without compatibility validation
- [Bug] [vllm-project/vllm#52551](https://github.com/vllm-project/vllm/issues/52551) [Bug]: Qwen3.6-27B (dense Gated-DeltaNet) permanently hard-wedges the V1 engine — two reproducible modes (2 large images; long multi-turn text), possibly related
- [Bug] [vllm-project/vllm#52583](https://github.com/vllm-project/vllm/issues/52583) [Bug]: Prefix Caching hangs with large multimodal inputs (Qwen3.8-VL) – CPU-bound hash alignment blocks prefill
- [Bug] [vllm-project/vllm#52589](https://github.com/vllm-project/vllm/issues/52589) [Bug]:Is it possible to install vllm >= 0.18.0 on Ubuntu 20, CUDA 12.6, and Torch 2.11?
- [Bug] [vllm-project/vllm#52594](https://github.com/vllm-project/vllm/issues/52594) [Bug]: muse_glimmer cannot combine reasoning with structured outputs — schema is silently skipped when enable_in_reasoning=False
- [Bug] [vllm-project/vllm#52614](https://github.com/vllm-project/vllm/issues/52614) [Bug]: lm-format-enforcer 0.11.3 integration is incompatible with vLLM 0.26.0 due to stale MistralTokenizer import path
- [Bug] [vllm-project/vllm#52620](https://github.com/vllm-project/vllm/issues/52620) [Bug]: `ngram_gpu` speculative decoding with xgrammar returns HTTP 500 under concurrent structured-output requests

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#52590](https://github.com/vllm-project/vllm/issues/52590) [Bug]: num_blocks division is a no-op in get_moe_wna16_block_config because block_size_k is reassigned first

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#52591](https://github.com/vllm-project/vllm/issues/52591) [Bug]: two logger calls have mismatched %-args, so the log record is dropped
- [Bug] [vllm-project/vllm#52617](https://github.com/vllm-project/vllm/issues/52617) [Bug]: vLLM 0.26.0 LMCache P/D receiver reports a full KV-cache hit but decoding diverges from the monolithic baseline at token 0

### New Model Integration

- [Bug] [sgl-project/sglang#35080](https://github.com/sgl-project/sglang/issues/35080) [Bug] Flashinfer backend is not supported on Blackwell GPUs
- [RFC] [vllm-project/vllm#52567](https://github.com/vllm-project/vllm/issues/52567) [RFC]: First-class agentic inference support in vLLM

### Performance / Memory / OOM

- [Bug] [vllm-project/vllm#52511](https://github.com/vllm-project/vllm/issues/52511) [Bug]: FlashInfer TRT-LLM bf16 MoE weight-conversion OOM recurs post-#45589 at TP2 (120B MoE, GB200) — cumem MemPool still doesn't reclaim under pressure

### Quantization

- [Bug] [sgl-project/sglang#35148](https://github.com/sgl-project/sglang/issues/35148) [Bug] Qwen3.8-27B-FP8 reasoning content does not parse correctly in rust sgl-model-gateway
- [Bug] [vllm-project/vllm#52540](https://github.com/vllm-project/vllm/issues/52540) [Bug]: ModelOpt NVFP4 on SM120 dies or wedges under sustained load with CUDA graphs (not the NVFP4 GEMM backend)
- [Bug] [vllm-project/vllm#52613](https://github.com/vllm-project/vllm/issues/52613) [Bug]: MiniMax-M3 (MXFP8) streaming: generation stops (empty delta, finish_reason=stop) right after reasoning closes, whenever a tool call should follow — non-streaming with identical payload succeeds

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#35144](https://github.com/sgl-project/sglang/issues/35144) [Bug] EAGLE/NEXTN TP=2 hangs at warmup on Intel XPU after #34238 moved the verify-decision TP broadcast out of the sampling branch
- [Bug] [sgl-project/sglang#35150](https://github.com/sgl-project/sglang/issues/35150) [Bug] Qwen3.8 DSpark forced-reject is not lossless: accumulated GDN state drift vs Base decode
- [Feature] [vllm-project/vllm#52536](https://github.com/vllm-project/vllm/issues/52536) [Feature] Allow random dataset to use --dataset-path for realistic token sampling

### Scheduler / Batching

- [Bug] [sgl-project/sglang#35129](https://github.com/sgl-project/sglang/issues/35129) [Bug] DeepSeek-V4-Flash-0731 + dsv4 + DSPARK + HiCache: long agentic sessions get #cached-token: 0 every turn despite stable 50%+ prefix (short requests hit ~98%)
- [Bug] [vllm-project/vllm#52520](https://github.com/vllm-project/vllm/issues/52520) [Bug]: hybrid Mamba + `--mamba-cache-mode align`: a request near the KV-pool ceiling is admitted, prefilled to 98.9 %, requeued, and re-prefilled forever with zero output tokens and zero preemption accounting

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#52586](https://github.com/vllm-project/vllm/issues/52586) [Bug]: when setting dp=2 dsv4f0731 ,console log and metric running-request can not see both grafana and console log
