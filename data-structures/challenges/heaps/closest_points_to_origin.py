import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = set()
        dist_point = dict()

        for point in points:
            d = math.sqrt((point[0] ** 2) + point[1] ** 2)
            distances.add(d)
            if dist_point.get(d):
                dist_point[d].append(point)
            else:
                dist_point[d] = [point]

        distances = sorted(distances)
        res = []
        for d in distances:
            res.extend(dist_point[d])
        return res[:k]
