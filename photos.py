class Photo:
    objectCount = 0

    # nazwy w pythonie o dwóch podkreśleniach mają specjalne znaczenie
    # __init__ to funkcja która odpalana jest po utworzeniu obiektu, uzywana do inicjializacji
    # metody jako pierwszy argument przyjmuja self (takie this z c++), ale nie wpisuje sie go przy uruchamianiu
    def __init__(self, orientation, number_of_tags):  # pythonie nazwy zmiennych piszemy z podkresleniami
        self.orientation = orientation
        self.number_of_tags = number_of_tags
        self.tags = set()
        self.id = Photo.objectCount + 1
        Photo.objectCount += 1

    def __str__(self):  # to taka metoda to_string z javy
        result = f'Photo#{self.id} {self.orientation} {self.number_of_tags} ('
        for tag in self.tags:
            result += f'{tag.tag_string} '
        result += ')\n'
        return result


class Photos(list):  # dziedziczymy po list
    # ta struktura nazywa sie list, ale pod spodem tak naprawde to wektor, nie wiem czemu takie nazewnictwo xd

    def __str__(self):  # to taka metoda to_string z javy
        result = "Photos = {\n"

        for photo in self:
            result += str(photo)
        result += "}\n"
        return result
