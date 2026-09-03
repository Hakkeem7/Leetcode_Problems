class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_defense = 0
        weak = 0

        for attack, defense in properties:

            # A character with higher attack and higher defense exists
            if defense < max_defense:
                weak += 1

            # Track maximum defense among characters
            # with greater attack
            max_defense = max(max_defense, defense)

        return weak