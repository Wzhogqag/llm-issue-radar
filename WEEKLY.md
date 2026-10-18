# Weekly Trends — 2026-10-18

Window: 2026-10-12 → 2026-10-18 (7 snapshots)

**Totals:** 7 → 10  (10 appeared, 7 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Build / Install / Platform | 1 | 1 | 0 | 1 | 1 |
| Distributed / TP / PP / EP | 1 | 0 | -1 | 0 | 1 |
| KV Cache / Connector / PD Disagg | 2 | 1 | -1 | 1 | 2 |
| New Model Integration | 0 | 1 | +1 | 1 | 0 |
| Quantization | 0 | 3 | +3 | 3 | 0 |
| Sampling / Speculative Decoding | 2 | 3 | +1 | 3 | 2 |
| Scheduler / Batching | 0 | 1 | +1 | 1 | 0 |
| Uncategorized | 1 | 0 | -1 | 0 | 1 |

## Appeared this week

### Build / Install / Platform

- [other] [sgl-project/sglang#44959](https://github.com/sgl-project/sglang/issues/44959) [NPU] Please keep publishing Docker images for Ascend 910B

### KV Cache / Connector / PD Disagg

- [Feature] [vllm-project/vllm#62283](https://github.com/vllm-project/vllm/issues/62283) [Feature][KV Offload]: Require canonical_layout when a secondary tier shares KV across TP sizes (direct layout silently corrupts)

### New Model Integration

- [Feature] [sgl-project/sglang#44885](https://github.com/sgl-project/sglang/issues/44885) [Feature] kv-shard: Pass Q instead of KV for short prefills with long cached prefixes

### Quantization

- [Bug] [sgl-project/sglang#44998](https://github.com/sgl-project/sglang/issues/44998) [Bug] NVFP4 Marlin fallback (SM80-SM90) garbles every output when the block scales are small (vllm-project/vllm#34577 not ported)
- [Bug] [sgl-project/sglang#44999](https://github.com/sgl-project/sglang/issues/44999) [Bug] Marlin MoE (AWQ W4A16) on SM86 intermittently returns wrong expert outputs, even for a single request; the Triton WNA16 kernel is exact
- [Bug] [sgl-project/sglang#45000](https://github.com/sgl-project/sglang/issues/45000) [Bug] FP8 block-quantized checkpoint on SM86 (FP8 Marlin) intermittently gives wrong tokens with the overlap scheduler; exact without it

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#44997](https://github.com/sgl-project/sglang/issues/44997) [Bug] NGRAM speculative decoding corrupts radix-cached KV with the overlap scheduler when requests end on a stop token (0.5.22)
- [Bug] [sgl-project/sglang#45002](https://github.com/sgl-project/sglang/issues/45002) [Bug] Client-controlled RID prefix allows cross-request abort through disconnect cleanup
- [Bug] [vllm-project/vllm#62304](https://github.com/vllm-project/vllm/issues/62304) [Bug]: Hybrid GDN models (Qwen3.5) with n-gram speculative decoding: greedy outputs go wrong when drafts are partly accepted; the GDN state misses the last accepted token's update

### Scheduler / Batching

- [RFC] [vllm-project/vllm#62257](https://github.com/vllm-project/vllm/issues/62257) [RFC]: Add Single-Process In-Memory Engine Mode for Low-Tier Sandbox Environments (Colab T4 / Jupyter)

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Build / Install / Platform

- [Bug] [vllm-project/vllm#61204](https://github.com/vllm-project/vllm/issues/61204) [Bug]: [ROCm] requirements/rocm.txt hard-requires mooncake-transfer-engine-rocm, which has no Python 3.14 wheel

### Distributed / TP / PP / EP

- [Bug] [vllm-project/vllm#61169](https://github.com/vllm-project/vllm/issues/61169) [Bug]: custom all-reduce creates its NVLink multicast reduce-scatter buffer mid-serving (not at startup); the run then crashes (Xid + CUBLAS_STATUS_EXECUTION_FAILED)

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#61131](https://github.com/vllm-project/vllm/issues/61131) [Bug]: CPU without Triton: slot-mapping fallback has a stale signature after #57169, V1 inference fails on the first forward step
- [Bug] [vllm-project/vllm#61160](https://github.com/vllm-project/vllm/issues/61160) [Bug]: Cross-request context contamination via shared-prefix KV reuse in PD disaggregation with automatic prefix caching — clean with `--no-enable-prefix-caching`

### Sampling / Speculative Decoding

- [Bug] [vllm-project/vllm#61117](https://github.com/vllm-project/vllm/issues/61117) [Bug]: CPU backend: C++ rejection_random_sample kernel accepts -1 placeholder drafts, so structured-output requests can sample from an unmasked row
- [Bug] [vllm-project/vllm#61157](https://github.com/vllm-project/vllm/issues/61157) [Bug] GLM hybrid-SSM + MTP: deep-ctx agent session sharply degrades (fabricated tool args, self-amnesia) exactly when a concurrent request arrives — persists after #58454/#58368

### Uncategorized

- [no-prefix] [sgl-project/sglang#43810](https://github.com/sgl-project/sglang/issues/43810) CI/CD Speed Up Optimizations
