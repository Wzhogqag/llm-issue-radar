# LLM Serving Issue Radar

_Last run: 2026-10-13T13:41+00:00_

**14 issues** — sgl-project/sglang: 3, vllm-project/vllm: 11 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#61396](https://github.com/vllm-project/vllm/issues/61396) [RFC] [KV Offload]: Store trigger and store admission policies for the offloading manager (lazy offloading)

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#43965](https://github.com/sgl-project/sglang/issues/43965) [Feature] [RFC] SGLang Engine Initialization Snapshots: Reusing Initialized State for Faster Startup

### vllm-project/vllm

- [Bug] 🆕 [#61389](https://github.com/vllm-project/vllm/issues/61389) [Bug][MoRIIO] P-side remote decode completion skips FINISHED_STOPPED
- [Bug] 🆕 [#61313](https://github.com/vllm-project/vllm/issues/61313) [Bug]: disable_hybrid_kv_cache_manager=True crashes engine startup on hybrid mamba models — ValueError: Failed to promote local KV cache specs to one unified type

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#43988](https://github.com/sgl-project/sglang/issues/43988) [Bug] --fp4-gemm-backend marlin crashes with NVFP4 W4A4 checkpoints on SM100 (mm_fp4 has no 'marlin' backend)
- [Bug] 🆕 [#43956](https://github.com/sgl-project/sglang/issues/43956) [Bug] Qwen3.8-27B scores depend on batch shape and can change borderline decisions (FP8 and BF16)

### vllm-project/vllm

- [Bug] 🆕 [#61319](https://github.com/vllm-project/vllm/issues/61319) [Bug]:  Greedy (temperature=0) decoding is not reproducible across repeated calls on the same engine for LiquidAI/LFM2-8B-A1B (hybrid mamba)
- [Bug] 🆕 [#61316](https://github.com/vllm-project/vllm/issues/61316) [Bug]:  fp8 kernel selection discards per-kernel rejection reasons — quantization="fp8_per_channel" surfaces as a misleading "Requires SM89+ for Cutlass FP8" with no indication of what actually failed
- [Bug] 🆕 [#61314](https://github.com/vllm-project/vllm/issues/61314) [Bug]: quantization="fp8" + kv_cache_dtype="float16" on a bf16 model crashes at startup — same flash-attn dtype assert as #60859, now on the online-quant path

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#61317](https://github.com/vllm-project/vllm/issues/61317) [Bug]: jit_monitor_mode="error" kills the engine on the first real request for hybrid mamba models — JIT warmup never covers precopy_mamba_align_fused_kernel
- [Bug] 🆕 [#61315](https://github.com/vllm-project/vllm/issues/61315) [Bug]: enable_lora with max_lora_rank=320 crashes engine startup on MoE models — AssertionError: fused_moe_lora_one_shot supports max_lora_rank<=128

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#61383](https://github.com/vllm-project/vllm/issues/61383) [Bug]: Intermittent XGrammar request termination with V2 DFlash probabilistic drafting and block rejection

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#61372](https://github.com/vllm-project/vllm/issues/61372) [Bug][Rust Frontend] DeepSeek V4/V4.1 renderer rejects `latest_reminder`, which the Python encoder renders

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#61330](https://github.com/vllm-project/vllm/issues/61330) [Bug]: DFlash speculative decoding with gpt-oss target crashes with FA3 illegal memory access
