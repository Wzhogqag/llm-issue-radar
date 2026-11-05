# LLM Serving Issue Radar

_Last run: 2026-11-05T13:22+00:00_

**17 issues** — sgl-project/sglang: 7, vllm-project/vllm: 10 — 🆕 **17 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Quantization](#quantization) — 6
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 5
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Perf] 🆕 [#48623](https://github.com/sgl-project/sglang/issues/48623) [Perf] radix cache: each eviction rebuilds a heap over all evictable leaves

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#48618](https://github.com/sgl-project/sglang/issues/48618) [Bug]
- [RFC] 🆕 [#48582](https://github.com/sgl-project/sglang/issues/48582) [RFC] Integrate MindIE-SD as an Acceleration Library for SGLang Diffusion

### vllm-project/vllm

- [Bug] 🆕 [#65907](https://github.com/vllm-project/vllm/issues/65907) [Bug]: v0.33.0: DeepSeek-V4.1 + DSpark speculative decoding OOMs at startup with `--gpu-memory-utilization=0.97` (worked in v0.32.0) — speculator CUDA-graph-capture allocation (~4 GiB in `sparse_attn_indexer`) not accounted for by memory profiling
- [Bug] 🆕 [#65906](https://github.com/vllm-project/vllm/issues/65906) [Bug]: Qwen3.5-122B-A10B-FP8 GSM8K accuracy decreases at commit 0fae39a
- [Bug] 🆕 [#65873](https://github.com/vllm-project/vllm/issues/65873) [Bug]: Nemotron-3.5-Super-VL-120B-A12B-NVFP4 native MTP fails to load: "start (0) + length (5376) exceeds dimension size (2688)"
- [Bug] 🆕 [#65807](https://github.com/vllm-project/vllm/issues/65807) [Bug]: cyankiwi/Qwen3.8-27B-AWQ-INT4输出混乱

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#65841](https://github.com/vllm-project/vllm/issues/65841) [Feature]: Support n > 1 sampling and multimodal processor kwargs in vllm.Inference

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#48601](https://github.com/sgl-project/sglang/issues/48601) [Bug] Decode HiCache returns HTTP 500 when a shorter prefix has no Mamba checkpoint

### vllm-project/vllm

- [RFC] 🆕 [#65813](https://github.com/vllm-project/vllm/issues/65813) [RFC]: Add a Tree Speculative Decoding Framework

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#48561](https://github.com/sgl-project/sglang/issues/48561) [Bug] DeepSeek V4.1: natural EOS with unclosed reasoning produces a successful empty answer
- [Feature] 🆕 [#48581](https://github.com/sgl-project/sglang/issues/48581) [Feature] Honor chat-template stop strings when ChatCompletionRequest carries input_ids
- [Feature] 🆕 [#48580](https://github.com/sgl-project/sglang/issues/48580) [Feature] Add per-request skip_detokenize option to sglang.api.v1.GenerateRequest

### vllm-project/vllm

- [Bug] 🆕 [#65811](https://github.com/vllm-project/vllm/issues/65811) [Bug]: Qwen3.5-122B + LoRA crashes at startup: _inject_lora_into_fused_moe asserts TritonExperts, but FlashInferExperts is auto-selected
- [RFC] 🆕 [#65797](https://github.com/vllm-project/vllm/issues/65797) [RFC]: Token-id parity with the Python frontend as a tested contract for the Rust frontend

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#65793](https://github.com/vllm-project/vllm/issues/65793) [Bug]: DeepSeek-V4.1-Flash: some DP ranks of a multi-node DP/EP decode engine produce degenerate output (rank-sticky, reproduces without P/D transfer)

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 ⚠maintainer-authored [#65886](https://github.com/vllm-project/vllm/issues/65886) [Feature]: Add gc-moe as an option for moe-backend
