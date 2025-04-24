from pathlib import Path
import timeit


from kmp import kmp_search
from bm import boyer_moore_search 
from rk import rabin_karp_search


current_dir = Path.cwd()

with open(current_dir / 'text_1.txt', 'r', encoding='utf-8') as f:
    content_1 = f.read()

with open(current_dir / 'text_2.txt', 'r', encoding='utf-8') as f:
    content_2 = f.read()

if __name__ == "__main__":
    print("\nТекст 1, підрядок існує")
    print(f"КМП: {timeit.timeit("kmp_search(content_1, 'дві монети по 10 копійок')", globals=globals(), number=1000)}")
    print(f"БМ: {timeit.timeit("boyer_moore_search(content_1, 'дві монети по 10 копійок')", globals=globals(), number=1000)}")
    print(f"РК: {timeit.timeit("rabin_karp_search(content_1, 'дві монети по 10 копійок')", globals=globals(), number=1000)}")
    print("\nТекст 2, підрядок існує")
    print(f"КМП: {timeit.timeit("kmp_search(content_1, 'Ryzen 5 3600 та 32 Гб')", globals=globals(), number=1000)}")
    print(f"БМ: {timeit.timeit("boyer_moore_search(content_1, 'Ryzen 5 3600 та 32 Гб')", globals=globals(), number=1000)}")
    print(f"РК: {timeit.timeit("rabin_karp_search(content_1, 'Ryzen 5 3600 та 32 Гб')", globals=globals(), number=1000)}")
    print("\nТекст 1, підрядок не існує")
    print(f"КМП: {timeit.timeit("kmp_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
    print(f"БМ: {timeit.timeit("boyer_moore_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
    print(f"РК: {timeit.timeit("rabin_karp_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
    print("\nТекст 2, підрядок не існує")
    print(f"КМП: {timeit.timeit("kmp_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
    print(f"БМ: {timeit.timeit("boyer_moore_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
    print(f"РК: {timeit.timeit("rabin_karp_search(content_2, 'asdfsdf')", globals=globals(), number=1000)}")
