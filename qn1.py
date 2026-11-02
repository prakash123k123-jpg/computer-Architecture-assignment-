cache = []
capacity = 3
pages = [4, 2, 1, 4, 3, 2, 5, 4]

hits = 0
misses = 0

print("Block\tStatus\tCache\t\tRemoved")

for page in pages:
    removed = "-"

    if page in cache:
        hits += 1
        cache.remove(page)
        cache.append(page)
        status = "HIT"
    else:
        misses += 1
        status = "MISS"

        if len(cache) == capacity:
            removed = cache.pop(0)

        cache.append(page)

    print(f"{page}\t{status}\t{cache}\t{removed}")

print("\nTotal Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", round(hits / len(pages), 2))