# LLM Serving Issue Radar

_Last run: 2026-07-18T13:51+00:00_

**21 issues** — sgl-project/sglang: 7, vllm-project/vllm: 14 — 🆕 **13 new** since last run

## Contents

- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 2
- [Quantization](#quantization) — 9
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 1
- [Performance / Memory / OOM](#performance--memory--oom) — 2
- [Build / Install / Platform](#build--install--platform) — 2

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] 🆕 [#31640](https://github.com/sgl-project/sglang/issues/31640) [Bug] FA4 decode passes unsupported descale tensors on FP8 nemotron_h; forward_decode lacks the FA4 guard used by forward_extend

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#48959](https://github.com/vllm-project/vllm/issues/48959) CPU offload fatal: valid unaligned SWA external load exceeds aligned pending-block bound

## Attention Backend

### sgl-project/sglang

- [Bug] 🆕 [#31594](https://github.com/sgl-project/sglang/issues/31594) [Bug] [AMD] Qwen3.5 GatedDeltaNet + dp-attention on ROCm/MoRI: HIP "invalid configuration argument" (linear-attn/Mamba state path); process hangs in chunk_gated_delta_rule_fwd under kernel serialization
- [Feature] [#31578](https://github.com/sgl-project/sglang/issues/31578) [Feature] Native SM120 (Blackwell) support for flash_mla_sparse_fwd (DeepSeek-V4 sparse-attention prefill)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#31600](https://github.com/sgl-project/sglang/issues/31600) [Bug] glm-5.2-w4afp8 +l2(hicache)+l3(mooncake) kvcache dram cluster ,cache hit is slower than prefill+ decoder
- [Feature] [#31570](https://github.com/sgl-project/sglang/issues/31570) [Feature] [NPU] Implement CI test for different quantization prefixes (w1/2/3; gate/up/down_proj)

### vllm-project/vllm

- [Bug] 🆕 [#49031](https://github.com/vllm-project/vllm/issues/49031) [Bug]:  FlashInfer B12x W4A16 runtime repacking retains original and packed MoE weights, causing startup OOM
- [Bug] 🆕 [#49012](https://github.com/vllm-project/vllm/issues/49012) [Bug]: nvfp4 reshape_and_cache_flash assumes NHD layout — silently mis-swizzles HND caches when num_kv_heads % 4 == 0
- [Bug] 🆕 [#49010](https://github.com/vllm-project/vllm/issues/49010) [Bug]: XQA decode under FULL cudagraph capture silently corrupts attention output (fp8 and nvfp4 KV)
- [Feature] 🆕 [#49011](https://github.com/vllm-project/vllm/issues/49011) [Feature]: nvfp4 KV cache on SM120 — flashinfer ships the kernels, vLLM isn't wired to them (working prototype, 245K ctx on a 5090)
- [Bug] [#48946](https://github.com/vllm-project/vllm/issues/48946) [Bug][XPU]: gpt-oss-120b (MXFP4 MoE, TP=2) corrupt under piecewise XPU graph capture on Data Center GPU Max 1100 (PVC); compile-mode correct
- [Bug] [#48945](https://github.com/vllm-project/vllm/issues/48945) [Bug]: Ministral is broken with --kv-cache-dtype fp8 in 0.25.1
- [RFC] [#48941](https://github.com/vllm-project/vllm/issues/48941) [RFC] Recursive Tensor Collector: Fix CUDA Graph Invalidation After Weight Reload

## Distributed / TP / PP / EP

### sgl-project/sglang

- [Bug] [#31568](https://github.com/sgl-project/sglang/issues/31568) [Bug] Unused/unnecessary tl.constexpr params causing Triton cache-key pollution in KV-cache and FLA kernels

### vllm-project/vllm

- [Bug] 🆕 [#49004](https://github.com/vllm-project/vllm/issues/49004) [Bug]: DBRX MoE weight loading crashes with KeyError after FusedMoE/MoERunner inversion refactor (#41184) — dbrx.py missed by follow-up fix #45054

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#49002](https://github.com/vllm-project/vllm/issues/49002) [Bug]: Speculative Decoding + Structured Output（tool call）组合下，decode 阶段出现秒级卡顿

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] [#48931](https://github.com/vllm-project/vllm/issues/48931) [Bug] DeepSeek-V4 tool-call parser leaks raw DSML into content when the model omits the `<｜DSML｜tool_calls>` START token (long context)

## Performance / Memory / OOM

### vllm-project/vllm

- [Perf] 🆕 [#49013](https://github.com/vllm-project/vllm/issues/49013) [Perf] ~2x decode throughput regression for structured outputs since #45424: apply_grammar_bitmask staging rewrite (bisected to commit, file, and hunk)
- [no-prefix] 🆕 ⚠no-prefix [#48966](https://github.com/vllm-project/vllm/issues/48966) Unexpected EngineCore death exits serving process 0, defeating Restart=on-failure

## Build / Install / Platform

### sgl-project/sglang

- [Bug] [#31545](https://github.com/sgl-project/sglang/issues/31545) [Bug][ROCm] MI355X: CUDA-graph decode kernels are captured but async-deferred into one post-marker burst — per-step timing unrecoverable (torch profiler)

### vllm-project/vllm

- [Bug] 🆕 [#48934](https://github.com/vllm-project/vllm/issues/48934) [Bug]: Qwen3.5 CausalLM missing embedding_modules breaks LoRA on embed_tokens/lm_head
