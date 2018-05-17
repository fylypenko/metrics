#!/usr/bin/python3
# The script prints basic information about your OS to console
# It accept a single parameter to specify which metrics set to print:
# cpu - prints CPU metrics
# mem - prints RAM metrics

import sys
import psutil
 
# memory metrics
def mem():
   virtual_mem=psutil.virtual_memory()
   swap_mem=psutil.swap_memory()
   print("Memory:")
   print("virtual total:",virtual_mem.total)
   print("virtual used:",virtual_mem.used)
   print("virtual free:",virtual_mem.free)
   print("virtual shared:",virtual_mem.shared)
   print("swap total:",swap_mem.total)
   print("swap used:",swap_mem.used)
   print("swap free:",swap_mem.free)

# cpu metrics
def cpu():
   cpu_t=psutil.cpu_times()
   print("CPU:")
   print("cpu.idle:",cpu_t.idle)
   print("cpu.user:",cpu_t.user)
   print("cpu.system:",cpu_t.system)
   print("cpu.iowait:",cpu_t.iowait)
   print("cpu.stolen:",cpu_t.steal)
   print("cpu.guest:",cpu_t.guest)
  
# main  
if __name__ == '__main__':  
  
  if len(sys.argv)==2:
     if sys.argv[1]=='cpu':
        cpu()
     elif sys.argv[1]=='mem':
        mem()
     else:
        print("Unknown parameter. Use single parameter <cpu> or <mem>")
  else:
     print("Wrong parameters. Use single parameter <cpu> or <mem>")
# end main