from tags import *
from photos import *


class InputReader:
    def __init__(self):
        # nie ma ochrony pol prywatnych w klasach (jezyk nie wie co to jest pole prywatne)
        # zwyczajowo jezeli chcemy zasugerowac ze zmienna jest prywatna to stawiamy przed nia dwa podkreslenia
        self.__tagFactory = TagsFactory()
        self.__photos = Photos()

    def read_photos_and_tags(self):
        number_of_photos = int(input())
        for i in range(number_of_photos):
            self.read_photo_and_tags()

        tags = self.__tagFactory.return_all_created_tags()

        return self.__photos, tags  # zwracamy tuple

    def read_photo_and_tags(self):
        line = input()
        words = line.split()
        orientation = words[0]
        number_of_tags = int(words[1])

        photo = Photo(orientation, number_of_tags)
        self.__photos.append(photo)

        # wczytaj tagi, polacz tag ze zdjeciem i na odwrot
        words = line.split()
        for i in range(2, len(words)):  # iteruj zaczynajac od drugiej pozycji
            tag_string = words[i]
            tag = self.__tagFactory.return_tag_or_create_if_doesnt_exist(tag_string)
            photo.tags.add(tag)
            tag.photos.add(photo)
        return photo
