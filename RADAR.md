# LLM Serving Issue Radar

_Last run: 2026-08-26T13:39+00:00_

**21 issues** — sgl-project/sglang: 11, vllm-project/vllm: 10 — 🆕 **21 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [Quantization](#quantization) — 6
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#36500](https://github.com/sgl-project/sglang/issues/36500) [Bug] [NGRAM] Removing a corpus during asynchronous loading returns success without cancelling the load

### vllm-project/vllm

- [Performance] 🆕 [#53810](https://github.com/vllm-project/vllm/issues/53810) [Performance]: [MRV2][PP]: Post sampled-result receives closer to T+PP consumption

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36481](https://github.com/sgl-project/sglang/issues/36481) [Bug] SGLANG_RAGGED_VERIFY_MODE=compact crashes decode CUDA-graph capture on Qwen3.5 hybrid linear attention: IMA in extend_attention_fwd (triton_backend)
- [Bug] 🆕 [#36390](https://github.com/sgl-project/sglang/issues/36390) [Bug] [ROCm] DeepSeek-V4-Flash FP8 on MI300X (gfx942): output degrades with context length — coherent <100 tokens, garbage by ~300, NIAH 0/3
- [Feature] 🆕 [#36447](https://github.com/sgl-project/sglang/issues/36447) [Feature] Support GLM-5.2 MXFP4 with DSA/NSA and Mega-MoE
- [Feature] 🆕 [#36460](https://github.com/sgl-project/sglang/issues/36460) [Feature] Support expert-wise FP8/W4A16_AWQ mixed precision for ModelOpt MoE checkpoints

### vllm-project/vllm

- [Bug] 🆕 [#53887](https://github.com/vllm-project/vllm/issues/53887) [Bug]: MTP draft allocates a second full vocab embedding, OOMing a 27B INT4 target that the baseline fits
- [no-prefix] 🆕 ⚠no-prefix [#53888](https://github.com/vllm-project/vllm/issues/53888) Sleep level=1 wake silently corrupts LoRA state (NemotronH NVFP4/Marlin, TP=2, WSL2): fixed-seed generation diverges after wake, adapter stops applying, no error raised

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 ⚠maintainer-authored [#36429](https://github.com/sgl-project/sglang/issues/36429) [Bug] #35061 rejects multi-node custom all-reduce v2 without expandable segments, causing ~19% Llama-4 TP8 regression on GB300

### vllm-project/vllm

- [other] 🆕 [#53890](https://github.com/vllm-project/vllm/issues/53890) [Installation]: 0.28.0 build error in jetson agx orin 64G jetpack 7.2.1

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#36495](https://github.com/sgl-project/sglang/issues/36495) [Bug] NGRAM trie capacity equal to max depth causes an invalid free and scheduler abort
- [Bug] 🆕 [#36480](https://github.com/sgl-project/sglang/issues/36480) [Bug] Qwen3.5 greedy outputs differ A LOT between v0.5.12 and v0.5.17.dev for the same multimodal request; v0.5.17.dev36 not self-consistent behind router
- [Perf] 🆕 [#36452](https://github.com/sgl-project/sglang/issues/36452) [Perf] NEXTN/EAGLE: draft embed_tokens/lm_head copies are released after KV pool sizing, significantly shrinking max_total_num_tokens

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [RFC] 🆕 [#36431](https://github.com/sgl-project/sglang/issues/36431) [RFC] Resumable raw token stream for /v1/chat/completions

### vllm-project/vllm

- [Bug] 🆕 [#53836](https://github.com/vllm-project/vllm/issues/53836) [Bug]: NVIDIA DGX Spark vllms and gemma 4 26B won't work

## Performance / Memory / OOM

### vllm-project/vllm

- [RFC] 🆕 [#53788](https://github.com/vllm-project/vllm/issues/53788) [RFC]: Using Helion for Selected vLLM CustomOps

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#53894](https://github.com/vllm-project/vllm/issues/53894) [Bug]: v0.28.0 hangs when starting distributed inference with DeepSeek-V4-Pro on 2 nodes × 16 H100 GPUs
- [Bug] 🆕 [#53863](https://github.com/vllm-project/vllm/issues/53863) [Bug]: Out-of-bounds attrIdxs in the C++ batch memcpy path (cache_kernels.cu)
- [Bug] 🆕 [#53822](https://github.com/vllm-project/vllm/issues/53822) [Bug]: XPU TP>1 consumes host RAM equal to total VRAM; workers are never isolated to their own device
- [Bug] 🆕 [#53796](https://github.com/vllm-project/vllm/issues/53796) [Bug]: PD-disaggregation cannot use PCIe P2P for KV transfer on Intel Arc Pro B60 (BMG)

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#36427](https://github.com/sgl-project/sglang/issues/36427) [Bug] Several ambiguous points in the installation documentation, please check
