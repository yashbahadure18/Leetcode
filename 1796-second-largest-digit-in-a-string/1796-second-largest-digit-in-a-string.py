class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """

        largest = -1
        second_largest = -1

        for i in range(len(s)):

            if s[i].isdigit():

                num = int(s[i])

                if num>largest:
                    second_largest = largest
                    largest = num

                elif num<largest and num>second_largest:
                    second_largest = num

        return second_largest