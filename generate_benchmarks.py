#!/usr/bin/env python

import argparse

from pathlib import Path


DEFAULT_NUM_ITERATIONS = 492


def generate_bash_shebang():
    return """#!/usr/bin/env python
"""


def generate_datadog_import():
    return """from ddtrace import tracer
"""


def generate_recursive_code(num_iterations=DEFAULT_NUM_ITERATIONS, apm=False):
    decorator = ""

    if apm:
        decorator = "@tracer.wrap()"

    code = f"""
{decorator}
def my_func(count=0):
    count += 1

    if count == {num_iterations} - 1:
        return count

    return my_func(count)

if __name__ == '__main__':
    my_func()
"""

    return code


def generate_iterative_code(num_iterations=DEFAULT_NUM_ITERATIONS, apm=False):
    result = ""

    decorator = ""

    if apm:
        decorator = "@tracer.wrap()"

    for i in range(num_iterations):
        num = i
        next_num = i+1

        if i < num_iterations - 1:
            template_code = f"""
{decorator}
def my_func_{num}(my_num):
    my_num += 1

    return my_func_{next_num}(my_num)
"""
        else:
            template_code = f"""
{decorator}
def my_func_{num}(my_num):
    my_num += 1

    return my_num


if __name__ == '__main__':
    my_func_0(0)
"""

        result += template_code

    return result


def generate_iterative_file(num_iterations=DEFAULT_NUM_ITERATIONS):
    # generate non-apm test
    result = generate_bash_shebang()
    result += generate_iterative_code(num_iterations)

    filename = "./iterative_non_apm.py"

    with open(filename, "w") as fp:
        fp.write(result)

    p = Path(filename)
    p.chmod(0o755)

    # generate apm test
    result = generate_bash_shebang()
    result += generate_datadog_import()
    result += generate_iterative_code(num_iterations, apm=True)

    filename = "./iterative_with_apm.py"

    with open(filename, "w") as fp:
        fp.write(result)

    p = Path(filename)
    p.chmod(0o755)



def generate_recursive_file(num_iterations=DEFAULT_NUM_ITERATIONS):
    # generate non-apm test
    result = generate_bash_shebang()
    result += generate_recursive_code(num_iterations)

    filename = "./recursive_non_apm.py"

    with open(filename, "w") as fp:
        fp.write(result)

    p = Path(filename)
    p.chmod(0o755)

    # generate apm test
    result = generate_bash_shebang()
    result += generate_datadog_import()
    result += generate_recursive_code(num_iterations, apm=True)

    filename = "./recursive_with_apm.py"

    with open(filename, "w") as fp:
        fp.write(result)

    p = Path(filename)
    p.chmod(0o755)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-n",
        "--call-depth",
        help=f"the depth of the call stack for this test - default({DEFAULT_NUM_ITERATIONS}) - max({DEFAULT_NUM_ITERATIONS})",
        type=int,
        default=DEFAULT_NUM_ITERATIONS
    )

    args = parser.parse_args()

    if args.call_depth > DEFAULT_NUM_ITERATIONS:
        raise argparse.ArgumentTypeError(f"Maximum value of call-depth is {DEFAULT_NUM_ITERATIONS}")

    return args


if __name__ == "__main__":
    args = parse_args()

    generate_iterative_file(args.call_depth)
    generate_recursive_file(args.call_depth)
