# LLM Serving Issue Radar

_Last run: 2026-07-28T14:05+00:00_

**24 issues** — sgl-project/sglang: 8, vllm-project/vllm: 16 — 🆕 **24 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 5
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 ⚠maintainer-authored [#50031](https://github.com/vllm-project/vllm/issues/50031) [RFC]: Back-pressure detection for KV cache offloading tiers

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#32652](https://github.com/sgl-project/sglang/issues/32652) [Bug] [Security tracking][PD disaggregation] Decode control-path failure can remain invisible to health checks
- [Bug] 🆕 [#32605](https://github.com/sgl-project/sglang/issues/32605) [Bug] maybe hicache mix-up request in new version(0.5.15)

## Attention Backend

### sgl-project/sglang

- [RFC] 🆕 [#32657](https://github.com/sgl-project/sglang/issues/32657) [RFC] A Unified KV-Cache Sparsity Framework for Post-Hoc Sparse Attention
- [Feature] 🆕 ⚠maintainer-authored [#32607](https://github.com/sgl-project/sglang/issues/32607) [Feature] Kimi K3 Roadmap

### vllm-project/vllm

- [Bug] 🆕 [#50147](https://github.com/vllm-project/vllm/issues/50147) [Bug]: Kimi-K3 (TP=8, prefix caching / mamba 'align' mode): recurring illegal-memory-access crashes under concurrent load; crash site varies; MTBF scales inversely with concurrency
- [Bug] 🆕 [#50067](https://github.com/vllm-project/vllm/issues/50067) [Bug]: EngineCore dies silently during warmup on GB10/sm_121 (dense model, FLASH_ATTN); avoided by CUDA_LAUNCH_BLOCKING=1
- [Bug] 🆕 [#50064](https://github.com/vllm-project/vllm/issues/50064) [Bug]: ROCm ROCMAiterMLASparseMetadata missing num_decode_tokens, sparse MLA (DSA) models fail to start on MI300X on main

## Quantization

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#32655](https://github.com/sgl-project/sglang/issues/32655) [Bug] Kimi-K2.6 NVFP4 throughput regression after enabling piecewise prefill CUDA graph (#30889)

### vllm-project/vllm

- [Bug] 🆕 [#50056](https://github.com/vllm-project/vllm/issues/50056) [Bug]: kimi-k3 --kvcache-dtype-fp8 error
- [other] 🆕 [#50143](https://github.com/vllm-project/vllm/issues/50143) [Bug/Feature]: w8a8_block_int8_matmul kernel is dormant
- [no-prefix] 🆕 ⚠no-prefix [#50059](https://github.com/vllm-project/vllm/issues/50059) LoRA on a compressed-tensors int4 (W4A16) model: rank-32 all-layer adapters produce weak, non-reproducible outputs; rank-8 partial-coverage adapters work fine (0.17.1–0.24.0, RTX 5090)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#50142](https://github.com/vllm-project/vllm/issues/50142) [Bug]: Qwen3-Omni does not propagate effective sampled FPS to audio/video interleaving
- [Bug] 🆕 [#50136](https://github.com/vllm-project/vllm/issues/50136) [Bug] should_custom_ar()'s size threshold makes all-reduce kernel selection batch-dependent, which is why custom all-reduce can't simply be re-enabled under VLLM_BATCH_INVARIANT
- [Feature] 🆕 [#50098](https://github.com/vllm-project/vllm/issues/50098) [Feature]: Kimi K3 DSpark Pipeline Parallelism

## New Model Integration

### sgl-project/sglang

- [other] 🆕 [#32646](https://github.com/sgl-project/sglang/issues/32646) [Model] Support Microsoft Mage-VL (4B Codec-Native VLM)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#32549](https://github.com/sgl-project/sglang/issues/32549) [Bug] Decode starved to ~1 batch per 24s under sustained chunked-prefill load (strict prefill-first scheduling, spec decode)
- [Bug] 🆕 ⚠maintainer-authored [#32582](https://github.com/sgl-project/sglang/issues/32582) [Bug] Glm5.2 Decode's Perf decrease a lot

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#50026](https://github.com/vllm-project/vllm/issues/50026) [Bug]: /v1/chat/completions/batch accepts stream: true and returns empty output with HTTP 200; tools are silently dropped

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#50127](https://github.com/vllm-project/vllm/issues/50127) [RFC]: Shared Context Parallelism: peer-addressable GPU objects for PCP and DCP
- [other] 🆕 ⚠maintainer-authored [#50130](https://github.com/vllm-project/vllm/issues/50130) [CI] Transformers backend llava-onevision test needs default_torch_num_threads=1 to avoid hanging

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#50135](https://github.com/vllm-project/vllm/issues/50135) [Bug]: ValueError: Free memory on device xpu:0 (0.22/30.3 GiB) on startup is less than desired GPU memory utilization (0.7, 21.21 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes.
- [Bug] 🆕 [#50046](https://github.com/vllm-project/vllm/issues/50046) [Bug]: Qwen3.5/Qwen3-Next GDN attention crashes at warmup with torch.compile stride mismatch (expected size 3==3, stride 4097==512) — recurrence of #29014 on splitting_ops boundary
- [Bug] 🆕 [#50024](https://github.com/vllm-project/vllm/issues/50024) [Bug]: get_open_port() hangs forever when VLLM_PORT falls inside the data parallel reserved port range
