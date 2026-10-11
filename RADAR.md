# LLM Serving Issue Radar

_Last run: 2026-10-11T13:29+00:00_

**24 issues** — sgl-project/sglang: 4, vllm-project/vllm: 20 — 🆕 **21 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 4
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### vllm-project/vllm

- [RFC] [#60986](https://github.com/vllm-project/vllm/issues/60986) [RFC]: Scheduler-owned KV transfer obligations: release blocks only after both recv and send complete

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 [#43649](https://github.com/sgl-project/sglang/issues/43649) [Roadmap] PD Disaggregation Layerwise KV Transfer

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#61029](https://github.com/vllm-project/vllm/issues/61029) [Performance]: Triton decode with 64-token KV tiles beats FLASH_ATTN at kernel level on H100, but only +2.6% end to end

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#61069](https://github.com/vllm-project/vllm/issues/61069) [Bug]: GB10 (sm_121), NVFP4 + Marlin MoE + MTP: engine dies daily ~2k sequential short requests into a batch job (Xid 13+31 write to VA 0x0; Xid 13+43 at a fixed address on all SMs)
- [Performance] 🆕 [#61030](https://github.com/vllm-project/vllm/issues/61030) [Performance]: LoRA shrink launches empty split-K programs with the default config (split_k=64 > ceil(K/block_k))
- [Bug] 🆕 [#61027](https://github.com/vllm-project/vllm/issues/61027) [Bug]: CPU MXFP4 MoE (gpt-oss) broken on AMD EPYC after AMX gate 
- [Bug] 🆕 [#61007](https://github.com/vllm-project/vllm/issues/61007) [Bug]: GB10 (sm_121) engine hangs forever inside a cuDNN FP8 GEMM picked via FlashInferFP8ScaledMMLinearKernel; CutlassFP8ScaledMMLinearKernel avoids it
- [Bug] 🆕 [#61003](https://github.com/vllm-project/vllm/issues/61003) [Bug] DFlash draft model: fp8 `ignored_layers` are not aliased to global layer indices, so excluded bf16 projections are loaded into fp8 parameters (acceptance drops from 4.3 to 1.0)
- [other] 🆕 ⚠maintainer-authored [#61024](https://github.com/vllm-project/vllm/issues/61024) [Roadmap] vLLM Roadmap Q4 2026

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#61053](https://github.com/vllm-project/vllm/issues/61053) [Bug]: TP ranks can route the same token to different MoE experts because Inductor autotunes the fused add+RMSNorm reduction per rank
- [no-prefix] 🆕 ⚠no-prefix [#61049](https://github.com/vllm-project/vllm/issues/61049) Stateless DP group formation (port-pool path): leader silently rebinds the pooled rendezvous port after EADDRINUSE while members retry the stale port for the full timeout

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#43671](https://github.com/sgl-project/sglang/issues/43671) [Feature][Diffusion] Add native SANA-Sprint 0.6B support

### vllm-project/vllm

- [Feature] 🆕 [#61008](https://github.com/vllm-project/vllm/issues/61008) [Feature]: Add built-in support for TriAttention

## Sampling / Speculative Decoding

### vllm-project/vllm

- [other] 🆕 [#61072](https://github.com/vllm-project/vllm/issues/61072) [Spec Decode][DFlash2] Every public 27B draft pairing we could construct is a net regression vs full-vocab MTP — pairing validation + last-stage memory asks
- [no-prefix] 🆕 ⚠no-prefix [#60998](https://github.com/vllm-project/vllm/issues/60998) SamplingParams accepts float for int fields (max_tokens/min_tokens/logprobs), then LLM.generate() hangs on an EngineCore msgspec decode error
- [Bug] [#60981](https://github.com/vllm-project/vllm/issues/60981) [Bug]: ngram_gpu crashes with num_speculative_tokens_per_batch_size (assert num_speculative_tokens == self.k)

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#61045](https://github.com/vllm-project/vllm/issues/61045) [Bug]: Gemma 4 encoder CUDA graph capture allocates `max_frames_per_batch` full-image rows per budget (38.5 GiB with `--max-num-batched-tokens 4096`) and OOMs
- [Performance] [#60985](https://github.com/vllm-project/vllm/issues/60985) [Performance]: Resize video frames while decoding to skip full-resolution copies

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#43588](https://github.com/sgl-project/sglang/issues/43588) [Bug] PP>1 (GLM-5.3/DSA): intermittent runtime crash in RotaryEmbedding.forward_cuda — query.view(positions.size(0), -1, head_size) with a shorter positions tensor
- [Bug] 🆕 [#43580](https://github.com/sgl-project/sglang/issues/43580) [Bug] PP>1 + DSA skip-topk stage boundary: 'OwedOutput' object has no attribute 'shape' during decode CUDA-graph capture

### vllm-project/vllm

- [Bug] 🆕 [#61055](https://github.com/vllm-project/vllm/issues/61055) [Bug][ROCm]: `ENV HSA_ENABLE_IPC_MODE_LEGACY=1` in the ROCm Dockerfiles makes `hipIpcGetMemHandle` fail on in-tree amdgpu kernels
- [Bug] 🆕 [#60977](https://github.com/vllm-project/vllm/issues/60977) [Bug]: EmbeddingGemma 2 rejects dimensions=768 despite returning 768-dimensional embeddings

## Uncategorized

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#61078](https://github.com/vllm-project/vllm/issues/61078) docs(security): API Key Limitations list is missing /metrics, /kv_event_sources, and /fault_tolerance/* (all unauthenticated)
- [no-prefix] 🆕 ⚠no-prefix [#60987](https://github.com/vllm-project/vllm/issues/60987) Opt-in request security middleware for the API server (rate limiting, IP lists, payload screening)
