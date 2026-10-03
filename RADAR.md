# LLM Serving Issue Radar

_Last run: 2026-10-03T14:39+00:00_

**17 issues** — sgl-project/sglang: 3, vllm-project/vllm: 14 — 🆕 **15 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Build / Install / Platform](#build--install--platform) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#42272](https://github.com/sgl-project/sglang/issues/42272) [Bug] Anthropic /v1/messages: inline system messages are still merged into the top system block on system-first templates (Qwen), so the prefix cache misses every turn

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] [#59768](https://github.com/vllm-project/vllm/issues/59768) [Bug]: Illegal memory access (Xid 13) with SimpleCPUOffloadConnector on Qwen3.8-Flash-Next while an async CPU→GPU prefix load is in flight / sm120

## Attention Backend

### vllm-project/vllm

- [RFC] 🆕 [#59773](https://github.com/vllm-project/vllm/issues/59773) [RFC]: Octave KV, a native 3-bit KV cache for AMD GPUs

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#42361](https://github.com/sgl-project/sglang/issues/42361) [Bug] DeepSeek V4 Pro loading on Lustre takes 95 minutes despite prefetch; limiting tensor-copy workers reduces it to 3.3 minutes
- [Feature] 🆕 [#42392](https://github.com/sgl-project/sglang/issues/42392) [Feature] File-backed PLE table: concurrent host reads for cold rows (6.8x lower cold-prefill TTFT on GB10)

### vllm-project/vllm

- [Bug] 🆕 [#59876](https://github.com/vllm-project/vllm/issues/59876) [Bug]: Multimodal chat requests silently drop all images when request-level chat_template_kwargs is present (v0.30.0, Gemma-4-26B-A4B)
- [Bug] 🆕 [#59798](https://github.com/vllm-project/vllm/issues/59798) [Bug]: Qwen3.8-Flash-Next AutoRound/INC checkpoint fails because PLE rejects INCConfig even though PLE is unquantized
- [other] 🆕 [#59868](https://github.com/vllm-project/vllm/issues/59868) [Qwen4Exp] PLE pinned-host FP8 lookup will not compile on sm_86, so --engram-config cpu_offload is unusable on consumer Ampere
- [Performance] [#59770](https://github.com/vllm-project/vllm/issues/59770) [Performance]: Nemotron-3.5-Lightning NVFP4 decode ~16% slower on DGX Spark (GB10/SM121) since v0.29.0

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#59784](https://github.com/vllm-project/vllm/issues/59784) [Bug]: Qwen3-VL-Reranker fails to load because Qwen3VLTextConfig has no tie_word_embeddings
- [Feature] 🆕 [#59840](https://github.com/vllm-project/vllm/issues/59840) [Feature]: Support trainer-side pipeline parallelism with NCCL M2N weight transfer
- [Feature] 🆕 [#59835](https://github.com/vllm-project/vllm/issues/59835) [Feature]: Support fused MoE weights with NCCL M2N weight transfer

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#59786](https://github.com/vllm-project/vllm/issues/59786) [Bug][CPU] V1 CPU sampling (fused_gumbel_argmax) is biased: the 2^20 noise table makes about half of a 152K vocabulary unreachable
- [Bug] 🆕 [#59785](https://github.com/vllm-project/vllm/issues/59785) [Bug][CPU] apply_top_k_top_p_triton drops tokens that top-p must keep (kernel logic; reproduces end to end on V1 and V2)

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#59799](https://github.com/vllm-project/vllm/issues/59799) [Bug]:  LoRA adapters with PEFT rank_pattern / alpha_pattern are served with the wrong scaling
- [other] 🆕 [#59820](https://github.com/vllm-project/vllm/issues/59820) [ROCm][AMD] GLM5.3 Flash Performance Optimization on gfx950 / MI355X
- [other] 🆕 ⚠maintainer-authored [#59818](https://github.com/vllm-project/vllm/issues/59818) [ROCm]: run-to-run GSM8K accuracy variance for simple-nemotron-h-8b in KV-Offload test on MI300
