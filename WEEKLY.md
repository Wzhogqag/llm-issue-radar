# Weekly Trends — 2026-07-26

Window: 2026-07-20 → 2026-07-26 (7 snapshots)

**Totals:** 24 → 24  (24 appeared, 24 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 0 | 2 | +2 | 2 | 0 |
| Build / Install / Platform | 5 | 2 | -3 | 2 | 5 |
| Distributed / TP / PP / EP | 2 | 1 | -1 | 1 | 2 |
| KV Cache / Connector / PD Disagg | 2 | 2 | 0 | 2 | 2 |
| New Model Integration | 0 | 2 | +2 | 2 | 0 |
| Performance / Memory / OOM | 1 | 1 | 0 | 1 | 1 |
| Quantization | 6 | 5 | -1 | 5 | 6 |
| Sampling / Speculative Decoding | 3 | 2 | -1 | 2 | 3 |
| Scheduler / Batching | 2 | 3 | +1 | 3 | 2 |
| Serving / OpenAI API / Streaming | 3 | 2 | -1 | 2 | 3 |
| Uncategorized | 0 | 2 | +2 | 2 | 0 |

## Appeared this week

### Attention Backend

- [Bug] [vllm-project/vllm#49810](https://github.com/vllm-project/vllm/issues/49810) [Bug]: PCP (#46570) broken for non-compress models (GLM-5.2, compress_ratio=1) — multiple crash paths
- [Bug] [vllm-project/vllm#49851](https://github.com/vllm-project/vllm/issues/49851) [Bug]: Multimodal models fail to load on ROCm/RDNA4 (gfx1201) — `CUDA error: invalid argument` in `vit_torch_sdpa_wrapper` encoder attention

### Build / Install / Platform

- [Bug] [vllm-project/vllm#49778](https://github.com/vllm-project/vllm/issues/49778) [Bug]: gpt-oss-120b fails for ROCm on gfx950 with Triton 3.7.1
- [Bug] [vllm-project/vllm#49878](https://github.com/vllm-project/vllm/issues/49878) [Bug]: Dramatic KV cache size increase (~40%) for Gemma4 from v0.25.1 to v0.26

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#49826](https://github.com/vllm-project/vllm/issues/49826) [Bug]: Cross-node Pipeline Parallelism (PP) fails with "invalid device ordinal" at PyNccl warmup on ROCm (AMD RDNA4 / R9700), reproducible on first inference even after context-corruption workaround

### KV Cache / Connector / PD Disagg

- [Feature] [sgl-project/sglang#32309](https://github.com/sgl-project/sglang/issues/32309) [Feature] --enable-dsa-cache-layer-split support single deploy
- [RFC] [sgl-project/sglang#32321](https://github.com/sgl-project/sglang/issues/32321) [RFC] Make BaseTpWorker the explicit framework-to-backend boundary - MLX runner-stub redesign

### New Model Integration

- [RFC] [vllm-project/vllm#49752](https://github.com/vllm-project/vllm/issues/49752) [RFC]: vLLM Agentic Coding Readiness Survey
- [Feature] [vllm-project/vllm#49816](https://github.com/vllm-project/vllm/issues/49816) [Feature]: per gpu gpu-memory-utilization

### Performance / Memory / OOM

- [RFC] [sgl-project/sglang#32432](https://github.com/sgl-project/sglang/issues/32432) [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for Dynamic CUDA Graph Replay

### Quantization

- [Bug] [sgl-project/sglang#32311](https://github.com/sgl-project/sglang/issues/32311) [Bug] deepseek v4 flash hang on 4rtx 6000 pro with limited host ram
- [Bug] [sgl-project/sglang#32378](https://github.com/sgl-project/sglang/issues/32378) [Bug] mooncake with sglang:dev with glm-5.2-w4afp8 with pd error
- [Bug] [sgl-project/sglang#32426](https://github.com/sgl-project/sglang/issues/32426) [Bug] In version v0.5.16, the sakamakismile/Ornith-1.0-35B-NVFP4 model generates garbled characters.
- [Bug] [vllm-project/vllm#49783](https://github.com/vllm-project/vllm/issues/49783) [Bug]: DeepGEMM 2.6.x UE8M0 assert - vLLM passes uninitialized FP32 scale-factor padding to the packing kernel
- [Bug] [vllm-project/vllm#49844](https://github.com/vllm-project/vllm/issues/49844) [Bug]: PP=2 + GlmMoeDsa: inductor compile combined with CUDA-graph capture produces garbage output; either alone is clean (v0.24 & v0.26)

### Sampling / Speculative Decoding

- [Feature] [vllm-project/vllm#49848](https://github.com/vllm-project/vllm/issues/49848) [Feature]: MTP speculative decoding under pipeline parallelism — one real blocker (PP+async single-token assumption), everything else is guards
- [Bug] [vllm-project/vllm#49874](https://github.com/vllm-project/vllm/issues/49874) [Bug]: vllm+tilert+glm-5.1 error

### Scheduler / Batching

- [Bug] [sgl-project/sglang#32356](https://github.com/sgl-project/sglang/issues/32356) [Bug] DeepSeek-V4 DSpark TP=8 can permanently stall under HiCache long-prefix load
- [no-prefix] [sgl-project/sglang#32433](https://github.com/sgl-project/sglang/issues/32433) Question: unit mismatch in evict_from_tree_cache for SWATokenToKVPoolAllocator?
- [Bug] [vllm-project/vllm#49809](https://github.com/vllm-project/vllm/issues/49809) [Bug][KV Offload][P2P] EngineCore crash reconnecting to peer: stale dead ZmqConnection remains registered

### Serving / OpenAI API / Streaming

- [Feature] [sgl-project/sglang#32312](https://github.com/sgl-project/sglang/issues/32312) [Feature] [Kernel] cursor warp decode kernel for low latency small batch MOE inference
- [RFC] [vllm-project/vllm#49765](https://github.com/vllm-project/vllm/issues/49765) [RFC]: Native Disaggregated Pull-Based Queue Worker Interface and Heuristic Pull Router

### Uncategorized

- [no-prefix] [sgl-project/sglang#32355](https://github.com/sgl-project/sglang/issues/32355) Add REFUTE scientific critique + calibration benchmark
- [no-prefix] [vllm-project/vllm#49769](https://github.com/vllm-project/vllm/issues/49769) Add REFUTE scientific critique + calibration benchmark

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [no-prefix] [sgl-project/sglang#31763](https://github.com/sgl-project/sglang/issues/31763) How should I configure the service to make the model return tool calls that comply with the OpenAI standard instead of XML format?
- [Bug] [vllm-project/vllm#49106](https://github.com/vllm-project/vllm/issues/49106) [Bug]: False positive warning "Unexpected gate/up projection names" for non-gated MoE (Nemotron 3 Ultra / Nemotron H)
- [Bug] [vllm-project/vllm#49122](https://github.com/vllm-project/vllm/issues/49122) [Bug]: AriaForConditionalGeneration produces incoherent garbage output at tensor-parallel size > 1 (reproduces on CPU, no GPU/accelerator needed)
- [Bug] [vllm-project/vllm#49141](https://github.com/vllm-project/vllm/issues/49141) [Bug]: Fused_moe dimension mismatch for Qwen mxfp4 model on ROCM
- [Bug] [vllm-project/vllm#49203](https://github.com/vllm-project/vllm/issues/49203) [Bug]: Qwen3.6-35B-A3B (GDN hybrid) intermittently livelocks under load on GB10/SM121 — GPU 96% util, 0 tok/s, no crash, no Xid

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#49101](https://github.com/vllm-project/vllm/issues/49101) [Bug]: Failed: Cuda error /workspace/csrc/custom_all_reduce.cuh:455 'invalid argument'
- [Bug] [vllm-project/vllm#49105](https://github.com/vllm-project/vllm/issues/49105) [Bug]: inkling bf16 h20*2 start failed with vllm/vllm-openai:inkling

### KV Cache / Connector / PD Disagg

- [RFC] [sgl-project/sglang#31774](https://github.com/sgl-project/sglang/issues/31774) [RFC] Backend, KV dtype and platform compatibility is checked case by case, and the responses are inconsistent
- [Bug] [vllm-project/vllm#49125](https://github.com/vllm-project/vllm/issues/49125) [Bug]: Stale partial prefix-cache hash resurrected into the cache after full-block promotion

### Performance / Memory / OOM

- [Bug] [vllm-project/vllm#49182](https://github.com/vllm-project/vllm/issues/49182) [Bug]: vLLM serving Qwen3.6-27B with multimodal inputs causes InternalServerError due to CUDA OOM despite sufficient GPU memory

### Quantization

- [Bug] [sgl-project/sglang#31720](https://github.com/sgl-project/sglang/issues/31720) [Bug] Qwen3.6-27B (hybrid GDN) + AWQ degenerates on few-shot / multi-turn prompts at temperature 0; same checkpoint is clean on vLLM
- [Bug] [sgl-project/sglang#31740](https://github.com/sgl-project/sglang/issues/31740) [Bug] Error in starting kimi-k2.6 nvfp4 model in release v0.5.15: CUBLAS_STATUS_EXECUTION_FAILED.
- [other] [sgl-project/sglang#31783](https://github.com/sgl-project/sglang/issues/31783) [Roadmap] Quantization 2026 H2
- [Bug] [vllm-project/vllm#49165](https://github.com/vllm-project/vllm/issues/49165) [Bug] Deepseek-V4-Pro corruption: H100 multi-rank startup can select a FlashInfer block-FP8 path with a cold JIT cache race
- [Feature] [vllm-project/vllm#49198](https://github.com/vllm-project/vllm/issues/49198) [Feature]: Recency-based progressive mixed-precision KV cache
- [Bug] [vllm-project/vllm#49200](https://github.com/vllm-project/vllm/issues/49200) [Bug]: Kimi-K2.5 (compressed-tensors/int4) crashes with `ValueError: Mismatched mO.strides[0]` in FA4 CuTe MLA prefill context-chunk on Blackwell (long context)

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#31766](https://github.com/sgl-project/sglang/issues/31766) [Bug] fd exhaustion on the prefill side
- [Bug] [vllm-project/vllm#49112](https://github.com/vllm-project/vllm/issues/49112) [Bug]: Speculative decoding with a hybrid draft model (LFM2/LFM2.5 short_conv) fails — drafter requires all draft layers in one KV cache group
- [Bug] [vllm-project/vllm#49197](https://github.com/vllm-project/vllm/issues/49197) [Bug]: Beam Search is slower by a factor of 1000

### Scheduler / Batching

- [RFC] [sgl-project/sglang#31779](https://github.com/sgl-project/sglang/issues/31779) [RFC] An NPU-Native, Sparsity-Driven KV Offloading SubSystem for Efficient LLM Decoding
- [Bug] [vllm-project/vllm#49097](https://github.com/vllm-project/vllm/issues/49097) [Bug]: PRIORITY scheduling can silently skip a running request for a full step when the preemption victim was already deferred earlier in the same schedule() call

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#49103](https://github.com/vllm-project/vllm/issues/49103) [Bug]: Latest vllm is incompatible with `openai<2.25.0`
- [Bug] [vllm-project/vllm#49116](https://github.com/vllm-project/vllm/issues/49116) [Bug]: Transcription streaming uses Chat Completions SSE format instead of OpenAI transcript events
- [Bug] [vllm-project/vllm#49205](https://github.com/vllm-project/vllm/issues/49205) [Bug]: StreamingParserEngine leaks a bare tag fragment (e.g. '<tool_') into content when a PreLexedTerminal supersedes a buffered text-token prefix of the same tag
