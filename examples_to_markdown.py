"""Puts hypercomplex/examples.py into markdown format for use in README.md"""

import re
import os


def example_to_markdown(match):
    pass


def examples_to_markdown():
    md = []
    ex_pattern = r"^# %% (\d+\..*$)[\r\n]+((^.*$)[\r\n]+)*"
    with open(os.path.join('hypercomplex', 'examples.py')) as f:
        ex = f.read().splitlines()

    ex_lines = None
    for line in ex:
        if line.startswith('# %%'):
            md.append()

        # print(re.findall(ex_pattern, ex.read(), re.DOTALL | re.MULTILINE))
        for m in re.finditer(ex_pattern, ex.read(), re.MULTILINE):
            print(m.groups())


if __name__ == "__main__":
    examples_to_markdown()
