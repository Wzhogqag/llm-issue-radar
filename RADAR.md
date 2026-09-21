# LLM Serving Issue Radar

_Last run: 2026-09-21T13:29+00:00_

**15 issues** — sgl-project/sglang: 3, vllm-project/vllm: 12 — 🆕 **15 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 3
- [Build / Install / Platform](#build--install--platform) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#40522](https://github.com/sgl-project/sglang/issues/40522) [RFC] Decouple the SWA sidecar page size from the full-attention page size (DSv4, Hybrid Models)

### vllm-project/vllm

- [Bug] 🆕 [#57938](https://github.com/vllm-project/vllm/issues/57938) [Bug]: AssertionError in _update_from_kv_xfer_finished when LMCache KV load fails on heterogeneous attention models

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#57932](https://github.com/vllm-project/vllm/issues/57932) [Bug]: SM120 / RTX PRO 6000 Blackwell: GLM-5.3-Flash fails with FlashInfer attention backend

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#40558](https://github.com/sgl-project/sglang/issues/40558) [Bug] sm_120 - tvm.error.InternalError: Error in function 'TllmGenFmhaRunner' at sglang/lib/python3.12/site-packages/flashinfer/data/include/flashinfer/trtllm/fmha/fmhaRunner.cuh:37: Unsupported architecture

### vllm-project/vllm

- [Bug] 🆕 [#57838](https://github.com/vllm-project/vllm/issues/57838) [Bug]: RowWiseTorchFP8ScaledMMLinearKernel is selected on RDNA4 (gfx1201) from v0.28 and costs 5-24% decode
- [RFC] 🆕 ⚠maintainer-authored [#57895](https://github.com/vllm-project/vllm/issues/57895) [RFC]: Stable runtime tensor lifecycle for sleep and live weight reload

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Feature] 🆕 [#57837](https://github.com/vllm-project/vllm/issues/57837) [Feature]: [WideEP][CPU]: Add a CPU-only Wide Expert Parallelism well-lit path

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#57839](https://github.com/vllm-project/vllm/issues/57839) [Bug] [watermarking]: reference detection server does not support dual_key_gumbel; detector alpha default disagrees with generation default

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#57941](https://github.com/vllm-project/vllm/issues/57941) [Bug]: Spec decode hits illegal memory access when the draft model's context is shorter than the target's
- [Bug] 🆕 [#57935](https://github.com/vllm-project/vllm/issues/57935) [Bug]: `/v1/chat/completions/batch` leaks hidden reasoning through logprobs and token IDs when `include_reasoning=false`
- [Bug] 🆕 [#57929](https://github.com/vllm-project/vllm/issues/57929) [Bug]: `/v1/completions/derender` drops requested `prompt_logprobs`

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#40562](https://github.com/sgl-project/sglang/issues/40562) [Bug][Diffusion] Warmup request finalization reloads offloaded components and triggers OOM on Wan2.2 A14B

### vllm-project/vllm

- [Bug] 🆕 [#57936](https://github.com/vllm-project/vllm/issues/57936) [Bug]: --kv-cache-memory suggestion double-counts CUDAGraph memory (regression of #37426, reintroduced by #49208)
- [Bug] 🆕 [#57890](https://github.com/vllm-project/vllm/issues/57890) [Bug]: HunYuan Dense V1 fails CUDA graph capture on v0.29 — HF dynamic RoPE does a host-side sync during capture

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#57927](https://github.com/vllm-project/vllm/issues/57927) [Bug]: Chunked embeddings break dot-product scoring with `use_activation=true
