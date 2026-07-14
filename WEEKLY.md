# Weekly Trends — 2026-07-14

Window: 2026-07-14 → 2026-07-14 (4 snapshots)

**Totals:** 27 → 29  (5 appeared, 3 vanished)

## Movement by category

| Category | Start | End | Δ | Appeared | Vanished |
|---|---:|---:|---:|---:|---:|
| Build / Install / Platform | 4 | 4 | 0 | 0 | 0 |
| Distributed / TP / PP / EP | 2 | 3 | +1 | 1 | 0 |
| KV Cache / Connector / PD Disagg | 3 | 3 | 0 | 0 | 0 |
| New Model Integration | 1 | 2 | +1 | 1 | 0 |
| Performance / Memory / OOM | 1 | 1 | 0 | 0 | 0 |
| Quantization | 9 | 8 | -1 | 1 | 2 |
| Sampling / Speculative Decoding | 3 | 5 | +2 | 2 | 0 |
| Scheduler / Batching | 2 | 1 | -1 | 0 | 1 |
| Serving / OpenAI API / Streaming | 2 | 2 | 0 | 0 | 0 |

## Appeared this week

### Distributed / TP / PP / EP

- [no-prefix] [vllm-project/vllm#48591](https://github.com/vllm-project/vllm/issues/48591) 还不支持[Usage]: vllm 0.25版本在tp=8并行的时候走dflash 和dspark 命中 attention后端的时候出现错误报错定位 CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_api.cpp:697): invalid configuration argument 8个worker(TP0-TP7)

### New Model Integration

- [no-prefix] [sgl-project/sglang#31175](https://github.com/sgl-project/sglang/issues/31175) Add native OLMo3 (Olmo3ForCausalLM) support by reusing the Olmo2 implementation

### Quantization

- [Bug] [vllm-project/vllm#48492](https://github.com/vllm-project/vllm/issues/48492) [Bug]: Missing quant_config in MTP eh_proj causes severe silent precision loss during W8A8 quantization

### Sampling / Speculative Decoding

- [Bug] [sgl-project/sglang#31178](https://github.com/sgl-project/sglang/issues/31178) [Bug] D node deployed with sglang glm 5.2 pd is throwing an error when using speculative decoding.
- [Bug] [vllm-project/vllm#48592](https://github.com/vllm-project/vllm/issues/48592) [Bug]: v0.25.0 torchcodec not compatible with cu129 wheel

## Vanished this week

_Likely closed, PR merged, or dropped from top 100 by activity — worth spot-checking._

### Quantization

- [Bug] [vllm-project/vllm#48477](https://github.com/vllm-project/vllm/issues/48477) [Bug]: Qwen3.5-122B-A10B-FP8 serve crashes on nightly/0.25 (CUBLAS_STATUS_EXECUTION_FAILED at profile_run); no version serves FP8 hybrid GDN + DFlash together
- [RFC] [vllm-project/vllm#48480](https://github.com/vllm-project/vllm/issues/48480) [RFC]: Make Triton kernel unit tests hardware-agnostic and cover untested kernels

### Scheduler / Batching

- [RFC] [vllm-project/vllm#48478](https://github.com/vllm-project/vllm/issues/48478) [RFC] Fail-Closed Graph Storage Contract for Weight Reload
