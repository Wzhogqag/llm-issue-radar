# LLM Serving Issue Radar

_Last run: 2026-08-11T13:48+00:00_

**26 issues** — sgl-project/sglang: 8, vllm-project/vllm: 18 — 🆕 **26 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 6
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 5
- [Uncategorized](#uncategorized) — 3

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#51786](https://github.com/vllm-project/vllm/issues/51786) [Bug]: [KV-Transfer] Scheduler crashes due to duplicate `recving` completion events in `MultiConnector` across scheduler steps

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#34389](https://github.com/sgl-project/sglang/issues/34389) [Bug] [Diffusion] Attention backend fallback change introduced errors on most models

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#34340](https://github.com/sgl-project/sglang/issues/34340) [Bug] Two SM10x-gated cluster/tcgen05 kernels fail on B300 (sm_103): cutedsl TGV BF16 GEMM raises Xid 13 CGA "CTA Not Present", trtllm-gen MoE finalize hangs silently

### vllm-project/vllm

- [Bug] 🆕 [#51798](https://github.com/vllm-project/vllm/issues/51798) [Bug]: Kimi-K3-NVFP4 on 8xB300 produces degenerate, incoherent output in the reasoning channel on v0.27.0
- [RFC] 🆕 [#51751](https://github.com/vllm-project/vllm/issues/51751) [RFC]: Pluggable KV Cache Data Types

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#51782](https://github.com/vllm-project/vllm/issues/51782) [Bug]: persistent_topk silently drops top-k candidates when many values share a coarse histogram bin
- [Bug] 🆕 [#51752](https://github.com/vllm-project/vllm/issues/51752) [Bug]: Hybrid block-size alignment is skipped on pipeline-parallel ranks that own no attention layer
- [Bug] 🆕 [#51712](https://github.com/vllm-project/vllm/issues/51712) [Bug]: ray DP backend at --data-parallel-size 1 discards the derived DP master IP and falls back to 127.0.0.1

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#34397](https://github.com/sgl-project/sglang/issues/34397) [Feature] support read/write datalake（iceberg、delta lake、paimon、lance）

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#51822](https://github.com/vllm-project/vllm/issues/51822) [Bug]: deepseek-v4-flash-0731 use vllm 0.27.0 run error
- [Bug] 🆕 [#51761](https://github.com/vllm-project/vllm/issues/51761) [Bug][KV Offload] EAGLE volatile-tail boundary can collapse hybrid SWA replay to zero hits
- [Bug] 🆕 [#51743](https://github.com/vllm-project/vllm/issues/51743) [Bug]: DeepSeek-V4-Flash TP on H100: --max-num-batched-tokens >= 24576 crashes EngineCore in fused qnorm/rope/kv-insert op; allocation invisible to memory profiler
- [other] 🆕 [#51737](https://github.com/vllm-project/vllm/issues/51737) [Fix]: MTP speculative decoding crashes with RuntimeError on heterogeneous per-layer head_dim, fixed below and created a PR
- [RFC] 🆕 [#51788](https://github.com/vllm-project/vllm/issues/51788) [RFC]: Suffix decoding on GPU (`suffix_gpu`) under async scheduling, and variable draft-length scheduling for GPU-state drafters
- [no-prefix] 🆕 ⚠no-prefix [#51771](https://github.com/vllm-project/vllm/issues/51771) EAGLE/MTP block drop + prefix caching is untested for hybrid models with ≥3 attention groups (DeepSeek-V4-Flash + DSpark lands there)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#51762](https://github.com/vllm-project/vllm/issues/51762) [Bug][KV Offload] cudaHostRegister can leave mixed pinned/unpinned TP ranks

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#34384](https://github.com/sgl-project/sglang/issues/34384) [Bug] DSpark compact ragged CUDA Graph uses incompatible request-slot geometry for the same token tier

### vllm-project/vllm

- [Bug] 🆕 [#51799](https://github.com/vllm-project/vllm/issues/51799) [Bug]: DeepSeek-V4-Flash-0731 shows severe 1M KV concurrency regression on B300 (27.08x preview vs 7.73x 0731 + DSpark)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#34367](https://github.com/sgl-project/sglang/issues/34367) [Bug][diffusion] LongLive2 `longlive2_i2v` aborts: num_frames not divisible by num_frames_per_block (causal DMD)
- [Bug] 🆕 [#34366](https://github.com/sgl-project/sglang/issues/34366) [Bug][diffusion] JoyAI-Image-Edit fails at ImageEncodingStage: Qwen3-VL text encoder missing `mm_token_type_ids`

### vllm-project/vllm

- [Bug] 🆕 [#51776](https://github.com/vllm-project/vllm/issues/51776) [Bug]: CuTe FA4 forward (flash_fwd.py SM80/SM120) fails on first call: NameError 'mDynamicCausal' and missing self.is_split_kv
- [Bug] 🆕 [#51758](https://github.com/vllm-project/vllm/issues/51758) [Bug]: upgrade vllm from 0.26.0 to 0.27.0 run deepseek v4 flash error
- [Bug] 🆕 [#51744](https://github.com/vllm-project/vllm/issues/51744) [Bug]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#34419](https://github.com/sgl-project/sglang/issues/34419) [Bug] [Security tracking] Private advisory GHSA-8374-wrr5-7q7f has received no maintainer response
- [Bug] 🆕 [#34354](https://github.com/sgl-project/sglang/issues/34354) [Bug] 请问sglang的语义上 sliding_window_size 到底包不包含当前的token呢？

### vllm-project/vllm

- [Performance] 🆕 [#51791](https://github.com/vllm-project/vllm/issues/51791) [Performance][EPLB] Skip unchanged layers in async transfer cycles
