# LLM Serving Issue Radar

_Last run: 2026-09-20T13:25+00:00_

**19 issues** — sgl-project/sglang: 4, vllm-project/vllm: 15 — 🆕 **17 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 5
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#57738](https://github.com/vllm-project/vllm/issues/57738) [RFC]: Encoder-Only Prefill in P/D deployment for DeepSeek V4.1 Flash
- [Bug] [#57691](https://github.com/vllm-project/vllm/issues/57691) [Bug]: Task cancellation during _commit_scale_down_elastic_ep corrupts cluster state without rollback

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#40360](https://github.com/sgl-project/sglang/issues/40360) [Bug] Abort cleanup hook has no well-defined ordering vs. cache_finished_req: FlexKV needs it before, LMCache needs it after (session leak)

### vllm-project/vllm

- [Bug] 🆕 [#57716](https://github.com/vllm-project/vllm/issues/57716) [Bug] Kimi-K3 TP8xPP2 + DSpark spec-on: mid-decode target-forward NaN detonates MLA decode under concurrency (fp8 latent-cache bytes carry the corruption)

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 [#57712](https://github.com/vllm-project/vllm/issues/57712) [Feature]: OutOfResources: shared memory (98304 > 65536) on Turing (SM75) — global attention layers with head_dim=512

## Quantization

### sgl-project/sglang

- [Feature] 🆕 [#40437](https://github.com/sgl-project/sglang/issues/40437) [Feature][weight-cache] Support DeepSeek-V4-Flash MXFP4 IPC loading
- [no-prefix] 🆕 ⚠no-prefix [#40432](https://github.com/sgl-project/sglang/issues/40432) 4*5090 run nvidia/Qwen3.8-Flash-Next-NVFP4

### vllm-project/vllm

- [Bug] 🆕 [#57748](https://github.com/vllm-project/vllm/issues/57748) [Bug]: Running GLM-5.3-Flash-NVFP4 on Hopper GPUs
- [Bug] 🆕 ⚠maintainer-authored [#57713](https://github.com/vllm-project/vllm/issues/57713) [Bug]: GLM5.3-Flash does not support fp8 kv cache dtype on hopper
- [Feature] 🆕 [#57772](https://github.com/vllm-project/vllm/issues/57772) [Feature]: mega-MoE expert path for SM90 (H100/H20) DeepSeek-V4 / V4.1-Flash — Marlin weight-only is the only option today

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#57720](https://github.com/vllm-project/vllm/issues/57720) [Bug]: Mamba-hybrid models (granite-4.0-h) give a different, garbled greedy answer every time for a ONE-token prompt under full CUDA graphs
- [no-prefix] 🆕 ⚠no-prefix [#57755](https://github.com/vllm-project/vllm/issues/57755) Title

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#40417](https://github.com/sgl-project/sglang/issues/40417) [Bug] humming MoE runner picks tuning config with a 4x-inflated shape under EP, and the obvious EP-aware fix regresses serving

### vllm-project/vllm

- [Bug] 🆕 [#57730](https://github.com/vllm-project/vllm/issues/57730) [Bug]: /tokenize returns 400 "cannot pickle ValidatorIterator" for assistant `content: null` + `tool_calls` (DeepSeek-V4.1), while chat completions accepts the same messages
- [Bug] 🆕 [#57699](https://github.com/vllm-project/vllm/issues/57699) [Bug]: qwen3_coder tool parser drops the last parameter when the model omits </parameter> before </function> (non-streaming {}, streaming unterminated JSON)
- [Bug] 🆕 [#57688](https://github.com/vllm-project/vllm/issues/57688) [Bug][Reasoning] kimi_k3: streaming path classifies a response-only completion as reasoning (diverges from non-streaming after #57098)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#57727](https://github.com/vllm-project/vllm/issues/57727) [Bug]: `POST /reset_prefix_cache` returns success while the CPU offload tier keeps serving the same blocks
- [Bug] 🆕 [#57714](https://github.com/vllm-project/vllm/issues/57714) [Bug][Reasoning] kimi_k3: structured output never engages when the completion skips the think channel
- [other] [#57684](https://github.com/vllm-project/vllm/issues/57684) [Question] Support path for platform plugins that cannot install Triton (MRV2 requires it)
