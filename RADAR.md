# LLM Serving Issue Radar

_Last run: 2026-11-22T13:22+00:00_

**14 issues** — sgl-project/sglang: 5, vllm-project/vllm: 9 — 🆕 **14 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#69237](https://github.com/vllm-project/vllm/issues/69237) [Feature]: Process checkpoint support for the native CPU KV offload connector (OffloadingConnector)

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#52274](https://github.com/sgl-project/sglang/issues/52274) [Bug] gemma4: Vision attention ignores the padding mask on fa3 / fa4 / triton_attn

### vllm-project/vllm

- [Bug] 🆕 [#69228](https://github.com/vllm-project/vllm/issues/69228) [Bug]: Intermittent CUDA OOM in DCP a2a combine fallback (`_dcp_a2a_send_recv_buffers`) at high concurrency with short prompts — Kimi-K3.1-Pro, TP8 + DCP8, `gpu-memory-utilization 0.97`

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#52318](https://github.com/sgl-project/sglang/issues/52318) [Bug] Qwen3-Omni: vision and audio layers are built under names the quantization ignore list never matches, so cyankiwi/Qwen3-Omni-30B-A3B-Instruct-AWQ-4bit fails to start

### vllm-project/vllm

- [Bug] 🆕 [#69183](https://github.com/vllm-project/vllm/issues/69183) [Bug]: compressed-tensors W4A8 int (CompressedTensorsWNA8Int) serves W4A16 on SM86: Marlin takes the layer, and with Humming forced, the groupwise fallback drops the int8 input
- [Feature] 🆕 [#69156](https://github.com/vllm-project/vllm/issues/69156) [Feature]: Inkling 2 Mini on Ampere/Ada (SM80/86/89)

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Perf] 🆕 [#52213](https://github.com/sgl-project/sglang/issues/52213) [Perf] hicache: unconditional _all_reduce_attn_groups in the drain collective when the linker is idle

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#52215](https://github.com/sgl-project/sglang/issues/52215) [Bug][CP] DeepSeek-V4.1-Flash pre_from_prev + CP8: vision MoE router input_ids shape mismatch in moe_fused_gate (a2a=none)

### vllm-project/vllm

- [Bug] 🆕 [#69154](https://github.com/vllm-project/vllm/issues/69154) [Bug]: GLM-5.3-Flash + MTP + prefix caching on v0.34.0 (B200, TP4): silent constant-token degeneration ("locklock…"), MTP acceptance collapses to 0, persists for requests sharing the prefix
- [Performance] 🆕 [#69152](https://github.com/vllm-project/vllm/issues/69152) [Performance]: Fused CUDA GDN MTP decode kernel stores a full recurrent state per draft token

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#69241](https://github.com/vllm-project/vllm/issues/69241) [Bug]: Parser engine tool parsers (granite, llama3_json, inkling): arguments sent as a JSON-encoded string stream as '' but are returned without streaming
- [Bug] 🆕 [#69161](https://github.com/vllm-project/vllm/issues/69161) [Bug]: olmo3 tool parser: text before <function_calls> is dropped (stream=false) or the tool call is lost (stream=true)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#52191](https://github.com/sgl-project/sglang/issues/52191) [Bug] Diffusion orchestrator: deeply nested result frame escapes per-request handler and stops routing loop

## Uncategorized

### vllm-project/vllm

- [Bug] 🆕 [#69173](https://github.com/vllm-project/vllm/issues/69173) [Bug]: hy_v4 tool parser returns an argument as a string when its schema uses allOf
