# LLM Serving Issue Radar

_Last run: 2026-11-08T13:21+00:00_

**13 issues** — sgl-project/sglang: 4, vllm-project/vllm: 9 — 🆕 **13 new** since last run

## Contents

- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 3
- [New Model Integration](#new-model-integration) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 2
- [Build / Install / Platform](#build--install--platform) — 4

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#49133](https://github.com/sgl-project/sglang/issues/49133) [Bug] Breakable prefill CUDA graph: short prefills padded to a capture bucket give different logprobs than eager (Qwen3.8-27B-NVFP4, hybrid GDN, v0.5.23)
- [Bug] 🆕 [#49132](https://github.com/sgl-project/sglang/issues/49132) [Bug] Qwen3-VL vision encoder: full-size transient tensors (pos-embed blend `[4, patches, 1152]`, MLP `[patches, 4304]`) OOM memory-tight GPUs on large images; both can be computed in row chunks
- [Feature] 🆕 [#49123](https://github.com/sgl-project/sglang/issues/49123) [Feature] moe: FlashInfer cuTile NVFP4 MoE as the default runner on SM12x

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#66387](https://github.com/vllm-project/vllm/issues/66387) [Bug]: DFlash acceptance collapses at tensor parallel > 1 (MiMo-V2.6-Flash-MOPD, TP1 fine)
- [Feature] 🆕 [#66301](https://github.com/vllm-project/vllm/issues/66301) [Feature]: Deploying vLLM with Ray on SLURM-based university HPC clusters
- [RFC] 🆕 [#66290](https://github.com/vllm-project/vllm/issues/66290) [RFC]: Pipeline-parallel equivalence tests for every model that declares `SupportsPP`

## New Model Integration

### vllm-project/vllm

- [Bug] 🆕 [#66300](https://github.com/vllm-project/vllm/issues/66300) [Bug]: llama3.2_pythonic and toolace chat templates render string arguments unquoted, so the pythonic parser drops the call

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#66392](https://github.com/vllm-project/vllm/issues/66392) [Bug]: /v1/systemone caps Clef-Flash choice questions at 26 options, though the joint-schema read uses no labels
- [Bug] 🆕 [#66298](https://github.com/vllm-project/vllm/issues/66298) [Bug]: gemma3_pythonic chat template renders tool call arguments with no separator, so the pythonic parser rejects the whole call

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#49108](https://github.com/sgl-project/sglang/issues/49108) [Bug] Rust extension loader: cargo --version probe can deadlock in launcher spawn context (defensive timeout suggestion)

### vllm-project/vllm

- [Bug] 🆕 [#66288](https://github.com/vllm-project/vllm/issues/66288) [Bug]: Qwen3.5 RMSNorm JIT-compiles FlashInfer kernels on sm75 (T4)
- [Bug] 🆕 [#66293](https://github.com/vllm-project/vllm/issues/66293) [Bug]: vllm/vllm-openai:muse-spark-open needs to be rebuilt with the issue fixed in #62374
- [no-prefix] 🆕 ⚠no-prefix [#66345](https://github.com/vllm-project/vllm/issues/66345) `llguidance` is an unconditional dependency and is loaded by `from vllm import LLM`; it blocks install and import on glibc < 2.31
