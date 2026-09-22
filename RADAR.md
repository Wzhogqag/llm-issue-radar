# LLM Serving Issue Radar

_Last run: 2026-09-22T13:30+00:00_

**9 issues** — sgl-project/sglang: 4, vllm-project/vllm: 5 — 🆕 **9 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#58063](https://github.com/vllm-project/vllm/issues/58063) [Bug] NixlConnector on MNNVL/GB200: remote engine state is released only on new-engine handshake or shutdown, deadlocking P/D prefill replacement

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#58060](https://github.com/vllm-project/vllm/issues/58060) [Performance][ROCm]: Narrower KV tiles speed up Triton embedding/reranking attention on RDNA3/RDNA4

## Quantization

### sgl-project/sglang

- [Feature] 🆕 [#40706](https://github.com/sgl-project/sglang/issues/40706) [Feature] Add FP8 SSM state pool (`--mamba-ssm-dtype float8`) for GDN hybrid models
- [Bug] 🆕 ⚠maintainer-authored [#40623](https://github.com/sgl-project/sglang/issues/40623) [Bug] Illegal memory access in the Triton fused-MoE kernel when `flashinfer_megamoe` is combined with EAGLE speculative decoding (GLM-5.2-NVFP4, sm_107)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#40744](https://github.com/sgl-project/sglang/issues/40744) [Bug] DSV v4.1 Flash 2x4 H200 TP8/EP8 + DSPARK causes startup deadlock after DSpark draft weight load on dev-cu13-dsv41 and latest dev-cu13 image
- [Bug] 🆕 [#40735](https://github.com/sgl-project/sglang/issues/40735) [Bug] MiniMax-M3 incorrectly routes Ascend FuseEP through the normal MoE path

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#58145](https://github.com/vllm-project/vllm/issues/58145) [Bug]: Mistral's "always adjust_request" grammar path rebuilds the tool parser and compiles regex over the full vocab on the main event loop, on every request — even tool_choice="none"
- [Bug] 🆕 [#58144](https://github.com/vllm-project/vllm/issues/58144) [Bug]: `--api-key` is bypassed by `/invocations`, unauthenticated inference on a server that requires a key
- [Bug] 🆕 [#58105](https://github.com/vllm-project/vllm/issues/58105) [Bug]: Qwen streaming loses tool calls when text grammar permits ordinary-token delimiters
