# LLM Serving Issue Radar

_Last run: 2026-10-15T13:31+00:00_

**9 issues** — sgl-project/sglang: 3, vllm-project/vllm: 6 — 🆕 **9 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Distributed / TP / PP / EP](#distributed--tp--pp--ep) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 4
- [Build / Install / Platform](#build--install--platform) — 1

## Scheduler / Batching

### sgl-project/sglang

- [Feature] 🆕 [#44485](https://github.com/sgl-project/sglang/issues/44485) [Feature][Spec][Ngram] Freeze external-corpus SAMs into a compact layout after finalize()

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [RFC] 🆕 [#61787](https://github.com/vllm-project/vllm/issues/61787) [RFC]: Layerwise KV Pooling and P/D Disaggregation for High-Hit-Rate Agent Workloads

## Attention Backend

### sgl-project/sglang

- [other] 🆕 [#44445](https://github.com/sgl-project/sglang/issues/44445) [Report] DeepSeek-V4.1-Flash on 4x SM120 (83 GiB): 1M context + DSpark works on v0.5.21, setup notes and numbers

## Distributed / TP / PP / EP

### vllm-project/vllm

- [Bug] 🆕 [#61820](https://github.com/vllm-project/vllm/issues/61820) [Bug]: Whisper long-audio transcription loses words at the internal 30 s cut points in json/text (split_audio cuts inside speech, no overlap or merge)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#61762](https://github.com/vllm-project/vllm/issues/61762) [Bug]: Scheduler livelock with multi-module MTP + Mamba align prefix caching when prompt_len % block_size < num_speculative_tokens
- [Bug] 🆕 [#61738](https://github.com/vllm-project/vllm/issues/61738) [Bug]: Wide speculative decoding verify (num_speculative_tokens ≥ 7) samples EOS at `prompt_len+8` on hybrid GDN models (Qwen3.5): silent early stop, byte-clean until the EOS row — reproduced on both model runners (`ngram_gpu` V1, stock MTP V2)
- [Feature] 🆕 [#61771](https://github.com/vllm-project/vllm/issues/61771) [Feature]: Harden logit_bias against absolute-logit leakage
- [RFC] 🆕 [#61761](https://github.com/vllm-project/vllm/issues/61761) [RFC]: DFlash2 speculative decoding performance on ROCm (MI355X)

## Build / Install / Platform

### sgl-project/sglang

- [other] 🆕 ⚠maintainer-authored [#44479](https://github.com/sgl-project/sglang/issues/44479) [CI] Runner 5090-vast-no-0 is out of disk: every job fails in Install dependencies with 'No space left on device'
