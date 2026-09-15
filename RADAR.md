# LLM Serving Issue Radar

_Last run: 2026-09-15T13:30+00:00_

**16 issues** — vllm-project/vllm: 16 — 🆕 **16 new** since last run

## Contents

- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#57014](https://github.com/vllm-project/vllm/issues/57014) [Bug]: race in `hadacore_transform`'s tail warp, last rows % 8 rows read stale shared memory when rows % 8 is 1-4 
- [Performance] 🆕 [#56992](https://github.com/vllm-project/vllm/issues/56992) [Performance][ROCm][gfx1100] compressed-tensors silently enables fp8 KV cache, which is far slower than bf16 for paged decode attention on RDNA3
- [Performance] 🆕 [#56924](https://github.com/vllm-project/vllm/issues/56924) [Performance]: int8 W8A8 CUTLASS on Ada (sm_89) is 1.3x to 2x slower per call from M=17, at the dispatch bucket edge
- [Bug] 🆕 [#56900](https://github.com/vllm-project/vllm/issues/56900) [Bug]: Qwen/Qwen1.5-MoE-A2.7B-Chat produces degenerate output with torch.compile (VLLM_COMPILE) but correct output without it on vLLM 0.28.0 (H100, torch 2.13.0+cu130); CUDA graphs, compile cache and custom_ops make no difference
- [RFC] 🆕 [#56968](https://github.com/vllm-project/vllm/issues/56968) [RFC]: Plain-Python watermarking performance regression benchmark

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Performance] 🆕 [#56975](https://github.com/vllm-project/vllm/issues/56975) [Performance] GLM-5.3-Flash on 4x GB200 TP4: p99 ITL 15-20x SGLang's at c>=32; prefill-containing steps run outside CUDA graphs; raising --max-cudagraph-capture-size to the chunk size cuts the tail by about half (data)

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#57002](https://github.com/vllm-project/vllm/issues/57002) [Feature]: ModernBert LoRa support

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Feature] 🆕 [#57013](https://github.com/vllm-project/vllm/issues/57013) [Feature][Spec Decode] Support MiniCPM5-2B-DSpark
- [Feature] 🆕 [#56917](https://github.com/vllm-project/vllm/issues/56917) [Feature]: TP=2 graph capture + MTP speculative decoding crash on Arc B70 — fix already exists upstream, unmerged
- [RFC] 🆕 [#56993](https://github.com/vllm-project/vllm/issues/56993) [RFC]: Split scale-out into owned components (Renderer / Frontend / Generation) with dedicated launch commands
- [RFC] 🆕 [#56916](https://github.com/vllm-project/vllm/issues/56916) [RFC]: Windowed Hidden-State Collection for vLLM Rollouts

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#56943](https://github.com/vllm-project/vllm/issues/56943) [Bug]: Per-request EngineDeadError tracebacks accumulate stack frames and flood logs after a worker crash

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#56981](https://github.com/vllm-project/vllm/issues/56981) [Bug]:  Qwen3-ASR audio preprocessing produces different audio-token counts from Hugging Face
- [Bug] 🆕 [#56980](https://github.com/vllm-project/vllm/issues/56980) [Bug]: MiniMax-M3 MSA crashes with quack-kernels 0.6.5 on the standard SM100 CUDA path
- [Bug] 🆕 [#56945](https://github.com/vllm-project/vllm/issues/56945) [Bug]: rocm/vllm image never sets VLLM_ROCM_USE_AITER — Qwen3.5-122B-A10B-FP8 runs Triton MoE + ROCM_ATTN, 1.7x slower at short prompts and 3.7x at 12k than AITER + ROCM_AITER_UNIFIED_ATTN (MI300X/MI325X/MI355X)
- [no-prefix] 🆕 ⚠no-prefix [#57008](https://github.com/vllm-project/vllm/issues/57008) XPU: --cpu-offload-gb (UVA) does not reduce peak device memory for compressed-tensors WNA16 MoE models
