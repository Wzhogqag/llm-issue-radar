# LLM Serving Issue Radar

_Last run: 2026-07-22T14:00+00:00_

**16 issues** — sgl-project/sglang: 6, vllm-project/vllm: 10 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#31954](https://github.com/sgl-project/sglang/issues/31954) [Feature] Anti-starvation aging for the lpm schedule policy
- [Feature] 🆕 [#31953](https://github.com/sgl-project/sglang/issues/31953) [Feature] Runtime schedule_policy switching without an engine reload

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#49360](https://github.com/vllm-project/vllm/issues/49360) [Bug]: `MooncakeStoreConnector` KV Offload hangs the vLLM engine on a GDN model (`Qwen3.6-35B-A3B`)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#32021](https://github.com/sgl-project/sglang/issues/32021) [Bug] Intermittent CUTLASS NVFP4 GEMM 'Error Internal' in qkv_proj crashes one TP rank (SM121, MiniMax-M3, 4x DGX Spark)

### vllm-project/vllm

- [Feature] 🆕 [#49421](https://github.com/vllm-project/vllm/issues/49421) [Feature]: Support for GLM-5.2 NVFP4 on NVIDIA RTX PRO 6000 (SM120 Architecture)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#49368](https://github.com/vllm-project/vllm/issues/49368) [Bug]: GLM-4.1V fails to start at tensor-parallel size 32 — vision tower head-count mismatch

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 ⚠maintainer-authored [#31969](https://github.com/sgl-project/sglang/issues/31969) [Feature] Support Multi-Item Scoring for Qwen3.5 GDN layers

### vllm-project/vllm

- [Feature] 🆕 [#49404](https://github.com/vllm-project/vllm/issues/49404) [Feature]: enhance pcp with vllm

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#32038](https://github.com/sgl-project/sglang/issues/32038) [Bug] DSpark speculative decoding causes accuracy regression on DeepSeek-V4-Flash (AIME25 97.08→93.96)

### vllm-project/vllm

- [Bug] 🆕 [#49354](https://github.com/vllm-project/vllm/issues/49354) [Bug]: Qwen3.5 / Qwen3.6 hybrid-GDN LoRA: vLLM `enable_lora` does not change generations vs base, while HF Peft does
- [Bug] 🆕 [#49418](https://github.com/vllm-project/vllm/issues/49418) [Bug]: DeepSeek-V4-Flash-DSpark fails to launch with DSpark speculative decoding on SM120 Pro6000D (works fine when disabled)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#31970](https://github.com/sgl-project/sglang/issues/31970) [Bug] Mamba slot-donation debug asserts force a per-request cudaStreamSynchronize on the scheduler thread

### vllm-project/vllm

- [RFC] 🆕 [#49411](https://github.com/vllm-project/vllm/issues/49411) [RFC] [Feature] [Experimental] Support GigaToken Accelerated Tokenizer Mode

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#49449](https://github.com/vllm-project/vllm/issues/49449) [Bug]: V1 streaming-session rebuild leaves stale prefix-cache block hashes and can produce incorrect output
- [Bug] 🆕 [#49405](https://github.com/vllm-project/vllm/issues/49405) [Bug]: RuntimeError: _moe_C::topk_softmax() expected at most 6 argument(s) but received 7 argument(s). Declaration: _moe_C::topk_softmax(Tensor($0! -> ) topk_weights, Tensor($1! -> ) topk_indices, Tensor($2! -> ) .....

## Uncategorized

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#49349](https://github.com/vllm-project/vllm/issues/49349) Zero JIT compilation during runtime
