class Solution:
    def heightChecker(heights):
        count = [0] * 101

        for h in heights:
            count[h] += 1

        expected = []
        for h in range(0, 101):
            c = count[h]
            for i in range(c):
                expected.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res


        