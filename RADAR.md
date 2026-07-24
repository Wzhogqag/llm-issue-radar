# LLM Serving Issue Radar

_Last run: 2026-07-24T13:58+00:00_

**35 issues** — sgl-project/sglang: 15, vllm-project/vllm: 20 — 🆕 **35 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 4
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 6
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 5

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#32271](https://github.com/sgl-project/sglang/issues/32271) [RFC][Feature] Topology-transparent multi-NIC HTTP ingress with a single logical scheduling queue

### vllm-project/vllm

- [Bug] 🆕 [#49674](https://github.com/vllm-project/vllm/issues/49674) [Bug]: Deferred KV block frees cause zero-progress preemption cascades with async KV consumers

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#32309](https://github.com/sgl-project/sglang/issues/32309) [Feature] --enable-dsa-cache-layer-split support single deploy
- [RFC] 🆕 [#32321](https://github.com/sgl-project/sglang/issues/32321) [RFC] Make BaseTpWorker the explicit framework-to-backend boundary - MLX runner-stub redesign

### vllm-project/vllm

- [Feature] 🆕 [#49630](https://github.com/vllm-project/vllm/issues/49630) [Feature]: Integration of HieraSparse N:M Semi-Structured Sparse KV Cache Attention

## Attention Backend

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#32283](https://github.com/sgl-project/sglang/issues/32283) CUDA coredump in FlashInfer `RadixTopKRenormProbKernel_MultiCTA`

### vllm-project/vllm

- [other] 🆕 [#49649](https://github.com/vllm-project/vllm/issues/49649) [ROCm] Sparse-MLA persistent-kernel gate is unsafe for gqa_ratio=64 fp8 (no non-persistent kernel)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32311](https://github.com/sgl-project/sglang/issues/32311) [Bug] deepseek v4 flash hang on 4rtx 6000 pro with limited host ram
- [Bug] 🆕 [#32250](https://github.com/sgl-project/sglang/issues/32250) [Bug] --quantization marlin is accepted by CLI but missing from the registry

### vllm-project/vllm

- [Performance] 🆕 [#49723](https://github.com/vllm-project/vllm/issues/49723) [Performance]: Modelopt quantized model goes slower in fp8 than BF16 on B200 (sm100) using vLLM 0.25.1
- [Bug] 🆕 [#49716](https://github.com/vllm-project/vllm/issues/49716) [Bug]: int8_per_token_head KV cache corrupts Gemma-4 (hybrid attention) output under load on Triton
- [no-prefix] 🆕 ⚠no-prefix [#49638](https://github.com/vllm-project/vllm/issues/49638) NVFP4 fused-expert scales dropped in Qwen3_5_VL_MoE weight_loader (qwen3_5_vl_moe)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#32204](https://github.com/sgl-project/sglang/issues/32204) [Bug] DFlash aux hidden state capture fails when target_layer_ids includes the last decoder layer (qwen3_5 IndexError)
- [no-prefix] 🆕 ⚠no-prefix [#32200](https://github.com/sgl-project/sglang/issues/32200) NCCL SYMM: Add one-sided RMA support

### vllm-project/vllm

- [Bug] 🆕 [#49635](https://github.com/vllm-project/vllm/issues/49635) [Bug]: Final KV offload store after request finalization crashes EngineCore
- [RFC] 🆕 [#49702](https://github.com/vllm-project/vllm/issues/49702) [RFC]: Add an EPLB Platform Backend interface for out-of-tree accelerators

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#32291](https://github.com/sgl-project/sglang/issues/32291) [Feature] cp layer split only support layer first , but mooncacke can not support layer first

### vllm-project/vllm

- [Bug] 🆕 [#49712](https://github.com/vllm-project/vllm/issues/49712) [Bug]: Responses silently ignores named tool_choice for unsupported XML tool parsers
- [RFC] 🆕 [#49705](https://github.com/vllm-project/vllm/issues/49705) [RFC]: Support router-driven mixtures of multiple LoRA adapters

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#32290](https://github.com/sgl-project/sglang/issues/32290) [Bug] OpenAI top_logprobs: entries silently collapse when top-k candidates decode to identical text (dict keyed by decoded string)
- [Bug] 🆕 [#32226](https://github.com/sgl-project/sglang/issues/32226) [Bug] SGLang crashes when serving gpt-oss-120b with nvidia/gpt-oss-120b-Eagle3-v3 EAGLE head
- [Bug] 🆕 [#32202](https://github.com/sgl-project/sglang/issues/32202) [Bug] Speculative draft auto load format does not resolve object-storage paths
- [Feature] 🆕 [#32264](https://github.com/sgl-project/sglang/issues/32264) [Feature][MLX] Gemma 4 MTP speculative decoding on Apple Silicon

### vllm-project/vllm

- [Bug] 🆕 [#49711](https://github.com/vllm-project/vllm/issues/49711) [Bug]: poolside_v1 reports zero Responses reasoning_tokens for prompt-opened thinking spans
- [Bug] 🆕 [#49694](https://github.com/vllm-project/vllm/issues/49694) [Bug]: ngram_gpu spec decode + structured outputs (xgrammar) + async scheduling: verifier accepts grammar-illegal draft tokens → "Failed to advance FSM", HTTP 500s and silent truncation under concurrency

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Feature] 🆕 [#32312](https://github.com/sgl-project/sglang/issues/32312) [Feature] [Kernel] cursor warp decode kernel for low latency small batch MOE inference
- [RFC] 🆕 [#32300](https://github.com/sgl-project/sglang/issues/32300) [RFC] Add CI Infrastructure for the SGLang MLU Backend

### vllm-project/vllm

- [Bug] 🆕 [#49724](https://github.com/vllm-project/vllm/issues/49724) [Bug]: Responses custom tools are coerced to function_call on non-Harmony Qwen routes
- [Feature] 🆕 [#49661](https://github.com/vllm-project/vllm/issues/49661) [Feature]: Add a server-side tool strictness level for auto tool choice

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#49643](https://github.com/vllm-project/vllm/issues/49643) [RFC]: Enable full CUDA graphs for MoRIIO READ mode via async KV-load gating

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49725](https://github.com/vllm-project/vllm/issues/49725) [Bug]: Qwen3-Embedding-8B discrimination quality degrades under real concurrent multi-tenant traffic on RTX 6000 Blackwell (not reproducible in isolation, not fixed by dtype/pooler-config/prefix-caching)
- [Bug] 🆕 [#49717](https://github.com/vllm-project/vllm/issues/49717) [Bug]: Gemma4 streaming: `content` comes back completely empty while `reasoning` holds the model's entire output when the reasoning channel is left open
- [Bug] 🆕 [#49692](https://github.com/vllm-project/vllm/issues/49692) [Bug]: EPD correctness test produces different output for multi-image prompts
- [Performance] 🆕 [#49699](https://github.com/vllm-project/vllm/issues/49699) [Performance]: Compile mode 3 degrades triton w4a16 kernel performance in few request scenarios.
- [other] 🆕 [#49683](https://github.com/vllm-project/vllm/issues/49683) [Installation]: no cu129 nightly wheels for x86_64 platform
