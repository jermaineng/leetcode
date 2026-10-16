class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)

        start = 0
        end = n - 1
        count = 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            
            end -= 1
            count += 1

        return count

# sort, then have two pointers at start and end
# try to pair heaviest with lightest
# otherwise send heaviest by himself and try next heaviest with lightest
