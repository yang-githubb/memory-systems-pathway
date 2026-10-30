# Memory & Interconnect Systems — Notes and Practice Pathway

A self-made, ten-day study path into how modern memory systems and on-chip interconnects work, and how performance architects model them. Written as my own learning notes: each day has a full written lecture, practice questions with answers, and a hands-on build that grows into a small simulator and tooling project.

Topics: DRAM (DDR5, LPDDR5X, HBM3E/HBM4), memory controllers and scheduling, queueing and roofline analysis, networks on chip, AXI/CHI and UCIe, SystemC/TLM 2.0 performance modeling, the ASIC/FPGA design flow, and the Python/C++/Qt tooling around it all.

## How to use this repo

1. Open [`PLAN.md`](PLAN.md). It is the checklist: ten days, each with **Read**, **Build** and **Can you explain?** boxes, plus a glossary and reading list at the end.
2. For each day, read `day-NN/lesson.md` (about an hour), answer the practice questions on paper, then check the answers at the bottom of the chapter.
3. Do the build. Starter code is inside each chapter; the finished code lives in `day-NN/exercise/`.
4. Tick the boxes in `PLAN.md` as you go.

| Day | Chapter | What you build |
| --- | --- | --- |
| 1 | [DRAM and the request path](day-01/lesson.md) | repo, SimPy, address decoder |
| 2 | [Timing parameters and memory families](day-02/lesson.md) | FIFO DRAM controller with real timing |
| 3 | [What a memory controller does](day-03/lesson.md) | FR-FCFS scheduler, page policy, plots, timing tests |
| 4 | [Performance analysis](day-04/lesson.md) | two requesters with QoS, latency histograms |
| 5 | [Networks on chip](day-05/lesson.md) | 4×4 mesh simulator |
| 6 | [Bus protocols and chiplets](day-06/lesson.md) | virtual channels, hotspot and transpose traffic |
| 7 | [SystemC and TLM 2.0](day-07/lesson.md) | first loosely-timed model (full code) |
| 8 | [Timing styles and real simulators](day-08/lesson.md) | approximately-timed target, Ramulator 2 run |
| 9 | [Design flow, FPGAs and C++](day-09/lesson.md) | C++17 port with tests |
| 10 | [Tooling, GUI and self-check](day-10/lesson.md) | CLI, PySide GUI, README, final self-check |

## Repo layout

```
PLAN.md              the ten-day checklist, glossary and reading list
day-NN/
  lesson.md          the chapter: lectures, practice, answers, starter code
  exercise/          my build for that day (filled in as I go)
```

Exercises that span several days live in the day they start; the later days' `exercise/README.md` points there. The lessons call the exercise folders `ex1_dram_controller` and so on; the mapping is:

| Lesson name | Folder | Days |
| --- | --- | --- |
| ex1_dram_controller | day-01/exercise | 1–3 |
| ex2_qos | day-04/exercise | 4 |
| ex3_noc | day-05/exercise | 5–6 |
| ex4_tlm | day-07/exercise | 7–8 |
| ex5_ramulator | day-08/exercise | 8 |
| ex8_cpp | day-09/exercise | 9 |
| ex7_gui | day-10/exercise | 10 |

Shared YAML timing configs are in `day-01/exercise/configs/`.

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

Text and notes: CC BY 4.0. Code in `day-NN/exercise/`: MIT.
