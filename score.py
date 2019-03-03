class Score:
    @staticmethod
    def calculate_score(photo_show):
        if len(photo_show) < 2:
            return 0

        score = 0
        for i in range(len(photo_show)):
            if i == 0:
                continue
            score += Score.get_score_for_transition_between(photo_show[i - 1], photo_show[i])
        return score

    @staticmethod
    def get_score_for_transition_between(photo1, photo2):
        common_count = Score.count_of_common_tags_between(photo1, photo2)
        tags_only_in_self = photo1.number_of_tags - common_count
        tags_only_in_other = photo2.number_of_tags - common_count

        return min(common_count, tags_only_in_other, tags_only_in_self)

    @staticmethod
    def count_of_common_tags_between(photo1, photo2):
        common_tags = photo1.tags.intersection(photo2.tags)
        return len(common_tags)
