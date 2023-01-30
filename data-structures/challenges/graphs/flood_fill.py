class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        initial_value = image[sr][sc]
        visited = set()
        height, width = len(image), len(image[0])
        nodes = [(sr, sc)]

        for node in nodes:
            sr, sc = node
            if image[sr][sc] == initial_value:
                image[sr][sc] = color
                connected_coord = ((sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1))
                for connected in connected_coord:
                    if 0 <= connected[0] < height and 0 <= connected[1] < width and node not in visited:
                        nodes.append((connected[0], connected[1]))
            visited.add((sr, sc))

        return image
