class Solution:

    def __init__(self, photos):
        self.photos = photos

    def solve(self):

        # used_photos = 0
        photo_show = []
        # print(f"{len(self.photos)}")

        for photo in self.photos:
            if photo.used:
                continue

            # print(photo.id)
            photo_show.append(photo)
            photo.used = True
            # used_photos += 1

            while True:
                best = photo.get_best_unused_transition()
                if best is None:
                    break
                # print(best.id)
                photo_show.append(best)
                best.used = True
                # used_photos += 1
                # if used_photos > 300:
                #     exit(0)
                photo = best
                # print(used_photos)
            # print(used_photos)

        return photo_show
