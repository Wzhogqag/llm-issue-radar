# LLM Serving Issue Radar

_Last run: 2026-08-04T14:01+00:00_

**26 issues** — sgl-project/sglang: 10, vllm-project/vllm: 16 — 🆕 **26 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 5
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 6
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#33507](https://github.com/sgl-project/sglang/issues/33507) [Bug]

### vllm-project/vllm

- [Bug] 🆕 [#51008](https://github.com/vllm-project/vllm/issues/51008) [Bug]: Under MTP + chunked prefill, GDN runs eager Python only in prefill-mixed steps, and the MTP proposer forwards are forced to PIECEWISE (`llm_base_proposer` omits `uniform_decode`)

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#33549](https://github.com/sgl-project/sglang/issues/33549) [Bug] DeepSeek-V4 (dsv4 backend + DSPARK) TP=8 on 8×H20: decode forward hangs indefinitely at ~245K context — all GPUs spin at 100% util / low power, watchdog kills server
- [other] 🆕 [#33547](https://github.com/sgl-project/sglang/issues/33547) [MLX] Retracted request's decode KV can flush into a reused req_to_token row on the next extend forward

### vllm-project/vllm

- [Bug] 🆕 [#50953](https://github.com/vllm-project/vllm/issues/50953) [Bug][Rocm] LMcache running issues for the kimik3 Dspark

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33528](https://github.com/sgl-project/sglang/issues/33528) [Bug] Encountered an error while loading the Minimaxh3 model.

### vllm-project/vllm

- [Feature] 🆕 [#50963](https://github.com/vllm-project/vllm/issues/50963) [Feature]: shared expert fusion via Flashinfer kernels

## Quantization

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#33522](https://github.com/sgl-project/sglang/issues/33522) [Roadmap] Fast Engine Recovery: Weight Cache Daemon
- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#33470](https://github.com/sgl-project/sglang/issues/33470) inference_mode mismatch can break lazy buffers

### vllm-project/vllm

- [Bug] 🆕 [#50968](https://github.com/vllm-project/vllm/issues/50968) [Bug]: Kimi-K2.6 TP=4 segfaults in gptq_marlin_repack on GB200 ARM64 with vLLM 0.26.0
- [Bug] 🆕 [#50934](https://github.com/vllm-project/vllm/issues/50934) [Bug]: CUDA misaligned address crash on GB10 (sm_121) after ~10 days uptime — Nemotron NVFP4 + Marlin MoE + MTP speculative decoding
- [Bug] 🆕 [#50925](https://github.com/vllm-project/vllm/issues/50925) [Bug]: NVFP4 MoE falls back to Marlin on sm_121 (GB10) in published builds, making the model unservable on a unified 121 GiB pool

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#50938](https://github.com/vllm-project/vllm/issues/50938) [Bug]: Text emitted before the reasoning start tag escapes both the gemma4 parser and structured output, breaking json_schema responses
- [Bug] 🆕 [#50924](https://github.com/vllm-project/vllm/issues/50924) [Bug]: EngineCore dies on first guided-decoding request when dspark speculative decoding is enabled (grammar bitmask width mismatch)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#33501](https://github.com/sgl-project/sglang/issues/33501) [Bug] MiniMax H3 failed to run。
- [Bug] 🆕 [#33454](https://github.com/sgl-project/sglang/issues/33454) [Bug] DSpark verify window crosses the model context boundary and causes an illegal RoPE read

### vllm-project/vllm

- [Bug] 🆕 [#50954](https://github.com/vllm-project/vllm/issues/50954) [Bug]: System crash: Rust panic loading a tiktoken vocab file with duplicate ranks
- [Bug] 🆕 [#50927](https://github.com/vllm-project/vllm/issues/50927) [Bug]: stack overflow causing system crash: Rust unbounded recursion in the Gemma4 unified parser

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#33483](https://github.com/sgl-project/sglang/issues/33483) [Bug] Default decode CUDA Graph coverage causes a sharp performance cliff when batch size exceeds 32

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#33466](https://github.com/sgl-project/sglang/issues/33466) [Bug] MiniMax-H3 occurs args error

### vllm-project/vllm

- [Bug] 🆕 [#51009](https://github.com/vllm-project/vllm/issues/51009) [Bug]: DSpark acceptance collapses after position 0 on DeepSeek-V4-Flash-0731 (0.26.1rc1)
- [Bug] 🆕 [#50989](https://github.com/vllm-project/vllm/issues/50989) [Bug]: Qwen 3.* models go into doom loop if you use strict mode with tools without arguments.
- [Bug] 🆕 [#50948](https://github.com/vllm-project/vllm/issues/50948) [Bug]: Qwen parser routes grammar-constrained JSON to reasoning when `enable_in_reasoning=true`
- [Bug] 🆕 [#50947](https://github.com/vllm-project/vllm/issues/50947) [Bug]: Kimi-K3 PP>1 with IndexError: index_fill_(): Expected dtype int64 for index
- [RFC] 🆕 [#50966](https://github.com/vllm-project/vllm/issues/50966) [RFC]: Pluggable structured-output backends + GRID as a third contract point (declared outcomes for schemas you don't control)

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#51023](https://github.com/vllm-project/vllm/issues/51023) [Feature]: Parse Request Priority from HTTP Header
