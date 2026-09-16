# LLM Serving Issue Radar

_Last run: 2026-09-16T13:29+00:00_

**15 issues** — sgl-project/sglang: 1, vllm-project/vllm: 14 — 🆕 **15 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 3
- [New Model Integration](#new-model-integration) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#57111](https://github.com/vllm-project/vllm/issues/57111) [RFC]: Checkpoint-aware cache eviction and segmented recomputation for hybrid models
- [RFC] 🆕 [#57106](https://github.com/vllm-project/vllm/issues/57106) [RFC]: [FS Offloading][ThreadPool] Updates to Thread Pool

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [RFC] 🆕 [#39740](https://github.com/sgl-project/sglang/issues/39740) [RFC] Pluggable KV Compression for Disaggregated Serving

### vllm-project/vllm

- [Bug] 🆕 [#57159](https://github.com/vllm-project/vllm/issues/57159) [Bug]: OffloadingConnector KV events advertise block hashes that are not independently retrievable
- [RFC] 🆕 [#57103](https://github.com/vllm-project/vllm/issues/57103) [RFC]: Programmable KV Cache: Composable Policies for Agentic Serving

## Attention Backend

### vllm-project/vllm

- [Feature] 🆕 [#57144](https://github.com/vllm-project/vllm/issues/57144) [Feature]: SM8x (Ampere A100/A800) support for DeepSeek-V4.1-Flash

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#57125](https://github.com/vllm-project/vllm/issues/57125) [Bug]: Qwen3.8-Flash-Next-NVFP4  service cannot start normally.
- [Bug] 🆕 [#57087](https://github.com/vllm-project/vllm/issues/57087) [Bug] GLM-5.3 hybrid (nvfp4, GB10/sm121, TP2): concurrent batching corrupts non-ASCII generation — fragment-token state poisoning + silent DecodeStream FFFD flush
- [other] 🆕 [#57149](https://github.com/vllm-project/vllm/issues/57149) [ROCm][AMD] Qwen3.8-2.4T-A95B gfx950 / MI355X Performance Optimization

## New Model Integration

### vllm-project/vllm

- [Feature] 🆕 [#57166](https://github.com/vllm-project/vllm/issues/57166) [Feature]: lora support for deepseek v4.1 flash

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#57173](https://github.com/vllm-project/vllm/issues/57173) [Bug]: Multi-turn benchmark drops unfinished active conversations when the task queue is exhausted
- [Bug] 🆕 [#57099](https://github.com/vllm-project/vllm/issues/57099) [Bug]: Encountered `openai_harmony.HarmonyError` when using GPT-OSS-120B.
- [other] 🆕 [#57157](https://github.com/vllm-project/vllm/issues/57157) [Security]: remote media URLs allow SSRF to internal/link-local addresses by default
- [no-prefix] 🆕 ⚠no-prefix [#57082](https://github.com/vllm-project/vllm/issues/57082) Engine-initiated aborts end chat completion streams as if they completed: HTTP 200, terminal finish_reason "abort" (not an OpenAI enum value), then an unconditional data: [DONE]

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#57177](https://github.com/vllm-project/vllm/issues/57177) [RFC]: Retain MRV2 DBO CUDA Graph replay under DP imbalance through real-token staging
