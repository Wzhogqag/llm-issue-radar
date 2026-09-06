# Weekly Trends — 2026-09-06

Window: 2026-08-31 → 2026-09-06 (7 snapshots)

**Totals:** 22 → 29  (29 appeared, 22 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 3 | +2 | 3 | 1 |
| Build / Install / Platform | 8 | 4 | -4 | 4 | 8 |
| Distributed / TP / PP / EP | 1 | 2 | +1 | 2 | 1 |
| KV Cache / Connector / PD Disagg | 1 | 3 | +2 | 3 | 1 |
| New Model Integration | 1 | 1 | 0 | 1 | 1 |
| Performance / Memory / OOM | 0 | 1 | +1 | 1 | 0 |
| Quantization | 4 | 9 | +5 | 9 | 4 |
| Sampling / Speculative Decoding | 4 | 3 | -1 | 3 | 4 |
| Scheduler / Batching | 0 | 1 | +1 | 1 | 0 |
| Serving / OpenAI API / Streaming | 1 | 2 | +1 | 2 | 1 |
| Uncategorized | 1 | 0 | -1 | 0 | 1 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#38196](https://github.com/sgl-project/sglang/issues/38196) [Bug] [NPU] ascend attention backend silently corrupts output with page_size 16 (128 OK, 1 rejected per #25169)
- [Bug] [vllm-project/vllm#55526](https://github.com/vllm-project/vllm/issues/55526) [Bug]: DeepSeek-V4-Flash TP=16 on SM120 (RTX 5090 x16, ray multi-node) fails: DSV4 sparse MLA decode specialization error for (num_q_heads=8, top_k=128) despite FlashInfer dispatch table containing that config
- [Bug] [vllm-project/vllm#55568](https://github.com/vllm-project/vllm/issues/55568) [Bug]: [Portability][MSVC] Preprocessor directives inside BOOL_SWITCH macro arguments fail to compile

### Build / Install / Platform

- [Bug] [vllm-project/vllm#55502](https://github.com/vllm-project/vllm/issues/55502) [Bug]: /rerank keeps processing queued documents after the client disconnects, despite @with_cancellation
- [Bug] [vllm-project/vllm#55515](https://github.com/vllm-project/vllm/issues/55515) [Bug]: Qwen4Exp N-gram PLE embedding requires pipeline_parallel_size=1 because non-first pipeline ranks do not receive the raw input_ids it needs. Please run with PP=1
- [Bug] [vllm-project/vllm#55552](https://github.com/vllm-project/vllm/issues/55552) [Bug]: tool_choice="required" not enforced with Qwen3.8-Flash-Next when enable_thinking=false (streaming); xgrammar "Failed to advance FSM" / "matcher has terminated" with thinking on + MTP
- [Bug] [vllm-project/vllm#55555](https://github.com/vllm-project/vllm/issues/55555) [Bug]: multimodal LoRA/tower connector with float16 dtype reaches torch.empty(None)

### Distributed / TP / PP / EP

- [RFC] [vllm-project/vllm#55487](https://github.com/vllm-project/vllm/issues/55487) [RFC] Publish typed extra_keys in BlockStored KV events
- [Bug] [vllm-project/vllm#55517](https://github.com/vllm-project/vllm/issues/55517) [Bug]: qwen3.8-flash-next: assert numerator % denominator == 0, "{} is not divisible by {}".format

### KV Cache / Connector / PD Disagg

- [Performance] [sgl-project/sglang#38206](https://github.com/sgl-project/sglang/issues/38206) [Performance][PP/PD] Bootstrap admission waits ~7.8s for consensus under PP16 concurrent prefill
- [Bug] [sgl-project/sglang#38207](https://github.com/sgl-project/sglang/issues/38207) [Bug] GLM-5.3 DPC crashes
- [Bug] [vllm-project/vllm#55509](https://github.com/vllm-project/vllm/issues/55509) [Bug]: --attention-backend FLASHINFER fails the startup KV-cache check at a max-model-len that FLASH_ATTN serves; the message never names the backend

### New Model Integration

- [Feature] [vllm-project/vllm#55501](https://github.com/vllm-project/vllm/issues/55501) [Feature]: Warn or auto-select the shipped score template when serving an original Qwen3-Reranker without --chat-template

### Performance / Memory / OOM

- [Bug] [vllm-project/vllm#55561](https://github.com/vllm-project/vllm/issues/55561) [Bug]: Sweep Pareto plots include dominated throughput ties

### Quantization

- [Bug] [sgl-project/sglang#38143](https://github.com/sgl-project/sglang/issues/38143) [Bug] MiniMax-M3 W4A16 (compressed-tensors) on 2x DGX Spark (sm_121, TP=2): serves but every token is id 0 — all-NUL output on the Triton MiniMaxSparse path; same weights correct on vLLM
- [Bug] [vllm-project/vllm#55486](https://github.com/vllm-project/vllm/issues/55486) [Bug]: vLLM 0.28.0 — DeepSeek V4 on B200 (TP8+EP, fp8 KV, FULL_AND_PIECEWISE) generates only BOS tokens with V2 model runner default
- [Bug] [vllm-project/vllm#55495](https://github.com/vllm-project/vllm/issues/55495) [Bug]: qwen3_xml tool parser emits a truncated `arguments` string with a leaked `</parameter` tag; the Responses API then rejects every later request of the conversation with `400 Expecting value`
- [Bug] [vllm-project/vllm#55496](https://github.com/vllm-project/vllm/issues/55496) [Bug]: ModelOpt MIXED_PRECISION cannot load FP8_BLOCK_SCALES MTP experts (nvidia/Qwen3.8-Flash-Next-NVFP4 + MTP)
- [Bug] [vllm-project/vllm#55510](https://github.com/vllm-project/vllm/issues/55510) [Bug]: EngineCore and TP workers survive a SIGKILLed API server, keep the GPUs, and reparent to the launching process
- [other] [vllm-project/vllm#55512](https://github.com/vllm-project/vllm/issues/55512) [New Model]: K2-Horizon-MoVA (MoVA attention) — single-GPU Int4 via out-of-tree plugin; native support?
- [Bug] [vllm-project/vllm#55541](https://github.com/vllm-project/vllm/issues/55541) [Bug]: GLM-5.3-Flash with forced tool_choice (named function) fails to converge — runs to max_tokens and returns   ▎ truncated tool_call.arguments
- [Bug] [vllm-project/vllm#55560](https://github.com/vllm-project/vllm/issues/55560) [Bug]: CPU WNA16 GPTQ-Int4 MoE kernel (CPUExpertsInt4) produces NaN logits under torch.compile — fixed by --enforce-eager
- [Bug] [vllm-project/vllm#55571](https://github.com/vllm-project/vllm/issues/55571) [Bug]: Xid 13 "Out Of Range Address" / CUDA illegal memory access on RTX PRO 5000 (SM120) with FP8 model under sustained load — gone with VLLM_DISABLED_KERNELS=FlashInferFP8ScaledMMLinearKernel or --enforce-eager

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#55503](https://github.com/vllm-project/vllm/issues/55503) [Bug]: OffloadingConnector multi-tier (CPU+fs secondary tier) + MTP speculative decoding crashes EngineCore in _build_store_jobs (assert len(offload_keys) == len(offload_block_ids))
- [Bug] [vllm-project/vllm#55518](https://github.com/vllm-project/vllm/issues/55518) [Bug]: kv_cache_utils warns that prefix-cache reuse is disabled even when disable_eagle_block_drop keeps it working
- [Bug] [vllm-project/vllm#55533](https://github.com/vllm-project/vllm/issues/55533) [Bug][Spec Decode] Hybrid GDN (Qwen3.5/Qwen3.8 27B-class) + MTP: scheduler runs only ~3 concurrent sequences at batch >= 4 — acceptance/throughput collapse

### Scheduler / Batching

- [RFC] [vllm-project/vllm#55524](https://github.com/vllm-project/vllm/issues/55524) [RFC] Mamba2: exact-replay decode so that prefill, chunked prefill and decode produce identical bits

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#38167](https://github.com/sgl-project/sglang/issues/38167) [Bug][Diffusion] MiniMax-H3: 1344x768 fails deterministically with "CUDA driver error: device not ready" on 12GB, and the failed request poisons the server
- [Bug] [vllm-project/vllm#55530](https://github.com/vllm-project/vllm/issues/55530) [Bug]: Responses API automatic tool JSON retry crashes in ParsableContext

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#54567](https://github.com/vllm-project/vllm/issues/54567) [Bug]: Prefix caching never hits for DeepSeek-V4-Flash on Jetson Thor (SM110) — every request cold-prefills, TTFT scales linearly with context

### Build / Install / Platform

- [no-prefix] [sgl-project/sglang#37183](https://github.com/sgl-project/sglang/issues/37183) AMD MI308X SGLang GLM-5.3-Flash ValueError: The checkpoint you are trying to load has model type `glm5_next` but Transformers does not recognize this architecture.
- [Bug] [vllm-project/vllm#54486](https://github.com/vllm-project/vllm/issues/54486) [Bug]: openai chat-template content format breaks structured request contracts
- [Bug] [vllm-project/vllm#54487](https://github.com/vllm-project/vllm/issues/54487) [Bug]: prefix-caching hash configuration changes deterministic repeated output
- [Bug] [vllm-project/vllm#54490](https://github.com/vllm-project/vllm/issues/54490) [Bug]: enabling prefix caching changes deterministic repeated output
- [Bug] [vllm-project/vllm#54491](https://github.com/vllm-project/vllm/issues/54491) [Bug]: Qwen2.5 tool parser plus openai content format fails chat requests
- [Bug] [vllm-project/vllm#54493](https://github.com/vllm-project/vllm/issues/54493) [Bug]: --enable-dbo reaches an assertion-backed all2all backend validation failure
- [Feature] [vllm-project/vllm#54497](https://github.com/vllm-project/vllm/issues/54497) [Feature]: Upgrade XGrammar to >=0.2.4 and expose max_whitespace_cnt
- [Bug] [vllm-project/vllm#54569](https://github.com/vllm-project/vllm/issues/54569) [Bug]: FunASR get error result with fp16 dtype

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#37215](https://github.com/sgl-project/sglang/issues/37215) [Bug] --dp 8 intermittently fails with TCPStore EADDRINUSE on single-node 8×H800

### KV Cache / Connector / PD Disagg

- [Feature] [vllm-project/vllm#54536](https://github.com/vllm-project/vllm/issues/54536) [Feature][KV-offloading]: Host-staged RDMA for MooncakeStoreConnector requester-only ranks

### New Model Integration

- [Bug] [vllm-project/vllm#54459](https://github.com/vllm-project/vllm/issues/54459) [Bug] [Portability][MSVC]: M_LOG2E is unavailable when building Flash Attention with NVCC and MSVC

### Quantization

- [Feature] [sgl-project/sglang#37150](https://github.com/sgl-project/sglang/issues/37150) [Feature] Tuning / per-GPU config for DSv4 top-k v2 cluster launch plan (kClusterFloor / kNumPersistentClusters / kCandidates)
- [RFC] [vllm-project/vllm#54477](https://github.com/vllm-project/vllm/issues/54477) [RFC]: Selective Weight Reload for RL Training
- [Bug] [vllm-project/vllm#54521](https://github.com/vllm-project/vllm/issues/54521) [Bug]: Qwen3.8-Flash-Next: greedy decoding is non-deterministic from persistent_topk in prefill when prompt length nears indexer_budget (sm121/GB10)
- [Bug] [vllm-project/vllm#54559](https://github.com/vllm-project/vllm/issues/54559) [Bug]: qwen3.8-flash-next-fp8: No available shared memory broadcast block found in 60 seconds.

### Sampling / Speculative Decoding

- [RFC] [vllm-project/vllm#54506](https://github.com/vllm-project/vllm/issues/54506) [RFC]: Batch invariance for speculative decoding needs to cover the forward pass (M=1 vs M=k+1)
- [Bug] [vllm-project/vllm#54526](https://github.com/vllm-project/vllm/issues/54526) [Bug]: Cannot load an Eagle3 model, trained with Speculators
- [no-prefix] [vllm-project/vllm#54552](https://github.com/vllm-project/vllm/issues/54552) Qwen4Exp: QSA ring assert makes num_speculative_tokens 5..8 unreachable on all block sizes
- [Bug] [vllm-project/vllm#54555](https://github.com/vllm-project/vllm/issues/54555) [Bug]: V1 spec-decode proposer never constructs the positions buffer a both-XD-RoPE drafter seeds from

### Serving / OpenAI API / Streaming

- [Feature] [vllm-project/vllm#54528](https://github.com/vllm-project/vllm/issues/54528) [Feature]: Migrate MuseGlimmer reasoning/tool parsers to the Streaming Parser Engine

### Uncategorized

- [no-prefix] [sgl-project/sglang#37238](https://github.com/sgl-project/sglang/issues/37238) Does SGLang have a demo for running the VBench dataset accuracy evaluation on Wan2.2?
