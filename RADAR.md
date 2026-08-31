# LLM Serving Issue Radar

_Last run: 2026-08-31T13:29+00:00_

**22 issues** — sgl-project/sglang: 4, vllm-project/vllm: 18 — 🆕 **22 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 4
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Build / Install / Platform](#build--install--platform) — 8
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#54536](https://github.com/vllm-project/vllm/issues/54536) [Feature][KV-offloading]: Host-staged RDMA for MooncakeStoreConnector requester-only ranks

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#54567](https://github.com/vllm-project/vllm/issues/54567) [Bug]: Prefix caching never hits for DeepSeek-V4-Flash on Jetson Thor (SM110) — every request cold-prefills, TTFT scales linearly with context

## Quantization

### sgl-project/sglang

- [Feature] 🆕 [#37150](https://github.com/sgl-project/sglang/issues/37150) [Feature] Tuning / per-GPU config for DSv4 top-k v2 cluster launch plan (kClusterFloor / kNumPersistentClusters / kCandidates)

### vllm-project/vllm

- [Bug] 🆕 [#54559](https://github.com/vllm-project/vllm/issues/54559) [Bug]: qwen3.8-flash-next-fp8: No available shared memory broadcast block found in 60 seconds.
- [Bug] 🆕 [#54521](https://github.com/vllm-project/vllm/issues/54521) [Bug]: Qwen3.8-Flash-Next: greedy decoding is non-deterministic from persistent_topk in prefill when prompt length nears indexer_budget (sm121/GB10)
- [RFC] 🆕 ⚠maintainer-authored [#54477](https://github.com/vllm-project/vllm/issues/54477) [RFC]: Selective Weight Reload for RL Training

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#37215](https://github.com/sgl-project/sglang/issues/37215) [Bug] --dp 8 intermittently fails with TCPStore EADDRINUSE on single-node 8×H800

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#54459](https://github.com/vllm-project/vllm/issues/54459) [Bug] [Portability][MSVC]: M_LOG2E is unavailable when building Flash Attention with NVCC and MSVC

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#54555](https://github.com/vllm-project/vllm/issues/54555) [Bug]: V1 spec-decode proposer never constructs the positions buffer a both-XD-RoPE drafter seeds from
- [Bug] 🆕 [#54526](https://github.com/vllm-project/vllm/issues/54526) [Bug]: Cannot load an Eagle3 model, trained with Speculators
- [RFC] 🆕 [#54506](https://github.com/vllm-project/vllm/issues/54506) [RFC]: Batch invariance for speculative decoding needs to cover the forward pass (M=1 vs M=k+1)
- [no-prefix] 🆕 ⚠no-prefix [#54552](https://github.com/vllm-project/vllm/issues/54552) Qwen4Exp: QSA ring assert makes num_speculative_tokens 5..8 unreachable on all block sizes

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Feature] 🆕 [#54528](https://github.com/vllm-project/vllm/issues/54528) [Feature]: Migrate MuseGlimmer reasoning/tool parsers to the Streaming Parser Engine

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#37183](https://github.com/sgl-project/sglang/issues/37183) AMD MI308X SGLang GLM-5.3-Flash ValueError: The checkpoint you are trying to load has model type `glm5_next` but Transformers does not recognize this architecture.

### vllm-project/vllm

- [Bug] 🆕 [#54569](https://github.com/vllm-project/vllm/issues/54569) [Bug]: FunASR get error result with fp16 dtype
- [Bug] 🆕 [#54493](https://github.com/vllm-project/vllm/issues/54493) [Bug]: --enable-dbo reaches an assertion-backed all2all backend validation failure
- [Bug] 🆕 [#54491](https://github.com/vllm-project/vllm/issues/54491) [Bug]: Qwen2.5 tool parser plus openai content format fails chat requests
- [Bug] 🆕 [#54490](https://github.com/vllm-project/vllm/issues/54490) [Bug]: enabling prefix caching changes deterministic repeated output
- [Bug] 🆕 [#54487](https://github.com/vllm-project/vllm/issues/54487) [Bug]: prefix-caching hash configuration changes deterministic repeated output
- [Bug] 🆕 [#54486](https://github.com/vllm-project/vllm/issues/54486) [Bug]: openai chat-template content format breaks structured request contracts
- [Feature] 🆕 [#54497](https://github.com/vllm-project/vllm/issues/54497) [Feature]: Upgrade XGrammar to >=0.2.4 and expose max_whitespace_cnt

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#37238](https://github.com/sgl-project/sglang/issues/37238) Does SGLang have a demo for running the VBench dataset accuracy evaluation on Wan2.2?
