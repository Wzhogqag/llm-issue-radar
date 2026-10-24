# LLM Serving Issue Radar

_Last run: 2026-10-24T13:26+00:00_

**8 issues** — sgl-project/sglang: 2, vllm-project/vllm: 6 — 🆕 **8 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 2
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 2
- [Build / Install / Platform](#build--install--platform) — 1
- [Uncategorized](#uncategorized) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#46203](https://github.com/sgl-project/sglang/issues/46203) [Bug]  Xid 13 "CTA Not Present" in HiCache kvcacheio transfer kernels on Blackwell (B20Z) — 7 crashes across 4 machines / 7 GPU instances under agentic load

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#63465](https://github.com/vllm-project/vllm/issues/63465) [Bug]: Mooncake Store split-load failures omit unattempted KV blocks from invalidation
- [RFC] 🆕 [#63439](https://github.com/vllm-project/vllm/issues/63439) [RFC]: Reduce CPU overhead in Model Runner V2 for long-context P/D serving

## Attention Backend

### vllm-project/vllm

- [Performance] 🆕 [#63399](https://github.com/vllm-project/vllm/issues/63399) [Performance]: Startup sizing of FlashInfer workspace to recover KV-cache capacity

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#46259](https://github.com/sgl-project/sglang/issues/46259) [Bug] FlashInfer prefill is not split-invariant: radix-cache hit or chunked prefill flips greedy output on a Qwen3.5 hybrid GDN model

### vllm-project/vllm

- [Bug] 🆕 [#63455](https://github.com/vllm-project/vllm/issues/63455) [Bug]: [ROCm] AutoAWQ checkpoints never use the RDNA W4A16 kernel; AWQ decodes 2.5x slower than BF16 on gfx1151

## Build / Install / Platform

### vllm-project/vllm

- [Bug] 🆕 [#63467](https://github.com/vllm-project/vllm/issues/63467) [Bug]: Wrong token ids from fastokens' split cache before 0.3.4 (Rust frontend, VLLM_USE_FASTOKENS)

## Uncategorized

### vllm-project/vllm

- [Feature] 🆕 [#63470](https://github.com/vllm-project/vllm/issues/63470) [Feature]: Run Nemotron 3.5 Super VL without the --trust-remote-code flag
