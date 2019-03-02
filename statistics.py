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

    def __str__(self):
        result = ""
        for key, value in sorted(self.count_of_tags_that_repeat_key_times.items()):
            result += f"Tagów powstarzajcych sie {key} razy jest {value}\n"

        result += f"Number of vertical photos:   {self.vertical_count}\n"
        result += f"Number of horizontal photos: {self.horizontal_count}\n"


        return result
