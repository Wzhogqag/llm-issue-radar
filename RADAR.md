# LLM Serving Issue Radar

_Last run: 2026-10-07T13:35+00:00_

**20 issues** — sgl-project/sglang: 2, vllm-project/vllm: 18 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#60301](https://github.com/vllm-project/vllm/issues/60301) [Bug]: Engine core dies on `assert len(scheduled_loras) <= max_loras` with LoRA and pipeline parallelism

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#60350](https://github.com/vllm-project/vllm/issues/60350) [Bug]: FP8 KV cache startup can OOM because CUDA graph memory is omitted from the cache budget
- [Performance] 🆕 [#60316](https://github.com/vllm-project/vllm/issues/60316) [Performance][ROCm] KV connectors rule out ROCM_ATTN, so PD workers decode on ROCM_AITER_UNIFIED_ATTN (1.9–3.2x the per-token time for Qwen3 models on MI355X)
- [Bug] 🆕 [#60325](https://github.com/vllm-project/vllm/issues/60325) [Bug]: Default -O2 leaves DeepSeek MLA RoPE and KV-cache fusion off
- [RFC] 🆕 [#60366](https://github.com/vllm-project/vllm/issues/60366) [RFC]: Bounded prefix reuse for target-token prefill scoring

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#42917](https://github.com/sgl-project/sglang/issues/42917) [Bug] Qwen3.8-27B compressed-tensors W4A16 (int4, symmetric, group 128) serves with degraded quality on 0.5.19-0.5.21 (wikitext PPL 9.98 vs 6.05 on vLLM, same checkpoint)

### vllm-project/vllm

- [Bug] 🆕 [#60333](https://github.com/vllm-project/vllm/issues/60333) [Bug] MiMoV2MTP silently drops FP8 KV cache scales and every draft layer falls back to scale 1.0

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#60346](https://github.com/vllm-project/vllm/issues/60346) [Bug]: `append_replayssm_ring` asserts for supported non-divisible Mamba group counts
- [other] 🆕 [#60283](https://github.com/vllm-project/vllm/issues/60283) [Tracking] Nemotron Labs Diffusion: model support, fixes, and decision reads
- [other] 🆕 [#60311](https://github.com/vllm-project/vllm/issues/60311) [Build]: Build macOS wheel using Python’s stable ABI

## Sampling / Speculative Decoding

### sgl-project/sglang

- [RFC] 🆕 [#42915](https://github.com/sgl-project/sglang/issues/42915) [RFC] Use reasoning effort as an output-length hint for DP routing and retraction

### vllm-project/vllm

- [Bug] 🆕 [#60379](https://github.com/vllm-project/vllm/issues/60379) [Bug][XPU][MRV2]: engine dies at startup on the first PIECEWISE graph capture with TP=2 + MTP on a GDN/Mamba-hybrid model (oneCCL collective inside capture; regression from #56531; fixed by unmerged #58415)
- [Bug] 🆕 [#60349](https://github.com/vllm-project/vllm/issues/60349) [Bug]: `LLM.generate()` never returns when `max_num_scheduled_tokens=0`

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#60347](https://github.com/vllm-project/vllm/issues/60347) [Bug]: `TensorizerConfig(lora_dir=...)` leaves `tensorizer_dir=None` and breaks serialization round trips
- [Bug] 🆕 [#60341](https://github.com/vllm-project/vllm/issues/60341) [Bug]: InternLM2 tool parser (streaming) drops all content after `<|action_start|>` when no `<|plugin|>` follows
- [Bug] 🆕 [#60340](https://github.com/vllm-project/vllm/issues/60340) [Bug]: Olmo3 reasoning parser drops the final streamed delta when it is a substring of `<think>`/`</think>` (e.g. "think")
- [no-prefix] 🆕 ⚠no-prefix [#60396](https://github.com/vllm-project/vllm/issues/60396) Unvalidated passthrough in `_construct_message_from_response_item` lets 14 of 32 valid input item types reach the renderer — `KeyError: 'role'` for dicts, `TypeError: not subscriptable` for pydantic models

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#60391](https://github.com/vllm-project/vllm/issues/60391) [Bug]: AOT-compiled artifact loading is decided per rank, so a partial load leaves ranks on different startup paths
- [Bug] 🆕 [#60370](https://github.com/vllm-project/vllm/issues/60370) [Bug]: CPU arm64 image fails to start on Apple M4: "no support for 'sme' without 'sve2'" (PyTorch Inductor + GCC 15)
- [Bug] 🆕 [#60303](https://github.com/vllm-project/vllm/issues/60303) [Bug]: Images above Pillow's pixel limit get HTTP 500 instead of 400
