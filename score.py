class Score:
    @staticmethod
    def calculate_score(photo_show):
        if len(photo_show) < 2:
            return 0

        score = 0
        for i in range(len(photo_show)):
            if i == 0:
                continue
            score += photo_show[i - 1].calculate_score_for_transition_to(photo_show[i])
        return score
