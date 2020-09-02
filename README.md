# msc-project

### Requirements
- Java SE
- Python3 (incl. subprocess, sys, networkx)
- Mockito
- JBMC (https://github.com/diffblue/cbmc/tree/develop/jbmc)
- SV-COMP Benchmarks (https://github.com/sosy-lab/sv-benchmarks)

### Usage with SV-COMP Benchmarks
- Put script and validation harness template in `sv-benchmarks/java/common`
- Navigate to location of script and validation harness on CLI
- Run `python3 script.py filename.java`(recommended) or `python3 script.py filename.class` or `python3 script.py filename`
