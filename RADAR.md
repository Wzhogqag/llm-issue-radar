# LLM Serving Issue Radar

_Last run: 2026-08-20T13:35+00:00_

**25 issues** — sgl-project/sglang: 5, vllm-project/vllm: 20 — 🆕 **25 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 5
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#53049](https://github.com/vllm-project/vllm/issues/53049) [Bug]: MultiConnector: finished_recving lacks per-connector dedup — late/stale load reports crash scheduler assert in P/D + dual-connector setups
- [other] 🆕 [#53041](https://github.com/vllm-project/vllm/issues/53041) [Discussion] Tiered SWA/Mamba checkpointing (HBM tail + store periodic) + recompute backfill for divergent hybrid prefix hits

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#53095](https://github.com/vllm-project/vllm/issues/53095) [Bug] NixlPushConnector heartbeat fails to renew KV leases
- [Bug] 🆕 [#53084](https://github.com/vllm-project/vllm/issues/53084) [Bug]: MooncakeStoreConnector stores invalid recurrent states with mamba_cache_mode=align, causing silent output corruption
- [Bug] 🆕 [#53083](https://github.com/vllm-project/vllm/issues/53083) [Bug]: PD P2P supply and demand are computed independently, and nothing checks they match
- [Bug] 🆕 [#53042](https://github.com/vllm-project/vllm/issues/53042) [Bug][KV Offload] --kv-offloading-size allocates 1.92x the requested host memory as unreclaimable shmem
- [no-prefix] 🆕 ⚠no-prefix [#53028](https://github.com/vllm-project/vllm/issues/53028) Gemma 4 E2B + LoRA: illegal memory access in lora_expand at engine init once max_model_len >= 87383

## Quantization

### sgl-project/sglang

- [RFC] 🆕 [#35620](https://github.com/sgl-project/sglang/issues/35620) [RFC] Integrating Ascend MemCache as an HiCache L3 Backend

### vllm-project/vllm

- [Bug] 🆕 [#53107](https://github.com/vllm-project/vllm/issues/53107) [Bug]: LinearBase.load_weights substitutes the module for a missing parameter, surfacing as a confusing AttributeError
- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#53086](https://github.com/vllm-project/vllm/issues/53086) int4 per-token-head KV cache: triton_reshape_and_cache_flash_per_token_head_quant returns wrong values

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#53105](https://github.com/vllm-project/vllm/issues/53105) [Bug]: bare assert in BasevLLMParameter._assert_and_load gives no diagnostics on weight shape mismatch

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#35691](https://github.com/sgl-project/sglang/issues/35691) [Feature] Support Custom OTLP Trace Service Name

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#35705](https://github.com/sgl-project/sglang/issues/35705) [Bug] AttributeError: 'list' object has no attribute 'tolist' in move_logprobs_to_cpu

### vllm-project/vllm

- [Bug] 🆕 [#53030](https://github.com/vllm-project/vllm/issues/53030) [Bug]: `set_splitting_ops_for_v1` early return skips the empty-splitting-ops guard — breakable cudagraph + `cudagraph_mode=PIECEWISE` + spec decode silently rejects every draft
- [Bug] 🆕 [#53029](https://github.com/vllm-project/vllm/issues/53029) [Bug][Spec Decode] All-NaN logits row is laundered into an out-of-vocab token id by the rejection sampler (device assert far from origin); NaN-metric blind spot on the verify path; uninit-scratch audit
- [no-prefix] 🆕 ⚠no-prefix [#53031](https://github.com/vllm-project/vllm/issues/53031) DFlash speculator `capture()` logs "Capturing model ..." even when nothing is captured — makes drafter-capture state unobservable

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#53091](https://github.com/vllm-project/vllm/issues/53091) [Bug]: CLIP pooling model silently returns identical (empty-prompt) embeddings for all completion-style input text requests under sustained multimodal load
- [Bug] 🆕 [#53089](https://github.com/vllm-project/vllm/issues/53089) [Bug]: Assertion failure due to inconsistent block counts between P and D sides when tools dict key ordering differs in template serialization with tool calls enabled
- [Bug] 🆕 [#53066](https://github.com/vllm-project/vllm/issues/53066) [Bug] v1 detokenizer: client stop strings match inside the reasoning segment, decapitating think-in-prompt models (lm-eval sends stop on every request)
- [Bug] 🆕 [#53032](https://github.com/vllm-project/vllm/issues/53032) [Bug]: In a Python environment, when requesting a model deployed with vLLM and the output mode is streaming, there is a low probability that the connection is established but the model does not receive the request.

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#53013](https://github.com/vllm-project/vllm/issues/53013) [Bug]: CUDA graph memory profiling estimation is too huge

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#35673](https://github.com/sgl-project/sglang/issues/35673) [Bug] Gemma-4-31B-it TP=8 hangs in the vision path on AMD/ROCm
- [Bug] 🆕 [#35591](https://github.com/sgl-project/sglang/issues/35591) [Bug] ROCm images pin AITER below the FlyDSL MXFP4 MoE kernels, making tuned AITER_CONFIG_FMOE tables unusable on gfx950

### vllm-project/vllm

- [Bug] 🆕 [#53019](https://github.com/vllm-project/vllm/issues/53019) [Bug]: NemotronParseForConditionalGeneration does not tie lm_head.weight to decoder.embed_tokens.weight, produces garbage output
- [no-prefix] 🆕 ⚠no-prefix [#53063](https://github.com/vllm-project/vllm/issues/53063) DFlash draft model does not inherit the target's RoPE layout (is_neox_style)
