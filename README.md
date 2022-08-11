# APM Benchmarking Tools
## NOTES
In order to use this benchmark tool, you will need to execute on a host with the datadog agent installed and correctly emmitting telemetry to DataDog

## RESULTS
```
(venv) bradydeetz@192.168.1.2:~/datadog_apm_benchmarking > ./run_benchmarks.sh
iterative non apm
-------------------------

real   0m0.255s
user   0m0.211s
sys    0m0.044s
-------------------------

iterative with apm
-------------------------

real   0m6.183s
user   0m4.499s
sys    0m0.539s
-------------------------

recursive non apm
-------------------------

real   0m0.157s
user   0m0.135s
sys    0m0.022s
-------------------------

recursive with apm
-------------------------

real   0m5.406s
user   0m4.063s
sys    0m0.493s
-------------------------
```

## Setup
```
apt-get install python3.8-venv
git clone https://github.com/bdeetz/datadog_apm_benchmarking.git
cd datadog_apm_benchmarking
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Generating benchmark scripts
```
source venv/bin/activate
./generate_benchmarks.py
```

## Executing benchmarks
```
source venv/bin/activate
./run_benchmarks.sh
```
