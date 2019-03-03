class Solution:

    def __init__(self, photos):
        self.photos = photos

    def solve(self):

        photo_show = []
        # print(f"{len(self.photos)}")
        for photo in self.photos:
            if photo.used:
                continue

            # print(photo.id)
            photo_show.append(photo)
            photo.used = True

            while True:
                best = photo.get_best_unused_transition()
                if best is None:
                    break
                # print(best.id)
                photo_show.append(best)
                best.used = True
                photo = best
        return photo_show
