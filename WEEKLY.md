# Weekly Trends — 2026-10-25

Window: 2026-10-20 → 2026-10-25 (5 snapshots)

**Totals:** 11 → 11  (11 appeared, 11 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Build / Install / Platform | 3 | 2 | -1 | 2 | 3 |
| KV Cache / Connector / PD Disagg | 1 | 1 | 0 | 1 | 1 |
| Performance / Memory / OOM | 0 | 1 | +1 | 1 | 0 |
| Quantization | 2 | 2 | 0 | 2 | 2 |
| Sampling / Speculative Decoding | 2 | 0 | -2 | 0 | 2 |
| Scheduler / Batching | 2 | 2 | 0 | 2 | 2 |
| Serving / OpenAI API / Streaming | 1 | 2 | +1 | 2 | 1 |
| Uncategorized | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Build / Install / Platform

- [Bug] [sgl-project/sglang#46326](https://github.com/sgl-project/sglang/issues/46326) [Bug] ValueError: The checkpoint you are trying to load has model type `qwen4_exp` but Transformers does not recognize this architecture.
- [Bug] [vllm-project/vllm#63505](https://github.com/vllm-project/vllm/issues/63505) [Bug]: Qwen3.8-27B (GDN hybrid) with PP=3 on sm_86: illegal memory access (Xid 31) with prefix caching, gibberish output without it; regression since v0.28.0 (v0.31.0, v0.32.0, both model runners)

### KV Cache / Connector / PD Disagg

- [Perf] [vllm-project/vllm#63517](https://github.com/vllm-project/vllm/issues/63517) [Perf][Qwen4Exp] Hybrid KV-cache capacity accounting: merged main-KV+indexer groups share one block table — slots/request are coverage-set; page bytes buy blocks via bytes_per_block

### Performance / Memory / OOM

- [RFC] [vllm-project/vllm#63501](https://github.com/vllm-project/vllm/issues/63501) [RFC]: Select the MRV2 DBO microbatch count per step within an allocated capacity

### Quantization

- [Bug] [vllm-project/vllm#63514](https://github.com/vllm-project/vllm/issues/63514) [Bug]: `hadacore_transform` gives wrong results for odd row counts (INT4 per-token-head KV cache): garbage K/V and intermittent illegal memory access
- [Bug] [vllm-project/vllm#63536](https://github.com/vllm-project/vllm/issues/63536) [Bug]: [Usage]: RTX PRO 5000 (SM120) deadlocks at 3-4W during vLLM 0.32.0 startup with 70B NVFP4 model, even with --enforce-eager

### Scheduler / Batching

- [Bug] [vllm-project/vllm#63519](https://github.com/vllm-project/vllm/issues/63519) [Bug]: Deferred block-free fence (#45357) does not cover speculator `propose()` KV writes in the V2 model runner
- [Bug] [vllm-project/vllm#63549](https://github.com/vllm-project/vllm/issues/63549) [Bug]: Async scheduling + preemption crashes Model Runner V1 with KeyError all_token_ids[req_id] in _update_states

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#46390](https://github.com/sgl-project/sglang/issues/46390) [Bug] multimodal_gen: cross-node pure-Ulysses H3 serve (1 GPU/node x 4 nodes) freezes at the first distributed generation - /health never binds with --warmup-mode off, 0% GPU on all ranks, zero errors
- [Bug] [vllm-project/vllm#63573](https://github.com/vllm-project/vllm/issues/63573) [Bug][Anthropic API] /v1/messages/count_tokens requires --tool-call-parser when tools are present

### Uncategorized

- [Feature] [vllm-project/vllm#63470](https://github.com/vllm-project/vllm/issues/63470) [Feature]: Run Nemotron 3.5 Super VL without the --trust-remote-code flag

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [other] [sgl-project/sglang#45370](https://github.com/sgl-project/sglang/issues/45370) [Roadmap] Beam Development & Optimization
- [Bug] [vllm-project/vllm#62606](https://github.com/vllm-project/vllm/issues/62606) [Bug][ROCm]: ROCM_AITER_UNIFIED_ATTN gives wrong output on gfx950 when a layer's KV cache is 2–4 GiB
- [Bug] [vllm-project/vllm#62639](https://github.com/vllm-project/vllm/issues/62639) [Bug]: Responses API: tool_choice=allowed_tools does not work

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#62697](https://github.com/vllm-project/vllm/issues/62697) [Bug][ROCm] `ROCM_ATTN` returns wrong attention (and can fault the GPU) on RDNA for head size ≥ 96 with KV block size ≠ 16, and for MHA with head size 192/256

### Quantization

- [other] [sgl-project/sglang#45373](https://github.com/sgl-project/sglang/issues/45373) [Tracking] GLM-5.3-Flash performance optimization on Hopper (SM90)
- [Bug] [vllm-project/vllm#62609](https://github.com/vllm-project/vllm/issues/62609) [Bug]: A100 run Bolt (nv-community/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) throw :B12X NVFP4 kernels require a Blackwell 12x device

### Sampling / Speculative Decoding

- [RFC] [vllm-project/vllm#62640](https://github.com/vllm-project/vllm/issues/62640) [RFC]: Improve MTP configuration warning
- [Feature] [vllm-project/vllm#62694](https://github.com/vllm-project/vllm/issues/62694) [Feature]: [Spec Decode] Support model-based drafters (target hidden states) via custom_class

### Scheduler / Batching

- [Perf] [sgl-project/sglang#45351](https://github.com/sgl-project/sglang/issues/45351) [Perf] HiCache PP-sync drain makes the PP prefill scheduler lock-step across ranks
- [Bug] [sgl-project/sglang#45357](https://github.com/sgl-project/sglang/issues/45357) [Bug] PD prefill PP8 + HiCache cache mode hangs: PP0–PP3 blocked in the HiCache PP-sync drain

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#62598](https://github.com/vllm-project/vllm/issues/62598) [Bug][Rust Frontend] Long conversations fail with HTTP 500 (chat template fuel limit)
