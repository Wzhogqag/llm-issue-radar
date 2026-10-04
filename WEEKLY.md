# Weekly Trends — 2026-10-04

Window: 2026-09-28 → 2026-10-04 (7 snapshots)

**Totals:** 24 → 13  (13 appeared, 24 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 3 | 0 | -3 | 0 | 3 |
| Build / Install / Platform | 3 | 1 | -2 | 1 | 3 |
| Distributed / TP / PP / EP | 3 | 0 | -3 | 0 | 3 |
| KV Cache / Connector / PD Disagg | 2 | 1 | -1 | 1 | 2 |
| New Model Integration | 2 | 0 | -2 | 0 | 2 |
| Quantization | 2 | 4 | +2 | 4 | 2 |
| Sampling / Speculative Decoding | 3 | 4 | +1 | 4 | 3 |
| Scheduler / Batching | 3 | 2 | -1 | 2 | 3 |
| Serving / OpenAI API / Streaming | 3 | 1 | -2 | 1 | 3 |

## Appeared this week

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

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [sgl-project/sglang#41568](https://github.com/sgl-project/sglang/issues/41568) [Bug] MiMo-V2 processor fails to register when optional TorchCodec is unavailable
- [RFC] [vllm-project/vllm#59016](https://github.com/vllm-project/vllm/issues/59016) [RFC]: Software-dequant fp8 KV cache for MLA on Ampere (sm80/sm86) — consolidate the existing pieces, a 1M-ctx field case, and a validation offer
- [Bug] [vllm-project/vllm#59027](https://github.com/vllm-project/vllm/issues/59027) [Bug][ROCm] v0.30.0: GLM-5.3-Flash cannot boot on gfx942 — ROCMAiterMLASparseImpl missing record_logical_topk_ready (#57252 not in the release)

### Build / Install / Platform

- [Bug] [sgl-project/sglang#41539](https://github.com/sgl-project/sglang/issues/41539) [Bug] A worker whose launcher died during startup sends SIGQUIT to PID 1
- [other] [vllm-project/vllm#58928](https://github.com/vllm-project/vllm/issues/58928) [Installation]: macOS CPU build fails with Apple Clang 16 (structured binding capture under OpenMP in fla.cpp)
- [Bug] [vllm-project/vllm#58937](https://github.com/vllm-project/vllm/issues/58937) [Bug][ROCm]: ROCm nightly images not published since 2026-09-25

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#58920](https://github.com/vllm-project/vllm/issues/58920) [Bug]: Any KV connector makes pipeline-parallel decode 50-90% slower on Model Runner V2 (all ranks reply, reply-ring writer spins holding the GIL)
- [other] [vllm-project/vllm#58922](https://github.com/vllm-project/vllm/issues/58922) [ROCm] rocm_unquantized_gemm crashes on CPU tensors (dispatch ignores tensor device)
- [Bug] [vllm-project/vllm#58954](https://github.com/vllm-project/vllm/issues/58954) [Bug]: QSA indexer uses cooperative_topk on sm_110 (Jetson AGX Thor) and fails with "cluster misconfiguration"

### KV Cache / Connector / PD Disagg

- [other] [sgl-project/sglang#41514](https://github.com/sgl-project/sglang/issues/41514) [RFC / HiCache] Same-node peer L2 sharing across DP ranks via /dev/shm
- [other] [vllm-project/vllm#59024](https://github.com/vllm-project/vllm/issues/59024) [Tracking]: Hidden-state extraction for GLM-5.3-Flash

### New Model Integration

- [Bug] [vllm-project/vllm#58930](https://github.com/vllm-project/vllm/issues/58930) [Bug]: validate_xgrammar_grammar skips unsupported-feature checks for JSON schemas nested in structural tags
- [Feature] [vllm-project/vllm#58951](https://github.com/vllm-project/vllm/issues/58951) [Feature]: Support /v1/systemone endpoint for models like convaiinnovations/laya

### Quantization

- [Bug] [sgl-project/sglang#41569](https://github.com/sgl-project/sglang/issues/41569) [Bug] MiMo-V2 selects the FP8 MoE runner for packed MXFP4 experts on SM100
- [Bug] [vllm-project/vllm#58943](https://github.com/vllm-project/vllm/issues/58943) [Bug]: Official MiniCPM-V-4.6 GPTQ/AWQ checkpoints fail to load (vision tower built quantized)

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#41482](https://github.com/sgl-project/sglang/issues/41482) [Bug] `top_k`, `logprobs` and `n` have no upper bound, one request can DoS the server
- [Bug] [vllm-project/vllm#58973](https://github.com/vllm-project/vllm/issues/58973) [Bug]: V2 speculative prefill can change Qwen3-4B's first greedy token through RMSNorm autotune configuration
- [other] [vllm-project/vllm#58990](https://github.com/vllm-project/vllm/issues/58990) [Roadmap] Q4 2026 vLLM × RL

### Scheduler / Batching

- [Bug] [sgl-project/sglang#41463](https://github.com/sgl-project/sglang/issues/41463) [Bug] Falcon-H1 with tied word embeddings cannot serve a single request, tied LM head's `.float()` upcasts the embedding in place
- [Bug] [sgl-project/sglang#41471](https://github.com/sgl-project/sglang/issues/41471) [Bug] Two concurrent requests using DisallowedTokensLogitsProcessor with different token_ids crash the server
- [Bug] [vllm-project/vllm#58931](https://github.com/vllm-project/vllm/issues/58931) [Bug]: MooncakeStoreConnector crashes EngineCore when a request is preempted by `reset_prefix_cache(reset_running_requests=True)` and re-admitted in the next step

### Serving / OpenAI API / Streaming

- [no-prefix] [sgl-project/sglang#41510](https://github.com/sgl-project/sglang/issues/41510) AttributeError: 'ComponentData' object has no attribute 'parent'
- [Bug] [vllm-project/vllm#58934](https://github.com/vllm-project/vllm/issues/58934) [Bug]: MiMo-V2.6 omni declares no embedding_fields, so an EPD encoder/consumer pair rejects every image with 400
- [Bug] [vllm-project/vllm#58969](https://github.com/vllm-project/vllm/issues/58969) [Bug]: bench serve drops or mis-buckets several result fields, including all E2EL metrics for pooling
