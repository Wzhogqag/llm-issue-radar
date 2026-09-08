# LLM Serving Issue Radar

_Last run: 2026-09-08T13:29+00:00_

**12 issues** — sgl-project/sglang: 7, vllm-project/vllm: 5 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#38452](https://github.com/sgl-project/sglang/issues/38452) [Bug] UnifiedRadixCache: L3 storage is never consulted when a prefix survives only as backuped stubs after host-tier eviction

### vllm-project/vllm

- [Performance] 🆕 [#55798](https://github.com/vllm-project/vllm/issues/55798) [Performance]: A performance optimization in the Scheduler regarding pad_spec_decode

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#55870](https://github.com/vllm-project/vllm/issues/55870) [Bug]: Mooncake bootstrap and KV transfer failures can leave PD requests waiting without terminal error propagation
- [Feature] 🆕 [#55855](https://github.com/vllm-project/vllm/issues/55855) [Feature]: Add RDMA-capable NIXL OBJ support for KV offload secondary tier

## Quantization

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#38514](https://github.com/sgl-project/sglang/issues/38514) Docs: official BFL FLUX.2-klein FP8 is Comfy split-QKV, not a packed SGLang --transformer-weights-path drop-in
- [no-prefix] 🆕 ⚠no-prefix [#38513](https://github.com/sgl-project/sglang/issues/38513) supports_fp8() always True; _apply_fallback_scaled_mm still calls torch._scaled_mm (no escape on SM<89)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#55856](https://github.com/vllm-project/vllm/issues/55856) [Bug] v0.20.2 empty build incompatible with V1 engine (missing vllm._C)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#38450](https://github.com/sgl-project/sglang/issues/38450) [Bug] DeepSeek-V4-Flash-Vision preview image: multi-turn tool calls come back wrapped in {"arguments": {...}}

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#38516](https://github.com/sgl-project/sglang/issues/38516) Diffusion CUDA JIT: rsqrt host/CRT clash burns tens of seconds before soft-fail (fail fast / skip on sm<80)
- [no-prefix] 🆕 ⚠no-prefix [#38515](https://github.com/sgl-project/sglang/issues/38515) sgl_kernel AOT: rmsnorm NoKernelImage on sm_75 while silu_and_mul / gelu_and_mul work (per-op cubin gap)

### vllm-project/vllm

- [Bug] 🆕 [#55845](https://github.com/vllm-project/vllm/issues/55845) [Bug] tencent/Hunyuan-A13B-Instruct fails with ImportError: cannot import name 'is_torch_fx_available' (trust_remote_code, transformers v5)

## Uncategorized

### sgl-project/sglang

- [other] 🆕 [#38424](https://github.com/sgl-project/sglang/issues/38424) [First-time contributor] Looking for beginner-friendly issues to contribute
