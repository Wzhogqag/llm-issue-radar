# LLM Serving Issue Radar

_Last run: 2026-10-12T13:51+00:00_

**7 issues** — sgl-project/sglang: 1, vllm-project/vllm: 6 — 🆕 **7 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#61160](https://github.com/vllm-project/vllm/issues/61160) [Bug]: Cross-request context contamination via shared-prefix KV reuse in PD disaggregation with automatic prefix caching — clean with `--no-enable-prefix-caching`
- [Bug] 🆕 [#61131](https://github.com/vllm-project/vllm/issues/61131) [Bug]: CPU without Triton: slot-mapping fallback has a stale signature after #57169, V1 inference fails on the first forward step

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#61169](https://github.com/vllm-project/vllm/issues/61169) [Bug]: custom all-reduce creates its NVLink multicast reduce-scatter buffer mid-serving (not at startup); the run then crashes (Xid + CUBLAS_STATUS_EXECUTION_FAILED)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#61157](https://github.com/vllm-project/vllm/issues/61157) [Bug] GLM hybrid-SSM + MTP: deep-ctx agent session sharply degrades (fabricated tool args, self-amnesia) exactly when a concurrent request arrives — persists after #58454/#58368
- [Bug] 🆕 [#61117](https://github.com/vllm-project/vllm/issues/61117) [Bug]: CPU backend: C++ rejection_random_sample kernel accepts -1 placeholder drafts, so structured-output requests can sample from an unmasked row

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#61204](https://github.com/vllm-project/vllm/issues/61204) [Bug]: [ROCm] requirements/rocm.txt hard-requires mooncake-transfer-engine-rocm, which has no Python 3.14 wheel

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#43810](https://github.com/sgl-project/sglang/issues/43810) CI/CD Speed Up Optimizations
