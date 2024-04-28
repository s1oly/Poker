from poker import Card

class HandEvaluator:

    hand_length = 2
    board_length = 5





# Royal Flush: 10 + highestRemaining/20

# Straight Flush: 9 + highestCardInStraight/28 + highestRemaining/300

# 4 of a Kind: 8 + cardNumber/20 + highestRemaining/300

# Full House: 7 + tripleNumber/20 + pairNumber/300 + highestRemaining/4000

# Flush: 6 + highestCardInFlush/20

# Straight: 5 + highestNumberInStraight/20 + highestRemainingCard/300

# 3 of a Kind: 4 + tripleNumber/20 + highestRemainingCard/300

# 2 Pair: 3 + pair1Number/20 + pair2Number/300 + highestRemainingCard/4000

# Pair: 2 + pairNumber/20 + highestRemainingCard/300

# High Card: 1 + highestCard/20
