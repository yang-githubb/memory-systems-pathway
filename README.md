# Memory & Interconnect Systems — Notes and Practice Pathway

A self-made, ten-day study path into how modern memory systems and on-chip interconnects work, and how performance architects model them. Written as my own learning notes: each day has a full written lecture, practice questions with answers, and a hands-on build that grows into a small simulator and tooling project.

Topics: DRAM (DDR5, LPDDR5X, HBM3E/HBM4), memory controllers and scheduling, queueing and roofline analysis, networks on chip, AXI/CHI and UCIe, SystemC/TLM 2.0 performance modeling, the ASIC/FPGA design flow, and the Python/C++/Qt tooling around it all.

## How to use this repo

1. Open [`PLAN.md`](PLAN.md). It is the checklist: ten days, each with **Read**, **Build** and **Can you explain?** boxes, plus a glossary and reading list at the end.
2. For each day, read the matching chapter in [`lessons/`](lessons/) (about an hour), answer the practice questions on paper, then check the answers at the bottom of the chapter.
3. Do the build. Starter code is inside each chapter; the finished code lives in [`exercises/`](exercises/).
4. Tick the boxes in `PLAN.md` as you go.

| Day | Chapter | What you build |
| --- | --- | --- |
| 1 | [DRAM and the request path](lessons/day-01-dram-and-the-request-path.md) | repo, SimPy, address decoder |
| 2 | [Timing parameters and memory families](lessons/day-02-timing-and-memory-families.md) | FIFO DRAM controller with real timing |
| 3 | [What a memory controller does](lessons/day-03-memory-controller.md) | FR-FCFS scheduler, page policy, plots, timing tests |
| 4 | [Performance analysis](lessons/day-04-performance-analysis.md) | two requesters with QoS, latency histograms |
| 5 | [Networks on chip](lessons/day-05-networks-on-chip.md) | 4×4 mesh simulator |
| 6 | [Bus protocols and chiplets](lessons/day-06-bus-protocols-and-chiplets.md) | virtual channels, hotspot and transpose traffic |
| 7 | [SystemC and TLM 2.0](lessons/day-07-systemc-and-tlm.md) | first loosely-timed model (full code) |
| 8 | [Timing styles and real simulators](lessons/day-08-timing-styles-and-simulators.md) | approximately-timed target, Ramulator 2 run |
| 9 | [Design flow, FPGAs and C++](lessons/day-09-design-flow-fpga-cpp.md) | C++17 port with tests |
| 10 | [Tooling, GUI and self-check](lessons/day-10-tooling-gui-selfcheck.md) | CLI, PySide GUI, README, final self-check |

## Repo layout

```
PLAN.md              the ten-day checklist, glossary and reading list
lessons/             one chapter per day: lectures, practice, answers, starter code
exercises/           my implementations of the builds (filled in as I go)
  ex1_dram_controller/   SimPy DRAM controller (days 1–3)
  ex2_qos/               two-requester QoS study (day 4)
  ex3_noc/               mesh NoC simulator (days 5–6)
  ex4_tlm/               SystemC / TLM 2.0 models (days 7–8)
  ex5_ramulator/         notes and configs for the Ramulator 2 runs (day 8)
  ex7_gui/               PySide explorer GUI (day 10)
  ex8_cpp/               C++17 port of exercise 1 (day 9)
configs/             YAML timing/organization configs shared by the simulators
tools/               CLI entry points
tests/               pytest and Catch2 tests, including the calibration test
results/             generated plots and CSVs (git-ignored)
```

## Setup

```bash
uv init --no-workspace   # or: python -m venv .venv && source .venv/bin/activate
uv add simpy numpy matplotlib pytest click pyyaml pyside6
pytest
```

SystemC (days 7–8) and Ramulator 2 (day 8) have their own install steps inside those chapters.

## Notes on the content

The timing numbers are typical datasheet values rounded for teaching (DDR5-4800, LPDDR5X-8533, HBM3E at 9.6 Gb/s). Use the real part's datasheet for anything that matters. The lectures were drafted with AI assistance and then reviewed and reworked as I studied; mistakes are mine.

## License

Text and notes: CC BY 4.0. Code in `exercises/`, `tools/` and `tests/`: MIT.
