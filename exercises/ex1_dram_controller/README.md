# Exercise 1 — SimPy DRAM controller

Spec and starter code: `lessons/day-01-*.md` (Build 1), `day-02-*.md` (Build 2), `day-03-*.md` (Build 3).

Files to create here: `model.py` (Request, decode, streams), `config.py` or load from `../configs/`, `sim.py` (Bank, Controller, run_stream), `sweep.py`, `test_decode.py`, `test_timing.py`.
Plots expected: `ex1_bw_vs_hitrate.png`, `ex1_latency_vs_depth.png` (git-ignored).

## Day 1 — done

`uv run pytest exercises/ex1_dram_controller` and `uv run python exercises/ex1_dram_controller/model.py`.

**Random stream, 5 requests, same bank?** One pair: requests 2 and 4 both land in bank group 7, bank 3. The other three are alone. (32 banks, 5 draws: a shared bank is more likely than not, the same birthday-paradox math.)

**For 1,000?** About 31 per bank (1000 / 32), spread fairly evenly; `test_random_stream_spreads_over_banks` checks all 32 banks get hit and none gets more than double its share. So a random stream has almost no row-buffer locality (consecutive requests to the same bank almost always open a different row) but plenty of bank-level parallelism.

**Stretch:** `decode_row_interleaved` puts bank bits above row bits. On the demo, address `0x2000` (next row) goes to bank 1 under `decode` but stays in bank 0 under the row-interleaved map. Compare their bandwidth on Day 3.
