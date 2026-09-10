# LLM Serving Issue Radar

_Last run: 2026-09-10T13:26+00:00_

**20 issues** — sgl-project/sglang: 16, vllm-project/vllm: 4 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 5
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#38849](https://github.com/sgl-project/sglang/issues/38849) [Bug] GLM 5.3 segfault on MI300 in SGLang scheduler
- [no-prefix] 🆕 ⚠no-prefix [#38785](https://github.com/sgl-project/sglang/issues/38785) pp scheduler in prefill node

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#38840](https://github.com/sgl-project/sglang/issues/38840) [Bug] Encoder-decoder KV cache: shared boundary page is double-freed when page_size > 1
- [Bug] 🆕 [#38788](https://github.com/sgl-project/sglang/issues/38788) [Bug] Scripted-runtime rid reuse loses a race with rid_to_state release, surfacing as a 60s recv timeout (3 tests red in test/manual/chunked_prefill)
- [Feature] 🆕 [#38889](https://github.com/sgl-project/sglang/issues/38889) [Feature] Move shared cache transfer types out of hicache_storage.py
- [Feature] 🆕 [#38846](https://github.com/sgl-project/sglang/issues/38846) [Feature] Expose the effective `max_running_requests` (after the mamba/linear-attention state-cache cap) in `/get_server_info`
- [Feature] 🆕 [#38819](https://github.com/sgl-project/sglang/issues/38819) [Feature] End-to-end PD disaggregation + DSpark support for DeepSeek-V4.1

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 ⚠maintainer-authored [#56217](https://github.com/vllm-project/vllm/issues/56217) [Feature]: DeepSeek-V4.1-Flash kernels integration

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#38854](https://github.com/sgl-project/sglang/issues/38854) [Bug] Qwen3.5 hybrid (GDN) GPTQ checkpoint: `linear_attn.in_proj_ba` built as quantized although the checkpoint stores `in_proj_a/b` as bf16 → 96× "not found in params_dict", then `gptq_marlin_repack` fails (size_n=96)
- [Bug] 🆕 [#38817](https://github.com/sgl-project/sglang/issues/38817) [Bug] RuntimeError: Promotion for Float8 Types is not supported, attempted to promote Float8_e4m3fn and BFloat16
- [Bug] 🆕 [#38795](https://github.com/sgl-project/sglang/issues/38795) [Bug] NVFP4 + flashinfer_cutlass + --speculative-adaptive: CUDA-graph capture raises "Unsupported moe_runner_backend ... Use flashinfer_cutlass instead" for the backend already in use
- [Feature] 🆕 [#38856](https://github.com/sgl-project/sglang/issues/38856) [Feature] Batched asynchronous Engram host-row prefetch

### vllm-project/vllm

- [Bug] 🆕 [#56206](https://github.com/vllm-project/vllm/issues/56206) [Bug]: v0.29.0 fails to start on SM110 (AGX Thor) — illegal memory access in Qwen GDN prefill warmup

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#56251](https://github.com/vllm-project/vllm/issues/56251) [Bug]: vLLM 并发缺陷报告：6 项确认缺陷

## New Model Integration

### sgl-project/sglang

- [Bug] 🆕 [#38821](https://github.com/sgl-project/sglang/issues/38821) [Bug] GLM-5.3-Flash vision: single JPEG data URL is misidentified as an unrelated bird on 8x H20
- [Feature] 🆕 [#38794](https://github.com/sgl-project/sglang/issues/38794) [Feature] Korean Localization for SGLang Cookbook

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#38899](https://github.com/sgl-project/sglang/issues/38899) [Bug] DSpark compact SPS profiling ignores forced budgets and fails on ragged mRoPE positions
- [Bug] 🆕 [#38787](https://github.com/sgl-project/sglang/issues/38787) [Bug] DSA attention: `tl.constexpr` strides in `transform_index_page_table_{prefill,decode}_kernel` cause unbounded Triton recompiles and stall

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#38793](https://github.com/sgl-project/sglang/issues/38793) [Bug] H20 8card can't launch Qwen3.8-Flash-Next-FP8

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#56172](https://github.com/vllm-project/vllm/issues/56172) [Feature]: Lightweight vLLM Render API: Offload Heavy Multimodal Preprocessing from CPU Sidecars
