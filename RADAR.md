# LLM Serving Issue Radar

_Last run: 2026-11-01T13:21+00:00_

**5 issues** — sgl-project/sglang: 1, vllm-project/vllm: 4 — 🆕 **5 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#64972](https://github.com/vllm-project/vllm/issues/64972) [Bug]: CudaPlatform.log_warnings() aborts startup on an unqueryable NVML device even when CUDA_VISIBLE_DEVICES excludes it

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#64973](https://github.com/vllm-project/vllm/issues/64973) [RFC]: Hybrid KV Backend: Eliminating Disk Restore Pipeline Bubbles Without CPU Memory Bloat

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#64936](https://github.com/vllm-project/vllm/issues/64936) [Bug]: NCCL weight sync: packed transfer fails to unpack misaligned tensors (pack_tensors has no alignment)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#64953](https://github.com/vllm-project/vllm/issues/64953) [Bug]:  `seed=-1` passes config validation and kills engine init inside `np.random.seed` ("Seed must be between 0 and 2**32 - 1") — while `SamplingParams` already treats `-1` as "no seed"

## Performance / Memory / OOM

### sgl-project/sglang

- [Perf] 🆕 ⚠maintainer-authored [#47734](https://github.com/sgl-project/sglang/issues/47734) [Perf] sglang-kernel FA3 picks MmaPV_is_RS=false for hdim 128 non-causal on H200 (1.5-3% slower than flash-attn's hopper build)
