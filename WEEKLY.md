# Weekly Trends — 2026-11-15

Window: 2026-11-09 → 2026-11-15 (7 snapshots)

**Totals:** 10 → 12  (12 appeared, 10 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 0 | 1 | +1 | 1 | 0 |
| Build / Install / Platform | 1 | 1 | 0 | 1 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 1 | -1 | 1 | 2 |
| New Model Integration | 0 | 1 | +1 | 1 | 0 |
| Performance / Memory / OOM | 2 | 2 | 0 | 2 | 2 |
| Quantization | 3 | 2 | -1 | 2 | 3 |
| Sampling / Speculative Decoding | 2 | 3 | +1 | 3 | 2 |
| Scheduler / Batching | 0 | 1 | +1 | 1 | 0 |

## Appeared this week

### Attention Backend

- [no-prefix] [sgl-project/sglang#50499](https://github.com/sgl-project/sglang/issues/50499) dspark_accept SoftmaxTemp.execute (flashinfer branch) returns NaN rows on GB10 in 6/17 cold starts — cross-ref flashinfer#9486

### Build / Install / Platform

- [RFC] [vllm-project/vllm#67696](https://github.com/vllm-project/vllm/issues/67696) [RFC]: CPU Backend support for VLLM_BATCH_INVARIANT=1

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#67692](https://github.com/vllm-project/vllm/issues/67692) [Bug]: Unauthenticated P2P Offload Exposes Full CPU KV Cache to Arbitrary Peers

### New Model Integration

- [no-prefix] [vllm-project/vllm#67683](https://github.com/vllm-project/vllm/issues/67683) Feature request: a documented, supported pattern for fast weight synchronization between an RL trainer and vLLM rollout workers

### Performance / Memory / OOM

- [Bug] [sgl-project/sglang#50566](https://github.com/sgl-project/sglang/issues/50566) [Bug][Humming backend] Tree K-partial reduction reports divergent barriers under synccheck
- [Bug] [sgl-project/sglang#50577](https://github.com/sgl-project/sglang/issues/50577) [Bug] DFlash auxiliary CUDA graphs retain per-batch-size buffers, causing excessive GPU memory growth

### Quantization

- [Bug] [sgl-project/sglang#50521](https://github.com/sgl-project/sglang/issues/50521) [Bug][Humming] FP16 Stream-K GEMM produces NaNs for an exact-zero result
- [RFC] [vllm-project/vllm#67769](https://github.com/vllm-project/vllm/issues/67769) [RFC]: MLP-only pruning of unconsumed rows in the final dense Llama layer

### Sampling / Speculative Decoding

- [Feature] [sgl-project/sglang#50497](https://github.com/sgl-project/sglang/issues/50497) [Feature] EAGLE tree verify without per-node state snapshots for GDN layers
- [RFC] [sgl-project/sglang#50547](https://github.com/sgl-project/sglang/issues/50547) [RFC] pd: Let decode compute the prompt tail and sample the first token, for any model
- [Bug] [vllm-project/vllm#67755](https://github.com/vllm-project/vllm/issues/67755) [Bug]: Tekken Mistral tokenizers garble emoji and other multi-byte characters when special tokens are kept

### Scheduler / Batching

- [Performance] [vllm-project/vllm#67674](https://github.com/vllm-project/vllm/issues/67674) [Performance]: `--prefix-match-unit` recovers hybrid-model prefix hits on multi-turn and agent traces, but on the Triton/FLA GDN backend it costs about 30 ms of TTFT on almost every request

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [Bug] [vllm-project/vllm#66525](https://github.com/vllm-project/vllm/issues/66525) [Bug]: Gemma4 suppression-token cache causes UnexpectedTracerError on TPU

### KV Cache / Connector / PD Disagg

- [RFC] [vllm-project/vllm#66556](https://github.com/vllm-project/vllm/issues/66556) [RFC]: Define an Optional In-Tree Integration Path for Hardware Backends
- [RFC] [vllm-project/vllm#66570](https://github.com/vllm-project/vllm/issues/66570) [RFC]: Async CPU tier setup for OffloadingConnector

### Performance / Memory / OOM

- [Feature] [sgl-project/sglang#49257](https://github.com/sgl-project/sglang/issues/49257) [Feature][RFC] STANDALONE PD: homogeneous TP=2 handoff and rank-consistent seed rejection
- [no-prefix] [vllm-project/vllm#66515](https://github.com/vllm-project/vllm/issues/66515) enable_gqa=True can be 2.59x slower than materializing the KV cache - silent MATH-backend fallback at decode

### Quantization

- [Feature] [sgl-project/sglang#49296](https://github.com/sgl-project/sglang/issues/49296) [Feature] flashinfer: Split the extend into ragged and paged passes under full prefill CUDA graphs with an FP8 KV cache
- [RFC] [vllm-project/vllm#66491](https://github.com/vllm-project/vllm/issues/66491) [RFC]: Packed-weight INT4 GEMM (W4A16 / W4A8) for RDNA4 (gfx1200/gfx1201)
- [Bug] [vllm-project/vllm#66573](https://github.com/vllm-project/vllm/issues/66573) [Bug]: Qwen3.5 `qwen3_5.py` embedding drops `quant_config` — GGUF embeddings fall back to dense

### Sampling / Speculative Decoding

- [no-prefix] [sgl-project/sglang#49274](https://github.com/sgl-project/sglang/issues/49274) Silent deterministic output corruption: first token id 0 ("!") then [PAD] (id 163839) loop, spec accept-length pinned at 1.00, zero errors — Kimi-K3.1-Pro (hybrid mamba + DFlash2 draft) on AMD MI300X/AITER, fp8 KV, v0.5.23.dev20261104 (e67b2062e2)
- [Bug] [sgl-project/sglang#49295](https://github.com/sgl-project/sglang/issues/49295) [Bug] Breakable prefill CUDA graphs return wrong, non-repeatable prompt logprobs for short prompts on Qwen3.8-2.4T-A95B-NVFP4 (B300)
