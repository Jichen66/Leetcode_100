class Solution:
    def reconstructQueue(self, people):
        people.sort(key =  (-x[0], x[1])) #lambda x:
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

a = Solution()
pe = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(a.reconstructQueue(pe))