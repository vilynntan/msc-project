# msc-project

### Requirements
- Java SE
- Python3 (incl. subprocess, sys, networkx)
- Mockito
- JBMC (https://github.com/diffblue/cbmc/tree/develop/jbmc)
- SV-COMP Benchmarks (https://github.com/sosy-lab/sv-benchmarks)

### Usage with SV-COMP Benchmarks
Run `python3 script.py filename.java`(recommended) or `python3 script.py filename.class` or `python3 script.py filename`

Note: The benchmark file must be modified to remove any use of `static` keyword. Refer to the samples provided. 
