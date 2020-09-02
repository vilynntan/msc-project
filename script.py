#Requires python 3 and above

import subprocess, sys
import networkx as nx

#Extract class name
classnameArray = sys.argv[1].split('.')
classname = classnameArray[0]
if len(classnameArray) == 2 and classnameArray[1] == 'java':
          subprocess.Popen(['javac', sys.argv[1]]).wait() #Compile Java program

#Run JBMC
cmd = 'jbmc ' + classname + ' --stop-on-fail --graphml-witness witness'
try:
     result = subprocess.check_output(cmd, shell=True)
except subprocess.CalledProcessError as e:
     result = e.output

#Check for violation
witnessFile = nx.read_graphml("witness")
violation = False
for violationKey in witnessFile.nodes(data=True):
     if 'isViolationNode' in violationKey[1]:
          violation = True

#Violation == True / Violation occurs
if (violation):
     #Determine verifier variable type - only possible with .java/user supplied
     if (len(sys.argv) == 3):
         type = sys.argv[2].lower()
     else:
         with open(sys.argv[1], "rt") as fin:
             for line in fin:
                 index = line.find('verifier.') 
                 if(index != -1):
                     type = line[index + 15 : -4].lower().replace(')','').replace('(','')
     
     #Extract counterexample
     for data in witnessFile.edges(data=True):
          if 'assumption' in data[2]:
               str = data[2]['assumption']
               #Get counterexample between ' = ' and ';' 
               #E.g. "anonlocal::1i = 1000;"
               if (str.startswith('anonlocal')):
                    counterexample = str.split(' = ')[1][:-1]

     #Create validation harness from template
     with open("ValidationHarnessTemplate.txt", "rt") as fin:
         with open("ValidationHarness.java", "wt") as fout:
             for line in fin:
                 line = line.replace('ClassName', classname)
                 if(type == 'int'):
                     line = line.replace('Type', 'nondetInt').replace('Counterexample', counterexample)
                 if(type == 'short'):
                     line = line.replace('Type', 'nondetShort').replace('Counterexample', counterexample)
                 if(type == 'long'):
                     line = line.replace('Type', 'nondetLong').replace('Counterexample', counterexample)
                 if(type == 'float'):
                     line = line.replace('Type', 'nondetFloat').replace('Counterexample', counterexample)
                 if(type == 'double'):
                     line = line.replace('Type', 'nondetDouble').replace('Counterexample', counterexample)
                 if(type == 'string'):
                     try:
                         counterexample = int(counterexample)
                         line = line.replace('Type', 'nondetString').replace('Counterexample', 'null')
                     except ValueError:
                         line = line.replace('Type', 'nondetString').replace('Counterexample', '"' + counterexample + '"')
                 if(type == 'char'):
                     line = line.replace('Type', 'nondetChar').replace('Counterexample', '\'' + chr(int(counterexample)) + '\'')
                 if(type == 'boolean'):
                     if(counterexample == '1'):
                         line = line.replace('Type', 'nondetBoolean').replace('Counterexample', 'true')
                     if(counterexample == '0'):
                         line = line.replace('Type', 'nondetBoolean').replace('Counterexample', 'false')
                 fout.write(line)

     #Compile validation harness
     subprocess.Popen(['javac', 'ValidationHarness.java']).wait()

     #Execute validation harness
     subprocess.Popen(['java', '-ea', 'ValidationHarness']).wait()
else:
     #Exit if no violation found by JBMC
     print ('No violation found')
     exit(1)
