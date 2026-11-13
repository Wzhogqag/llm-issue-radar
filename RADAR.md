# LLM Serving Issue Radar

_Last run: 2026-11-13T13:22+00:00_

**8 issues** — sgl-project/sglang: 1, vllm-project/vllm: 7 — 🆕 **8 new** since last run

## Contents

- [Quantization](#quantization) — 3
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 3
- [Performance / Memory / OOM](#performance--memory--oom) — 1

## Quantization

### sgl-project/sglang

- [other] 🆕 [#50241](https://github.com/sgl-project/sglang/issues/50241) [Tracking] Deterministic inference on AMD Instinct MI350X / MI355X (gfx950)

### vllm-project/vllm

- [Feature] 🆕 [#67412](https://github.com/vllm-project/vllm/issues/67412) [Feature]: Add native support for ZAQERIS AXIOM (ZaqerisAxiomForCausalLM)
- [other] 🆕 [#67384](https://github.com/vllm-project/vllm/issues/67384) [ROCm][AMD] MiniMax-M3.1-Flash gfx950 / MI355X Performance Optimization (vLLM)

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#67416](https://github.com/vllm-project/vllm/issues/67416) [Bug]: sharded_state reload fails for DeepSeek-V4.1-Flash (TP4): "size of tensor a (1792) must match the size of tensor b (5120) at non-singleton dimension 0" in ShardedStateLoader.load_weights

## Serving / OpenAI API / Streaming

### vllm-project/vllm

- [Bug] 🆕 [#67464](https://github.com/vllm-project/vllm/issues/67464) [Bug]: Non-streaming Responses API puts reasoning-token logprobs on output_text
- [Feature] 🆕 [#67430](https://github.com/vllm-project/vllm/issues/67430) [Feature]: vllm.Inference: metadata-only media items, render fingerprint check, and retryable KV and EC load errors
- [Feature] 🆕 [#67478](https://github.com/vllm-project/vllm/issues/67478) [Feature]: Bound the lifetime of per-name LoRA locks in serving

## Performance / Memory / OOM

### vllm-project/vllm

- [Performance] 🆕 [#67462](https://github.com/vllm-project/vllm/issues/67462) [Performance]: [V1] [Performance Benchmark] Find benchmark setups that can test the effectiveness of combining all different optimizations.
