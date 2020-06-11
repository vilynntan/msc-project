import os, mmap, subprocess, re

#Compile into class file
#os.system('javac IntegerBug.java')

#Find line number where Verifier is
lineNum = 0
with open('IntegerBug.java') as f:
    for num, line in enumerate(f, 1):
        if 'Verifier.nondet' in line:
            lineNum = num

print lineNum

#Run JBMC
#Require python 2.7 and above
#os.system('./jbmc IntegerBug --stop-on-fail');
cmd = './jbmc IntegerBug --stop-on-fail'
try:
     result = subprocess.check_output(cmd, shell=True)
except subprocess.CalledProcessError as e:
     result = e.output

for line in result.splitlines():
     if line.startswith('  anonlocal'):
	print line
	temp = re.split('=| ', line)
	print temp[3] #counterexample
	