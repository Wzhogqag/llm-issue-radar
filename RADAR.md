# LLM Serving Issue Radar

_Last run: 2026-07-19T13:52+00:00_

**19 issues** — sgl-project/sglang: 4, vllm-project/vllm: 15 — 🆕 **9 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 3
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 10
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 2
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Scheduler / Batching

### vllm-project/vllm

- [Bug] 🆕 [#49089](https://github.com/vllm-project/vllm/issues/49089) [Bug]: assert req_id in self.requests in Scheduler._update_from_kv_xfer_finished kills the engine on late KV xfer-finished for an already-failed request

## KV Cache / Connector / PD Disagg

### sgl-project/sglang

- [Bug] [#31640](https://github.com/sgl-project/sglang/issues/31640) [Bug] FA4 decode passes unsupported descale tensors on FP8 nemotron_h; forward_decode lacks the FA4 guard used by forward_extend

### vllm-project/vllm

- [Bug] 🆕 [#49049](https://github.com/vllm-project/vllm/issues/49049) [Bug] Inkling on sm_121a (GB10): unclamped q-row in rel-bias score-mod gather causes deterministic illegal address (coredump evidence); + aux-stream KV-write race in fused_qkvr_prep
- [other] 🆕 [#49064](https://github.com/vllm-project/vllm/issues/49064) [Usability] Engine fails to start when available Mamba cache blocks < max_num_seqs (hybrid models + LoRA) — suggest auto-clamping with a warning

## Attention Backend

### sgl-project/sglang

- [Bug] [#31594](https://github.com/sgl-project/sglang/issues/31594) [Bug] [AMD] Qwen3.5 GatedDeltaNet + dp-attention on ROCm/MoRI: HIP "invalid configuration argument" (linear-attn/Mamba state path); process hangs in chunk_gated_delta_rule_fwd under kernel serialization

## Quantization

### sgl-project/sglang

- [Bug] [#31600](https://github.com/sgl-project/sglang/issues/31600) [Bug] glm-5.2-w4afp8 +l2(hicache)+l3(mooncake) kvcache dram cluster ,cache hit is slower than prefill+ decoder

### vllm-project/vllm

- [Bug] 🆕 [#49079](https://github.com/vllm-project/vllm/issues/49079) [Bug]: --moe-backend flashinfer_b12x roughly doubles peak activation memory vs default, cutting available KV cache ~55%
- [Bug] 🆕 [#49076](https://github.com/vllm-project/vllm/issues/49076) [Bug]:  --linear-backend=flashinfer_b12x crashes on Qwen3.6-35B-A3B-NVFP4 — no kernel for FP8-quantized GDN QKVZ layer
- [Bug] 🆕 [#49070](https://github.com/vllm-project/vllm/issues/49070) [Bug]: MiniMax-M3 NVFP4 produces garbage output + CUDA illegal memory access on Hopper (sm90) via Marlin FP4-MoE
- [Bug] 🆕 [#49005](https://github.com/vllm-project/vllm/issues/49005) [Bug]: Minimax MSA - AttributeError: module 'cutlass.cute.core' has no attribute 'ThrMma'
- [RFC] 🆕 ⚠maintainer-authored [#49090](https://github.com/vllm-project/vllm/issues/49090) [RFC][SpecDecode] Move MTP completeness validation to the weight-update transaction boundary
- [Bug] [#49012](https://github.com/vllm-project/vllm/issues/49012) [Bug]: nvfp4 reshape_and_cache_flash assumes NHD layout — silently mis-swizzles HND caches when num_kv_heads % 4 == 0
- [Bug] [#49010](https://github.com/vllm-project/vllm/issues/49010) [Bug]: XQA decode under FULL cudagraph capture silently corrupts attention output (fp8 and nvfp4 KV)
- [Bug] [#49031](https://github.com/vllm-project/vllm/issues/49031) [Bug]:  FlashInfer B12x W4A16 runtime repacking retains original and packed MoE weights, causing startup OOM
- [Feature] [#49011](https://github.com/vllm-project/vllm/issues/49011) [Feature]: nvfp4 KV cache on SM120 — flashinfer ships the kernels, vLLM isn't wired to them (working prototype, 245K ctx on a 5090)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] [#49004](https://github.com/vllm-project/vllm/issues/49004) [Bug]: DBRX MoE weight loading crashes with KeyError after FusedMoE/MoERunner inversion refactor (#41184) — dbrx.py missed by follow-up fix #45054

## Sampling / Speculative Decoding

### sgl-project/sglang

- [Bug] 🆕 [#31711](https://github.com/sgl-project/sglang/issues/31711) [Bug] XGrammar rollback copies the full token history during EAGLE constrained decoding

### vllm-project/vllm

- [Bug] [#49002](https://github.com/vllm-project/vllm/issues/49002) [Bug]: Speculative Decoding + Structured Output（tool call）组合下，decode 阶段出现秒级卡顿

## Performance / Memory / OOM

### vllm-project/vllm

- [Perf] [#49013](https://github.com/vllm-project/vllm/issues/49013) [Perf] ~2x decode throughput regression for structured outputs since #45424: apply_grammar_bitmask staging rewrite (bisected to commit, file, and hunk)
