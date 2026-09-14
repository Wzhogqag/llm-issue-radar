# LLM Serving Issue Radar

_Last run: 2026-09-14T13:30+00:00_

**27 issues** — sgl-project/sglang: 6, vllm-project/vllm: 21 — 🆕 **26 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 3
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 3
- [Quantization](#quantization) — 8
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#39348](https://github.com/sgl-project/sglang/issues/39348) [Feature] [NPU] Add topology-aware CPU and NUMA affinity for Ascend worker ranks

### vllm-project/vllm

- [Bug] 🆕 [#56795](https://github.com/vllm-project/vllm/issues/56795) [Bug]: Native KV offload advances next_stored_block_idx for every KV group when no keys were stored
- [Feature] 🆕 [#56767](https://github.com/vllm-project/vllm/issues/56767) [Feature]: Compact LM Head fast path for fixed-candidate-set scoring (rerankers / relevance scoring)

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Feature] 🆕 [#39355](https://github.com/sgl-project/sglang/issues/39355) [Feature] [NPU] Add ScatterPaKvCache as an optional KV-cache write backend
- [Bug] [#39302](https://github.com/sgl-project/sglang/issues/39302) [Bug] GLM-5.x NoPE MLA (qk_rope_head_dim=0) cannot run on SM120: every DSA sparse-MLA backend is unavailable

### vllm-project/vllm

- [other] 🆕 [#56772](https://github.com/vllm-project/vllm/issues/56772) [KV Connector][Offloading] Canonical MLA+DSA secondary transfers use TP-dependent row sizes

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#56837](https://github.com/vllm-project/vllm/issues/56837) [Bug] DeepSeek-V4.1 on sm_120 (RTX PRO 2000 Blackwell): no FlashInfer SM120 sparse-MLA kernel for (num_heads=64, topk=1152); FlashMLA sparse is SM90a/SM100f only
- [Bug] 🆕 [#56785](https://github.com/vllm-project/vllm/issues/56785) [Bug]: HiSparse MLA indexer crashes with CUDA error: invalid argument during piecewise cudagraph capture - logical_topk_ready is recorded inside the capture segment but waited on after eager_break_during_capture ends capture
- [Bug] 🆕 [#56771](https://github.com/vllm-project/vllm/issues/56771) [Bug]: DeepSeek-V4.1-Flash + DSpark speculative decoding — illegal memory access in SM120 sparse-MLA prefill on long prompts

## Quantization

### sgl-project/sglang

- [other] 🆕 [#39393](https://github.com/sgl-project/sglang/issues/39393) [Feature Request] Add pipeline-parallel support to Qwen4-Exp (`qwen4_exp.py`) — four gaps, working reference patches, and an undocumented mHC PP-boundary contract

### vllm-project/vllm

- [Bug] 🆕 [#56832](https://github.com/vllm-project/vllm/issues/56832) [Bug]: --moe-backend marlin is applied to the unquantized MTP draft MoE and aborts (Qwen3.8-Flash-Next NVFP4 + speculative mtp)
- [Bug] 🆕 [#56829](https://github.com/vllm-project/vllm/issues/56829) [Bug]: cu129-nightly image ships torch 2.14.0+cu130 with cu129 torchvision/torchaudio, vllm serve dies on 'operator torchvision::nms does not exist'
- [Bug] 🆕 [#56824](https://github.com/vllm-project/vllm/issues/56824) [Bug]: Engine startup on DGX Spark (GB10, unified memory) collapses host memory — NV_ERR_NO_MEMORY while MemAvailable reports ~22 GiB
- [Bug] 🆕 [#56770](https://github.com/vllm-project/vllm/issues/56770) [Bug]: compressed-tensors MXFP4 W4A16 is misclassified as W4A4 and dispatched to W4A4 kernel on SM100+
- [Bug] 🆕 [#56769](https://github.com/vllm-project/vllm/issues/56769) [Bug] Greedy LoRA decode nondeterministic on Qwen3.8-27B-FP8 (rank-64 Unsloth, linear_attn modules)
- [Bug] 🆕 [#56759](https://github.com/vllm-project/vllm/issues/56759) [Bug]: Humming MoE permute scratch memory scales with number of MoE layers
- [RFC] 🆕 [#56727](https://github.com/vllm-project/vllm/issues/56727) [RFC] Separate CLI input definitions from runtime configuration

## New Model Integration

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#56792](https://github.com/vllm-project/vllm/issues/56792) DSpark checkpoints exported in fill-in (DFlash 1+N) layout silently serve with <1% acceptance: the optional layout flag is absent from their configs, and the default anchor-first sampler is wrong for them

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Perf] 🆕 [#56797](https://github.com/vllm-project/vllm/issues/56797) [Perf][Spec Decode] DeepSeek-V4.1-Flash DSpark mean acceptance length only 2.82 on GSM8K (k=5, 2×8 H20)
- [no-prefix] 🆕 ⚠no-prefix [#56736](https://github.com/vllm-project/vllm/issues/56736) hybrid Mamba/GDN + speculative decoding: Xid 31 in the align mamba path (fault address below the CUDA segment)

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [RFC] 🆕 [#56745](https://github.com/vllm-project/vllm/issues/56745) [RFC]: Return `routed_experts` on the terminal streaming chunk

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#39412](https://github.com/sgl-project/sglang/issues/39412) [Bug] pd bootstrap params silently dropped on rust frontend openai endpoints

### vllm-project/vllm

- [Bug] 🆕 [#56828](https://github.com/vllm-project/vllm/issues/56828) [Bug][KV Offload][P2P] Peer-down on one rank does not fail loads or block new loads to sibling ranks of the same source

## Build / Install / Platform

### sgl-project/sglang

- [no-prefix] 🆕 ⚠no-prefix [#39343](https://github.com/sgl-project/sglang/issues/39343) 按照指导操作后，A5仍然无法拉起dsv4.1，报错如下：ValueError: The checkpoint you are trying to load has model type deepseek_v41 but Transformers does not recognize this architecture.

### vllm-project/vllm

- [Bug] 🆕 [#56830](https://github.com/vllm-project/vllm/issues/56830) [Bug]: Startup memory-profiling assertion aborts whenever free memory grows, contradicting documented support for GPU co-tenancy
- [Bug] 🆕 [#56815](https://github.com/vllm-project/vllm/issues/56815) [Bug]: Engram async prefetch (#56512) reintroduces silent ctx-load decode flake on single-GPU Qwen4Exp PLE CPU-offload (nightlies past 2026-09-13)
- [Bug] 🆕 [#56787](https://github.com/vllm-project/vllm/issues/56787) [Bug]: DFlash2 draft model fails torch.compile on XPU — dynamic-shape stride assert in custom-op fake kernel (workaround: disable compile on draft class)
