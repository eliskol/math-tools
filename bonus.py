import re


def check_if_valid(exp):
    try:
        assert exp[0] != "+"
        assert exp[-1] != "+"
        assert (exp.count("(")) == (exp.count(")"))
        assert re.search(r"\d", exp) is not None
        assert re.search(r"\+{2}", exp) is None
        assert re.search(r"\+)", exp) is None
        return True
    except AssertionError:
        return False