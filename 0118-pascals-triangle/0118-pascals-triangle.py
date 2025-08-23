class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        all_list = [[1]]
        for i in range(1,numRows):
            new = [1]
            for j in range(1,i):
                new.append(all_list[-1][j-1]+all_list[-1][j])
            new.append(1)
            all_list.append(new)
        return all_list