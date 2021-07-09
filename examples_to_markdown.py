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
