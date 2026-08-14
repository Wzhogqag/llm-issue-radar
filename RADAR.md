# LLM Serving Issue Radar

_Last run: 2026-08-14T13:48+00:00_

**16 issues** — sgl-project/sglang: 5, vllm-project/vllm: 11 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#34815](https://github.com/sgl-project/sglang/issues/34815) PP8 disaggregated prefill has a load-independent ~30 s TTFT floor on Kimi-K3

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#52339](https://github.com/vllm-project/vllm/issues/52339) [Bug]: DeepSeek-V4 FlashMLA sparse prefill phase1.cuh:614 on H20-3e TP8 at ~161K context
- [Bug] 🆕 [#52276](https://github.com/vllm-project/vllm/issues/52276) [Bug]: DeepSeek-V4 NIXL failure returns corrupted reasoning with empty content

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#52317](https://github.com/vllm-project/vllm/issues/52317) [Bug]: MRv2: --enable-prefix-caching (mamba_cache_mode 'all') + dspark spec decode crashes at startup — prev_last_scheduled_idx never passed by MambaHybridAttnMetadata

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#52330](https://github.com/vllm-project/vllm/issues/52330) [Bug]: Data-parallel startup ignores DP in startup_omp_num_threads, causing CPU thread oversubscription and 15x slower weight loading (engine-ready timeout)
- [Bug] 🆕 [#52319](https://github.com/vllm-project/vllm/issues/52319) [Bug]: Silent generation stall (Avg generation throughput drops to 0.0, no errors, /health and /v1/chat/completions still return 200) on Qwen3.5-397B-A17B / Qwen3.5-397B-A17B-FP8 / Qwen3.5-122B-A10B across v0.18.0, v0.19.0, v0.25.1
- [Feature] 🆕 [#52347](https://github.com/vllm-project/vllm/issues/52347) [Feature]: Native OCP MXFP6 execution on NVIDIA SM120

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#34800](https://github.com/sgl-project/sglang/issues/34800) [Bug] macOS: shared-memory names can exceed the 31-char POSIX limit, deadlocking `in_the_same_node_as` with no error output

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#34786](https://github.com/sgl-project/sglang/issues/34786) [Bug] TypeError in set_mamba_track_indices_from_reqs during NEXTN TARGET_VERIFY — mamba_next_track_idx is None (hybrid-mamba + speculative decoding + lazy buffer mode)

### vllm-project/vllm

- [Bug] 🆕 [#52262](https://github.com/vllm-project/vllm/issues/52262) [Bug]: Error while trying Speculative Decoding on Intel XPU for Qwen/Qwen3.6-35B-A3B
- [Feature] 🆕 [#52258](https://github.com/vllm-project/vllm/issues/52258) [Feature]: Restore length-based speculation skip (speculative max_model_len) or per-request speculative decoding control in V1

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#34772](https://github.com/sgl-project/sglang/issues/34772) [Bug][Diffusion] Native-fallback component loading drops all CPU-offload decisions (should_offload called without model_config) → fatal OOM on 8GB GPUs

## Build / Install / Platform

### sgl-project/sglang

- [Feature] 🆕 ⚠maintainer-authored [#34758](https://github.com/sgl-project/sglang/issues/34758) [Feature] Router GEMM should keep fp32 output under deterministic inference (DeepSeek V3/V4)

### vllm-project/vllm

- [Bug] 🆕 [#52306](https://github.com/vllm-project/vllm/issues/52306) [Bug]:  A multimodal item can still be split across prefill chunks with disable_chunked_mm_input=True
- [Bug] 🆕 [#52280](https://github.com/vllm-project/vllm/issues/52280) [Bug]: Muse-glimmer flawed on formatting (qwen3.6-35b also affected): so many Latex escape errors?

## Uncategorized

### vllm-project/vllm

- [Bug] 🆕 [#52300](https://github.com/vllm-project/vllm/issues/52300) [Bug]:  ImportError: libcudart.so.13: cannot open shared object file: No such file or directory
