---
title: "Running on another GPU is not the same as being portable"
description: "CUDA lock-in is more than a compiler problem. A practical guide to assessing AI workload portability across NVIDIA, AMD and other accelerator stacks."
date: 2026-11-27
status: draft
author: Priyam Jain
slug: running-on-another-gpu-is-not-portability
category: AI Infrastructure
tags:
  - GPU portability
  - CUDA
  - ROCm
  - LLM inference
---

# Running on another GPU is not the same as being portable

A model might run on two types of GPU and still be expensive to move between them.

That is the part of the CUDA discussion I find most interesting. We usually talk about access to accelerators or whether a particular model *supports* another vendor. But a production team has a harder question: **can I move this exact workload without breaking its behavior, missing its latency target, or spending more to operate it?**

While exploring what heterogeneous GPU infrastructure might look like, I kept coming back to that distinction. The problem isn't simply whether code compiles. It's what *portability* ought to mean when the software is actually serving users.

This is a technical assessment, not the result of a cross-vendor benchmark I've run. The examples below are hypothetical; the capabilities and constraints are drawn from the linked project documentation.

## CUDA is not one dependency

CUDA is often discussed as if it were a language that could be swapped for another language. In practice, NVIDIA's toolkit encompasses development tools, runtime components and mathematical libraries; applications may also depend on optimized kernels, collective communication, drivers, profiling tools and specific build configurations. NVIDIA's [CUDA Toolkit documentation and license](https://docs.nvidia.com/cuda/eula/index.html) describe the scope of the SDK.

Not all these components have the same portability problem. A model written in high-level PyTorch can be much easier to move than a project with custom CUDA kernels and assumptions about memory, execution or multi-GPU communication.

There is an important counterexample to the claim that everything is locked to CUDA: **PyTorch's ROCm build intentionally exposes AMD GPUs through familiar `torch.cuda` interfaces**. A working `torch.cuda` call therefore does not, by itself, prove that NVIDIA hardware is required. See [PyTorch's HIP semantics](https://docs.pytorch.org/docs/stable/notes/hip.html).

Similarly, [vLLM documents support for NVIDIA CUDA, AMD ROCm and other backends](https://docs.vllm.ai/en/latest/getting_started/installation/index.html). Many common workloads already have a realistic alternative path. Support, however, remains specific to devices, software versions, models, operators and configurations.

The difficult cases sit at the boundaries between layers.

## Five different meanings of "it works on another GPU"

| Layer | Question worth asking | Example of a blocker |
| --- | --- | --- |
| **Framework** | Can the model and its operators execute? | An unsupported operation or missing build |
| **Kernels and libraries** | Are the optimized execution paths available? | A CUDA-specific attention or quantization extension |
| **Runtime and communication** | Can it be deployed and scaled reliably? | Driver/version mismatches or incompatible collective behavior |
| **Correctness** | Are outputs acceptably equivalent for this application? | Numerical or precision differences outside the application's tolerance |
| **Performance and operations** | Does it meet latency, throughput, memory and cost requirements? | Higher tail latency or operational burden despite lower hardware price |

Passing the first row is useful. It is not the same as passing all five.

### A hypothetical inference migration

Imagine a team serving an open-weight language model on NVIDIA hardware using PyTorch and vLLM, with a particular quantization path and one custom CUDA extension.

The team wants to evaluate an AMD deployment. A reasonable first attempt would be to use documented ROCm builds and supported vLLM configurations. That might eliminate much of the migration effort.

But they would still need to check:

1. Whether the exact model, precision and quantization combination is supported.
2. Whether that custom extension has an equivalent kernel or fallback.
3. Whether the outputs and error behavior remain acceptable on a representative test set.
4. Whether the deployment can achieve its required concurrency and latency.
5. Whether operational cost actually improves after accounting for integration, capacity and maintenance.

None of these steps proves AMD is generally slower, NVIDIA is always better or migration is impossible. The outcome depends on the workload and the exact hardware/software combination. That uncertainty is precisely why a compatibility label cannot settle an infrastructure decision.

## Existing open-source tools already solve meaningful pieces

A credible portability discussion has to start with what exists.

**[AMD HIP and HIPIFY](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html)** help developers migrate CUDA-oriented source to HIP. AMD explicitly advises reviewing translated code and replacing unsupported libraries or constructs. Translation is a starting point, not a correctness or performance certificate.

**[Triton](https://github.com/triton-lang/triton)** is an open-source language and compiler for GPU kernels, with documented NVIDIA and AMD support. It can reduce reliance on vendor-specific kernel implementations for supported hardware and operators, but it does not guarantee equal performance, universal hardware support or compatibility with every existing CUDA library.

**[SYCLomatic](https://www.intel.com/content/www/us/en/developer/tools/oneapi/training/migrate-from-cuda-to-cpp-with-sycl.html)** provides another approach: assisted CUDA-to-SYCL migration. The resulting code still needs review, target-specific validation and potentially optimization.

And at a higher layer, **PyTorch and vLLM already abstract much of the device-specific work** for supported configurations.

This changes the question. We don't need to pretend the industry has no portability tools. We need to understand the gaps between *conversion, deployment, verification and acceptable economics*.

## A better definition of portable

I would treat portability as a measurable contract rather than a binary label.

For a specific workload, target accelerator and software version, a portability report ought to answer:

- **Compatibility:** Which dependencies, operators, kernels and communication paths work natively, require adaptation or remain unsupported?
- **Correctness:** What tests were run, what tolerances were chosen, and what changed?
- **Performance:** What are time-to-first-token, output-token throughput, p50/p95 latency, memory usage and error rates under comparable load?
- **Economics:** What is the cost of serving valid requests while meeting the actual service-level objective?
- **Reproducibility:** Can another engineer reproduce the result with pinned versions, a documented workload and the same acceptance criteria?

It is especially easy to make misleading cost comparisons. A GPU with a lower hourly rental price can be worse value if it produces fewer acceptable tokens at the required latency or needs significant extra engineering work.

For a **defined measurement window**, an illustrative comparison is:

```text
effective cost per 1M valid output tokens =
  (accelerator cost + incremental infrastructure + operations
   + amortized migration/maintenance effort)
  / valid output tokens served
  × 1,000,000
```

The numerator should avoid double counting energy or networking already included in rental prices. The denominator must use the same workload definition and output validation across candidates. This isn't an industry-standard benchmark formula—it's a way to make the accounting assumptions explicit.

[MLCommons publishes inference benchmarking methods](https://mlcommons.org/benchmarks/inference-datacenter/) precisely because workload shapes, quality requirements, throughput, and latency constraints all affect what a performance number means. A headline "tokens per second" comparison without those details is often insufficient for a procurement decision.

## What would a useful portability test look like?

I would start narrowly: **one representative LLM inference workload, two supported accelerator backends, and a public test harness**.

The experiment should be reproducible and boring in the best sense:

1. Fix the model revision, tokenizer, prompt set, input/output lengths, precision and quality criteria.
2. Pin the serving framework, runtime, driver and kernel versions separately for each backend.
3. Run functional checks first; document differences and unsupported features rather than silently substituting workloads.
4. Warm up and test at matched offered load or realistic concurrent request levels, not just single-request speed.
5. Record throughput, time-to-first-token, tail latency, errors, GPU memory, utilization and deployment effort.
6. Publish the environment, configuration, test methodology and failures alongside the measurements.

There may be valid reasons to choose different optimizations for different architectures. If that happens, publish *both* a close-to-equivalent configuration comparison and a separately labeled best-tuned-per-platform comparison. Otherwise the benchmark can accidentally measure tuning effort rather than the portability trade-off.

I have not run this comparison yet; the checklist describes how I would evaluate the claim, not what the result will be.

## What about combining different GPU vendors into one compute pool?

This is where portability becomes especially relevant to smaller compute operators. Imagine a platform with NVIDIA servers in one location and AMD servers in another.

A practical first step is **workload-level routing**: decide which compatible pool should run a whole job or inference deployment, based on availability, measured performance, data movement and economics.

That is very different from making multiple GPU brands behave like a single tightly coupled accelerator. Tensor parallelism and other distributed execution schemes have additional constraints around communication, synchronization, interconnects and supported kernels. For example, [NVIDIA NCCL](https://developer.nvidia.com/nccl) and [AMD RCCL](https://rocm.docs.amd.com/projects/rccl/en/latest/) are each optimized collective-communication stacks for their respective GPU ecosystems. A common job scheduler cannot make those constraints disappear.

The sensible initial objective is *portable placement of supported workloads*, not the promise of universally interchangeable GPU memory.

## The unsolved work is verification

I don't think the useful goal is "replace CUDA tomorrow." There are already serious compiler, runtime, library and framework efforts reducing that dependence.

A more actionable goal is to make **switching costs observable**: identify what will break, show the work needed to fix it, and demonstrate whether an alternative is worth running for this workload.

For some projects, the answer may be that the existing stack is portable enough. For others, one custom kernel or performance requirement could make switching uneconomical.

Both are useful results.

AI infrastructure becomes more flexible when engineers can make that choice using reproducible evidence instead of assuming either complete lock-in or effortless portability.

---

## Sources and further reading

- [NVIDIA CUDA Toolkit and license scope](https://docs.nvidia.com/cuda/eula/index.html)
- [PyTorch: HIP (ROCm) semantics](https://docs.pytorch.org/docs/stable/notes/hip.html)
- [vLLM: supported hardware backends](https://docs.vllm.ai/en/latest/getting_started/installation/index.html)
- [AMD HIPIFY documentation](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html)
- [AMD HIP porting guide](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html)
- [Triton language and compiler](https://github.com/triton-lang/triton)
- [Intel: CUDA-to-SYCL migration](https://www.intel.com/content/www/us/en/developer/tools/oneapi/training/migrate-from-cuda-to-cpp-with-sycl.html)
- [MLCommons: datacenter inference benchmarking](https://mlcommons.org/benchmarks/inference-datacenter/)
- [NVIDIA NCCL communication primitives](https://developer.nvidia.com/nccl)
- [AMD RCCL communication primitives](https://rocm.docs.amd.com/projects/rccl/en/latest/)
