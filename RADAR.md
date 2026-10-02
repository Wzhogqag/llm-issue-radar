# LLM Serving Issue Radar

_Last run: 2026-10-02T13:32+00:00_

**26 issues** — sgl-project/sglang: 16, vllm-project/vllm: 10 — 🆕 **26 new** since last run

## Contents

- [Scheduler / Batching](#scheduler--batching) — 1
- [KV Cache / Connector / PD Disagg](#kv-cache--connector--pd-disagg) — 1
- [Attention Backend](#attention-backend) — 1
- [Quantization](#quantization) — 6
- [New Model Integration](#new-model-integration) — 1
- [Sampling / Speculative Decoding](#sampling--speculative-decoding) — 1
- [Serving / OpenAI API / Streaming](#serving--openai-api--streaming) — 10
- [Build / Install / Platform](#build--install--platform) — 3
- [Uncategorized](#uncategorized) — 2

## Scheduler / Batching

### sgl-project/sglang

- [Bug] 🆕 [#42222](https://github.com/sgl-project/sglang/issues/42222) [Bug] expert-distribution endpoints terminate the scheduler when expert_distribution_recorder_mode is unset

## KV Cache / Connector / PD Disagg

### vllm-project/vllm

- [Bug] 🆕 [#59768](https://github.com/vllm-project/vllm/issues/59768) [Bug]: Illegal memory access (Xid 13) with SimpleCPUOffloadConnector on Qwen3.8-Flash-Next while an async CPU→GPU prefix load is in flight / sm120

## Attention Backend

### vllm-project/vllm

- [Bug] 🆕 [#59724](https://github.com/vllm-project/vllm/issues/59724) [Bug][SM120] MTP speculative decoding acceptance rate drops to 0% on nightly with native FLASHINFER_MLA_SPARSE_SM120 backend (GLM-5.3-Flash)

## Quantization

### sgl-project/sglang

- [Bug] 🆕 [#42146](https://github.com/sgl-project/sglang/issues/42146) [Bug] DeepSeek-V4 on SM120: the default SGLANG_FP8_PAGED_MQA_LOGITS_TORCH=True also turns off the C4 indexer's row-chunk planner (+3.3–3.8 GiB at 128k)
- [Feature] 🆕 ⚠maintainer-authored [#42176](https://github.com/sgl-project/sglang/issues/42176) [Feature] Integrate Cake kernels via FlashInfer: model-by-model tracker
- [other] 🆕 ⚠maintainer-authored [#42170](https://github.com/sgl-project/sglang/issues/42170) [Roadmap] DeepSeek V4.1 Optimization

### vllm-project/vllm

- [Performance] 🆕 [#59770](https://github.com/vllm-project/vllm/issues/59770) [Performance]: Nemotron-3.5-Lightning NVFP4 decode ~16% slower on DGX Spark (GB10/SM121) since v0.29.0
- [Feature] 🆕 [#59725](https://github.com/vllm-project/vllm/issues/59725) [Feature]: Integrate Cake kernels via FlashInfer: model-by-model tracker
- [RFC] 🆕 ⚠maintainer-authored [#59665](https://github.com/vllm-project/vllm/issues/59665) [RFC]: Fast-Track Merging for Model Optimization PRs

## New Model Integration

### vllm-project/vllm

- [no-prefix] 🆕 ⚠no-prefix [#59675](https://github.com/vllm-project/vllm/issues/59675) GitHub API version 2022-11-28 is retired in March 2028 (run_ci_command.py)

## Sampling / Speculative Decoding

### vllm-project/vllm

- [Bug] 🆕 [#59764](https://github.com/vllm-project/vllm/issues/59764) [Bug]: Qwen3.6-35B-A3B (hybrid GDN + MoE): identical batches give different logprobs from run to run, and a prompt's logprobs move by up to 0.2 when another sequence shares its step (v0.30.0, sm_120)

## Serving / OpenAI API / Streaming

### sgl-project/sglang

- [Bug] 🆕 [#42144](https://github.com/sgl-project/sglang/issues/42144) [Bug] XGrammarGrammarBackend._sanitize_structural_format` skips `optional`, `star`, `plus`, `repeat`, `dispatch`, `token_dispatch` and `token_triggered_tags`, so a `null` `json_schema` inside them is rejected
- [Bug] 🆕 [#42143](https://github.com/sgl-project/sglang/issues/42143) [Bug] HarmonyParser streaming: arguments of a tool call on the analysis channel are emitted as reasoning
- [Bug] 🆕 [#42138](https://github.com/sgl-project/sglang/issues/42138) [Bug] deepseekv31 detector (streaming): greedy name regex drops a call and attaches the next call's arguments to it
- [Bug] 🆕 [#42137](https://github.com/sgl-project/sglang/issues/42137) [Bug] deepseekv31 detector (streaming): greedy name regex drops a call and attaches the next call's arguments to it
- [Bug] 🆕 [#42136](https://github.com/sgl-project/sglang/issues/42136) [Bug] deepseekv31 detector (streaming) drops the text that shares a delta with the start of a tool call
- [Bug] 🆕 [#42135](https://github.com/sgl-project/sglang/issues/42135) [Bug] cohere_command4 detector (streaming) drops the tool call when text and the whole action block arrive in one chunk
- [Bug] 🆕 [#42132](https://github.com/sgl-project/sglang/issues/42132) [Bug] Glm4MoeDetector streaming emits invalid JSON when a non-string parameter's value is not valid JSON
- [Bug] 🆕 [#42131](https://github.com/sgl-project/sglang/issues/42131) [Bug] DeepSeekV31Detector.structure_info() omits `<｜tool▁calls▁begin｜>`, so its own detect_and_parse returns no tool call
- [no-prefix] 🆕 ⚠no-prefix [#42217](https://github.com/sgl-project/sglang/issues/42217) MultiDetokenizerRouter splits each batch into per-request IPC sends

### vllm-project/vllm

- [RFC] 🆕 [#59750](https://github.com/vllm-project/vllm/issues/59750) [RFC]: Handle empty responses in synthetic acceptance benchmarks

## Build / Install / Platform

### sgl-project/sglang

- [Bug] 🆕 [#42140](https://github.com/sgl-project/sglang/issues/42140) [Bug] trinity detector removes `<think>` / `</think>` from inside tool-call arguments

### vllm-project/vllm

- [Bug] 🆕 [#59765](https://github.com/vllm-project/vllm/issues/59765) [Bug]: ~2% output throughput regression on DeepSeek-R1 NVFP4 (DP4 + EP, GB300) from #48247 (AITER custom AG/RS)
- [Feature] 🆕 [#59755](https://github.com/vllm-project/vllm/issues/59755) [Feature][ROCm]: GLM-5.3-Flash prefill checkpoints

## Uncategorized

### sgl-project/sglang

- [Bug] 🆕 [#42134](https://github.com/sgl-project/sglang/issues/42134) [Bug] ChatCompletionRequest.set_json_schema mutates the caller's response_format schema (reused schemas change behaviour)
- [Bug] 🆕 [#42133](https://github.com/sgl-project/sglang/issues/42133) [Bug]  Glm4MoeDetector changes string-typed argument values that look like JSON ("true" → "True", "1.50" → "1.5")
