from collections import Counter

from model import decode, LINE_BYTES, ROW_BYTES, sequential_stream, random_stream, Request


def test_consecutive_lines_share_a_row():
    a, b = decode(0), decode(LINE_BYTES)
    assert a[:3] == b[:3] and b[3] == a[3] + 1


def test_next_row_moves_to_next_bank():
    a, b = decode(0), decode(ROW_BYTES)
    assert a[2] == b[2] and a[1] != b[1]


def test_streams_have_length():
    assert len(sequential_stream(10)) == 10


def test_request_decodes_itself():
    r = Request(addr=ROW_BYTES + LINE_BYTES, is_write=False, arrival=0)
    assert (r.bg, r.bank, r.row, r.col) == (0, 1, 0, 1) and r.done is None


def test_random_stream_spreads_over_banks():
    banks = Counter(decode(a)[:2] for a in random_stream(1000))
    assert len(banks) == 32 and max(banks.values()) < 1000 / 32 * 2
