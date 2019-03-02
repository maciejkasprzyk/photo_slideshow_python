class Tag:

    def __init__(self, tag_string):
        self.tag_string = tag_string
        self.photos = set()  # set bo do jednego taga moze byc przypisane duzo zdjec i bede chcial szybko wyszukiwac

    # to taka metoda ktora udaje pole, wywoluje sie ja tak jakby odwolowyalo sie do pola czyli tags.number_of_photos
    @property
    def number_of_photos(self):
        return len(self.photos)

    def __str__(self):  # to taka metoda to_string z javy
        result = f'\"{self.tag_string}\" on {self.number_of_photos} photos: '
        for photo in self.photos:
            result += f"{photo.id} "
        result += "\n"
        return result


class Tags(set):  # dziedziczymy po secie, w sumie nie wiem czy to dobrze XD
    def __str__(self):  # to taka metoda to_string z javy
        result = "Tags = {\n"
        for tag in self:
            result += f"{tag}"
        return result + "}\n"


class TagsFactory:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__map_strings_to_tags = {}  # te nawiasy klamrowe sa rownowazne zapisowi dict(), czyli tworzymy slownik

    def return_tag_or_create_if_doesnt_exist(self, tag_string):
        try:
            tag = self.__map_strings_to_tags[tag_string]
        except KeyError:
            tag = Tag(tag_string)
            self.__map_strings_to_tags[tag_string] = tag
        return tag

    def return_all_created_tags(self):
        tags = Tags()
        for tag in self.__map_strings_to_tags.values():
            tags.add(tag)
        return tags
