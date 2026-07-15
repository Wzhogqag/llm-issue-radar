# LLM Serving Issue Radar

_Last run: 2026-07-15T06:10+00:00_

**37 issues** — sgl-project/sglang: 17, vllm-project/vllm: 20 — 🆕 **30 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 4
- [Attention Backend](#attention-backend) — 4
- [Quantization](#quantization) — 9
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 3
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Build / Install / Platform](#build--install--platform) — 6
- [Uncategorized](#uncategorized) — 1

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#31252](https://github.com/sgl-project/sglang/issues/31252) [Bug] HiCache draft KV pool backup crashes with cudaMemcpyBatchAsync invalid argument in PD disaggregation
- [Bug] 🆕 [#31205](https://github.com/sgl-project/sglang/issues/31205) [Bug] PD prefill silently starves forever when a request's SWA budget exceeds the SWA pool (DeepSeek-V4 hybrid pool)
- [Feature] 🆕 [#31207](https://github.com/sgl-project/sglang/issues/31207) [Feature] DeepSeek-V4 hybrid KV pool: host/storage integrations assume k/v two-buffer pools (LMCache connector, decode KV offload)

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#48620](https://github.com/vllm-project/vllm/issues/48620) V1 EngineCore: SIGTERM teardown runs two full-heap gen-2 GC passes (~4-7 s) to collect a few hundred objects

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#48611](https://github.com/vllm-project/vllm/issues/48611) [Bug]: #47327 dense-MHA split breaks FlashMLA sparse: OOB write in top-k index conversion, corrupted fp8_ds_mla context gather
- [Bug] 🆕 [#48650](https://github.com/vllm-project/vllm/issues/48650) [Bug]: Runtime-varying tl.constexpr params force Triton kernel recompiles on the serving path (unified attention MAX_MM_RANGES et al.)
- [Perf] 🆕 [#48576](https://github.com/vllm-project/vllm/issues/48576) [Perf][ROCm] Optimize DSA lightning-indexer fp8_mqa_logits scoring kernel on MI300X (gfx942)
- [Feature] [#48613](https://github.com/vllm-project/vllm/issues/48613) [Feature]: [Batch-Invariant-Kernels] GDN_ATTN does not support batch-invariant mode for Qwen3.5/Qwen3.6 GDN models

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31236](https://github.com/sgl-project/sglang/issues/31236) [Bug] 'Gemma4ForConditionalGeneration' object has no attribute 'get_embed_and_head' when modelopt_fp4
- [Bug] 🆕 [#31183](https://github.com/sgl-project/sglang/issues/31183) [Bug] Humming quantization probe raises KeyError for configs without quant_method
- [Bug] 🆕 [#31283](https://github.com/sgl-project/sglang/issues/31283) [Bug] _mxfp8_block_scaled_matmul_kernel declares M (token count) as tl.constexpr — full GEMM recompile per 128-token batch bucket
- [Feature] 🆕 [#31248](https://github.com/sgl-project/sglang/issues/31248) [Feature] Support CompressedTensorsW4A16Sparse24
- [Feature] 🆕 [#31235](https://github.com/sgl-project/sglang/issues/31235) [Feature] Support serialized static-FP8 MXFP4 MoE on the resident FlashInfer backend (SM120/SM121)
- [no-prefix] 🆕 ⚠no-prefix [#31224](https://github.com/sgl-project/sglang/issues/31224) Misleading "FP8 KV cache but no scaling factors provided" warning fires even when per-layer ModelOpt/compressed-tensors KV scales are present and loaded

### vllm-project/vllm

- [Bug] 🆕 [#48689](https://github.com/vllm-project/vllm/issues/48689) [Bug]: GLM-5.2 nvpf4 quantization not loading with TP
- [Bug] 🆕 [#48680](https://github.com/vllm-project/vllm/issues/48680) [Bug]: `--enable-sleep-mode` OOMs loading an NVFP4 (modelopt) 30B on 16GB SM120 cards where the identical model loads fine without it — cumem MemPool overhead, not resolved by raising max_split_size_mb
- [Bug] [#48590](https://github.com/vllm-project/vllm/issues/48590) [Bug]: LoRA `lora_expand` Triton kernel outputs NaN on Hopper (sm_90) with `block_n=128`, producing garbled LoRA output

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] 🆕 [#31243](https://github.com/sgl-project/sglang/issues/31243) [Bug] can't deploy Mimo V2.5

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#48661](https://github.com/vllm-project/vllm/issues/48661) Expose public get_layer_params(config) helper for Gemma4 per-layer attention/FFN params
- [no-prefix] ⚠no-prefix [#48591](https://github.com/vllm-project/vllm/issues/48591) 还不支持[Usage]: vllm 0.25版本在tp=8并行的时候走dflash 和dspark 命中 attention后端的时候出现错误报错定位 CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_api.cpp:697): invalid configuration argument 8个worker(TP0-TP7)

## New Model Integration

### sgl-project/sglang

- [Feature] 🆕 [#31261](https://github.com/sgl-project/sglang/issues/31261) [Feature] Support Deterministic Inference for Qwen3_5ForConditionalGeneration
- [no-prefix] ⚠no-prefix [#31175](https://github.com/sgl-project/sglang/issues/31175) Add native OLMo3 (Olmo3ForCausalLM) support by reusing the Olmo2 implementation

### vllm-project/vllm

- [Feature] 🆕 [#48644](https://github.com/vllm-project/vllm/issues/48644) [Feature]: Support fast weight updates from disk

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#31249](https://github.com/sgl-project/sglang/issues/31249) [Bug] Qwen/Qwen3.6-27B-FP8 crash with MTP speculative decoding
- [Bug] [#31178](https://github.com/sgl-project/sglang/issues/31178) [Bug] D node deployed with sglang glm 5.2 pd is throwing an error when using speculative decoding.

### vllm-project/vllm

- [RFC] 🆕 [#48627](https://github.com/vllm-project/vllm/issues/48627) [RFC]: Context-length-aware speculative token scheduling — extending num_speculative_tokens_per_batch_size with a context-length axis
- [Bug] [#48592](https://github.com/vllm-project/vllm/issues/48592) [Bug]: v0.25.0 torchcodec not compatible with cu129 wheel

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#31240](https://github.com/sgl-project/sglang/issues/31240) [Bug] RunAI streamer: get_processor() leaves model_name as raw s3://gs:// URI (incomplete fix of #22715), crashes multimodal models from object storage
- [no-prefix] 🆕 ⚠no-prefix [#31271](https://github.com/sgl-project/sglang/issues/31271) Can not load gpt-oss-20b model specific tokenizer

### vllm-project/vllm

- [Feature] 🆕 [#48635](https://github.com/vllm-project/vllm/issues/48635) [Feature][KV-offloading]: Relax Offloading Block Size asserts

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#31206](https://github.com/sgl-project/sglang/issues/31206) [Bug] sgl-router (PD): open circuit breaker still dispatches to decode, producing a permanent fake-dead prefill

### vllm-project/vllm

- [Bug] 🆕 [#48645](https://github.com/vllm-project/vllm/issues/48645) [Bug]: deepseek_v4 parser: reply without </think> routes the whole answer to reasoning_content (content empty), trailing EOS not stripped
- [Bug] 🆕 [#48621](https://github.com/vllm-project/vllm/issues/48621) [Bug]: Ministral3 RoPE scaling ignores YaRN mscale and nested Llama 4 fields
- [Bug] 🆕 [#48603](https://github.com/vllm-project/vllm/issues/48603) [Bug]: MiniMax M3 Triton path misinterprets token-major top-k buffer
- [no-prefix] 🆕 ⚠no-prefix [#48667](https://github.com/vllm-project/vllm/issues/48667) Idefics3/SmolVLM: num_patches=0 for non-tiled images mis-sizes pixel_values while the prompt still reserves image_seq_len placeholder tokens
- [Bug] [#48602](https://github.com/vllm-project/vllm/issues/48602) [Bug]: DeepSeekv4 flash on RTXpro6000 vllm benchmark input 8192 output 1024 encounter a err

## Uncategorized

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#48662](https://github.com/vllm-project/vllm/issues/48662) Serving note: pairing vLLM with BGPT evidence MCP for science agents
