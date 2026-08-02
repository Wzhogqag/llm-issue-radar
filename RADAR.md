# LLM Serving Issue Radar

_Last run: 2026-08-02T13:53+00:00_

**25 issues** — sgl-project/sglang: 7, vllm-project/vllm: 18 — 🆕 **18 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 5
- [Attention Backend](#attention-backend) — 5
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#33268](https://github.com/sgl-project/sglang/issues/33268) [Bug] HiCache storage keys omit kv_cache_dtype — silent cross-run cache collisions

### vllm-project/vllm

- [Bug] 🆕 [#50719](https://github.com/vllm-project/vllm/issues/50719) [Bug][PD][Mooncake] Decode requests stuck in WAITING_FOR_REMOTE_KVS and fail with Timeout waiting for P side ready
- [Bug] 🆕 [#50709](https://github.com/vllm-project/vllm/issues/50709) [Bug]: TurboQuant hybrid model crashes at determine_available_memory with 'Unknown cache dtype: auto' on v0.25.0+
- [no-prefix] 🆕 ⚠no-prefix [#50687](https://github.com/vllm-project/vllm/issues/50687) Hybrid multi-group KV: _update_requests_with_invalid_blocks crashes (too many values to unpack) on connector load-error blocks
- [no-prefix] ⚠no-prefix [#50630](https://github.com/vllm-project/vllm/issues/50630) No capability flag declares which KV-cache kinds may be peeked past a candidate boundary — each margin implementation excludes Mamba by hand

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33207](https://github.com/sgl-project/sglang/issues/33207) [Bug] Unrecognized configuration class <class 'sglang.srt.utils.hf_transformers.common._DeepseekV4ConfigAlias'>
- [no-prefix] 🆕 ⚠no-prefix [#33223](https://github.com/sgl-project/sglang/issues/33223) Kimi K3 encountered accuracy problems when testing τ³-Banking, and scored only 17.53

### vllm-project/vllm

- [Bug] 🆕 [#50720](https://github.com/vllm-project/vllm/issues/50720) [Bug]: DeepSeek-V4-Flash-0731 + DSpark fails on RTX PRO 6000 (SM120) with FlashInfer sparse MLA decode kernel routing
- [Bug] 🆕 [#50707](https://github.com/vllm-project/vllm/issues/50707) [Bug] DFlash on SM121 (GB10 / DGX Spark): attention autoselect picks FLASH_ATTN for non-causal draft attention and device-asserts in _vllm_fa2_C.varlen_fwd
- [Bug] 🆕 [#50705](https://github.com/vllm-project/vllm/issues/50705) [Bug]: sm_120 + local CUDA toolkit < 12.9: FlashInfer JIT failures kill engine init in three default paths (sampler, fused-MoE, FP8 KV) instead of falling back

## Quantization

### sgl-project/sglang

- [Bug] [#33163](https://github.com/sgl-project/sglang/issues/33163) [Bug] deepseek-v4-flash toolcall error runner_backend from marlin to  flashinfer_mxfp4

### vllm-project/vllm

- [Bug] 🆕 [#50702](https://github.com/vllm-project/vllm/issues/50702) [Bug]: int8_per_token_head KV + prefix caching corrupts output when the KV pool is pinned at 100% (Gemma-4 hybrid, Triton)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] [#33181](https://github.com/sgl-project/sglang/issues/33181) [Bug] Inkling reasoning parser leaks the tool name into visible content when a turn opens with a tool call

### vllm-project/vllm

- [Bug] 🆕 [#50706](https://github.com/vllm-project/vllm/issues/50706) [Bug]: Mistral3 (HF format): default text-only LLM() init fails in multimodal profiling — "Failed to apply PixtralProcessor on data={'text': '[IMG]'}"
- [RFC] 🆕 [#50738](https://github.com/vllm-project/vllm/issues/50738) [RFC]: Dual Batch Overlap (DBO) for Model Runner V2

## New Model Integration

### vllm-project/vllm

- [other] [#50672](https://github.com/vllm-project/vllm/issues/50672) [Installation]:vllm-openai:kimi-k3 cpuoffloadgb not support?

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#50722](https://github.com/vllm-project/vllm/issues/50722) [Bug]: With qwen3.5-35b-a3b, the performance is relatively poor both when using dflash and when not using it, but the accepted length of dflash is around 5–6.
- [Bug] 🆕 [#50708](https://github.com/vllm-project/vllm/issues/50708) [Bug] Speculative decoding with a large num_speculative_tokens fails with a bare negative max_num_scheduled_tokens instead of naming the flags that fix it

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] [#33185](https://github.com/sgl-project/sglang/issues/33185) [Bug] DeepSeek-V4-Flash-0731: reasoning_effort mapped one level off — `high` is a no-op and vendor `max` is unreachable

### vllm-project/vllm

- [Bug] 🆕 [#50690](https://github.com/vllm-project/vllm/issues/50690) [Bug]: gpt-oss chat completions return 500 "Unexpected token 200002 while expecting start token 200006" when ignore_eos=true
- [Bug] 🆕 [#50660](https://github.com/vllm-project/vllm/issues/50660) [Bug]: deepseek-v4-flash-0731 can not be Stablize running

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#50699](https://github.com/vllm-project/vllm/issues/50699) [Bug]: DiffusionGemma: runtime CUDA OOM under concurrent decode (fp32 canvas×vocab temporaries)
- [Bug] 🆕 [#50681](https://github.com/vllm-project/vllm/issues/50681) [Bug]: Qwen3.6-35B-A3B produces corrupted output with EP and sequence parallelism enabled
- [other] ⚠maintainer-authored [#50682](https://github.com/vllm-project/vllm/issues/50682) [ROCm][AMD] Kimi-K3 Gap and Roadmap Tracking

## Uncategorized

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#33180](https://github.com/sgl-project/sglang/issues/33180) @copilot resolve the merge conflicts on this branch.
