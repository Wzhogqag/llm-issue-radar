# Weekly Trends — 2026-08-02

Window: 2026-07-27 → 2026-08-02 (7 snapshots)

**Totals:** 26 → 25  (25 appeared, 26 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 2 | 5 | +3 | 5 | 2 |
| Build / Install / Platform | 3 | 3 | 0 | 3 | 3 |
| Distributed / TP / PP / EP | 3 | 3 | 0 | 3 | 3 |
| KV Cache / Connector / PD Disagg | 2 | 5 | +3 | 5 | 2 |
| New Model Integration | 1 | 1 | 0 | 1 | 1 |
| Performance / Memory / OOM | 1 | 0 | -1 | 0 | 1 |
| Quantization | 5 | 2 | -3 | 2 | 5 |
| Sampling / Speculative Decoding | 4 | 2 | -2 | 2 | 4 |
| Scheduler / Batching | 2 | 0 | -2 | 0 | 2 |
| Serving / OpenAI API / Streaming | 2 | 3 | +1 | 3 | 2 |
| Uncategorized | 1 | 1 | 0 | 1 | 1 |

## Appeared this week

### Attention Backend

- [Bug] [sgl-project/sglang#33207](https://github.com/sgl-project/sglang/issues/33207) [Bug] Unrecognized configuration class <class 'sglang.srt.utils.hf_transformers.common._DeepseekV4ConfigAlias'>
- [no-prefix] [sgl-project/sglang#33223](https://github.com/sgl-project/sglang/issues/33223) Kimi K3 encountered accuracy problems when testing τ³-Banking, and scored only 17.53
- [Bug] [vllm-project/vllm#50705](https://github.com/vllm-project/vllm/issues/50705) [Bug]: sm_120 + local CUDA toolkit < 12.9: FlashInfer JIT failures kill engine init in three default paths (sampler, fused-MoE, FP8 KV) instead of falling back
- [Bug] [vllm-project/vllm#50707](https://github.com/vllm-project/vllm/issues/50707) [Bug] DFlash on SM121 (GB10 / DGX Spark): attention autoselect picks FLASH_ATTN for non-causal draft attention and device-asserts in _vllm_fa2_C.varlen_fwd
- [Bug] [vllm-project/vllm#50720](https://github.com/vllm-project/vllm/issues/50720) [Bug]: DeepSeek-V4-Flash-0731 + DSpark fails on RTX PRO 6000 (SM120) with FlashInfer sparse MLA decode kernel routing

### Build / Install / Platform

- [Bug] [vllm-project/vllm#50681](https://github.com/vllm-project/vllm/issues/50681) [Bug]: Qwen3.6-35B-A3B produces corrupted output with EP and sequence parallelism enabled
- [other] [vllm-project/vllm#50682](https://github.com/vllm-project/vllm/issues/50682) [ROCm][AMD] Kimi-K3 Gap and Roadmap Tracking
- [Bug] [vllm-project/vllm#50699](https://github.com/vllm-project/vllm/issues/50699) [Bug]: DiffusionGemma: runtime CUDA OOM under concurrent decode (fp32 canvas×vocab temporaries)

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#33181](https://github.com/sgl-project/sglang/issues/33181) [Bug] Inkling reasoning parser leaks the tool name into visible content when a turn opens with a tool call
- [Bug] [vllm-project/vllm#50706](https://github.com/vllm-project/vllm/issues/50706) [Bug]: Mistral3 (HF format): default text-only LLM() init fails in multimodal profiling — "Failed to apply PixtralProcessor on data={'text': '[IMG]'}"
- [RFC] [vllm-project/vllm#50738](https://github.com/vllm-project/vllm/issues/50738) [RFC]: Dual Batch Overlap (DBO) for Model Runner V2

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#33268](https://github.com/sgl-project/sglang/issues/33268) [Bug] HiCache storage keys omit kv_cache_dtype — silent cross-run cache collisions
- [no-prefix] [vllm-project/vllm#50630](https://github.com/vllm-project/vllm/issues/50630) No capability flag declares which KV-cache kinds may be peeked past a candidate boundary — each margin implementation excludes Mamba by hand
- [no-prefix] [vllm-project/vllm#50687](https://github.com/vllm-project/vllm/issues/50687) Hybrid multi-group KV: _update_requests_with_invalid_blocks crashes (too many values to unpack) on connector load-error blocks
- [Bug] [vllm-project/vllm#50709](https://github.com/vllm-project/vllm/issues/50709) [Bug]: TurboQuant hybrid model crashes at determine_available_memory with 'Unknown cache dtype: auto' on v0.25.0+
- [Bug] [vllm-project/vllm#50719](https://github.com/vllm-project/vllm/issues/50719) [Bug][PD][Mooncake] Decode requests stuck in WAITING_FOR_REMOTE_KVS and fail with Timeout waiting for P side ready

### New Model Integration

- [other] [vllm-project/vllm#50672](https://github.com/vllm-project/vllm/issues/50672) [Installation]:vllm-openai:kimi-k3 cpuoffloadgb not support?

### Quantization

- [Bug] [sgl-project/sglang#33163](https://github.com/sgl-project/sglang/issues/33163) [Bug] deepseek-v4-flash toolcall error runner_backend from marlin to  flashinfer_mxfp4
- [Bug] [vllm-project/vllm#50702](https://github.com/vllm-project/vllm/issues/50702) [Bug]: int8_per_token_head KV + prefix caching corrupts output when the KV pool is pinned at 100% (Gemma-4 hybrid, Triton)

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#50708](https://github.com/vllm-project/vllm/issues/50708) [Bug] Speculative decoding with a large num_speculative_tokens fails with a bare negative max_num_scheduled_tokens instead of naming the flags that fix it
- [Bug] [vllm-project/vllm#50722](https://github.com/vllm-project/vllm/issues/50722) [Bug]: With qwen3.5-35b-a3b, the performance is relatively poor both when using dflash and when not using it, but the accepted length of dflash is around 5–6.

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#33185](https://github.com/sgl-project/sglang/issues/33185) [Bug] DeepSeek-V4-Flash-0731: reasoning_effort mapped one level off — `high` is a no-op and vendor `max` is unreachable
- [Bug] [vllm-project/vllm#50660](https://github.com/vllm-project/vllm/issues/50660) [Bug]: deepseek-v4-flash-0731 can not be Stablize running
- [Bug] [vllm-project/vllm#50690](https://github.com/vllm-project/vllm/issues/50690) [Bug]: gpt-oss chat completions return 500 "Unexpected token 200002 while expecting start token 200006" when ignore_eos=true

### Uncategorized

- [no-prefix] [sgl-project/sglang#33180](https://github.com/sgl-project/sglang/issues/33180) @copilot resolve the merge conflicts on this branch.

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#49886](https://github.com/vllm-project/vllm/issues/49886) [Bug]: GLM-5.2-NVFP4 produces garbled/incorrect output and hits NotImplementedError in forward_mha on GB10 (SM121a) with FLASHINFER_MLA_SPARSE_SM120
- [Bug] [vllm-project/vllm#49980](https://github.com/vllm-project/vllm/issues/49980) [Bug]: FlashInfer builder ValueError 'provided out is the wrong size for the accumulation' with Llama-4 chunked local attention when a prefill exceeds attention_chunk_size and max_num_seqs is small

### Build / Install / Platform

- [Bug] [vllm-project/vllm#49878](https://github.com/vllm-project/vllm/issues/49878) [Bug]: Dramatic KV cache size increase (~40%) for Gemma4 from v0.25.1 to v0.26
- [Bug] [vllm-project/vllm#49924](https://github.com/vllm-project/vllm/issues/49924) [Bug][XPU]: GDN attention silently corrupts memory under load — fix merged in vllm-xpu-kernels but requirements/xpu.txt pins a release that predates it
- [other] [vllm-project/vllm#49955](https://github.com/vllm-project/vllm/issues/49955) [Regression] Trailing <turn|> token appearing at the end of generated text in vLLM 0.26.0

### Distributed / TP / PP / EP

- [Bug] [sgl-project/sglang#32470](https://github.com/sgl-project/sglang/issues/32470) [Bug]  CUDA illegal memory access during compact ragged-verify graph capture (c128 plan kernel race)
- [Perf] [vllm-project/vllm#49921](https://github.com/vllm-project/vllm/issues/49921) [Perf] BF16x3 router GEMM gated off family-120 Blackwell (GB10 / DGX Spark, sm_121) — the only barrier for DeepSeek-V4-Flash's fp32 router
- [Bug] [vllm-project/vllm#49983](https://github.com/vllm-project/vllm/issues/49983) [Bug]: /metrics returns 500 when PROMETHEUS_MULTIPROC_DIR resolves to a network-backed/mounted volume (TP>1)

### KV Cache / Connector / PD Disagg

- [Bug] [sgl-project/sglang#32521](https://github.com/sgl-project/sglang/issues/32521) [Bug] [MLX] Hunyuan cannot be served: auto_map fails in kv_cache_builder.resolve_transformers_arch
- [Bug] [vllm-project/vllm#49920](https://github.com/vllm-project/vllm/issues/49920) [Bug]: DiffusionGemma - Unconditional minimax_m3 warmup import in kernel_warmup() crashes engine startup for unrelated models (Triton JIT fails to parse index_topk kernel)

### New Model Integration

- [Feature] [vllm-project/vllm#49973](https://github.com/vllm-project/vllm/issues/49973) [Feature]: Support ubuntu 26.04 runtime container

### Performance / Memory / OOM

- [RFC] [sgl-project/sglang#32432](https://github.com/sgl-project/sglang/issues/32432) [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for Dynamic CUDA Graph Replay

### Quantization

- [Bug] [sgl-project/sglang#32426](https://github.com/sgl-project/sglang/issues/32426) [Bug] In version v0.5.16, the sakamakismile/Ornith-1.0-35B-NVFP4 model generates garbled characters.
- [Bug] [vllm-project/vllm#49893](https://github.com/vllm-project/vllm/issues/49893) [Bug]: SpeculativeConfig method="draft_model" cannot load mixed-precision compressed-tensors checkpoints (config_groups)
- [Feature] [vllm-project/vllm#49905](https://github.com/vllm-project/vllm/issues/49905) [Feature]: DeepGEMM kernels are never warmed — only 2 of 24 entry points, so fp8_einsum JIT-loads during serving
- [Bug] [vllm-project/vllm#49926](https://github.com/vllm-project/vllm/issues/49926) [Bug]: EngineDeadError NVFP4 marlin
- [Bug] [vllm-project/vllm#49981](https://github.com/vllm-project/vllm/issues/49981) [Bug]: tool_choice: "required" causes xgrammar FSM crash / infinite hang with GLM-5.2-NVFP4 on vLLM 0.24.0

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#32527](https://github.com/sgl-project/sglang/issues/32527) [BUG] EAGLE + DP Attention + PD Disaggregation: Deadlock when `index_share_for_mtp_iteration` is enabled for GLM-5.2
- [Bug] [vllm-project/vllm#49896](https://github.com/vllm-project/vllm/issues/49896) [Bug] DeepSeek-V4 on SM12x: NaN MQA logits drive top_k_per_row_prefill to emit uninitialized smem as indices -> illegal memory access
- [Bug] [vllm-project/vllm#49918](https://github.com/vllm-project/vllm/issues/49918) [Bug]: Prefill with prompt length == 1 + num_speculative_tokens misclassified as uniform decode → FULL spec-verify cudagraph skips GDN/hybrid recurrent-state write → deterministic garbage (any spec method incl. ngram; v0.25.1 & v0.26.0)
- [Perf] [vllm-project/vllm#49927](https://github.com/vllm-project/vllm/issues/49927) [Perf] #48137 costs ~10.6% spec-decode acceptance and #48660 shifts output distributions on DeepSeek-V4-Flash — isolated via #48660-only arm on a production 2-node deployment

### Scheduler / Batching

- [no-prefix] [sgl-project/sglang#32433](https://github.com/sgl-project/sglang/issues/32433) Question: unit mismatch in evict_from_tree_cache for SWATokenToKVPoolAllocator?
- [Bug] [vllm-project/vllm#49902](https://github.com/vllm-project/vllm/issues/49902) [Bug]: Tiered KV offload promotes every waiting request (which fills primary DRAM pool)

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#32536](https://github.com/sgl-project/sglang/issues/32536) [Bug] poolside_v1 reasoning parser doesn't separate reasoning for Laguna-S-2.1 (thinking-on template default)
- [Bug] [vllm-project/vllm#49922](https://github.com/vllm-project/vllm/issues/49922) [Bug]: [Regression] Assertion res == CUresult::CUDA_SUCCESS failed in FlashMLA (phase1.cuh) for DeepSeek-V4 on v0.26.0 (Works in v0.25.0)

### Uncategorized

- [other] [sgl-project/sglang#32519](https://github.com/sgl-project/sglang/issues/32519) [WIP]
