def win_fight(army, energy, fill_energy):
    count = 0
    i = 0
    while i < len(army):
        a = army[i]
        if a < energy:
            energy -= a
            i = i + 1
        else:
            energy += fill_energy
            count += 1
    return count


# Write your code here
t = int(input())

for i in range(t):
    input1 = input().strip().split(" ")
    input1 = [int(inp.strip()) for inp in input1]
    army = input().strip().split(" ")
    army = [int(a) for a in army]
    army.sort()
    ans = win_fight(army, input1[1], input1[2])
    print(ans)

