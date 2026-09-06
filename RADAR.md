# LLM Serving Issue Radar

_Last run: 2026-09-06T13:23+00:00_

**29 issues** — sgl-project/sglang: 5, vllm-project/vllm: 24 — 🆕 **29 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 9
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#55524](https://github.com/vllm-project/vllm/issues/55524) [RFC] Mamba2: exact-replay decode so that prefill, chunked prefill and decode produce identical bits

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#38207](https://github.com/sgl-project/sglang/issues/38207) [Bug] GLM-5.3 DPC crashes
- [Performance] 🆕 [#38206](https://github.com/sgl-project/sglang/issues/38206) [Performance][PP/PD] Bootstrap admission waits ~7.8s for consensus under PP16 concurrent prefill

### vllm-project/vllm

- [Bug] 🆕 [#55509](https://github.com/vllm-project/vllm/issues/55509) [Bug]: --attention-backend FLASHINFER fails the startup KV-cache check at a max-model-len that FLASH_ATTN serves; the message never names the backend

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#38196](https://github.com/sgl-project/sglang/issues/38196) [Bug] [NPU] ascend attention backend silently corrupts output with page_size 16 (128 OK, 1 rejected per #25169)

### vllm-project/vllm

- [Bug] 🆕 [#55568](https://github.com/vllm-project/vllm/issues/55568) [Bug]: [Portability][MSVC] Preprocessor directives inside BOOL_SWITCH macro arguments fail to compile
- [Bug] 🆕 [#55526](https://github.com/vllm-project/vllm/issues/55526) [Bug]: DeepSeek-V4-Flash TP=16 on SM120 (RTX 5090 x16, ray multi-node) fails: DSV4 sparse MLA decode specialization error for (num_q_heads=8, top_k=128) despite FlashInfer dispatch table containing that config

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#38143](https://github.com/sgl-project/sglang/issues/38143) [Bug] MiniMax-M3 W4A16 (compressed-tensors) on 2x DGX Spark (sm_121, TP=2): serves but every token is id 0 — all-NUL output on the Triton MiniMaxSparse path; same weights correct on vLLM

### vllm-project/vllm

- [Bug] 🆕 [#55571](https://github.com/vllm-project/vllm/issues/55571) [Bug]: Xid 13 "Out Of Range Address" / CUDA illegal memory access on RTX PRO 5000 (SM120) with FP8 model under sustained load — gone with VLLM_DISABLED_KERNELS=FlashInferFP8ScaledMMLinearKernel or --enforce-eager
- [Bug] 🆕 [#55560](https://github.com/vllm-project/vllm/issues/55560) [Bug]: CPU WNA16 GPTQ-Int4 MoE kernel (CPUExpertsInt4) produces NaN logits under torch.compile — fixed by --enforce-eager
- [Bug] 🆕 [#55541](https://github.com/vllm-project/vllm/issues/55541) [Bug]: GLM-5.3-Flash with forced tool_choice (named function) fails to converge — runs to max_tokens and returns   ▎ truncated tool_call.arguments
- [Bug] 🆕 [#55510](https://github.com/vllm-project/vllm/issues/55510) [Bug]: EngineCore and TP workers survive a SIGKILLed API server, keep the GPUs, and reparent to the launching process
- [Bug] 🆕 [#55496](https://github.com/vllm-project/vllm/issues/55496) [Bug]: ModelOpt MIXED_PRECISION cannot load FP8_BLOCK_SCALES MTP experts (nvidia/Qwen3.8-Flash-Next-NVFP4 + MTP)
- [Bug] 🆕 [#55495](https://github.com/vllm-project/vllm/issues/55495) [Bug]: qwen3_xml tool parser emits a truncated `arguments` string with a leaked `</parameter` tag; the Responses API then rejects every later request of the conversation with `400 Expecting value`
- [Bug] 🆕 [#55486](https://github.com/vllm-project/vllm/issues/55486) [Bug]: vLLM 0.28.0 — DeepSeek V4 on B200 (TP8+EP, fp8 KV, FULL_AND_PIECEWISE) generates only BOS tokens with V2 model runner default
- [other] 🆕 [#55512](https://github.com/vllm-project/vllm/issues/55512) [New Model]: K2-Horizon-MoVA (MoVA attention) — single-GPU Int4 via out-of-tree plugin; native support?

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#55517](https://github.com/vllm-project/vllm/issues/55517) [Bug]: qwen3.8-flash-next: assert numerator % denominator == 0, "{} is not divisible by {}".format
- [RFC] 🆕 [#55487](https://github.com/vllm-project/vllm/issues/55487) [RFC] Publish typed extra_keys in BlockStored KV events

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#55501](https://github.com/vllm-project/vllm/issues/55501) [Feature]: Warn or auto-select the shipped score template when serving an original Qwen3-Reranker without --chat-template

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#55533](https://github.com/vllm-project/vllm/issues/55533) [Bug][Spec Decode] Hybrid GDN (Qwen3.5/Qwen3.8 27B-class) + MTP: scheduler runs only ~3 concurrent sequences at batch >= 4 — acceptance/throughput collapse
- [Bug] 🆕 [#55518](https://github.com/vllm-project/vllm/issues/55518) [Bug]: kv_cache_utils warns that prefix-cache reuse is disabled even when disable_eagle_block_drop keeps it working
- [Bug] 🆕 [#55503](https://github.com/vllm-project/vllm/issues/55503) [Bug]: OffloadingConnector multi-tier (CPU+fs secondary tier) + MTP speculative decoding crashes EngineCore in _build_store_jobs (assert len(offload_keys) == len(offload_block_ids))

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#38167](https://github.com/sgl-project/sglang/issues/38167) [Bug][Diffusion] MiniMax-H3: 1344x768 fails deterministically with "CUDA driver error: device not ready" on 12GB, and the failed request poisons the server

### vllm-project/vllm

- [Bug] 🆕 [#55530](https://github.com/vllm-project/vllm/issues/55530) [Bug]: Responses API automatic tool JSON retry crashes in ParsableContext

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#55561](https://github.com/vllm-project/vllm/issues/55561) [Bug]: Sweep Pareto plots include dominated throughput ties

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#55555](https://github.com/vllm-project/vllm/issues/55555) [Bug]: multimodal LoRA/tower connector with float16 dtype reaches torch.empty(None)
- [Bug] 🆕 [#55552](https://github.com/vllm-project/vllm/issues/55552) [Bug]: tool_choice="required" not enforced with Qwen3.8-Flash-Next when enable_thinking=false (streaming); xgrammar "Failed to advance FSM" / "matcher has terminated" with thinking on + MTP
- [Bug] 🆕 [#55515](https://github.com/vllm-project/vllm/issues/55515) [Bug]: Qwen4Exp N-gram PLE embedding requires pipeline_parallel_size=1 because non-first pipeline ranks do not receive the raw input_ids it needs. Please run with PP=1
- [Bug] 🆕 [#55502](https://github.com/vllm-project/vllm/issues/55502) [Bug]: /rerank keeps processing queued documents after the client disconnects, despite @with_cancellation
