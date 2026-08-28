# LLM Serving Issue Radar

_Last run: 2026-08-28T17:24+00:00_

**40 issues** — sgl-project/sglang: 16, vllm-project/vllm: 24 — 🆕 **40 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 4
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 17
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 6
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#36877](https://github.com/sgl-project/sglang/issues/36877) [Bug] Anthropic /v1/messages: rolling cache_control breakpoints (Claude Code default behavior) invalidate prefix cache every few turns
- [Bug] 🆕 [#36855](https://github.com/sgl-project/sglang/issues/36855) [Bug] skip_radix_cache_insert livelocks and OOM-kills the scheduler on chunked prefill (reachable from any client via bootstrap_host="2.2.2.2")
- [no-prefix] 🆕 ⚠no-prefix [#36876](https://github.com/sgl-project/sglang/issues/36876) Zombie requests after client disconnect: abort_request fails to set to_finish during batch-transition window

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#54227](https://github.com/vllm-project/vllm/issues/54227) vllm bench serve with a fixed --seed against a default server can end up benchmarking the prefix cache (measured: TPOT -34%, TTFT 49x, throughput 2.32x on one cell)

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#54193](https://github.com/vllm-project/vllm/issues/54193) [Bug]: KV offloading connector: finished-request store watermark includes a KV slot never written by any forward pass (silent cross-request poisoning with offload_prompt_only=False)

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#54199](https://github.com/vllm-project/vllm/issues/54199) [Bug]: Illegal memory access in precopy_mamba_align_fused_kernel when a prefix-cache-hit request is admitted while the donor request's lifecycle overlaps (hybrid GDN, align mode, equal block sizes — not the #53142 divisor mismatch)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#36830](https://github.com/sgl-project/sglang/issues/36830) [Bug] GLM-5.3-Flash cannot use FP8 KV cache: `index_kpool > 1` excludes `flashmla_kv`, and no CUDA DSA backend supports bf16-query x fp8-KV
- [Bug] 🆕 [#36822](https://github.com/sgl-project/sglang/issues/36822) [Bug] GPTQ Marlin MoE fails or produces NaNs with BF16 and tensor parallelism
- [Bug] 🆕 [#36802](https://github.com/sgl-project/sglang/issues/36802) [Bug] GLM-5.3-Flash: server hangs during warmup when `--enable-dp-attention` is on (idle forward blocks in dsv4 gemm, requests never scheduled)
- [Performance] 🆕 [#36797](https://github.com/sgl-project/sglang/issues/36797) [Performance] NVFP4 KV cache regresses Qwen4Exp decode ~29% on DGX Spark (SM121) vs fp8_e4m3 — consider arch-gating the default
- [other] 🆕 [#36889](https://github.com/sgl-project/sglang/issues/36889) [DFLASH] Mamba state cache silently caps effective concurrency on hybrid-KDA models — 5 state slots/request, info-level log only (+75% throughput hidden behind one flag)

### vllm-project/vllm

- [Bug] 🆕 [#54237](https://github.com/vllm-project/vllm/issues/54237) [Bug]: 0.28.0 consume all host memory at start and freeze (OK with 0.27.1)
- [Bug] 🆕 [#54225](https://github.com/vllm-project/vllm/issues/54225) [Bug]: FlashInfer attention backend causes CUDA illegal memory access on sm_120 with NVFP4 + fp8 KV cache; crashes on a 16-token request; TRITON_ATTN unaffected
- [Bug] 🆕 [#54219](https://github.com/vllm-project/vllm/issues/54219) [Bug]: fp8e4nv data type error on A100
- [Bug] 🆕 [#54206](https://github.com/vllm-project/vllm/issues/54206) [Bug]: Quark FSE compatibility check matches `shared_expert_gate`, silently disabling fused shared experts on Qwen MoE MXFP4
- [Bug] 🆕 [#54184](https://github.com/vllm-project/vllm/issues/54184) [Bug]: Engine liveness monitor can SIGTERM a healthy EngineCore after spurious sentinel readiness
- [Bug] 🆕 [#54179](https://github.com/vllm-project/vllm/issues/54179) [Bug]: FlashMLA sparse prefill assertion failed on H20 with DeepSeek-V4-Flash + DSpark + long context (v0.26.0 regression)
- [Bug] 🆕 [#54173](https://github.com/vllm-project/vllm/issues/54173) [Bug] Qwen3.8-Flash-Next: CUBLAS_STATUS_INTERNAL_ERROR / illegal memory access in GDN path with prefix caching on GB10 (sm_121); --no-async-scheduling does not help
- [Bug] 🆕 [#54150](https://github.com/vllm-project/vllm/issues/54150) [Bug]: GLM-5.3-Flash — ModelOpt NVFP4 checkpoints emit invalid UTF-8 byte tokens on SM120, while a compressed-tensors NVFP4 of the same model is clean
- [Bug] 🆕 [#54126](https://github.com/vllm-project/vllm/issues/54126) [Bug]: ModelOpt FP8_PB_WO checkpoints using the weight_scale_inv / rank-2 export convention fail to load
- [Bug] 🆕 [#54125](https://github.com/vllm-project/vllm/issues/54125) [Bug]: DeepGEMM is reported supported on sm_121 (GB10) but faults — support_deep_gemm() accepts the whole 120 capability family

## Distributed / TP / PP / EP

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#54187](https://github.com/vllm-project/vllm/issues/54187) Use `dtype` instead of deprecated `torch_dtype` for transformers >= 4.56

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#54153](https://github.com/vllm-project/vllm/issues/54153) [Bug]: an installed-but-unusable optional dependency (boto3) aborts model architecture resolution for every model

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#36886](https://github.com/sgl-project/sglang/issues/36886) [Bug] DCP in GLM-5.3-Flash: index-K cache OOB corruption crash past max_total_num_tokens; output quality still degraded after sizing fix
- [no-prefix] 🆕 ⚠no-prefix [#36840](https://github.com/sgl-project/sglang/issues/36840) TBO unreachable for GLM-5.3-Flash (DSA+mamba hybrid): silent --enable-dp-attention reset + missing Glm5NextDecoderLayer strategy
- [no-prefix] 🆕 ⚠no-prefix [#36829](https://github.com/sgl-project/sglang/issues/36829) GLM-5.3-Flash (glm5_next, mHC) EAGLE3/MTP: fused_eh_norm width mismatch with mHC-flattened aux hidden; acceptance ~1.0 after workarounds

### vllm-project/vllm

- [Bug] 🆕 [#54197](https://github.com/vllm-project/vllm/issues/54197) [Bug] GlmMoeDsa (V2 model runner) cannot use torch.compile — silent fallback, then fullgraph failures when force-enabled
- [Bug] 🆕 [#54170](https://github.com/vllm-project/vllm/issues/54170) [Bug]: Video pruning crashes during inference on Qwen3.5 9B AWQ with `AttributeError: video_pruning_method` on v0.27.1
- [RFC] 🆕 [#54143](https://github.com/vllm-project/vllm/issues/54143) [RFC]: Backend-stable stateless RNG for Gumbel sampling

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#36776](https://github.com/sgl-project/sglang/issues/36776) [Bug] False assertions exist in the mmlu test of PR:24689
- [Feature] 🆕 [#36858](https://github.com/sgl-project/sglang/issues/36858) [Feature] Optimize the configuration and server startup of sgl-model-gateway

### vllm-project/vllm

- [Feature] 🆕 [#54139](https://github.com/vllm-project/vllm/issues/54139) [Feature]: MORE VELOCITY TO INFERENCE
- [no-prefix] 🆕 ⚠no-prefix [#54224](https://github.com/vllm-project/vllm/issues/54224) Responses API input_item_parsing only backfills id when the key is absent, not when it is explicitly null

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#36853](https://github.com/sgl-project/sglang/issues/36853) [Bug][Diffusion] Qwen-Image native SP=4 is killed by host OOM while loading DiT on 4×48GB GPUs
- [Performance] 🆕 [#36796](https://github.com/sgl-project/sglang/issues/36796) [Performance] Qwen4Exp decode on DGX Spark (SM121): QSA/PLE/GDN kernel time dominates; requests for SM121 tuning (QSA gather, GDN KDA backends, torch.compile+CUDA graph)

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#36807](https://github.com/sgl-project/sglang/issues/36807) [Bug] fast_topk_v2 can silently return wrong top-k sets when a radix threshold bucket exceeds its 4096-entry candidate buffer (k=2048, long rows)

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#54207](https://github.com/vllm-project/vllm/issues/54207) [Feature]: Add explicit cache IDs for reusable multimodal and inference state
- [no-prefix] 🆕 ⚠no-prefix [#54200](https://github.com/vllm-project/vllm/issues/54200) vLLM lacks Blackwell unified-memory paging telemetry — reference mapping exists in dgx-spark-monitoring
