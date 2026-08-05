# LLM Serving Issue Radar

_Last run: 2026-08-05T14:00+00:00_

**26 issues** — sgl-project/sglang: 17, vllm-project/vllm: 9 — 🆕 **26 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 11
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 6
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#33713](https://github.com/sgl-project/sglang/issues/33713) unified_cache: MAMBA component nodes are pruned instead of downgraded on device eviction, breaking host-tier loadback

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix ⚠maintainer-authored [#33714](https://github.com/sgl-project/sglang/issues/33714) unified_cache: back up long prompts past their first (chunked) extend — currently skipped when extend exceeds chunked_prefill_size

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#33603](https://github.com/sgl-project/sglang/issues/33603) [Bug] backend ignores bidirectional sliding window attention for encoder models

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#33693](https://github.com/sgl-project/sglang/issues/33693) [Bug] deepseek v4 flash 0731版本启动失败
- [Bug] 🆕 [#33670](https://github.com/sgl-project/sglang/issues/33670) [Bug] nvidia/MiniMax-M3-NVFP4 (#31989) fails to load on B200 — VL class crashes with 6144 vs 3072 in MoE _load_w13; --disable-shared-experts-fusion insufficient
- [Bug] 🆕 [#33656](https://github.com/sgl-project/sglang/issues/33656) [Bug] DeepSeek-V4 + hierarchical cache: deterministic SWA KV position corruption (kv-canary TAIL_K_SWA write_position), downstream NaN sampling crash
- [Feature] 🆕 ⚠maintainer-authored [#33706](https://github.com/sgl-project/sglang/issues/33706) [Feature] Support shared to sparse experts fusion for Qwen3.5 / Qwen3.6 MoE on SM120 (blockwise FP8)
- [Feature] 🆕 ⚠maintainer-authored [#33711](https://github.com/sgl-project/sglang/issues/33711) [Feature] Support dense NVFP4 W4A16 (bf16 activations) GEMM on SM120
- [Feature] 🆕 ⚠maintainer-authored [#33709](https://github.com/sgl-project/sglang/issues/33709) [Feature] Finish the B12X FlashInfer NVFP4 MoE integration for SM120 (#29190)
- [Feature] 🆕 ⚠maintainer-authored [#33632](https://github.com/sgl-project/sglang/issues/33632) [Feature] Optimize Per-Tensor FP8 GEMM on SM120
- [Feature] 🆕 ⚠maintainer-authored [#33629](https://github.com/sgl-project/sglang/issues/33629) [Feature] Optimize FP8 Blockwise GEMM on SM120

### vllm-project/vllm

- [Bug] 🆕 [#51066](https://github.com/vllm-project/vllm/issues/51066) [Bug]: nvidia/Kimi-K2.6-NVFP4 TP=4 segfaults during cuDNN vision profiling on GB200 ARM64 unless --language-model-only is set
- [Feature] 🆕 [#51142](https://github.com/vllm-project/vllm/issues/51142) [Feature][CI] Speed up `Quantization` mi300/mi355 test groups
- [no-prefix] 🆕 ⚠no-prefix [#51136](https://github.com/vllm-project/vllm/issues/51136) AITER is not enabled on RDNA3 (gfx1100) — integration gap between CDNA3 and RDNA4

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#33642](https://github.com/sgl-project/sglang/issues/33642) [Bug] All schedulers hang in cuModuleLoadData on first EAGLE verify (DSA attention, PD-disagg decode), watchdog timeout

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Feature] 🆕 [#33708](https://github.com/sgl-project/sglang/issues/33708) [Feature] [Diffusion] Overlap Ulysses A2A with attention compute for Wan2.2-TI2V-5B
- [Feature] 🆕 [#33625](https://github.com/sgl-project/sglang/issues/33625) [Feature] Add opt-in bounded-load routing-key affinity to SGLang Model Gateway

## Performance / Memory / OOM

### vllm-project/vllm

- [Bug] 🆕 [#51049](https://github.com/vllm-project/vllm/issues/51049) [Bug]: `fused_qk_norm_rope` multi-head-per-warp kernel corrupts partial-NeoX (`rotary_dim < head_dim`) QK-Norm models on SM90

## Build / Install / Platform

### sgl-project/sglang

- [Feature] 🆕 ⚠maintainer-authored [#33627](https://github.com/sgl-project/sglang/issues/33627) [Feature] Should we make the LM head GEMM output fp32 instead of bf16?

### vllm-project/vllm

- [Bug] 🆕 [#51140](https://github.com/vllm-project/vllm/issues/51140) [Bug]: Gemma 4 31B | Incoherent responses high context
- [Bug] 🆕 [#51106](https://github.com/vllm-project/vllm/issues/51106) [Bug]: DeepSeek-V4-Flash-0731 crashes on RTX PRO 5000 because FlashInfer cannot reshape a tensor with 0 elements into the shape [0, -1]
- [Bug] 🆕 [#51063](https://github.com/vllm-project/vllm/issues/51063) [Bug]: Composite VLM wrapper (Mistral3ForConditionalGeneration) resolves tie_word_embeddings from the wrong (top-level) config, silently discarding a real lm_head.weight and producing coherent-vocabulary-but-incoherent output
- [Feature] 🆕 [#51057](https://github.com/vllm-project/vllm/issues/51057) [Feature]: Follow Up from inital ROCm DI CI enablement PR to break it up into smaller chunks -  Use production grade vLLM router in ROCm nightly DI CI instead of "toy proxy"
- [Feature] 🆕 [#51056](https://github.com/vllm-project/vllm/issues/51056) [Feature] Follow Up from inital ROCm DI CI enablement PR to break it up into smaller chunks -  Nightly ROCm WideEP (EP>=16) DI CI

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#33657](https://github.com/sgl-project/sglang/issues/33657) [BUG] sunset Gemini Code Assist referenced in CI
- [no-prefix] 🆕 ⚠no-prefix [#33628](https://github.com/sgl-project/sglang/issues/33628) nightly-dev image revision can differ from installed SGLang source
