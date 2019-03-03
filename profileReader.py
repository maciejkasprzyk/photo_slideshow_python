import pstats


def main():
    ProfileReader.read_print_stats()

# najpierw odpalasz komende np taka:  python -m cProfile -o output/profiling_results main.py < input/a_example.txt
# potem python profileReader.py
# widzisz w ktorych funkacjach program spedzil najwiecej czasu

class ProfileReader:
    @staticmethod
    def read_print_stats():
        stats = pstats.Stats("output/profiling_results")
        stats.sort_stats("tottime")
        stats.print_stats(20)


if __name__ == '__main__':
    main()
