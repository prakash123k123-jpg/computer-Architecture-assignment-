tlb_time = 10
memory_time = 80

h = 0.90

print("TLB Lookup Time:", tlb_time, "ns")
print("Memory Access Time:", memory_time, "ns")
print("TLB Hit Ratio:", h)

eat1 = h * (tlb_time + memory_time) + (1 - h) * (tlb_time + 2 * memory_time)

print("EAT for hit ratio 0.90:", eat1, "ns")

h = 0.75

eat2 = h * (tlb_time + memory_time) + (1 - h) * (tlb_time + 2 * memory_time)

print("TLB Hit Ratio:", h)
print("EAT for hit ratio 0.75:", eat2, "ns")

if eat1 < eat2:
    print("Hit ratio 0.90 gives better performance")
else:
    print("Hit ratio 0.75 gives better performance")