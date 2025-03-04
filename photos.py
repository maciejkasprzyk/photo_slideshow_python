from score import Score


class Photo:
    objectCount = 0

    # nazwy w pythonie o dwóch podkreśleniach mają specjalne znaczenie
    # __init__ to funkcja która odpalana jest po utworzeniu obiektu, uzywana do inicjializacji
    # metody jako pierwszy argument przyjmuja self (takie this z c++), ale nie wpisuje sie go przy uruchamianiu
    def __init__(self, orientation, number_of_tags):  # pythonie nazwy zmiennych piszemy z podkresleniami
        self.orientation  = orientation
        self.number_of_tags = number_of_tags
        self.tags = set()
        self.id = Photo.objectCount
        self.used = False
        Photo.objectCount += 1
        self.photos_with_similar_tags = set()

    def __str__(self):  # to taka metoda to_string z javy
        result = f'Photo#{self.id} {self.orientation} {self.number_of_tags} ('
        for tag in self.tags:
            result += f'{tag.tag_string} '
        result += ')\n'
        return result

    def __calc_photos_with_similar_tags(self):
        for tag in self.tags:
            photos_with_tag = tag.photos
            self.photos_with_similar_tags.update(photos_with_tag)
        self.photos_with_similar_tags.remove(self)

    def get_best_unused_transition(self):
        if len(self.photos_with_similar_tags) is 0:
            self.__calc_photos_with_similar_tags()

        max_points = 0
        best = None
        for other in self.photos_with_similar_tags:
            if other.used:
                continue
            points = Score.get_score_for_transition_between(self, other)
            if max_points < points:
                max_points = points
                best = other
        # self.photos_with_similar_tags = set()
        return best


class Photos(list):  # dziedziczymy po list
    # ta struktura nazywa sie list, ale pod spodem tak naprawde to wektor, nie wiem czemu takie nazewnictwo xd

    def __str__(self):  # to taka metoda to_string z javy
        result = "Photos = {\n"

        for photo in self:
            result += str(photo)
        result += "}\n"
        return result
