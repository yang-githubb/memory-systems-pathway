"""Exercise 1, Day 1: request type, address decoder, traffic generators.

No timing yet. Timing (Day 2) comes from configs/*.yaml; the organization
constants below are the same values as configs/ddr5_4800.yaml.
"""
from dataclasses import dataclass, field
import random

# --- configuration (DDR5-4800-like, one sub-channel, one rank) ---
N_BANK_GROUPS = 8
N_BANKS_PER_GROUP = 4
ROW_BYTES = 8192          # row size across the rank
LINE_BYTES = 64           # one request = one 64-byte burst
LINES_PER_ROW = ROW_BYTES // LINE_BYTES


@dataclass
class Request:
    addr: int
    is_write: bool
    arrival: int                       # cycle it entered the controller
    bg: int = field(init=False)
    bank: int = field(init=False)
    row: int = field(init=False)
    col: int = field(init=False)
    done: int | None = None            # cycle data was returned

    def __post_init__(self) -> None:
        self.bg, self.bank, self.row, self.col = decode(self.addr)


def decode(addr: int) -> tuple[int, int, int, int]:
    """Slice an address into (bank_group, bank, row, column).

    Column bits are lowest so consecutive lines stay in one row (row-buffer
    hits); bank bits sit just above so consecutive rows spread across banks
    (bank-level parallelism)."""
    line = addr // LINE_BYTES
    col = line % LINES_PER_ROW
    rest = line // LINES_PER_ROW
    bank = rest % N_BANKS_PER_GROUP
    rest //= N_BANKS_PER_GROUP
    bg = rest % N_BANK_GROUPS
    row = rest // N_BANK_GROUPS
    return bg, bank, row, col


def decode_row_interleaved(addr: int) -> tuple[int, int, int, int]:
    """Stretch: bank bits ABOVE the row bits. Consecutive rows stay in one
    bank, so a sequential stream hammers a single bank (compare on Day 3)."""
    line = addr // LINE_BYTES
    col = line % LINES_PER_ROW
    rest = line // LINES_PER_ROW
    n_rows = (1 << 30) // (ROW_BYTES * N_BANKS_PER_GROUP * N_BANK_GROUPS)  # 1 GiB span
    row = rest % n_rows
    rest //= n_rows
    bank = rest % N_BANKS_PER_GROUP
    bg = rest // N_BANKS_PER_GROUP
    return bg, bank, row, col


def sequential_stream(n: int, start: int = 0) -> list[int]:
    """n requests walking through memory one line at a time."""
    return [start + i * LINE_BYTES for i in range(n)]


def random_stream(n: int, span_bytes: int = 1 << 30, seed: int = 1) -> list[int]:
    rng = random.Random(seed)
    return [rng.randrange(0, span_bytes, LINE_BYTES) for _ in range(n)]


if __name__ == "__main__":
    print("sequential (bank-interleaved vs row-interleaved):")
    for a in sequential_stream(5) + sequential_stream(3, start=ROW_BYTES):
        print(f"  {a:#010x}  {decode(a)}  {decode_row_interleaved(a)}")
    print("random:")
    for a in random_stream(5):
        print(f"  {a:#010x}  {decode(a)}")
