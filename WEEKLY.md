# Weekly Trends — 2026-11-01

Window: 2026-10-26 → 2026-10-31 (6 snapshots)

**Totals:** 15 → 13  (13 appeared, 15 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 1 | 0 | 1 | 1 |
| Build / Install / Platform | 0 | 4 | +4 | 4 | 0 |
| Distributed / TP / PP / EP | 1 | 2 | +1 | 2 | 1 |
| KV Cache / Connector / PD Disagg | 1 | 1 | 0 | 1 | 1 |
| New Model Integration | 2 | 1 | -1 | 1 | 2 |
| Quantization | 4 | 2 | -2 | 2 | 4 |
| Sampling / Speculative Decoding | 1 | 0 | -1 | 0 | 1 |
| Serving / OpenAI API / Streaming | 3 | 2 | -1 | 2 | 3 |
| Uncategorized | 2 | 0 | -2 | 0 | 2 |

## Appeared this week

### Attention Backend

- [Bug] [vllm-project/vllm#64874](https://github.com/vllm-project/vllm/issues/64874) [Bug]: [ROCm][GLM-5.3-Flash]: "Workspace is locked" AssertionError in rocm_fp8_paged_mqa_logits under high decode concurrency (glm5next AMD indexer reserves decode logits via torch.empty, not the workspace)

### Build / Install / Platform

- [other] [sgl-project/sglang#47562](https://github.com/sgl-project/sglang/issues/47562) [AITER-Upgrade] PR readiness gfx1250 (MI45x)
- [Performance] [vllm-project/vllm#64791](https://github.com/vllm-project/vllm/issues/64791) [Performance][ROCm]: set HSA_SCRATCH_SINGLE_LIMIT in the ROCm image: per-dispatch scratch allocation costs ~130 us before large RCCL all-reduces on MI355X
- [Bug] [vllm-project/vllm#64809](https://github.com/vllm-project/vllm/issues/64809) [Bug]: `raw_logprobs` are computed after the structured-output grammar mask
- [Feature] [vllm-project/vllm#64866](https://github.com/vllm-project/vllm/issues/64866) [Feature]: [CI] Restore Ascend interface compatibility checks with locked test dependencies

### Distributed / TP / PP / EP

- [RFC] [vllm-project/vllm#64776](https://github.com/vllm-project/vllm/issues/64776) [RFC]: Single Batch Overlap (down GEMM ↔ combine) for DeepEP LL
- [RFC] [vllm-project/vllm#64780](https://github.com/vllm-project/vllm/issues/64780) [RFC]: DBO support for FlashInfer NVLink all-to-all backends (single-node H200/B200 first)

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#64790](https://github.com/vllm-project/vllm/issues/64790) [Bug]: In-tree LMCache integration can't be imported with lmcache >= 0.5.6

### New Model Integration

- [Bug] [vllm-project/vllm#64845](https://github.com/vllm-project/vllm/issues/64845) [Bug]: EmbeddingGemma 2 rejects `dimensions` by default although the model supports Matryoshka (128/256/512/768)

### Quantization

- [RFC] [sgl-project/sglang#47624](https://github.com/sgl-project/sglang/issues/47624) [RFC] NPU RL Test Consolidation: File Ownership, Coverage Docstrings, and CI Integration (Ascend)
- [Bug] [vllm-project/vllm#64814](https://github.com/vllm-project/vllm/issues/64814) [Bug]: MooncakeStoreConnector: one TP rank stalls (its GPU idle, peers spinning) on Kimi-K3 under agentic load

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#64778](https://github.com/vllm-project/vllm/issues/64778) [Bug]: Non-streaming `/v1/chat/completions/derender` and `/v1/completions/derender` report `usage.prompt_tokens: 0` when the request omits `prompt_tokens`, ignoring `generate_response.usage`
- [Bug] [vllm-project/vllm#64789](https://github.com/vllm-project/vllm/issues/64789) [Bug]: Responses API rejects `input_text` content for Mistral Large 4 with --tokenizer-mode mistral

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Feature] [vllm-project/vllm#63743](https://github.com/vllm-project/vllm/issues/63743) [Feature]: [Case Study] Agent Context Compaction Breaks RadixAttention Prefix Caching (10.1% -> 99.6% Hit Rate)

### Distributed / TP / PP / EP

- [Performance] [vllm-project/vllm#63705](https://github.com/vllm-project/vllm/issues/63705) [Performance]: MiniMax-M2.7 throughput regression on TP4+EP in vLLM 0.29 0.31 0.32

### KV Cache / Connector / PD Disagg

- [Bug] [vllm-project/vllm#63693](https://github.com/vllm-project/vllm/issues/63693) [Bug]: P/D disaggregation (NixlConnector): decode output differs from a non-disaggregated run whenever repetition_penalty != 1.0

### New Model Integration

- [other] [sgl-project/sglang#46550](https://github.com/sgl-project/sglang/issues/46550) [MUSA][help]
- [Feature] [sgl-project/sglang#46598](https://github.com/sgl-project/sglang/issues/46598) [Feature] Support reasoning and content continuation through model renderers/encoders

### Quantization

- [RFC] [sgl-project/sglang#46520](https://github.com/sgl-project/sglang/issues/46520) [RFC] [XPU] paged-experts: Intel XPU support with Lookahead Expert Scheduling (LES) and an SSD tier for iGPU, single-GPU MoE offload
- [other] [sgl-project/sglang#46579](https://github.com/sgl-project/sglang/issues/46579) [Roadmap] Humming integration maintenance
- [other] [sgl-project/sglang#46588](https://github.com/sgl-project/sglang/issues/46588) [Roadmap] TDX/CC Prefill–Decode Disaggregation
- [Bug] [vllm-project/vllm#63732](https://github.com/vllm-project/vllm/issues/63732) [Bug]: Gemma 4 + online --quantization fp8: image requests crash since v0.23.0 (FP8-cast pixel values reach quantized patch_embedder.input_proj); v0.22.0 works

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#46508](https://github.com/sgl-project/sglang/issues/46508) [Bug][MUSA] fa3: scheduler metadata is computed from the draft backend under speculative decoding, hanging when the radix cache hits

### Serving / OpenAI API / Streaming

- [Bug] [sgl-project/sglang#46566](https://github.com/sgl-project/sglang/issues/46566) [Bug] MiMoDetector: string "null" becomes None, invalid booleans become false, and text around tool calls is dropped
- [RFC] [vllm-project/vllm#63734](https://github.com/vllm-project/vllm/issues/63734) [RFC]: Define a graceful-draining contract for external Kubernetes controllers
- [Bug] [vllm-project/vllm#63751](https://github.com/vllm-project/vllm/issues/63751) [Bug]: IndexError in _create_chat_logprobs / _create_completion_logprobs (top_logprobs shorter than token_ids) causes 500s

### Uncategorized

- [other] [vllm-project/vllm#63741](https://github.com/vllm-project/vllm/issues/63741) [RFC / Performance] How LLM Agent Context Compaction Collapses Automatic Prefix Caching (APC)
- [Feature] [vllm-project/vllm#63744](https://github.com/vllm-project/vllm/issues/63744) [Feature]: [RFC / Performance] How LLM Agent Context Compaction Collapses Automatic Prefix Caching (APC)
