# Weekly Trends — 2026-11-08

Window: 2026-11-02 → 2026-11-08 (7 snapshots)

**Totals:** 20 → 13  (13 appeared, 20 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Attention Backend | 1 | 0 | -1 | 0 | 1 |
| Build / Install / Platform | 6 | 4 | -2 | 4 | 6 |
| Distributed / TP / PP / EP | 2 | 3 | +1 | 3 | 2 |
| KV Cache / Connector / PD Disagg | 1 | 0 | -1 | 0 | 1 |
| New Model Integration | 2 | 1 | -1 | 1 | 2 |
| Performance / Memory / OOM | 1 | 0 | -1 | 0 | 1 |
| Quantization | 1 | 3 | +2 | 3 | 1 |
| Sampling / Speculative Decoding | 2 | 0 | -2 | 0 | 2 |
| Scheduler / Batching | 2 | 0 | -2 | 0 | 2 |
| Serving / OpenAI API / Streaming | 2 | 2 | 0 | 2 | 2 |

## Appeared this week

### Build / Install / Platform

- [Bug] [sgl-project/sglang#49108](https://github.com/sgl-project/sglang/issues/49108) [Bug] Rust extension loader: cargo --version probe can deadlock in launcher spawn context (defensive timeout suggestion)
- [Bug] [vllm-project/vllm#66288](https://github.com/vllm-project/vllm/issues/66288) [Bug]: Qwen3.5 RMSNorm JIT-compiles FlashInfer kernels on sm75 (T4)
- [Bug] [vllm-project/vllm#66293](https://github.com/vllm-project/vllm/issues/66293) [Bug]: vllm/vllm-openai:muse-spark-open needs to be rebuilt with the issue fixed in #62374
- [no-prefix] [vllm-project/vllm#66345](https://github.com/vllm-project/vllm/issues/66345) `llguidance` is an unconditional dependency and is loaded by `from vllm import LLM`; it blocks install and import on glibc < 2.31

### Distributed / TP / PP / EP

- [RFC] [vllm-project/vllm#66290](https://github.com/vllm-project/vllm/issues/66290) [RFC]: Pipeline-parallel equivalence tests for every model that declares `SupportsPP`
- [Feature] [vllm-project/vllm#66301](https://github.com/vllm-project/vllm/issues/66301) [Feature]: Deploying vLLM with Ray on SLURM-based university HPC clusters
- [Bug] [vllm-project/vllm#66387](https://github.com/vllm-project/vllm/issues/66387) [Bug]: DFlash acceptance collapses at tensor parallel > 1 (MiMo-V2.6-Flash-MOPD, TP1 fine)

### New Model Integration

- [Bug] [vllm-project/vllm#66300](https://github.com/vllm-project/vllm/issues/66300) [Bug]: llama3.2_pythonic and toolace chat templates render string arguments unquoted, so the pythonic parser drops the call

### Quantization

- [Feature] [sgl-project/sglang#49123](https://github.com/sgl-project/sglang/issues/49123) [Feature] moe: FlashInfer cuTile NVFP4 MoE as the default runner on SM12x
- [Bug] [sgl-project/sglang#49132](https://github.com/sgl-project/sglang/issues/49132) [Bug] Qwen3-VL vision encoder: full-size transient tensors (pos-embed blend `[4, patches, 1152]`, MLP `[patches, 4304]`) OOM memory-tight GPUs on large images; both can be computed in row chunks
- [Bug] [sgl-project/sglang#49133](https://github.com/sgl-project/sglang/issues/49133) [Bug] Breakable prefill CUDA graph: short prefills padded to a capture bucket give different logprobs than eager (Qwen3.8-27B-NVFP4, hybrid GDN, v0.5.23)

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#66298](https://github.com/vllm-project/vllm/issues/66298) [Bug]: gemma3_pythonic chat template renders tool call arguments with no separator, so the pythonic parser rejects the whole call
- [Bug] [vllm-project/vllm#66392](https://github.com/vllm-project/vllm/issues/66392) [Bug]: /v1/systemone caps Clef-Flash choice questions at 26 options, though the joint-schema read uses no labels

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Attention Backend

- [Bug] [vllm-project/vllm#65105](https://github.com/vllm-project/vllm/issues/65105) [Bug]: [ROCm] AITER MLA `paged_kv_indices` sized max_num_seqs x max_model_len (4 GiB per builder) pins a cached segment, Kimi-K3 DBO OOMs at startup

### Build / Install / Platform

- [Bug] [vllm-project/vllm#65071](https://github.com/vllm-project/vllm/issues/65071) [Bug]: CustomDataset converts numeric-string prompts to integers before tokenization
- [Bug] [vllm-project/vllm#65072](https://github.com/vllm-project/vllm/issues/65072) [Bug]: ASRDataset uses channel count as duration when filtering stereo audio bytes
- [Bug] [vllm-project/vllm#65073](https://github.com/vllm-project/vllm/issues/65073) [Bug]: Duplicate MCP server names advertise tools from a different execution server
- [Bug] [vllm-project/vllm#65074](https://github.com/vllm-project/vllm/issues/65074) [Bug]: MCP tool discovery drops tools after the first tools/list page
- [Bug] [vllm-project/vllm#65106](https://github.com/vllm-project/vllm/issues/65106) [Bug]: [ROCm][Kimi-K3] DBO: MoE workspace locked smaller than the DP-gathered batch, first request fails
- [Feature] [vllm-project/vllm#65151](https://github.com/vllm-project/vllm/issues/65151) [Feature][ROCm]: Configurable HIP host wait policy for WSL GPU workers

### Distributed / TP / PP / EP

- [RFC] [vllm-project/vllm#65121](https://github.com/vllm-project/vllm/issues/65121) [RFC]: DBO with the allgather_reducescatter all2all backend on CUDA
- [RFC] [vllm-project/vllm#65122](https://github.com/vllm-project/vllm/issues/65122) [RFC]: Zero-copy DeepEP low-latency combine, safe under DBO

### KV Cache / Connector / PD Disagg

- [Performance] [vllm-project/vllm#65161](https://github.com/vllm-project/vllm/issues/65161) [Performance]: With EAGLE and the OffloadingConnector, a prefix-cache hit loads its dropped last block from the CPU tier

### New Model Integration

- [Bug] [vllm-project/vllm#65095](https://github.com/vllm-project/vllm/issues/65095) [Bug]: The message API doesn't support min_tokens for now
- [RFC] [vllm-project/vllm#65120](https://github.com/vllm-project/vllm/issues/65120) [RFC]: DBO for the decoder of multimodal MoE models in Model Runner V2

### Performance / Memory / OOM

- [Bug] [sgl-project/sglang#47916](https://github.com/sgl-project/sglang/issues/47916) [Bug] [mamba/hybrid] MambaPool.copy_from gathers all source temporal states into one temporary (n x state_size) - CUDA OOM under parallel admission bursts

### Quantization

- [Bug] [vllm-project/vllm#65070](https://github.com/vllm-project/vllm/issues/65070) [Bug]:  CPU WNA16 MoE cannot load poolside/Laguna-XS-2.1-INT4

### Sampling / Speculative Decoding

- [RFC] [vllm-project/vllm#65119](https://github.com/vllm-project/vllm/issues/65119) [RFC]: DBO for the MTP/EAGLE drafter forward in Model Runner V2
- [Bug] [vllm-project/vllm#65139](https://github.com/vllm-project/vllm/issues/65139) [Bug]: b12x attention — CUDA illegal memory access at the first MTP verify step (cold-JIT `PagedForwardKernel`) on v0.33.0; regression from v0.32.0 (SM120, NVFP4 MoE, fp8 KV, chunked prefill, prefix caching, MTP spec decode)

### Scheduler / Batching

- [Bug] [vllm-project/vllm#65114](https://github.com/vllm-project/vllm/issues/65114) [Bug]: vllm-rs chat render and native render select opposite thinking modes when a thinking toggle is combined with a reasoning-effort control
- [Bug] [vllm-project/vllm#65115](https://github.com/vllm-project/vllm/issues/65115) [Bug]: DeepSeek render parity — native appends EOS for continue_final_message, vllm-rs does not

### Serving / OpenAI API / Streaming

- [Bug] [vllm-project/vllm#65075](https://github.com/vllm-project/vllm/issues/65075) [Bug]: Bi-encoder scoring token limits fail with MistralTokenizer
- [Bug] [vllm-project/vllm#65096](https://github.com/vllm-project/vllm/issues/65096) [Bug]: Unbounded startup wait holds --data-parallel-rpc-port; crashed frontend leaves orphaned processes holding accelerator memory and the shared API listen socket
