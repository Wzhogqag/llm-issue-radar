# LLM Serving Issue Radar

_Last run: 2026-09-28T13:34+00:00_

**24 issues** — sgl-project/sglang: 8, vllm-project/vllm: 16 — 🆕 **24 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#41471](https://github.com/sgl-project/sglang/issues/41471) [Bug] Two concurrent requests using DisallowedTokensLogitsProcessor with different token_ids crash the server
- [Bug] 🆕 [#41463](https://github.com/sgl-project/sglang/issues/41463) [Bug] Falcon-H1 with tied word embeddings cannot serve a single request, tied LM head's `.float()` upcasts the embedding in place

### vllm-project/vllm

- [Bug] 🆕 [#58931](https://github.com/vllm-project/vllm/issues/58931) [Bug]: MooncakeStoreConnector crashes EngineCore when a request is preempted by `reset_prefix_cache(reset_running_requests=True)` and re-admitted in the next step

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [other] 🆕 [#41514](https://github.com/sgl-project/sglang/issues/41514) [RFC / HiCache] Same-node peer L2 sharing across DP ranks via /dev/shm

### vllm-project/vllm

- [other] 🆕 [#59024](https://github.com/vllm-project/vllm/issues/59024) [Tracking]: Hidden-state extraction for GLM-5.3-Flash

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#41568](https://github.com/sgl-project/sglang/issues/41568) [Bug] MiMo-V2 processor fails to register when optional TorchCodec is unavailable

### vllm-project/vllm

- [Bug] 🆕 [#59027](https://github.com/vllm-project/vllm/issues/59027) [Bug][ROCm] v0.30.0: GLM-5.3-Flash cannot boot on gfx942 — ROCMAiterMLASparseImpl missing record_logical_topk_ready (#57252 not in the release)
- [RFC] 🆕 [#59016](https://github.com/vllm-project/vllm/issues/59016) [RFC]: Software-dequant fp8 KV cache for MLA on Ampere (sm80/sm86) — consolidate the existing pieces, a 1M-ctx field case, and a validation offer

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#41569](https://github.com/sgl-project/sglang/issues/41569) [Bug] MiMo-V2 selects the FP8 MoE runner for packed MXFP4 experts on SM100

### vllm-project/vllm

- [Bug] 🆕 [#58943](https://github.com/vllm-project/vllm/issues/58943) [Bug]: Official MiniCPM-V-4.6 GPTQ/AWQ checkpoints fail to load (vision tower built quantized)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#58954](https://github.com/vllm-project/vllm/issues/58954) [Bug]: QSA indexer uses cooperative_topk on sm_110 (Jetson AGX Thor) and fails with "cluster misconfiguration"
- [Bug] 🆕 [#58920](https://github.com/vllm-project/vllm/issues/58920) [Bug]: Any KV connector makes pipeline-parallel decode 50-90% slower on Model Runner V2 (all ranks reply, reply-ring writer spins holding the GIL)
- [other] 🆕 ⚠maintainer-authored [#58922](https://github.com/vllm-project/vllm/issues/58922) [ROCm] rocm_unquantized_gemm crashes on CPU tensors (dispatch ignores tensor device)

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 ⚠maintainer-authored [#58930](https://github.com/vllm-project/vllm/issues/58930) [Bug]: validate_xgrammar_grammar skips unsupported-feature checks for JSON schemas nested in structural tags
- [Feature] 🆕 [#58951](https://github.com/vllm-project/vllm/issues/58951) [Feature]: Support /v1/systemone endpoint for models like convaiinnovations/laya

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#41482](https://github.com/sgl-project/sglang/issues/41482) [Bug] `top_k`, `logprobs` and `n` have no upper bound, one request can DoS the server

### vllm-project/vllm

- [Bug] 🆕 [#58973](https://github.com/vllm-project/vllm/issues/58973) [Bug]: V2 speculative prefill can change Qwen3-4B's first greedy token through RMSNorm autotune configuration
- [other] 🆕 ⚠maintainer-authored [#58990](https://github.com/vllm-project/vllm/issues/58990) [Roadmap] Q4 2026 vLLM × RL

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#41510](https://github.com/sgl-project/sglang/issues/41510) AttributeError: 'ComponentData' object has no attribute 'parent'

### vllm-project/vllm

- [Bug] 🆕 [#58969](https://github.com/vllm-project/vllm/issues/58969) [Bug]: bench serve drops or mis-buckets several result fields, including all E2EL metrics for pooling
- [Bug] 🆕 [#58934](https://github.com/vllm-project/vllm/issues/58934) [Bug]: MiMo-V2.6 omni declares no embedding_fields, so an EPD encoder/consumer pair rejects every image with 400

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#41539](https://github.com/sgl-project/sglang/issues/41539) [Bug] A worker whose launcher died during startup sends SIGQUIT to PID 1

### vllm-project/vllm

- [Bug] 🆕 [#58937](https://github.com/vllm-project/vllm/issues/58937) [Bug][ROCm]: ROCm nightly images not published since 2026-09-25
- [other] 🆕 [#58928](https://github.com/vllm-project/vllm/issues/58928) [Installation]: macOS CPU build fails with Apple Clang 16 (structured binding capture under OpenMP in fla.cpp)
