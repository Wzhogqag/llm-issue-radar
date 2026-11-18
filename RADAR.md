# LLM Serving Issue Radar

_Last run: 2026-11-18T13:22+00:00_

**19 issues** — sgl-project/sglang: 5, vllm-project/vllm: 14 — 🆕 **19 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 6
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#68343](https://github.com/vllm-project/vllm/issues/68343) [Bug][Rust Frontend] NIXL metrics silently dropped due to Python/Rust NixlStats schema mismatch (9 vs 7 fields)
- [Bug] 🆕 [#68316](https://github.com/vllm-project/vllm/issues/68316) [Bug]: Raw OOM with misleading hint when model weights nearly fill the GPU (lost "not enough GPU memory" message)

## Attention Backend

### sgl-project/sglang

- [Perf] 🆕 [#51208](https://github.com/sgl-project/sglang/issues/51208) [Perf][NVIDIA] GDN decode on SM120 stays on Triton by default and reaches only ~23% of the bandwidth roofline; flashinfer already ships cc=120 fused decode kernels

### vllm-project/vllm

- [Bug] 🆕 [#68416](https://github.com/vllm-project/vllm/issues/68416) [Bug]: recurrent delta-rule kernels read the wrong state slots for strided index tables
- [Bug] 🆕 [#68415](https://github.com/vllm-project/vllm/issues/68415) [Bug]: fused_recurrent_kda allocates the wrong output shape when key and value sizes differ
- [Bug] 🆕 [#68414](https://github.com/vllm-project/vllm/issues/68414) [Bug]: chunk_gated_delta_rule skips every sequence after a zero-length sequence in cu_seqlens
- [Bug] 🆕 [#68413](https://github.com/vllm-project/vllm/issues/68413) [Bug]: decode_attention_fwd reads the wrong KV head when the GQA group is above 16 and not a multiple of 16
- [no-prefix] 🆕 ⚠no-prefix [#68410](https://github.com/vllm-project/vllm/issues/68410) Triton backend rejects fp8_per_token_head KV cache on SM 8.x: the guard is one dtype predicate too wide

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#51184](https://github.com/sgl-project/sglang/issues/51184) [Bug] CUDA graph replay returns degenerate output (all token id 0) on sm_120 with NVFP4 + tilelang DSA + Mamba hybrid

### vllm-project/vllm

- [other] 🆕 [#68336](https://github.com/vllm-project/vllm/issues/68336) [Compatibility] Qwen3.6 MoE CT INT4 checkpoint stores a packed `shared_expert_gate`, but vLLM expects `weight`
- [other] 🆕 [#68312](https://github.com/vllm-project/vllm/issues/68312) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#68412](https://github.com/vllm-project/vllm/issues/68412) [Bug]: causal_conv1d_fn writes before the state tensor for pad_slot_id=-1
- [RFC] 🆕 ⚠maintainer-authored [#68341](https://github.com/vllm-project/vllm/issues/68341) [RFC]: Optional weight staging and trainer-managed pause for weight transfer engines

## Sampling / Speculative Decoding

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#51175](https://github.com/sgl-project/sglang/issues/51175) Speculative state reservation on hybrid-GDN targets scales with draft length; a block-16 draft does not fit on 72 GB

### vllm-project/vllm

- [Bug] 🆕 [#68411](https://github.com/vllm-project/vllm/issues/68411) [Bug]: apply_top_k_top_p_triton keeps the whole row when top-p normalization underflows
- [Bug] 🆕 [#68324](https://github.com/vllm-project/vllm/issues/68324) [Bug]: Incremental detokenizers drop a trailing U+FFFD at end of generation

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#51218](https://github.com/sgl-project/sglang/issues/51218) [Bug] Legacy HTTP P/D router truncates SSE when a tool argument contains data: [DONE]

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#51223](https://github.com/sgl-project/sglang/issues/51223) [Bug] /v1/responses subtracts 2 from max_output_tokens and rejects max_output_tokens=1

### vllm-project/vllm

- [Feature] 🆕 [#68322](https://github.com/vllm-project/vllm/issues/68322) [Feature]: Add reasoning_content for message output content
