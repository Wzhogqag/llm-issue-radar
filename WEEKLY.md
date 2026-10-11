# Weekly Trends — 2026-10-11

Window: 2026-10-04 → 2026-10-11 (8 snapshots)

**Totals:** 13 → 24  (24 appeared, 13 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 0 | 1 | +1 | 1 | 0 |
| Build / Install / Platform | 1 | 4 | +3 | 4 | 1 |
| Distributed / TP / PP / EP | 0 | 2 | +2 | 2 | 0 |
| KV Cache / Connector / PD Disagg | 1 | 1 | 0 | 1 | 1 |
| New Model Integration | 0 | 2 | +2 | 2 | 0 |
| Performance / Memory / OOM | 0 | 2 | +2 | 2 | 0 |
| Quantization | 4 | 6 | +2 | 6 | 4 |
| Sampling / Speculative Decoding | 4 | 3 | -1 | 3 | 4 |
| Scheduler / Batching | 2 | 1 | -1 | 1 | 2 |
| Serving / OpenAI API / Streaming | 1 | 0 | -1 | 0 | 1 |
| Uncategorized | 0 | 2 | +2 | 2 | 0 |

## Appeared this week

### Attention Backend

- [Performance] [vllm-project/vllm#61029](https://github.com/vllm-project/vllm/issues/61029) [Performance]: Triton decode with 64-token KV tiles beats FLASH_ATTN at kernel level on H100, but only +2.6% end to end

### Build / Install / Platform

- [Bug] [sgl-project/sglang#43580](https://github.com/sgl-project/sglang/issues/43580) [Bug] PP>1 + DSA skip-topk stage boundary: 'OwedOutput' object has no attribute 'shape' during decode CUDA-graph capture
- [Bug] [sgl-project/sglang#43588](https://github.com/sgl-project/sglang/issues/43588) [Bug] PP>1 (GLM-5.3/DSA): intermittent runtime crash in RotaryEmbedding.forward_cuda — query.view(positions.size(0), -1, head_size) with a shorter positions tensor
- [Bug] [vllm-project/vllm#60977](https://github.com/vllm-project/vllm/issues/60977) [Bug]: EmbeddingGemma 2 rejects dimensions=768 despite returning 768-dimensional embeddings
- [Bug] [vllm-project/vllm#61055](https://github.com/vllm-project/vllm/issues/61055) [Bug][ROCm]: `ENV HSA_ENABLE_IPC_MODE_LEGACY=1` in the ROCm Dockerfiles makes `hipIpcGetMemHandle` fail on in-tree amdgpu kernels

### Distributed / TP / PP / EP

- [no-prefix] [vllm-project/vllm#61049](https://github.com/vllm-project/vllm/issues/61049) Stateless DP group formation (port-pool path): leader silently rebinds the pooled rendezvous port after EADDRINUSE while members retry the stale port for the full timeout
- [Bug] [vllm-project/vllm#61053](https://github.com/vllm-project/vllm/issues/61053) [Bug]: TP ranks can route the same token to different MoE experts because Inductor autotunes the fused add+RMSNorm reduction per rank

### KV Cache / Connector / PD Disagg

- [other] [sgl-project/sglang#43649](https://github.com/sgl-project/sglang/issues/43649) [Roadmap] PD Disaggregation Layerwise KV Transfer

### New Model Integration

- [Feature] [sgl-project/sglang#43671](https://github.com/sgl-project/sglang/issues/43671) [Feature][Diffusion] Add native SANA-Sprint 0.6B support
- [Feature] [vllm-project/vllm#61008](https://github.com/vllm-project/vllm/issues/61008) [Feature]: Add built-in support for TriAttention

### Performance / Memory / OOM

- [Performance] [vllm-project/vllm#60985](https://github.com/vllm-project/vllm/issues/60985) [Performance]: Resize video frames while decoding to skip full-resolution copies
- [Bug] [vllm-project/vllm#61045](https://github.com/vllm-project/vllm/issues/61045) [Bug]: Gemma 4 encoder CUDA graph capture allocates `max_frames_per_batch` full-image rows per budget (38.5 GiB with `--max-num-batched-tokens 4096`) and OOMs

### Quantization

- [Bug] [vllm-project/vllm#61003](https://github.com/vllm-project/vllm/issues/61003) [Bug] DFlash draft model: fp8 `ignored_layers` are not aliased to global layer indices, so excluded bf16 projections are loaded into fp8 parameters (acceptance drops from 4.3 to 1.0)
- [Bug] [vllm-project/vllm#61007](https://github.com/vllm-project/vllm/issues/61007) [Bug]: GB10 (sm_121) engine hangs forever inside a cuDNN FP8 GEMM picked via FlashInferFP8ScaledMMLinearKernel; CutlassFP8ScaledMMLinearKernel avoids it
- [other] [vllm-project/vllm#61024](https://github.com/vllm-project/vllm/issues/61024) [Roadmap] vLLM Roadmap Q4 2026
- [Bug] [vllm-project/vllm#61027](https://github.com/vllm-project/vllm/issues/61027) [Bug]: CPU MXFP4 MoE (gpt-oss) broken on AMD EPYC after AMX gate
- [Performance] [vllm-project/vllm#61030](https://github.com/vllm-project/vllm/issues/61030) [Performance]: LoRA shrink launches empty split-K programs with the default config (split_k=64 > ceil(K/block_k))
- [Bug] [vllm-project/vllm#61069](https://github.com/vllm-project/vllm/issues/61069) [Bug]: GB10 (sm_121), NVFP4 + Marlin MoE + MTP: engine dies daily ~2k sequential short requests into a batch job (Xid 13+31 write to VA 0x0; Xid 13+43 at a fixed address on all SMs)

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#60981](https://github.com/vllm-project/vllm/issues/60981) [Bug]: ngram_gpu crashes with num_speculative_tokens_per_batch_size (assert num_speculative_tokens == self.k)
- [no-prefix] [vllm-project/vllm#60998](https://github.com/vllm-project/vllm/issues/60998) SamplingParams accepts float for int fields (max_tokens/min_tokens/logprobs), then LLM.generate() hangs on an EngineCore msgspec decode error
- [other] [vllm-project/vllm#61072](https://github.com/vllm-project/vllm/issues/61072) [Spec Decode][DFlash2] Every public 27B draft pairing we could construct is a net regression vs full-vocab MTP — pairing validation + last-stage memory asks

### Scheduler / Batching

- [RFC] [vllm-project/vllm#60986](https://github.com/vllm-project/vllm/issues/60986) [RFC]: Scheduler-owned KV transfer obligations: release blocks only after both recv and send complete

### Uncategorized

- [no-prefix] [vllm-project/vllm#60987](https://github.com/vllm-project/vllm/issues/60987) Opt-in request security middleware for the API server (rate limiting, IP lists, payload screening)
- [no-prefix] [vllm-project/vllm#61078](https://github.com/vllm-project/vllm/issues/61078) docs(security): API Key Limitations list is missing /metrics, /kv_event_sources, and /fault_tolerance/* (all unauthenticated)

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [Feature] [sgl-project/sglang#42459](https://github.com/sgl-project/sglang/issues/42459) [Feature] Upgrade Nsight Compute bundled by the CUDA devel base image

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#59956](https://github.com/vllm-project/vllm/issues/59956) [Bug]: NIXL: `remove_remote_agent` does not release UCX endpoints, so each `engine_ttl` eviction + re-handshake leaks until handshakes fail

### Quantization

- [no-prefix] [sgl-project/sglang#42473](https://github.com/sgl-project/sglang/issues/42473) Test issue (deprecated)
- [Feature] [sgl-project/sglang#42511](https://github.com/sgl-project/sglang/issues/42511) [Feature] server-level control over GPU image decoding
- [other] [vllm-project/vllm#59868](https://github.com/vllm-project/vllm/issues/59868) [Qwen4Exp] PLE pinned-host FP8 lookup will not compile on sm_86, so --engram-config cpu_offload is unusable on consumer Ampere
- [Bug] [vllm-project/vllm#59946](https://github.com/vllm-project/vllm/issues/59946) [Bug]: gemma4 loader requires k_proj/v_proj/k_norm for KV-shared layers that transformers 5.5.4 never saves; any transformers-saved gemma4 checkpoint is refused

### Sampling / Speculative Decoding

- [no-prefix] [sgl-project/sglang#42415](https://github.com/sgl-project/sglang/issues/42415) fix(mlx): repeated chat returns unrelated text after native generation
- [Bug] [sgl-project/sglang#42510](https://github.com/sgl-project/sglang/issues/42510) [Bug] EAGLE/MTP same-checkpoint draft keeps redundant embed_tokens/lm_head copies resident during KV pool sizing → under-sized pool, startup OOM
- [Bug] [vllm-project/vllm#59926](https://github.com/vllm-project/vllm/issues/59926) [Bug] DeepSeek-V4-Flash tool-call format failures associated with prefix-cache reuse; worst for short cached head + long uncached suffix; `cache_salt` reduces failures but is confounded with hit shape (v0.27.1, fp8 KV, MTP)
- [Bug] [vllm-project/vllm#59933](https://github.com/vllm-project/vllm/issues/59933) [Bug]: RecoverSSM align mode commits the final SSM state to an unwritten block at exact block boundaries (floor vs ceil-1)

### Scheduler / Batching

- [Bug] [sgl-project/sglang#42508](https://github.com/sgl-project/sglang/issues/42508) [Bug] Scheduler aborts with `double free or corruption` inside the idle-loop invariant check (`session_held_tokens` walk); server hangs permanently afterwards
- [Bug] [vllm-project/vllm#59907](https://github.com/vllm-project/vllm/issues/59907) [Bug]: Priority scheduling can un-schedule a request it already scheduled in the same step (encoder cache miss, prefix hits on unwritten KV, priority inversion)

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#42465](https://github.com/sgl-project/sglang/issues/42465) [Bug] DeepSeek-V4 + HiCache write_through: TP ranks deadlock under concurrent long prefills (scheduler and detokenizer go silent, /health 503)
