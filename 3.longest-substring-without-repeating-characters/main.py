#!/bin/env python3
#-*- coding: utf8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        初始化：map结构m用于存储当前的子串。b记录子串的起始位置，e记录当前检查的位置。
        1. 检查b是否超过检查范围，是则扫描结束。否则，将b位置的字符记录到m
        2. 记录e位置的字符到m. 如果e+1大于(字符串长度-1)，则扫描结束。否则，e移动到下个位置.
        3. 如果e指向位置的字符在m中不存在，则重复2-3. 否则4
        4. 计算本次扫描的长度（注意不能包含e），如果为当前最大长度，则更新。获取相同的字符的位置，记录si
        5. 删除m中b到si的字符，b移动到si+1
        """
        b, e, maxLen, maxBIndex = 0, 0, 0, 0
        substrMap = {} # 记录单次扫描中的已扫描的字符
        strLen = len(s)
        # print("scan s:{}".format(s))
        while b < strLen:
            # 最长子串长度大于等于剩余待检查字符数，可以不用继续了
            if maxLen >= strLen - b:
                # print("early end. s:{} start_pos:{} char:{} maxLen:{} leftLen:{}".format(s, b, bChar, maxLen, strLen - (b + 1)))
                break

            bChar = s[b]
            substrMap[bChar] = b
            # print("s:{} start_pos:{} char:{} substrMap:{}".format(s, b, bChar, substrMap))
            while True:
                # 记录已通过检查的字符
                eChar = s[e]
                substrMap[eChar] = e

                # 大于字符串长度，扫描结束。
                # 计算b到e的子串长度，如果大于当前记录的最大长度，则更新，并记录b
                if e + 1 >= strLen:
                    if e - b + 1 > maxLen:
                        maxLen = e - b + 1
                        maxBIndex = b
                        # print("exceed. maxLen:{} maxBIndex:{} bChar:{} substrMap:{}".format(maxLen, maxBIndex, bChar, substrMap))
                    # b要移动到下个位置
                    b = b + 1
                    break
                # 获取下个字符
                e = e + 1
                eChar = s[e]
                
                # print("b:{} bChar:{} e:{} eChar:{} maxLen:{} maxBIndex:{}".format(b, bChar, e, eChar, maxLen, maxBIndex))
                # 在已有子串查找e
                # e在子串中不存在，则继续检查。
                si = substrMap.get(eChar, None)
                if si is None:
                    continue

                # e在子串中存在，本次扫描结束。计算b到e的子串长度。如果大于当前记录的最大长度，则更新最大长度，并记录b。
                # 注意，此时e指向的字符在子串中已存在，因此不能计算到子串中
                if e - b > maxLen:
                    maxLen = e - b
                    maxBIndex = b
                    # print("maxLen:{} maxBIndex:{} bChar:{} substrMap:{}".format(maxLen, maxBIndex, bChar, substrMap))
                # 从子串中删除b到si的字符
                for i in range(b, si+1):
                    del substrMap[s[i]]
                # b移动到相同位置到字符后开始检查
                b = si + 1
                # 本次扫描结束
                break
        # print("finish. maxLen:{} maxBIndex:{} substr:{} substrMap:{}".format(maxLen, maxBIndex, s[maxBIndex:maxBIndex+maxLen], substrMap))
        return maxLen

if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("abcabcdfgabcdfg") == 6
    assert s.lengthOfLongestSubstring("abcabcdfgabcdfgi") == 7
