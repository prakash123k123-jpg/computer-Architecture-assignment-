capacity = 3
pages = [4, 2, 1, 4, 3, 2, 5, 4]

cache = []
hits = 0
misses = 0

for page in pages:
    removed = "None"

    if page in cache:
        hits += 1
        cache.remove(page)
        cache.append(page)
        result = "HIT"
    else:
        misses += 1

        if len(cache) >= capacity:
            removed = cache.pop(0)

        cache.append(page)
        result = "MISS"

    print("Requested Block:", page)
    print("Result:", result)
    print("Cache:", cache)
    print("Removed Block:", removed)
    print()

print("Total Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hits / len(pages))