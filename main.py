#!/usr/bin/env python
import os
input_filename = os.path.normpath(input("Location of your log file:"))
output_filename = os.path.normpath(input("Location to output your monitor file:"))
lookup = 'ERROR'
lineno = []

logfile = open(input_filename, "r")
for num, line in enumerate(logfile, 1):
    if lookup in line:
        lineno.append(num)

for x in lineno:
    print ('Error is found at line:', x)

logfile = open(input_filename, "r")
monitorfile = open(output_filename, "a")
for num5, line in enumerate(logfile, 1):
    for num in lineno:
        num2 = num - 3
        num3 = num - 2
        num4 = num - 1
        if num5 == num2:
            if lookup not in line:
                monitorfile.write("Line " + str(num5) + ": " + line)
        elif num5 == num3:
            if lookup not in line:
                monitorfile.write("Line " + str(num5) + ": " + line)
        elif num5 == num4:
            if lookup not in line:
                monitorfile.write("Line " + str(num5) + ": " + line)
        elif num5 == num:
            monitorfile.write("Line " + str(num5) + ": " + line.rstrip() + "----- \n")
monitorfile.close()

lines_seen = set()
output = ""
for line in open("monitor.txt", "r"):
    if line not in lines_seen:
        output = output + line
        lines_seen.add(line)
outfile = open("monitor.txt", "w")
outfile.write(output)
outfile.close()
