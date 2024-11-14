from collections import Counter

file_path = r"2023\input\07.txt"


def classify_hand(hand) -> int:
    # count the occurance of every card in the hand.  
    counts = Counter(hand).values()
    match sorted(counts):
        # Five of a kind
        case *_, 5: 
            return 7
        # Four of a kind
        case *_, 4: 
            return 6
        # Full House
        case *_, 2, 3:
            return 5
        # Three of a kind
        case *_, 3:
            return 4
        # Two pair
        case *_, 2, 2:
            return 3
        # One pair
        case *_, 2:
            return 2
    # High card
    return 1


def part_one() -> int:
    with open(file_path) as file:
        lines = file.read().strip()
        data = [line.split() for line in lines.split('\n')]
        hand_data = []
        for hand, bid in data:
            # Classify the type of hand
            hand_classification = classify_hand(hand)
            card_indices = []
            # Classify the strength of each card
            for card in hand:
                card_indices.append("23456789TJQKA".index(card))
            hand_data.append((hand_classification, *card_indices, int(bid)))
        # Sort the hands 
        sorted_hands =  sorted(hand_data)
        total = 0
        for index, (*_, bid) in enumerate(sorted_hands, 1):
            total += index * bid

        return total
        

# Part 1: 250946742
print("Part One:", part_one())

# Part 2: 251824095
#print(solve(lines.replace("J", "*")))