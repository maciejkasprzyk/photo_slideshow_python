# staralem sie opisywac kod tlumaczac konstrukcje pythonowe
# w pycharmie: setting->editor->inspections->spelling->typo ustawcie sobie nie sprawdzanie bledow w komentarzach

from inputReader import *


def main():
    photos, tags = InputReader().read_photos_and_tags()
    print(photos)
    print(tags)
    # statistics = Statistics(photos)
    # print(statistics)


if __name__ == '__main__':
    main()
    # chcialem sam wytlumaczyc po co ten if, ale mi sie nie udało XD macie linka
    # https://codecouple.pl/2016/02/27/python-specjalna-zmienna-__name__/
