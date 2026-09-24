# LLM Serving Issue Radar

_Last run: 2026-09-24T13:29+00:00_

**9 issues** — sgl-project/sglang: 6, vllm-project/vllm: 3 — 🆕 **9 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#41124](https://github.com/sgl-project/sglang/issues/41124) penalties use one step stale history under the overlap scheduler

### vllm-project/vllm

- [RFC] 🆕 [#58537](https://github.com/vllm-project/vllm/issues/58537) [RFC]: KV Context Editing — Relaxed Prefix Alignment for KV Allocation and Reuse

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#58544](https://github.com/vllm-project/vllm/issues/58544) [Feature]: [Helm] Add configurable startupProbe for slow model initialization
- [RFC] 🆕 [#58520](https://github.com/vllm-project/vllm/issues/58520) [RFC]: Publish Mooncake Store residency once per complete block

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#41129](https://github.com/sgl-project/sglang/issues/41129) [Feature] Support configurable retention for request log files
- [Feature] 🆕 [#41110](https://github.com/sgl-project/sglang/issues/41110) [Feature] Qwen3.5forsequenceclassification model is supported

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Feature] 🆕 [#41070](https://github.com/sgl-project/sglang/issues/41070) [Feature][Spec][XPU] Honor rejection sampling in EAGLE chain verification

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#41077](https://github.com/sgl-project/sglang/issues/41077) [Bug] DWDP: expert weight copy peaks at 2x local expert memory, causing OOM at startup
- [Bug] 🆕 [#41076](https://github.com/sgl-project/sglang/issues/41076) [Bug] DeepSeek-V4.1-Flash + DSPARK: unbounded SparsePrefillWorkspace allocation OOM-crashes the whole TP group
