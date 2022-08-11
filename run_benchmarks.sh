#!/usr/bin/env bash

set -e

NUM_ITERATIONS=10

./generate_benchmarks.py

echo "iterative non apm"
echo "-------------------------"
time (for i in `seq 0 ${NUM_ITERATIONS}`; do python iterative_non_apm.py; done;)
echo "-------------------------"
echo ""

echo "iterative with apm"
echo "-------------------------"
time (for i in `seq 0 ${NUM_ITERATIONS}`; do DD_SERVICE="benchmark_iterative" DD_ENV="stage" DD_LOGS_INJECTION=true DD_PROFILING_ENABLED=true ddtrace-run python iterative_with_apm.py; done;)
echo "-------------------------"
echo ""

echo "recursive non apm"
echo "-------------------------"
time (for i in `seq 0 ${NUM_ITERATIONS}`; do python recursive_non_apm.py; done;)
echo "-------------------------"
echo ""

echo "recursive with apm"
echo "-------------------------"
time (for i in `seq 0 ${NUM_ITERATIONS}`; do DD_SERVICE="benchmark_recursive" DD_ENV="stage" DD_LOGS_INJECTION=true DD_PROFILING_ENABLED=true ddtrace-run python recursive_with_apm.py; done;)
echo "-------------------------"
echo ""
