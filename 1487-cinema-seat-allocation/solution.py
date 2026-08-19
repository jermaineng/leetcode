class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        block1 = 0b11110000 # seats 2-5 bitmask
        block2 = 0b11000011 # seats 4-7 bitmask
        block3 = 0b00001111 # seats 6-9 bitmask

        reserved = defaultdict(int)

        for seats in reservedSeats:
            row = seats[0]
            seat = seats[1] 
            if 2 <= seat <= 9:
                reserved[row] |= 1 << (seat - 2)
        
        max_groups = (n - len(reserved)) * 2 # add rows that dont have reserved seats

        for block in reserved.values():
            if (block | block1) == block1 or (block | block2) == block2 or (block | block3) == block3:
                max_groups += 1

        return max_groups

# only need to consider seats 2-9 whereby max families = 2 when there are no reserved seats among seats 2-9. otherwise, at most 1
# hash table to store reserved seats in every row
# if seat is reserved, make bit 1 (bitwise or operation)
