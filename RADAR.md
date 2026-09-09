# LLM Serving Issue Radar

_Last run: 2026-09-09T13:28+00:00_

**17 issues** — sgl-project/sglang: 8, vllm-project/vllm: 9 — 🆕 **17 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#38627](https://github.com/sgl-project/sglang/issues/38627) [Bug] Chunked prefill splits the encoder region of encoder-decoder models, corrupting `extend_num_tokens` and crashing the scheduler
- [Feature] 🆕 [#38676](https://github.com/sgl-project/sglang/issues/38676) [Feature] Expose multimodal preprocessing latency metrics (media download / load / processor) in Prometheus

## Quantization

### sgl-project/sglang

- [Performance] 🆕 ⚠maintainer-authored [#38628](https://github.com/sgl-project/sglang/issues/38628) [Performance] tiny_gemm regresses DeepSeek-R1 NVFP4 decode on Blackwell despite faster standalone kernel
- [no-prefix] 🆕 ⚠no-prefix [#38673](https://github.com/sgl-project/sglang/issues/38673) Title: [Bug] Gemma4UnifiedForConditionalGeneration crashes on CUDA graph capture: 'lm_head_is_tied' not set

### vllm-project/vllm

- [Bug] 🆕 [#56041](https://github.com/vllm-project/vllm/issues/56041) [Bug]: FixFunctionalizationPass crashes with "Tried to erase Node auto_functionalized but it still had N users" when the graph contains control_deps nodes
- [other] 🆕 [#56064](https://github.com/vllm-project/vllm/issues/56064) [SM121 / GB10 (DGX Spark)] `moe_wna16_marlin_gemm` no-split-K (data-parallel) path: CUDA illegal memory access at M=256 — clean for M≤128; default split-K path clean at M=256

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Feature] 🆕 [#38580](https://github.com/sgl-project/sglang/issues/38580) [Feature] Enforce attention metadata consistency after post-plan padding

### vllm-project/vllm

- [Bug] 🆕 [#56007](https://github.com/vllm-project/vllm/issues/56007) [Bug]: GLM5.3-Flash v0.29.0 loading checkpoints error

## New Model Integration

### vllm-project/vllm

- [RFC] 🆕 [#55986](https://github.com/vllm-project/vllm/issues/55986) [RFC] Multi-channel target audio ignores channel_reduction in normalize_audio

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#56077](https://github.com/vllm-project/vllm/issues/56077) [Bug]: ngram speculative decoding corrupts qwen3_coder tool-call parser output (empty/mangled arguments) for Qwen3.x models

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Feature] 🆕 [#38651](https://github.com/sgl-project/sglang/issues/38651) [Feature] Allow caller-provided multimodal cache IDs to avoid repeated hashing and preprocessing

### vllm-project/vllm

- [Bug] 🆕 [#55994](https://github.com/vllm-project/vllm/issues/55994) [Bug][Rust Frontend] : /v1/chat/completions/render (and scale-out routes) return 404

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#38605](https://github.com/sgl-project/sglang/issues/38605) [Bug] MiniMax-H3 FL2VA generates visually corrupted video with layerwise offloading

### vllm-project/vllm

- [Bug] 🆕 [#56022](https://github.com/vllm-project/vllm/issues/56022) [Bug]: Assistant message contains both non-empty content and tool_calls in Agent loop, with persistent failure after first occurrence
- [no-prefix] 🆕 ⚠no-prefix [#56009](https://github.com/vllm-project/vllm/issues/56009) Possible response/request cross-talk: distinct non-overlapping requests return mismatched application binding values

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#38669](https://github.com/sgl-project/sglang/issues/38669) [Bug] 主线版本ascend后端对swa模型的注意力计算有bug

### vllm-project/vllm

- [Feature] 🆕 [#56049](https://github.com/vllm-project/vllm/issues/56049) [Feature]: Fast Start For vLLM
