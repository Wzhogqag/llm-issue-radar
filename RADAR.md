# LLM Serving Issue Radar

_Last run: 2026-09-01T13:28+00:00_

**42 issues** — sgl-project/sglang: 11, vllm-project/vllm: 31 — 🆕 **42 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 4
- [Quantization](#quantization) — 13
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 6
- [Uncategorized](#uncategorized) — 3

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#37372](https://github.com/sgl-project/sglang/issues/37372) [Feature] [RFC] [HiCache] Out-of-process HiCache data plane with device-memory IPC

### vllm-project/vllm

- [RFC] 🆕 [#54749](https://github.com/vllm-project/vllm/issues/54749) [RFC]: The dynamic-SD K decision is a batch-keyed array index — agreeing on its shape before more signals arrive

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#37430](https://github.com/sgl-project/sglang/issues/37430) [Bug] Kimi-K3 tool_choice=required requests hang until ReadTimeout in 2P2D TP8/DCP8 deployment

### vllm-project/vllm

- [Bug] 🆕 [#54764](https://github.com/vllm-project/vllm/issues/54764) [Bug]: PLE short-conv batched prefill pads all requests to batch-max query length, causing transient activation OOM on mixed-length workloads(Qwen3.8-Flash-Next)
- [Bug] 🆕 [#54711](https://github.com/vllm-project/vllm/issues/54711) [Bug]: PP: a KV-cache group projected empty still emits `KVCacheTensor`s for other ranks' layers, causing a bare `StopIteration` in `allocate_kv_cache`
- [RFC] 🆕 [#54777](https://github.com/vllm-project/vllm/issues/54777) [RFC]: GDS kv offloading

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#54775](https://github.com/vllm-project/vllm/issues/54775) [Bug]: KDA/gated-delta-rule chunked-scan buffers are outside memory profiling — runtime OOM at large --max-num-batched-tokens
- [Bug] 🆕 [#54761](https://github.com/vllm-project/vllm/issues/54761) [Bug]: On ROCm, DCP and non-FP8 KV dtypes are unreachable, but the errors suggest fixes that don't exist there
- [Bug] 🆕 [#54710](https://github.com/vllm-project/vllm/issues/54710) [Bug]: `resolve_kv_cache_layout` asserts every worker reports identical KV layouts — false for hybrid models under pipeline parallelism
- [Bug] 🆕 [#54690](https://github.com/vllm-project/vllm/issues/54690) [Bug]: Speculative kv_cache_dtype=fp8 crashes startup on hybrid GDN models - FlashInfer "Unrecognized dtype: auto", then native crash on SM89 with explicit target dtype

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#37342](https://github.com/sgl-project/sglang/issues/37342) [Bug] DeepSeek-V4-Flash-0731 fails to load on v0.5.17/v0.5.18: AssertionError: Hidden size mismatch in the mxfp4 MoE path (works on main)
- [Bug] 🆕 [#37326](https://github.com/sgl-project/sglang/issues/37326) [Bug] NEXTN/MTP draft acceptance decays to ~0 over server uptime on qwen4_exp (Qwen3.8-Flash-Next), fully restored by a restart
- [Perf] 🆕 [#37348](https://github.com/sgl-project/sglang/issues/37348) [Perf] DeepSeek-V4-Flash-0731 on 4×H800 (SM90, TP4, no EP): ~40% lower per-stream decode at conc=32; dp-attention regresses and TBO is gated — what is the recommended small-node config?
- [other] 🆕 [#37379](https://github.com/sgl-project/sglang/issues/37379) [Model] Qwen3.5-MoE: RuntimeError when using --quantization-param-path for FP8 KV cache

### vllm-project/vllm

- [Bug] 🆕 [#54765](https://github.com/vllm-project/vllm/issues/54765) [Bug]: Qwen3.8-Flash-Next: ModelOpt NVFP4 checkpoint with an FP8-quantized PLE n-gram table fails to load (ngram_embedding.weight_scale)
- [Bug] 🆕 [#54740](https://github.com/vllm-project/vllm/issues/54740) [Bug]: [XPU] gdn_attention asserts on ragged ngram draft lengths (single stream, survives #53077)
- [Bug] 🆕 [#54739](https://github.com/vllm-project/vllm/issues/54739) [Bug]: Qwen3.8-Flash-Next generates corrupted Thai orthography under vLLM; the same model under llama.cpp at the same QSA budget is clean
- [Bug] 🆕 [#54723](https://github.com/vllm-project/vllm/issues/54723) [Bug]: FlashInfer TRTLLM MoE Backend stuck under DP/EP (Kimi K2 base, DeepSeek v3 base)
- [Bug] 🆕 [#54712](https://github.com/vllm-project/vllm/issues/54712) [Bug]: `--load-format dummy` OOMs on large FP8 parameters — `initialize_single_dummy_weight` materializes a full-size fp16 temporary
- [Performance] 🆕 [#54703](https://github.com/vllm-project/vllm/issues/54703) [Performance]: Tiny-window SlidingWindowSpec conv state dominates per-request KV accounting via the in-flight admission reserve
- [Bug] 🆕 [#54698](https://github.com/vllm-project/vllm/issues/54698) [Bug]: EngineCore hangs indefinitely in torch.xpu.graphs.replay() under concurrent load on Intel Arc B70 (Battlemage)
- [Feature] 🆕 [#54666](https://github.com/vllm-project/vllm/issues/54666) [Feature]: Consider B12X in automatic NVFP4 MoE backend selection on SM120/SM121 before the Marlin fallback
- [RFC] 🆕 [#54704](https://github.com/vllm-project/vllm/issues/54704) [RFC]: fp8 KV cache support for Inkling on SM100-family GPUs

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#37393](https://github.com/sgl-project/sglang/issues/37393) [Bug] Kimi-K3 chunked prefill submits different VocabParallelEmbedding ALLREDUCE sizes across TP ranks

### vllm-project/vllm

- [Perf] 🆕 [#54763](https://github.com/vllm-project/vllm/issues/54763) [Perf] Qwen3-Next MoE: gate and shared_expert_gate are two separate ReplicatedLinear over the same input
- [Bug] 🆕 [#54732](https://github.com/vllm-project/vllm/issues/54732) [Bug]: AITER topK meta buffer ignores pcp_size — every PCP start fails with fused shared experts on ROCm

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#54709](https://github.com/vllm-project/vllm/issues/54709) [Bug]: Qwen4Exp (Qwen3.8-Flash-Next) hard-refuses PP>1 for any PLE checkpoint, and its MTP draft head branches on the global `is_first_rank`
- [RFC] 🆕 [#54688](https://github.com/vllm-project/vllm/issues/54688) [RFC] Remove torch.compile dependency from Qwen3.8-Flash-Next NVIDIA path

## Sampling / Speculative Decoding

### sgl-project/sglang

- [other] 🆕 [#37349](https://github.com/sgl-project/sglang/issues/37349) [Guide] Setup and Troubleshooting for SGLang on V100

### vllm-project/vllm

- [Bug] 🆕 [#54691](https://github.com/vllm-project/vllm/issues/54691) [Bug][Spec Decode]: DFlash is a net loss at long context (~185k) on hybrid GDN models - drafter re-scans full accumulated KV every cycle; no per-sequence-length disable hook

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#54701](https://github.com/vllm-project/vllm/issues/54701) [Bug] kimi_k2 streaming tool parser intermittently emits empty tool_calls deltas under concurrent load (finish_reason=tool_calls, no name/arguments)
- [Bug] 🆕 [#54670](https://github.com/vllm-project/vllm/issues/54670) [Bug]: multimodal convert plus skip-tokenizer-init breaks processor construction

## Performance / Memory / OOM

### vllm-project/vllm

- [Perf] 🆕 [#54677](https://github.com/vllm-project/vllm/issues/54677) [Perf][Retracted] DeepSeek-V4-Flash-0731 apparent first-token regression 0.26→0.28 was my measurement error (default thinking mode); see correction below

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#54744](https://github.com/vllm-project/vllm/issues/54744) [Bug]: GLM-5.3 reasoning leaks into content when clients pass enable_thinking/thinking=false — parser gates on kwargs the GLM-5.3 template never reads
- [Bug] 🆕 [#54726](https://github.com/vllm-project/vllm/issues/54726) [Bug]: Qwen3.8-Flash-Next-FP8 + MooncakeStoreConnector fails at startup
- [Bug] 🆕 [#54671](https://github.com/vllm-project/vllm/issues/54671) [Bug]: LoRA and KV-cache settings reach a compiled torch assertion
- [Bug] 🆕 [#54667](https://github.com/vllm-project/vllm/issues/54667) [Bug]: zero pipeline/prefill context parallel size selects no executor backend
- [Bug] 🆕 [#54664](https://github.com/vllm-project/vllm/issues/54664) [Bug]: vllm 0.25.0 dsv4 flash PD混部流式输出，无参数可设置，默认输出usage，非流式输出默认带usage
- [Feature] 🆕 [#54728](https://github.com/vllm-project/vllm/issues/54728) [Feature]: [ROCm] Add gfx1030 (RDNA2) to Dockerfile archs + proper gate

## Uncategorized

### sgl-project/sglang

- [Feature] 🆕 [#37419](https://github.com/sgl-project/sglang/issues/37419) [Feature] Avoid raw media input prefixes in multimodal error logs
- [no-prefix] 🆕 ⚠no-prefix [#37421](https://github.com/sgl-project/sglang/issues/37421) CI: tests flaking on ubuntu-latest
- [other] 🆕 ⚠maintainer-authored [#37410](https://github.com/sgl-project/sglang/issues/37410) [Failure Tracker] PR Test (AMD)
