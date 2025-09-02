class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                A, B = points[i], points[j]
                if self.is_upper_left(A, B) and self.empty_rect_inclusive(A, B, points):
                    result += 1

        return result
    
    def is_upper_left(self, A, B):
        ax, ay = A
        bx, by = B
        return ax <= bx and ay >= by

    def empty_rect_inclusive(self, A, B, points):
        ax, ay = A
        bx, by = B
        xmin, xmax = min(ax, bx), max(ax, bx)
        ymin, ymax = min(ay, by), max(ay, by)

        for C in points:
            if C == A or C == B:
                continue
            x, y = C
            if xmin <= x <= xmax and ymin <= y <= ymax:
                return False
        
        return True


        