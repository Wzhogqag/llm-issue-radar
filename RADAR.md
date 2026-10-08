# LLM Serving Issue Radar

_Last run: 2026-10-08T13:36+00:00_

**16 issues** — sgl-project/sglang: 8, vllm-project/vllm: 8 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Attention Backend](#attention-backend) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 2
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#43061](https://github.com/sgl-project/sglang/issues/43061) [Bug] `--enable-deterministic-inference` + one request with `repetition_penalty` kills the scheduler on granite-4.0-h (torch.compile `InternalTorchDynamoError` in `apply_scaling_penalties`)
- [no-prefix] 🆕 ⚠no-prefix [#43050](https://github.com/sgl-project/sglang/issues/43050) Idle-wake hang at _low_ratio_index_topk_dense when --sleep-on-idle is enabled (post-#40111 prefill host-sync path)

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#43055](https://github.com/sgl-project/sglang/issues/43055) [Bug] `--enable-deterministic-inference` does not make gpt-oss-20b deterministic: `test_deterministic --test-mode prefix` returns several outputs for one prompt

### vllm-project/vllm

- [Bug] 🆕 [#60587](https://github.com/vllm-project/vllm/issues/60587) [Bug] DeepSeek-V4-Flash-Vision-Exp fails at engine init on v0.31.0: deep_gemm_fp8_o_proj shape mismatch '[4, 4096] vs [4, 1024]' from BOTH sparse-MLA backends (sm_121)
- [no-prefix] 🆕 ⚠no-prefix [#60551](https://github.com/vllm-project/vllm/issues/60551) External speculators (DSpark Qwen3 draft, DFlash2) crash with kv_cache_dtype=nvfp4_ds_mla on GLM-5.3 NVFP4: draft-model code assumes split k/v

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#60611](https://github.com/vllm-project/vllm/issues/60611) [Bug]: AOT compile artifacts fail to load with mode `DYNAMO_TRACE_ONCE`
- [Feature] 🆕 [#60563](https://github.com/vllm-project/vllm/issues/60563) [Feature]: Support per-parameter meshes in NCCL M2N weight transfer

## New Model Integration

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#43007](https://github.com/sgl-project/sglang/issues/43007) MiniMax-H3: blocky moving face in pre-encode RGB at 32 steps / short_edge 768 (evidence pack; exact prompt withheld)

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#43085](https://github.com/sgl-project/sglang/issues/43085) [Bug]

### vllm-project/vllm

- [Bug] 🆕 [#60580](https://github.com/vllm-project/vllm/issues/60580) [Bug]: xgrammar lets Muse Glimmer control tokens (<|eom|>, <|start|>, <|message|>) into JSON strings; muse_glimmer parser then silently truncates the answer
- [Feature] 🆕 [#60622](https://github.com/vllm-project/vllm/issues/60622) [Feature]: Export live EAGLE-3 training data (committed tokens + aux hidden states) for online draft-model adaptation

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#43096](https://github.com/sgl-project/sglang/issues/43096) Detokenizer return-path fanout performs one IPC send per request

### vllm-project/vllm

- [Bug] 🆕 [#60629](https://github.com/vllm-project/vllm/issues/60629) [Bug]: Boolean sweep plot filters discard or retain the wrong benchmark runs

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 [#43038](https://github.com/sgl-project/sglang/issues/43038) [Qwen4-Exp] aux-hidden capture at stage boundaries yields the hyper-connection-wide stream — intended width contract for consumers?

### vllm-project/vllm

- [Bug] 🆕 [#60536](https://github.com/vllm-project/vllm/issues/60536) [Bug]: GLM-5.3-Flash JIT-compiles DeepGEMM `tf32_hc_prenorm_gemm` during serving (20 mHC split-K variants are never warmed)

## Uncategorized

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#43034](https://github.com/sgl-project/sglang/issues/43034) A question about SGLang and SGLang Omni
