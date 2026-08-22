import unittest

from wtpy.SelContext import SelContext


class _Wrapper:
    def __init__(self):
        self.calls = []

    def sel_sub_ticks(self, *args):
        self.calls.append(args)


class _Strategy:
    def name(self):
        return "sel-context-test"


class _Engine:
    is_backtest = True


class SelContextTest(unittest.TestCase):
    def test_sel_sub_ticks_forwards_context_id_to_wrapper(self) -> None:
        wrapper = _Wrapper()
        context = SelContext(17, _Strategy(), wrapper, _Engine())

        context.stra_sub_ticks("SSE.STK.000001")

        self.assertEqual(wrapper.calls, [(17, "SSE.STK.000001")])


if __name__ == "__main__":
    unittest.main()
