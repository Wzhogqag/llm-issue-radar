# LLM Serving Issue Radar

_Last run: 2026-10-09T13:34+00:00_

**14 issues** — sgl-project/sglang: 3, vllm-project/vllm: 11 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#60744](https://github.com/vllm-project/vllm/issues/60744) [Bug] pause_generation(mode="keep", clear_cache=True) raises when a streaming-input session is parked between turns

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#60838](https://github.com/vllm-project/vllm/issues/60838) [Bug]: `--mamba-block-size` has no effect in any valid configuration after the removal of `mamba_cache_mode="all"`
- [Bug] 🆕 [#60755](https://github.com/vllm-project/vllm/issues/60755) [Bug]: vLLM 0.31.0 Mooncake connector crashes after Decode timeout
- [Bug] 🆕 ⚠maintainer-authored [#60791](https://github.com/vllm-project/vllm/issues/60791) [Bug]: MiniMax-M3: PP startup, NIXL+PP prefill, NIXL+HMA+DSpark, offload+PP, Mooncake recompute loop

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#43342](https://github.com/sgl-project/sglang/issues/43342) [Bug] RuntimeError: Failed at /sgl-workspace/sglang/python/sglang/kernels/jit/csrc/gemm/marlin/gptq_marlin_repack.cuh:311: size_n = 8608 is not divisible by tile_n_size = 64

### vllm-project/vllm

- [Performance] 🆕 [#60778](https://github.com/vllm-project/vllm/issues/60778) [Performance]: Reduce load_weights synchronization overhead for DeepSeek V4 Flash weight updates on H200

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#60845](https://github.com/vllm-project/vllm/issues/60845) [Bug]: CUDA graphs deadlock fully-sharded fused-MoE LoRA across TP ranks

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#43379](https://github.com/sgl-project/sglang/issues/43379) [Feature] [Diffusion] Support LingBot-VLA 2.0

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#60830](https://github.com/vllm-project/vllm/issues/60830) [Bug]: MTP speculative decoding makes response_format {"type": "json_schema", ...} invalid on request for Qwen3.8-Flash-Next
- [Bug] 🆕 [#60765](https://github.com/vllm-project/vllm/issues/60765) [Bug]: Qwen3.5 (hybrid GDN) models cannot run dflash speculative decoding with pipeline parallelism (missing supports_aux_hidden_states_over_pp opt-in)
- [Bug] 🆕 [#60829](https://github.com/vllm-project/vllm/issues/60829) [Bug]: `top_k_per_row_decode` raises an illegal memory access for runtime topK > 8192 instead of a clean error

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#60771](https://github.com/vllm-project/vllm/issues/60771) [Bug]: deepseek-v4-flash-0731 repeat and Garbled characters

## Performance / Memory / OOM

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#43314](https://github.com/sgl-project/sglang/issues/43314) MLLM Roadmap (2026 q4)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#60752](https://github.com/vllm-project/vllm/issues/60752) [Bug]: grouped_topk selects wrong experts with more than eight groups
