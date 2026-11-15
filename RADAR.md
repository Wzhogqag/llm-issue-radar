# LLM Serving Issue Radar

_Last run: 2026-11-15T13:22+00:00_

**12 issues** — sgl-project/sglang: 6, vllm-project/vllm: 6 — 🆕 **10 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Performance] 🆕 [#67674](https://github.com/vllm-project/vllm/issues/67674) [Performance]: `--prefix-match-unit` recovers hybrid-model prefix hits on multi-turn and agent traces, but on the Triton/FLA GDN backend it costs about 30 ms of TTFT on almost every request

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#67692](https://github.com/vllm-project/vllm/issues/67692) [Bug]: Unauthenticated P2P Offload Exposes Full CPU KV Cache to Arbitrary Peers

## Attention Backend

### sgl-project/sglang

- [no-prefix] ⚠no-prefix [#50499](https://github.com/sgl-project/sglang/issues/50499) dspark_accept SoftmaxTemp.execute (flashinfer branch) returns NaN rows on GB10 in 6/17 cold starts — cross-ref flashinfer#9486

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#50521](https://github.com/sgl-project/sglang/issues/50521) [Bug][Humming] FP16 Stream-K GEMM produces NaNs for an exact-zero result

### vllm-project/vllm

- [RFC] 🆕 [#67769](https://github.com/vllm-project/vllm/issues/67769) [RFC]: MLP-only pruning of unconsumed rows in the final dense Llama layer

## New Model Integration

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#67683](https://github.com/vllm-project/vllm/issues/67683) Feature request: a documented, supported pattern for fast weight synchronization between an RL trainer and vLLM rollout workers

## Sampling / Speculative Decoding

### sgl-project/sglang

- [RFC] 🆕 [#50547](https://github.com/sgl-project/sglang/issues/50547) [RFC] pd: Let decode compute the prompt tail and sample the first token, for any model
- [Feature] [#50497](https://github.com/sgl-project/sglang/issues/50497) [Feature] EAGLE tree verify without per-node state snapshots for GDN layers

### vllm-project/vllm

- [Bug] 🆕 [#67755](https://github.com/vllm-project/vllm/issues/67755) [Bug]: Tekken Mistral tokenizers garble emoji and other multi-byte characters when special tokens are kept

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#50577](https://github.com/sgl-project/sglang/issues/50577) [Bug] DFlash auxiliary CUDA graphs retain per-batch-size buffers, causing excessive GPU memory growth
- [Bug] 🆕 [#50566](https://github.com/sgl-project/sglang/issues/50566) [Bug][Humming backend] Tree K-partial reduction reports divergent barriers under synccheck

## Build / Install / Platform

### vllm-project/vllm

- [RFC] 🆕 [#67696](https://github.com/vllm-project/vllm/issues/67696) [RFC]: CPU Backend support for VLLM_BATCH_INVARIANT=1
