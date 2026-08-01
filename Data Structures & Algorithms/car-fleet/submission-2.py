class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []
        for idx in range(len(position)):
            position_speed.append((position[idx], speed[idx]))
        position_speed.sort(key=lambda x:x[0])
        times = []
        for item in position_speed:
            # print(item)
            time = (target - item[0]) / item[1]
            while times and times[-1] <= time:
                times.pop()
            times.append(time)

            # print(times)

        # print(times)
        return len(times)
        
