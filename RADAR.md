# LLM Serving Issue Radar

_Last run: 2026-11-02T13:22+00:00_

**20 issues** — sgl-project/sglang: 1, vllm-project/vllm: 19 — 🆕 **20 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 2
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 2
- [New Model Integration](#new-model-integration) — 2
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1
- [Build / Install / Platform](#build--install--platform) — 6

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#65115](https://github.com/vllm-project/vllm/issues/65115) [Bug]: DeepSeek render parity — native appends EOS for continue_final_message, vllm-rs does not
- [Bug] 🆕 [#65114](https://github.com/vllm-project/vllm/issues/65114) [Bug]: vllm-rs chat render and native render select opposite thinking modes when a thinking toggle is combined with a reasoning-effort control

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Performance] 🆕 [#65161](https://github.com/vllm-project/vllm/issues/65161) [Performance]: With EAGLE and the OffloadingConnector, a prefix-cache hit loads its dropped last block from the CPU tier

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#65105](https://github.com/vllm-project/vllm/issues/65105) [Bug]: [ROCm] AITER MLA `paged_kv_indices` sized max_num_seqs x max_model_len (4 GiB per builder) pins a cached segment, Kimi-K3 DBO OOMs at startup

## Quantization

### vllm-project/vllm

- [Bug] 🆕 [#65070](https://github.com/vllm-project/vllm/issues/65070) [Bug]:  CPU WNA16 MoE cannot load poolside/Laguna-XS-2.1-INT4

## Distributed / TP / PP / EP

### vllm-project/vllm

- [RFC] 🆕 [#65121](https://github.com/vllm-project/vllm/issues/65121) [RFC]: DBO with the allgather_reducescatter all2all backend on CUDA
- [RFC] 🆕 [#65122](https://github.com/vllm-project/vllm/issues/65122) [RFC]: Zero-copy DeepEP low-latency combine, safe under DBO

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#65095](https://github.com/vllm-project/vllm/issues/65095) [Bug]: The message API doesn't support min_tokens for now
- [RFC] 🆕 [#65120](https://github.com/vllm-project/vllm/issues/65120) [RFC]: DBO for the decoder of multimodal MoE models in Model Runner V2

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#65139](https://github.com/vllm-project/vllm/issues/65139) [Bug]: b12x attention — CUDA illegal memory access at the first MTP verify step (cold-JIT `PagedForwardKernel`) on v0.33.0; regression from v0.32.0 (SM120, NVFP4 MoE, fp8 KV, chunked prefill, prefix caching, MTP spec decode)
- [RFC] 🆕 [#65119](https://github.com/vllm-project/vllm/issues/65119) [RFC]: DBO for the MTP/EAGLE drafter forward in Model Runner V2

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#65096](https://github.com/vllm-project/vllm/issues/65096) [Bug]: Unbounded startup wait holds --data-parallel-rpc-port; crashed frontend leaves orphaned processes holding accelerator memory and the shared API listen socket
- [Bug] 🆕 [#65075](https://github.com/vllm-project/vllm/issues/65075) [Bug]: Bi-encoder scoring token limits fail with MistralTokenizer

## Performance / Memory / OOM

### sgl-project/sglang

- [Bug] 🆕 [#47916](https://github.com/sgl-project/sglang/issues/47916) [Bug] [mamba/hybrid] MambaPool.copy_from gathers all source temporal states into one temporary (n x state_size) - CUDA OOM under parallel admission bursts

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#65106](https://github.com/vllm-project/vllm/issues/65106) [Bug]: [ROCm][Kimi-K3] DBO: MoE workspace locked smaller than the DP-gathered batch, first request fails
- [Bug] 🆕 [#65074](https://github.com/vllm-project/vllm/issues/65074) [Bug]: MCP tool discovery drops tools after the first tools/list page
- [Bug] 🆕 [#65073](https://github.com/vllm-project/vllm/issues/65073) [Bug]: Duplicate MCP server names advertise tools from a different execution server
- [Bug] 🆕 [#65072](https://github.com/vllm-project/vllm/issues/65072) [Bug]: ASRDataset uses channel count as duration when filtering stereo audio bytes
- [Bug] 🆕 [#65071](https://github.com/vllm-project/vllm/issues/65071) [Bug]: CustomDataset converts numeric-string prompts to integers before tokenization
- [Feature] 🆕 [#65151](https://github.com/vllm-project/vllm/issues/65151) [Feature][ROCm]: Configurable HIP host wait policy for WSL GPU workers
