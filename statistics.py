from collections import defaultdict


class Statistics:

    def __init__(self, photos, tags):

        self.count_of_tags_that_repeat_key_times = defaultdict(int)
        for tag in tags:
            self.count_of_tags_that_repeat_key_times[tag.number_of_photos] += 1

        self.vertical_count = 0
        self.horizontal_count = 0
        for photo in photos:
            if photo.orientation == 'V':
                self.vertical_count += 1
            else:
                self.horizontal_count += 1

        self.number_of_different_tags = len(tags)

        self.number_of_tags = 0
        for photo in photos:
            self.number_of_tags += photo.number_of_tags

        self.number_of_photos = len(photos)
        self.average_number_of_tags_on_photo = self.number_of_tags/self.number_of_photos

    def __str__(self):
        result = "\n"
        for key, value in sorted(self.count_of_tags_that_repeat_key_times.items()):
            result += f"Tagów powstarzajcych sie {key} razy jest {value}\n"

        result +="\n"
        result += f"Number of vertical photos:   {self.vertical_count}\n"
        result += f"Number of horizontal photos: {self.horizontal_count}\n"
        result += f"Number of different tags: {self.number_of_different_tags}\n"
        result += f"Number of tags: {self.number_of_tags}\n"
        result += f"Number of photos: {self.number_of_photos}\n"
        result += f"Average number of tags on photo: {self.average_number_of_tags_on_photo}\n"


        return result
