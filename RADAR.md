# LLM Serving Issue Radar

_Last run: 2026-10-29T13:24+00:00_

**12 issues** — sgl-project/sglang: 4, vllm-project/vllm: 8 — 🆕 **12 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Feature] 🆕 [#64440](https://github.com/vllm-project/vllm/issues/64440) [Feature]: [MRV2][DBO] Scoped eager decode overlap with attention-only LoRA
- [Feature] 🆕 [#64422](https://github.com/vllm-project/vllm/issues/64422) [Feature]: [MRV2][DBO] Report executed microbatch counts and decision reasons
- [Feature] 🆕 [#64460](https://github.com/vllm-project/vllm/issues/64460) [Feature]: KV-pool-saturated admission retries inflate decode TPOT ~2.3x: request automatic admission backoff

## Quantization

### sgl-project/sglang

- [RFC] 🆕 ⚠maintainer-authored [#47170](https://github.com/sgl-project/sglang/issues/47170) [RFC] Model Independent Parallelism Layer Boundaries and Weight Loading

### vllm-project/vllm

- [RFC] 🆕 [#64508](https://github.com/vllm-project/vllm/issues/64508) [RFC]: Checkpoint-internal paging for hybrid recurrent state
- [RFC] 🆕 ⚠maintainer-authored [#64418](https://github.com/vllm-project/vllm/issues/64418) [RFC]: Load plan — an engine-neutral API for sharded weight transfer

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Feature] 🆕 [#47207](https://github.com/sgl-project/sglang/issues/47207) [Feature] Evaluate a fused DeepSeek-V4.1 mHC boundary for SM90 TP2 low-token decode

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#47213](https://github.com/sgl-project/sglang/issues/47213) [Bug] Qwen3.5 prefix-cache reuse changes logprobs with deterministic inference enabled
- [Feature] 🆕 [#47226](https://github.com/sgl-project/sglang/issues/47226) [Feature] Accept extra_params on /v1/audio/speech like vLLM-Omni (Qwen3-TTS currently ignores it without an error)

### vllm-project/vllm

- [Bug] 🆕 [#64427](https://github.com/vllm-project/vllm/issues/64427) [Bug][Spec Decode] Model Runner V2 + DSpark at n=8: target degenerates to one repeated token while acceptance reports 87.5%

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#64446](https://github.com/vllm-project/vllm/issues/64446) [Performance]: Evaluate SM90 TP2 mHC boundary fusion under rotating weights

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#64489](https://github.com/vllm-project/vllm/issues/64489) [Bug]: vllm/vllm-openai:unlimited-ocr image cannot serve Unlimited-OCR model
