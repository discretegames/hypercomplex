"""Puts hypercomplex/examples.py into markdown format for easy use in README.md"""

import os
import io
import sys


def get_print_results(lines):
    header = "from hypercomplex import *\n"
    code = header + '\n'.join(lines)
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    exec(code)
    output = sys.stdout.getvalue().splitlines()
    sys.stdout = stdout
    results = []
    i = 0
    for line in lines:  # Assumes each print remained on one line.
        out = None
        if line.strip().startswith('print'):
            out = output[i]
            i += 1
        results.append((line, out))
    return results


def example_to_markdown(example):
    lines = example.splitlines()
    start = f'{lines[0]}\n\n    ```py\n'
    lines = lines[1:]
    longest = max(map(len, lines))
    middle = []
    for line, output in get_print_results(lines):
        if output is not None:
            padding = longest - len(line)
            line += ' ' * padding + f'  # -> {output}'
        middle.append(f'    {line}')
    end = '\n    ```\n'
    return start + '\n'.join(middle) + end


def examples_to_markdown():
    with open(os.path.join('hypercomplex', 'examples.py')) as f:
        examples = [e.strip() for e in f.read().split('# %%')]
        examples = [e for e in examples if e][1:]
    markdown = '\n'.join(map(example_to_markdown, examples))
    with open('examples.md', 'w') as f:
        f.write(markdown)
    print(f"Converted {len(examples)} examples to markdown.")
    # print(markdown)


if __name__ == "__main__":
    examples_to_markdown()

# This is the only multiline example and examples_to_markdown can't handle it. Saving it here to avoid manually making it again.
e_matrix_example = """

11. `e_matrix` of a number class gives the multiplication table of `e(i)*e(j)`. Set `string=False` to get a 2D list instead of a string. Set `raw=True` to get the raw hypercomplex numbers.

    ```py
    print(O.e_matrix())                        # -> e1  e2  e3  e4  e5  e6  e7
                                               #   -e0  e3 -e2  e5 -e4 -e7  e6
                                               #   -e3 -e0  e1  e6  e7 -e4 -e5
                                               #    e2 -e1 -e0  e7 -e6  e5 -e4
                                               #   -e5 -e6 -e7 -e0  e1  e2  e3
                                               #    e4 -e7  e6 -e1 -e0 -e3  e2
                                               #    e7  e4 -e5 -e2  e3 -e0 -e1
                                               #   -e6  e5  e4 -e3 -e2  e1 -e0
                                               #
    print(C.e_matrix(string=False, raw=True))  # -> [[(1 0), (0 1)], [(0 1), (-1 0)]]
    ```

"""
