# LLM Serving Issue Radar

_Last run: 2026-11-27T13:22+00:00_

**13 issues** — sgl-project/sglang: 2, vllm-project/vllm: 11 — 🆕 **13 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [RFC] 🆕 [#53560](https://github.com/sgl-project/sglang/issues/53560) [RFC] Runtime Scheduling Policy Registration and Hot Switching

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#70350](https://github.com/vllm-project/vllm/issues/70350) [Bug]: ECMooncakeConnector producer never releases per-consumer-address ZMQ sockets/topology cache; fd exhaustion when consumer pod IPs change

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#70328](https://github.com/vllm-project/vllm/issues/70328) [Bug]: Intermittent IMA in MLA on SM120 with cuBLAS 13.5.x / 13.6.0: nvjet GEMM over-reads the interleaved W_UK / W_UV `torch.bmm` operands (deterministic repro, possibly #64266)

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#70273](https://github.com/vllm-project/vllm/issues/70273) [Bug]: Muse-Glimmer-30B-NVFP4 hangs or crashes with "illegal memory access" on RTX PRO 5000 Blackwell when another process on the same GPU is under load

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#70287](https://github.com/vllm-project/vllm/issues/70287) [Bug]: With VLLM_USE_NCCL_SYMM_MEM=1, all-reduces over non-TP groups (e.g. DCP) silently return the TP group's sum
- [Bug] 🆕 [#70257](https://github.com/vllm-project/vllm/issues/70257) [Bug]: KV event publisher binds or connects depending on how the same IPv6 address is spelled

## New Model Integration

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#53552](https://github.com/sgl-project/sglang/issues/53552) [CI] Shared GITHUB_TOKEN quota (15k/h) runs out daily at ~08:55–09:20 UTC; CI jobs fail with "API rate limit exceeded for installation"

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Feature] 🆕 [#70264](https://github.com/vllm-project/vllm/issues/70264) [Feature]: Support adaptive verification together with LoRA

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#70330](https://github.com/vllm-project/vllm/issues/70330) [Bug]: Untyped tool parameters return null as the string "null" (Python parsers; Rust frontend returns null)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#70298](https://github.com/vllm-project/vllm/issues/70298) [Bug]: Inkling 2 Mini: tool call written as XML text or never emitted, even with the official parsers (RTX 5090, image built for archs 10.0/10.3)
- [Bug] 🆕 [#70267](https://github.com/vllm-project/vllm/issues/70267) [Bug]: Inkling 2 Mini: DSpark greedy output differs from no speculation on plain-text prompts, deterministically
- [Bug] 🆕 [#70266](https://github.com/vllm-project/vllm/issues/70266) [Bug]: Inkling 2 Mini: prefix caching changes greedy output of image requests sent one at a time
- [Feature] 🆕 [#70265](https://github.com/vllm-project/vllm/issues/70265) [Feature]: Write the resolved vllm serve settings to a YAML file that --config can load
