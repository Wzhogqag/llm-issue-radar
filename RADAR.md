# LLM Serving Issue Radar

_Last run: 2026-08-23T13:30+00:00_

**24 issues** — sgl-project/sglang: 6, vllm-project/vllm: 18 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#53401](https://github.com/vllm-project/vllm/issues/53401) [RFC]: Experimental Recirculation for causal decoders

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#36083](https://github.com/sgl-project/sglang/issues/36083) [Feature] Extend cross-layer index-topk reuse (dsa_layer_skips_topk) to DeepSeek-V4
- [other] 🆕 ⚠maintainer-authored [#36033](https://github.com/sgl-project/sglang/issues/36033) [PD] Inconsistent prefill→decode failure notification across transfer backends; NIXL has none

### vllm-project/vllm

- [Feature] [#53368](https://github.com/vllm-project/vllm/issues/53368) [Feature]: Expose CPU vs P2P attribution for multi-tier KV restores
- [RFC] [#53371](https://github.com/vllm-project/vllm/issues/53371) [RFC]: Optimization: Take over a partial-hit block instead of CoW copy when ref_cnt == 1

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#53413](https://github.com/vllm-project/vllm/issues/53413) [Bug]: GLM-5.2 FP8 on 8×H200 dies with runtime CUDA OOM in sparse_decode_fwd

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36048](https://github.com/sgl-project/sglang/issues/36048) [Bug] Qwen3.8-27B AWQ has no usable fast path on single Ada SM89 32GB: CUDA graph hangs and native MTP cannot allocate requests

### vllm-project/vllm

- [Bug] 🆕 [#53390](https://github.com/vllm-project/vllm/issues/53390) [Bug]: int32 token-offset overflow in silu_and_mul_per_block_quant (act_quant fusion) — illegal memory access above ~2^31/(2*intermediate_size) batched tokens
- [Bug] 🆕 [#53387](https://github.com/vllm-project/vllm/issues/53387) [Bug]: Qwen3.5-family native MTP crashes with compressed-tensors WNA16 checkpoints (unquantized mtp.fc)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#36018](https://github.com/sgl-project/sglang/issues/36018) [Bug] Kimi-K3 crash in v0.5.18 release

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#53455](https://github.com/vllm-project/vllm/issues/53455) [Feature]: Optional torch.compile support for NVIDIA DeepSeek-V4
- [Feature] 🆕 [#53445](https://github.com/vllm-project/vllm/issues/53445) [Feature]: Native support for Granite Switch (GraniteSwitchForCausalLM)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#53436](https://github.com/vllm-project/vllm/issues/53436) [Bug]: Run-to-run performance non-determinism with speculative decoding at temperature=0 (fixed seed) on DeepSeek-V4-Flash / Blackwell SM120
- [Bug] 🆕 [#53391](https://github.com/vllm-project/vllm/issues/53391) [Bug][DSV4-Flash][DSpark] Startup dies in kernel warmup with "ragged spec decode batch: 7 tokens over 2 requests"
- [Bug] 🆕 [#53366](https://github.com/vllm-project/vllm/issues/53366) [Bug]: torch.compile cache key does not include num_speculative_tokens, causing compiled-graph collision across different speculative-token counts
- [Bug] [#53363](https://github.com/vllm-project/vllm/issues/53363) [Bug]: tool_choice="required" not enforced with gemma4 tool parser — prose-only response returned with finish_reason="tool_calls" and empty tool_calls

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#36081](https://github.com/sgl-project/sglang/issues/36081) [Bug] DSV4F0731+DSPARK ERROR IN SGLANG 0.5.18

### vllm-project/vllm

- [Bug] 🆕 [#53393](https://github.com/vllm-project/vllm/issues/53393) [Bug][Frontend]: Anthropic system-turn handling (merge or in-place) breaks prefix caching for clients that append a system turn every turn; in-place re-role to user satisfies all constraints
- [Feature] [#53349](https://github.com/vllm-project/vllm/issues/53349) [Feature]: Opt-in omission of unset vLLM-specific extension fields from /v1/chat/completions responses

## Performance / Memory / OOM

### vllm-project/vllm

- [Perf] 🆕 [#53459](https://github.com/vllm-project/vllm/issues/53459) [Perf] Indexer score GEMM uses fp32 accumulate on DeepSeek-V4; bf16 may be sufficient

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#36058](https://github.com/sgl-project/sglang/issues/36058) [Bug] /usr/bin/ld: cannot find -lcuda: No such file or directory collect2: error: ld returned 1 exit status ninja: build stopped: subcommand failed.

### vllm-project/vllm

- [Bug] 🆕 [#53434](https://github.com/vllm-project/vllm/issues/53434) [Bug]: Long term continuous operation leads to an increase in model output illusion
- [Bug] 🆕 [#53411](https://github.com/vllm-project/vllm/issues/53411) [Bug]: DeepSeek v4 Pro Base - The default MoE backend selection produces incorrect output and inflated logprobs (FlashInfer TRTLLM vs deep_gemm)
- [Bug] 🆕 [#53359](https://github.com/vllm-project/vllm/issues/53359) [Bug]: tool_call_parser_invocations_total no longer increments for engine-backed parsers (regression after ParserEngine refactor)
