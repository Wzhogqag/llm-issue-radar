# LLM Serving Issue Radar

_Last run: 2026-08-19T13:33+00:00_

**31 issues** — sgl-project/sglang: 7, vllm-project/vllm: 24 — 🆕 **31 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 6
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 10
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 3
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 4
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 4

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#35498](https://github.com/sgl-project/sglang/issues/35498) [Bug] TP>1 LoRA tensor hot-load reuses one-shot ForkingPickler FDs and crashes schedulers
- [Feature] 🆕 [#35495](https://github.com/sgl-project/sglang/issues/35495) [Feature] Add a tiered AdaLN cache manager for MiniMax-H3

### vllm-project/vllm

- [Bug] 🆕 [#52922](https://github.com/vllm-project/vllm/issues/52922) [Bug]: DSpark scheduling using an overly conservative input budget
- [Bug] 🆕 [#52909](https://github.com/vllm-project/vllm/issues/52909) [Bug]: Kimi-K3 chunked prefill diverges from one-shot prefill under TP8/PP2
- [Feature] 🆕 [#52884](https://github.com/vllm-project/vllm/issues/52884) [Feature]: warn from `vllm bench serve` when a repeated random-dataset run hits a warm prefix cache, which inflates throughput by up to 86%
- [RFC] 🆕 [#52906](https://github.com/vllm-project/vllm/issues/52906) [RFC]: Adaptive prefill token budget based on scheduling pressure

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Feature] 🆕 [#52913](https://github.com/vllm-project/vllm/issues/52913) [Feature]: Support Pipeline Parallelism (PP > 1) in NixlConnector for Disaggregated KV Cache Transfer
- [RFC] 🆕 [#52837](https://github.com/vllm-project/vllm/issues/52837) [RFC]: Derive KV offload save sources from prefix-cache records

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#52938](https://github.com/vllm-project/vllm/issues/52938) [Bug]: DeepSeek-V4-Flash on RTX PRO 6000 Blackwell (SM120) emits degenerate output — identical argmax token + identical logprob at every decode position, TP and DP+EP alike, confirmed independent of environment/install history (FLASHINFER_MLA_SPARSE_DSV4)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#35437](https://github.com/sgl-project/sglang/issues/35437) [Bug] DFLASH + prefill CUDA graph: BCG capture assert at startup, full-backend IndexError on first request
- [other] 🆕 [#35514](https://github.com/sgl-project/sglang/issues/35514) [Playground] Verified cell: rtx5090 / default / nvfp4 / undefined / single
- [other] 🆕 [#35476](https://github.com/sgl-project/sglang/issues/35476) [Playground] Verified cell: dgx-spark / default / nvfp4 / undefined / single
- [other] 🆕 [#35464](https://github.com/sgl-project/sglang/issues/35464) [Playground] Verified cell: dgx-spark / default / nvfp4 / undefined / single

### vllm-project/vllm

- [Bug] 🆕 [#52947](https://github.com/vllm-project/vllm/issues/52947) [Bug]: torchao 0.18.0 cannot load version-1 int8wo checkpoints; surfaces as an opaque VllmConfig ValidationError
- [Bug] 🆕 [#52872](https://github.com/vllm-project/vllm/issues/52872) [Bug] GDN/mamba-hybrid: profiled peak activation under-predicts prefill peak; max-num-batched-tokens also sizes the CUDA-graph pool
- [Bug] 🆕 [#52871](https://github.com/vllm-project/vllm/issues/52871) [Bug] Forward-pass CUDA OOM kills the whole EngineCore instead of preempting/rejecting the request
- [Bug] 🆕 [#52845](https://github.com/vllm-project/vllm/issues/52845) [Bug]: benchmark_moe.py --tune --dtype int4_w4a16 crashes on NVIDIA (BLOCK_SIZE_K vs group_size)
- [Bug] 🆕 [#52834](https://github.com/vllm-project/vllm/issues/52834) [Bug]: --mm-processor-kwargs cannot scope an override to one modality: videos_kwargs is ignored by profiling while a flat "size" leaks into the image budget (Qwen3-VL)
- [Bug] 🆕 [#52833](https://github.com/vllm-project/vllm/issues/52833) [Bug]: GLM-5.2 MTP accepts 0% of drafts on MI355X (gfx950); disabling expert parallelism hits hipErrorIllegalAddress

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#52877](https://github.com/vllm-project/vllm/issues/52877) [Bug]: Recurring EngineCore fatal errors on DGX Spark (GB10 / sm_121): CUDA kernel launch failures after 1.5–3 days of uptime (Triton JIT + FlashInfer cuDNN FP8 GEMM)
- [Bug] 🆕 [#52873](https://github.com/vllm-project/vllm/issues/52873) [Bug]: Qwen3-Next GDN + MTP: crossing sequence position 32768 permanently kills draft acceptance engine-wide (0% until restart)
- [other] 🆕 [#52843](https://github.com/vllm-project/vllm/issues/52843) [Rust frontend] /inference/v1/generate silently ignores n > 1; should reject it

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#52926](https://github.com/vllm-project/vllm/issues/52926) [Bug]: Voxtral-Mini-4B-Realtime permanent engine hang on a specific audio file via /v1/audio/transcriptions (empty multimodal embeddings)
- [Bug] 🆕 [#52852](https://github.com/vllm-project/vllm/issues/52852) [Bug] Streaming completions end with no finish_reason / no [DONE] — xgrammar "Failed to advance FSM" is one logged trigger, but some drops are fully silent (no engine error)
- [Bug] 🆕 [#52846](https://github.com/vllm-project/vllm/issues/52846) [Bug]: DeepSeek V4 buffers long string tool arguments until </parameter>
- [Bug] 🆕 [#52835](https://github.com/vllm-project/vllm/issues/52835) [Bug]: EngineCore fails to start with ValueError("value too large") when one processed multi-modal item exceeds mm_processor_cache_gb

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#35415](https://github.com/sgl-project/sglang/issues/35415) [Bug] MiniMax-H3 FL2VA + Turbo LoRA: `slice_lora_b_weights` crashes on merged/QKV linear layers with TP>1

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#52897](https://github.com/vllm-project/vllm/issues/52897) [Bug]: Align-mode prefix caching never hits (0 / 996k queries) with --scheduling-policy priority on hybrid GDN model (post-#51113)
- [Bug] 🆕 [#52860](https://github.com/vllm-project/vllm/issues/52860) [Bug]: MiniMax-M3 AITER sparse PA prototype corrupts output under speculative decoding with FP8 KV (ROCm)
- [no-prefix] 🆕 ⚠no-prefix [#52907](https://github.com/vllm-project/vllm/issues/52907) Multi-node startup deadlock in in_the_same_node_as() gloo barrier at 2 nodes x TP-16 with the Ray executor (regression between 0.26.1rc1.dev78 and 0.26.1rc1.dev148)
- [RFC] 🆕 ⚠maintainer-authored [#52911](https://github.com/vllm-project/vllm/issues/52911) [RFC]: DeepSeek-V4 Performance Optimization on ROCm (Phase Two)
