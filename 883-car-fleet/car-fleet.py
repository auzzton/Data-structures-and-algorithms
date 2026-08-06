class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Creating a list of pairs for each car
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)
        #We do this so that the closest car to the target is in index 0

# Calculate the time for each car to reach the target.
# If the current car takes longer than the fleet ahead, it forms a new fleet.
# Otherwise, it joins the existing fleet.
        fleet = 0
        last_time = 0 #time of the car
        for pos, spd in cars:
            time = (target - pos) / spd
            if last_time < time:
                fleet+=1
                last_time = time
        return fleet

        