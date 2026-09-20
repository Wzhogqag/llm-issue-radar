# Weekly Trends — 2026-09-20

Window: 2026-09-14 → 2026-09-20 (7 snapshots)

**Totals:** 27 → 19  (19 appeared, 27 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 3 | 1 | -2 | 1 | 3 |
| Build / Install / Platform | 4 | 3 | -1 | 3 | 4 |
| KV Cache / Connector / PD Disagg | 3 | 2 | -1 | 2 | 3 |
| New Model Integration | 1 | 0 | -1 | 0 | 1 |
| Performance / Memory / OOM | 2 | 0 | -2 | 0 | 2 |
| Quantization | 8 | 5 | -3 | 5 | 8 |
| Sampling / Speculative Decoding | 2 | 2 | 0 | 2 | 2 |
| Scheduler / Batching | 3 | 2 | -1 | 2 | 3 |
| Serving / OpenAI API / Streaming | 1 | 4 | +3 | 4 | 1 |

## Appeared this week

### Attention Backend

- [Feature] [vllm-project/vllm#57712](https://github.com/vllm-project/vllm/issues/57712) [Feature]: OutOfResources: shared memory (98304 > 65536) on Turing (SM75) — global attention layers with head_dim=512

### Build / Install / Platform

- [other] [vllm-project/vllm#57684](https://github.com/vllm-project/vllm/issues/57684) [Question] Support path for platform plugins that cannot install Triton (MRV2 requires it)
- [Bug] [vllm-project/vllm#57714](https://github.com/vllm-project/vllm/issues/57714) [Bug][Reasoning] kimi_k3: structured output never engages when the completion skips the think channel
- [Bug] [vllm-project/vllm#57727](https://github.com/vllm-project/vllm/issues/57727) [Bug]: `POST /reset_prefix_cache` returns success while the CPU offload tier keeps serving the same blocks

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#40360](https://github.com/sgl-project/sglang/issues/40360) [Bug] Abort cleanup hook has no well-defined ordering vs. cache_finished_req: FlexKV needs it before, LMCache needs it after (session leak)
- [Bug] [vllm-project/vllm#57716](https://github.com/vllm-project/vllm/issues/57716) [Bug] Kimi-K3 TP8xPP2 + DSpark spec-on: mid-decode target-forward NaN detonates MLA decode under concurrency (fp8 latent-cache bytes carry the corruption)

### Quantization

- [no-prefix] [sgl-project/sglang#40432](https://github.com/sgl-project/sglang/issues/40432) 4*5090 run nvidia/Qwen3.8-Flash-Next-NVFP4
- [Feature] [sgl-project/sglang#40437](https://github.com/sgl-project/sglang/issues/40437) [Feature][weight-cache] Support DeepSeek-V4-Flash MXFP4 IPC loading
- [Bug] [vllm-project/vllm#57713](https://github.com/vllm-project/vllm/issues/57713) [Bug]: GLM5.3-Flash does not support fp8 kv cache dtype on hopper
- [Bug] [vllm-project/vllm#57748](https://github.com/vllm-project/vllm/issues/57748) [Bug]: Running GLM-5.3-Flash-NVFP4 on Hopper GPUs
- [Feature] [vllm-project/vllm#57772](https://github.com/vllm-project/vllm/issues/57772) [Feature]: mega-MoE expert path for SM90 (H100/H20) DeepSeek-V4 / V4.1-Flash — Marlin weight-only is the only option today

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#57720](https://github.com/vllm-project/vllm/issues/57720) [Bug]: Mamba-hybrid models (granite-4.0-h) give a different, garbled greedy answer every time for a ONE-token prompt under full CUDA graphs
- [no-prefix] [vllm-project/vllm#57755](https://github.com/vllm-project/vllm/issues/57755) Title

### Scheduler / Batching

- [Bug] [vllm-project/vllm#57691](https://github.com/vllm-project/vllm/issues/57691) [Bug]: Task cancellation during _commit_scale_down_elastic_ep corrupts cluster state without rollback
- [RFC] [vllm-project/vllm#57738](https://github.com/vllm-project/vllm/issues/57738) [RFC]: Encoder-Only Prefill in P/D deployment for DeepSeek V4.1 Flash

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#40417](https://github.com/sgl-project/sglang/issues/40417) [Bug] humming MoE runner picks tuning config with a 4x-inflated shape under EP, and the obvious EP-aware fix regresses serving
- [Bug] [vllm-project/vllm#57688](https://github.com/vllm-project/vllm/issues/57688) [Bug][Reasoning] kimi_k3: streaming path classifies a response-only completion as reasoning (diverges from non-streaming after #57098)
- [Bug] [vllm-project/vllm#57699](https://github.com/vllm-project/vllm/issues/57699) [Bug]: qwen3_coder tool parser drops the last parameter when the model omits </parameter> before </function> (non-streaming {}, streaming unterminated JSON)
- [Bug] [vllm-project/vllm#57730](https://github.com/vllm-project/vllm/issues/57730) [Bug]: /tokenize returns 400 "cannot pickle ValidatorIterator" for assistant `content: null` + `tool_calls` (DeepSeek-V4.1), while chat completions accepts the same messages

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#56771](https://github.com/vllm-project/vllm/issues/56771) [Bug]: DeepSeek-V4.1-Flash + DSpark speculative decoding — illegal memory access in SM120 sparse-MLA prefill on long prompts
- [Bug] [vllm-project/vllm#56785](https://github.com/vllm-project/vllm/issues/56785) [Bug]: HiSparse MLA indexer crashes with CUDA error: invalid argument during piecewise cudagraph capture - logical_topk_ready is recorded inside the capture segment but waited on after eager_break_during_capture ends capture
- [Bug] [vllm-project/vllm#56837](https://github.com/vllm-project/vllm/issues/56837) [Bug] DeepSeek-V4.1 on sm_120 (RTX PRO 2000 Blackwell): no FlashInfer SM120 sparse-MLA kernel for (num_heads=64, topk=1152); FlashMLA sparse is SM90a/SM100f only

### Build / Install / Platform

- [no-prefix] [sgl-project/sglang#39343](https://github.com/sgl-project/sglang/issues/39343) 按照指导操作后，A5仍然无法拉起dsv4.1，报错如下：ValueError: The checkpoint you are trying to load has model type deepseek_v41 but Transformers does not recognize this architecture.
- [Bug] [vllm-project/vllm#56787](https://github.com/vllm-project/vllm/issues/56787) [Bug]: DFlash2 draft model fails torch.compile on XPU — dynamic-shape stride assert in custom-op fake kernel (workaround: disable compile on draft class)
- [Bug] [vllm-project/vllm#56815](https://github.com/vllm-project/vllm/issues/56815) [Bug]: Engram async prefetch (#56512) reintroduces silent ctx-load decode flake on single-GPU Qwen4Exp PLE CPU-offload (nightlies past 2026-09-13)
- [Bug] [vllm-project/vllm#56830](https://github.com/vllm-project/vllm/issues/56830) [Bug]: Startup memory-profiling assertion aborts whenever free memory grows, contradicting documented support for GPU co-tenancy

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#39302](https://github.com/sgl-project/sglang/issues/39302) [Bug] GLM-5.x NoPE MLA (qk_rope_head_dim=0) cannot run on SM120: every DSA sparse-MLA backend is unavailable
- [Feature] [sgl-project/sglang#39355](https://github.com/sgl-project/sglang/issues/39355) [Feature] [NPU] Add ScatterPaKvCache as an optional KV-cache write backend
- [other] [vllm-project/vllm#56772](https://github.com/vllm-project/vllm/issues/56772) [KV Connector][Offloading] Canonical MLA+DSA secondary transfers use TP-dependent row sizes

### New Model Integration

- [no-prefix] [vllm-project/vllm#56792](https://github.com/vllm-project/vllm/issues/56792) DSpark checkpoints exported in fill-in (DFlash 1+N) layout silently serve with <1% acceptance: the optional layout flag is absent from their configs, and the default anchor-first sampler is wrong for them

### Performance / Memory / OOM

- [Bug] [sgl-project/sglang#39412](https://github.com/sgl-project/sglang/issues/39412) [Bug] pd bootstrap params silently dropped on rust frontend openai endpoints
- [Bug] [vllm-project/vllm#56828](https://github.com/vllm-project/vllm/issues/56828) [Bug][KV Offload][P2P] Peer-down on one rank does not fail loads or block new loads to sibling ranks of the same source

### Quantization

- [other] [sgl-project/sglang#39393](https://github.com/sgl-project/sglang/issues/39393) [Feature Request] Add pipeline-parallel support to Qwen4-Exp (`qwen4_exp.py`) — four gaps, working reference patches, and an undocumented mHC PP-boundary contract
- [RFC] [vllm-project/vllm#56727](https://github.com/vllm-project/vllm/issues/56727) [RFC] Separate CLI input definitions from runtime configuration
- [Bug] [vllm-project/vllm#56759](https://github.com/vllm-project/vllm/issues/56759) [Bug]: Humming MoE permute scratch memory scales with number of MoE layers
- [Bug] [vllm-project/vllm#56769](https://github.com/vllm-project/vllm/issues/56769) [Bug] Greedy LoRA decode nondeterministic on Qwen3.8-27B-FP8 (rank-64 Unsloth, linear_attn modules)
- [Bug] [vllm-project/vllm#56770](https://github.com/vllm-project/vllm/issues/56770) [Bug]: compressed-tensors MXFP4 W4A16 is misclassified as W4A4 and dispatched to W4A4 kernel on SM100+
- [Bug] [vllm-project/vllm#56824](https://github.com/vllm-project/vllm/issues/56824) [Bug]: Engine startup on DGX Spark (GB10, unified memory) collapses host memory — NV_ERR_NO_MEMORY while MemAvailable reports ~22 GiB
- [Bug] [vllm-project/vllm#56829](https://github.com/vllm-project/vllm/issues/56829) [Bug]: cu129-nightly image ships torch 2.14.0+cu130 with cu129 torchvision/torchaudio, vllm serve dies on 'operator torchvision::nms does not exist'
- [Bug] [vllm-project/vllm#56832](https://github.com/vllm-project/vllm/issues/56832) [Bug]: --moe-backend marlin is applied to the unquantized MTP draft MoE and aborts (Qwen3.8-Flash-Next NVFP4 + speculative mtp)

### Sampling / Speculative Decoding

- [no-prefix] [vllm-project/vllm#56736](https://github.com/vllm-project/vllm/issues/56736) hybrid Mamba/GDN + speculative decoding: Xid 31 in the align mamba path (fault address below the CUDA segment)
- [Perf] [vllm-project/vllm#56797](https://github.com/vllm-project/vllm/issues/56797) [Perf][Spec Decode] DeepSeek-V4.1-Flash DSpark mean acceptance length only 2.82 on GSM8K (k=5, 2×8 H20)

### Scheduler / Batching

- [Feature] [sgl-project/sglang#39348](https://github.com/sgl-project/sglang/issues/39348) [Feature] [NPU] Add topology-aware CPU and NUMA affinity for Ascend worker ranks
- [Feature] [vllm-project/vllm#56767](https://github.com/vllm-project/vllm/issues/56767) [Feature]: Compact LM Head fast path for fixed-candidate-set scoring (rerankers / relevance scoring)
- [Bug] [vllm-project/vllm#56795](https://github.com/vllm-project/vllm/issues/56795) [Bug]: Native KV offload advances next_stored_block_idx for every KV group when no keys were stored

### Serving / OpenAI API / Streaming

- [RFC] [vllm-project/vllm#56745](https://github.com/vllm-project/vllm/issues/56745) [RFC]: Return `routed_experts` on the terminal streaming chunk
