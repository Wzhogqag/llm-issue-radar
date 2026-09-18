# LLM Serving Issue Radar

_Last run: 2026-09-18T13:27+00:00_

**14 issues** — sgl-project/sglang: 3, vllm-project/vllm: 11 — 🆕 **14 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 2

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#57562](https://github.com/vllm-project/vllm/issues/57562) [Bug]: AsyncScheduler num_output_placeholders underflow with chunked prefill + concurrency (no spec decode, no preemption) — regression from 0.24.0

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#57566](https://github.com/vllm-project/vllm/issues/57566) [RFC]: Stable, versioned plugin contract for out-of-tree attention backends + custom KV-cache specs

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#40083](https://github.com/sgl-project/sglang/issues/40083) [Bug] json_schema accepts uniqueItems and multipleOf but does not enforce them

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#57521](https://github.com/vllm-project/vllm/issues/57521) [Bug][Perf][DSpark] #54674 stacked context WKV regresses TTFT ~3.3% on 2-node DGX Spark (GB10, TP=2), with no decode gain
- [Bug] 🆕 [#57486](https://github.com/vllm-project/vllm/issues/57486) [Bug]: On SM12x, fp8 block linear still selects DeepGEMM when E8M0 is disabled, which now hard-fails after the a6bbb80 pin
- [Bug] 🆕 [#57473](https://github.com/vllm-project/vllm/issues/57473) [Bug]: Aria expert loading looks up w13_weight.weight / w2_weight.weight

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#40152](https://github.com/sgl-project/sglang/issues/40152) [Feature] Track DeepSeek-V4.1 support on the main branch

### vllm-project/vllm

- [Feature] 🆕 [#57544](https://github.com/vllm-project/vllm/issues/57544) [Feature]: Support jina-ocr-v1

## Sampling / Speculative Decoding

### vllm-project/vllm

- [RFC] 🆕 [#57499](https://github.com/vllm-project/vllm/issues/57499) [RFC]: Stateless Responses API in the Rust frontend

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#57550](https://github.com/vllm-project/vllm/issues/57550) [Bug]: xgrammar feature detection misses constraints when JSON Schema omits type
- [RFC] 🆕 ⚠maintainer-authored [#57479](https://github.com/vllm-project/vllm/issues/57479) [RFC]: Bound frontend drain latency for bulk aborts and long non-streaming completions

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#57475](https://github.com/vllm-project/vllm/issues/57475) [Bug] CUDA graph memory estimate under-reserves → OOM during graph capture at high `--gpu-memory-utilization`

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#40084](https://github.com/sgl-project/sglang/issues/40084) [ROCm][QuickReduce] Q8 BF16→FP16 low-amplitude scale saturation attenuates all-reduce output

### vllm-project/vllm

- [Bug] 🆕 [#57493](https://github.com/vllm-project/vllm/issues/57493) [Bug]: [ROCm][gfx1151] ROCM_ATTN returns different outputs for the same greedy request after other requests
