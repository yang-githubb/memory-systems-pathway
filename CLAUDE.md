# Working in this repo

This is a personal study repo: a ten-day pathway through memory systems, NoCs, bus protocols and SystemC/TLM performance modeling.

- `PLAN.md` is the checklist; `lessons/day-NN-*.md` are the chapters. Each chapter ends with **Build N** (the exercise spec with starter code) and **Answers**.
- Code goes under `exercises/<exN_name>/`, shared configs under `configs/`, CLI under `tools/`, tests under `tests/`. Keep `results/` out of git.
- When I ask for help with "exercise N" or "day N", read the matching chapter's Build section first and follow its interface (function names, config keys, plot file names) so the later days still fit together.
- Python: 3.11+, type hints, pytest, matplotlib; keep every timing parameter in `configs/*.yaml`, never hard-coded. C++: C++17, CMake, Catch2. SystemC: Accellera 2.3.4 or 3.x, TLM 2.0.
- Prefer explaining the mechanism (row-buffer hits, tFAW, credits, phases) over just making the numbers come out; this repo is for learning.
- Do not add external dependencies beyond those in README without asking.
