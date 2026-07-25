# LLM Serving Issue Radar

_Last run: 2026-07-25T13:56+00:00_

**33 issues** — sgl-project/sglang: 15, vllm-project/vllm: 18 — 🆕 **15 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 4
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 4
- [Uncategorized](#uncategorized) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#32331](https://github.com/sgl-project/sglang/issues/32331) [Bug] UnifiedRadixCache prefill crash: TypeError: object of type 'NoneType' has no len() in full_component.commit_hicache_transfer (LOAD_BACK), high concurrency on B200
- [no-prefix] 🆕 ⚠no-prefix [#32356](https://github.com/sgl-project/sglang/issues/32356) DeepSeek-V4 DSpark TP=8 can permanently stall under HiCache long-prefix load
- [RFC] [#32271](https://github.com/sgl-project/sglang/issues/32271) [RFC][Feature] Topology-transparent multi-NIC HTTP ingress with a single logical scheduling queue

### vllm-project/vllm

- [Bug] 🆕 [#49809](https://github.com/vllm-project/vllm/issues/49809) [Bug][KV Offload][P2P] EngineCore crash reconnecting to peer: stale closed ZmqConnection remains registered

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] [#32309](https://github.com/sgl-project/sglang/issues/32309) [Feature] --enable-dsa-cache-layer-split support single deploy
- [RFC] [#32321](https://github.com/sgl-project/sglang/issues/32321) [RFC] Make BaseTpWorker the explicit framework-to-backend boundary - MLX runner-stub redesign

## Attention Backend

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#32283](https://github.com/sgl-project/sglang/issues/32283) CUDA coredump in FlashInfer `RadixTopKRenormProbKernel_MultiCTA`

### vllm-project/vllm

- [other] 🆕 [#49708](https://github.com/vllm-project/vllm/issues/49708) [Model Validation] SmolLM2-360M-Instruct batch invariance
- [other] 🆕 ⚠maintainer-authored [#49735](https://github.com/vllm-project/vllm/issues/49735) [Tracking Issue]: `sm_107` enablement for Rubin GPUs and the Vera Rubin platform

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32378](https://github.com/sgl-project/sglang/issues/32378) [Bug] mooncake with sglang:dev with glm-5.2-w4afp8 with pd error
- [other] 🆕 [#32377](https://github.com/sgl-project/sglang/issues/32377) [GLM-5.2 FP4 Bug] tvm.error.InternalError in trtllm_bf16_moe on Blackwell (SM100) during speculative decoding (EAGLE) with GLM-5.2-NVFP4
- [Bug] [#32311](https://github.com/sgl-project/sglang/issues/32311) [Bug] deepseek v4 flash hang on 4rtx 6000 pro with limited host ram

### vllm-project/vllm

- [Bug] 🆕 [#49730](https://github.com/vllm-project/vllm/issues/49730) [Bug][Qwen 3.5 4B][H100]: Performance of DFlash is lower than expected
- [Bug] [#49716](https://github.com/vllm-project/vllm/issues/49716) [Bug]: int8_per_token_head KV cache corrupts Gemma-4 (hybrid attention) output under load on Triton
- [Performance] [#49723](https://github.com/vllm-project/vllm/issues/49723) [Performance]: Modelopt quantized model goes slower in fp8 than BF16 on B200 (sm100) using vLLM 0.25.1

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#32286](https://github.com/sgl-project/sglang/issues/32286) [Bug] MiniMax-M3 tool-call parser: top-level `oneOf` parameters schema not resolved (numbers become strings, arrays leak raw tags)

### vllm-project/vllm

- [RFC] [#49702](https://github.com/vllm-project/vllm/issues/49702) [RFC]: Add an EPLB Platform Backend interface for out-of-tree accelerators

## New Model Integration

### sgl-project/sglang

- [Feature] [#32291](https://github.com/sgl-project/sglang/issues/32291) [Feature] cp layer split only support layer first , but mooncacke can not support layer first

### vllm-project/vllm

- [RFC] 🆕 [#49752](https://github.com/vllm-project/vllm/issues/49752) [RFC]: vLLM Agentic Coding Readiness Survey
- [RFC] [#49705](https://github.com/vllm-project/vllm/issues/49705) [RFC]: Support router-driven mixtures of multiple LoRA adapters

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] [#49694](https://github.com/vllm-project/vllm/issues/49694) [Bug]: ngram_gpu spec decode + structured outputs (xgrammar) + async scheduling: verifier accepts grammar-illegal draft tokens → "Failed to advance FSM", HTTP 500s and silent truncation under concurrency
- [Bug] [#49711](https://github.com/vllm-project/vllm/issues/49711) [Bug]: poolside_v1 reports zero Responses reasoning_tokens for prompt-opened thinking spans

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Feature] [#32312](https://github.com/sgl-project/sglang/issues/32312) [Feature] [Kernel] cursor warp decode kernel for low latency small batch MOE inference
- [RFC] [#32300](https://github.com/sgl-project/sglang/issues/32300) [RFC] Add CI Infrastructure for the SGLang MLU Backend

### vllm-project/vllm

- [RFC] 🆕 [#49765](https://github.com/vllm-project/vllm/issues/49765) [RFC]: Native Disaggregated Pull-Based Queue Worker Interface and Heuristic Pull Router
- [Bug] [#49724](https://github.com/vllm-project/vllm/issues/49724) [Bug]: Responses custom tools are coerced to function_call on non-Harmony Qwen routes

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49804](https://github.com/vllm-project/vllm/issues/49804) [Bug]: flashinfer cubin version mismatch
- [Bug] [#49717](https://github.com/vllm-project/vllm/issues/49717) [Bug]: Gemma4 streaming: `content` comes back completely empty while `reasoning` holds the model's entire output when the reasoning channel is left open
- [Bug] [#49692](https://github.com/vllm-project/vllm/issues/49692) [Bug]: EPD correctness test produces different output for multi-image prompts
- [Performance] [#49699](https://github.com/vllm-project/vllm/issues/49699) [Performance]: Compile mode 3 degrades triton w4a16 kernel performance in few request scenarios.

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#32276](https://github.com/sgl-project/sglang/issues/32276) [Bug] MiniMax-M3: `thinking: {"type":"disabled"}` is silently ignored, model keeps reasoning
- [no-prefix] 🆕 ⚠no-prefix [#32355](https://github.com/sgl-project/sglang/issues/32355) Add REFUTE scientific critique + calibration benchmark

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#49769](https://github.com/vllm-project/vllm/issues/49769) Add REFUTE scientific critique + calibration benchmark
