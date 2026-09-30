# LLM Serving Issue Radar

_Last run: 2026-09-30T13:33+00:00_

**16 issues** — sgl-project/sglang: 5, vllm-project/vllm: 11 — 🆕 **16 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 4
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 5

## Scheduler / Batching

### vllm-project/vllm

- [RFC] 🆕 [#59382](https://github.com/vllm-project/vllm/issues/59382) [RFC]: MoRIIO WRITE failure handling and safe KV block reclamation

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#59415](https://github.com/vllm-project/vllm/issues/59415) [Bug]: Qwen3.6-35B-A3B-FP8 model with TP 4 gives gibberish output !!!!!!!!!!!! on Intel B70 cards

## Attention Backend

### sgl-project/sglang

- [other] 🆕 [#41852](https://github.com/sgl-project/sglang/issues/41852) [AMD][Diffusion] Add a reliable gfx1151 attention path without AOTriton

### vllm-project/vllm

- [Bug] 🆕 [#59404](https://github.com/vllm-project/vllm/issues/59404) [Bug] vendored flash_linear_attention chunk_o.py drops upstream mask before exp(), so boundary chunks can exponentiate unspecified lanes

## Quantization

### sgl-project/sglang

- [RFC] 🆕 [#41853](https://github.com/sgl-project/sglang/issues/41853) [RFC] Gluon MegaMoE: EP8 MXFP4 and EP16 FP8 Support

### vllm-project/vllm

- [Bug] 🆕 [#59403](https://github.com/vllm-project/vllm/issues/59403) [Bug] Marlin int8-activation path reads negative group scales as unsigned, corrupting every such group
- [Bug] 🆕 [#59381](https://github.com/vllm-project/vllm/issues/59381) [Bug]: Qwen3.5-35B-A3B merged SFT BF16 intermittently produces NaN logits and exclamation-only output on H20 (v0.19.1; HF control finite)
- [other] 🆕 ⚠maintainer-authored [#59433](https://github.com/vllm-project/vllm/issues/59433) [Startup UX]: Serial per-process Python imports across the API server → EngineCore → worker tree add significant startup time

## Sampling / Speculative Decoding

### vllm-project/vllm

- [RFC] 🆕 [#59365](https://github.com/vllm-project/vllm/issues/59365) [RFC]: /v1/decisions: First-class Jev typed decision endpoint in the API server (with /v1/systemone compatibility)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#41863](https://github.com/sgl-project/sglang/issues/41863) [Bug] [Diffusion] Hybrid SP+TP does not work correctly for the I2V models

### vllm-project/vllm

- [Bug] 🆕 [#59394](https://github.com/vllm-project/vllm/issues/59394) [Bug] DeepSeek-V4.1-Flash cannot use TP > 8: Engram hash-head sharding assertion rejects tp_size=16 across 2 nodes

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#41828](https://github.com/sgl-project/sglang/issues/41828) [Bug] PEFT adapters with bias="lora_only" or "all" crash or silently corrupt weights during normalize_qkv_proj
- [other] 🆕 ⚠maintainer-authored [#41892](https://github.com/sgl-project/sglang/issues/41892) [diffusion] LTX-2: overlap MP4 encode with VAE decode (follow-up to #41819)

### vllm-project/vllm

- [Bug] 🆕 [#59375](https://github.com/vllm-project/vllm/issues/59375) [Bug]: SIGTERM during engine startup is swallowed by zmq_socket_ctx; API server hangs until VLLM_ENGINE_READY_TIMEOUT_S
- [Bug] 🆕 [#59362](https://github.com/vllm-project/vllm/issues/59362) [Bug]: FA4 ignores `num_splits` on SM90 in v0.30.0 causing upto 48% slower decode
- [Feature] 🆕 [#59354](https://github.com/vllm-project/vllm/issues/59354) [Feature]: shechduling using predicted decode output length
