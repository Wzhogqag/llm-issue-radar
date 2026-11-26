# LLM Serving Issue Radar

_Last run: 2026-11-26T13:23+00:00_

**16 issues** — sgl-project/sglang: 2, vllm-project/vllm: 14 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#70060](https://github.com/vllm-project/vllm/issues/70060) [RFC]: Extend Mamba Internal Prefill Checkpoints to Non-Final Chunks

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#70055](https://github.com/vllm-project/vllm/issues/70055) [Bug]: HiSparse completes a wasted host import after the request is aborted
- [Bug] 🆕 [#70043](https://github.com/vllm-project/vllm/issues/70043) [Bug]: Inkling 2: copies of a prompt in one batch differ run to run with prefix caching on
- [RFC] 🆕 [#70051](https://github.com/vllm-project/vllm/issues/70051) [RFC]: Async Pre-Allocation Wait State in Scheduler for External KV Transfer and Lookup

## Quantization

### vllm-project/vllm

- [Feature] 🆕 [#70061](https://github.com/vllm-project/vllm/issues/70061) [Feature]: Opt-in fixed-order LoRA shrink reduction without global batch-invariant mode
- [RFC] 🆕 [#70046](https://github.com/vllm-project/vllm/issues/70046) [RFC]: Zero-VRAM progressive bit-sliced (2+2+4) sparse FP8 MoE backend for FusedMoEExpertsModular

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Performance] 🆕 [#70041](https://github.com/vllm-project/vllm/issues/70041) [Performance]: Cross-NUMA API tokenization increases TTFT on DeepSeek-V4-Pro with Ray

## Sampling / Speculative Decoding

### sgl-project/sglang

- [other] 🆕 [#53343](https://github.com/sgl-project/sglang/issues/53343) [Question] debug_utils/dumper: how to group dumps per step when a draft model has no root forward()

### vllm-project/vllm

- [Bug] 🆕 [#70098](https://github.com/vllm-project/vllm/issues/70098) [Bug]: Rust frontend silently accepts `thinking_token_budget` when no reasoning config is set

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#70056](https://github.com/vllm-project/vllm/issues/70056) [Bug]: Mistral parser emits blank tool names followed by orphaned streaming argument deltas
- [Bug] 🆕 [#70053](https://github.com/vllm-project/vllm/issues/70053) [Bug]: /v1/responses` streaming crashes with `ValidationError: ResponseFunctionToolCallItem.name ... NoneType` when a tool-call state is opened from a delta without `function.name
- [no-prefix] 🆕 ⚠no-prefix [#70049](https://github.com/vllm-project/vllm/issues/70049) FusedMoE default loader skips e_score_correction_bias and misses the router parameter alias

## Performance / Memory / OOM

### vllm-project/vllm

- [Feature] 🆕 [#70057](https://github.com/vllm-project/vllm/issues/70057) [Feature]: DFlash2 best-first tree verification for Qwen3.5/GDN on Model Runner V2

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#53341](https://github.com/sgl-project/sglang/issues/53341) [CI] Nightly Docker images not published since 2026-11-22: build runners moirai-a10-runner-0 and labubu stopped picking up jobs

### vllm-project/vllm

- [Bug] 🆕 [#70127](https://github.com/vllm-project/vllm/issues/70127) [Bug][XPU] Qwen3.6-35B-A3B MXFP4: more dropped items in long json_schema outputs after #64687
- [Bug] 🆕 [#70054](https://github.com/vllm-project/vllm/issues/70054) [Bug]: Rust frontend (vllm-rs) silently hangs on unbounded ZMQ input send while /health continues returning 200 OK
