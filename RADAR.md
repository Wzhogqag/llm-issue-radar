# LLM Serving Issue Radar

_Last run: 2026-09-03T13:28+00:00_

**18 issues** — sgl-project/sglang: 6, vllm-project/vllm: 12 — 🆕 **18 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 5
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#55140](https://github.com/vllm-project/vllm/issues/55140) [Bug] HunyuanOCR (Transformers backend) crashes on startup: "Expected 4 multimodal RoPE channels, got position_ids with shape (3, 1, N)"
- [Feature] 🆕 [#55155](https://github.com/vllm-project/vllm/issues/55155) [Feature]: Restart Lifecycle Hooks for KV Transfer Connectors (NIXL)

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#55132](https://github.com/vllm-project/vllm/issues/55132) [Bug][ROCm] Sparse-MLA indexer reserves a 32 GiB decode-logits workspace during profiling (max_num_batched_tokens rows), costing 21 % of the KV cache
- [Bug] 🆕 [#55046](https://github.com/vllm-project/vllm/issues/55046) [Bug]: embedding cache dtype combination finds no valid CUDA attention backend

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#37755](https://github.com/sgl-project/sglang/issues/37755) [Bug] MiMo-V2.5-Pro-W8A8 load weight failed via modelslim
- [Bug] 🆕 [#37712](https://github.com/sgl-project/sglang/issues/37712) [Bug] GLM-5.3-Flash: CUDA OOM in fp8_mqa_logits during long-context prefill kills all TP ranks
- [other] 🆕 [#37813](https://github.com/sgl-project/sglang/issues/37813) [Tracking] GLM-5.3-Flash on SM120 (RTX PRO 6000 / GB202): what it needs to work, be correct and be fast

### vllm-project/vllm

- [Bug] 🆕 [#55048](https://github.com/vllm-project/vllm/issues/55048) [Bug]: encoder attention rejects quantized KV cache only at request time
- [Feature] 🆕 [#55129](https://github.com/vllm-project/vllm/issues/55129) [Feature][CPU][Arm]: Add SME1 (FEAT_SME) dispatch for KleidiAI/QMX kernels

## Distributed / TP / PP / EP

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#55131](https://github.com/vllm-project/vllm/issues/55131) Batch-invariant matmul is not actually batch-invariant, and TF32 causes precision degradation

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#37710](https://github.com/sgl-project/sglang/issues/37710) [Feature] KVCache can support dtype:int

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Feature] 🆕 [#37772](https://github.com/sgl-project/sglang/issues/37772) [Feature] LoRA adapter support for Dspark speculative decoding draft models

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#37817](https://github.com/sgl-project/sglang/issues/37817) [Bug] DFlash misses Mamba checkpoints when accepted tokens cross a tracking boundary

## Performance / Memory / OOM

### vllm-project/vllm

- [Feature] 🆕 [#55117](https://github.com/vllm-project/vllm/issues/55117) [Feature]: Let `vllm launch render` / `--tokens-only` override an inherited `VLLM_ENABLE_SCALE_OUT_ENDPOINTS=0` instead of failing startup

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#55052](https://github.com/vllm-project/vllm/issues/55052) [Bug]: multimodal mm_encoder_only conversion fails across model families
- [Bug] 🆕 [#55050](https://github.com/vllm-project/vllm/issues/55050) [Bug]: encoder prompt embeddings trigger a compiled AttributeError
- [Bug] 🆕 [#55049](https://github.com/vllm-project/vllm/issues/55049) [Bug]: prefix caching and KV-scale calculation assert on encoder models
- [Bug] 🆕 [#55139](https://github.com/vllm-project/vllm/issues/55139) [Bug]: PP performance drop when MRV2 is set by default.
