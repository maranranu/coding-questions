"""
Problem
Marut is great warrior. Marut loves his girlfriend Shizuka very much. Being jealous from Marut's love, the Devil kidnaps his girlfriend. Hence, Marut declares a war against the Devil. The devil decides to send his army men one by one to fight with Marut. Marut being a smart person, he has a secret energy booster named "CodeRas". If Marut drinks "CodeRas" one time, his energy increases by V unit. Marut has an infinite amount of "CodeRas".

Each army man does some damage to Marut. If an army man has X amount energy and fights with Marut, energy of both of them will decrease by X unit. A person dies if his energy becomes zero unit.

Now, Marut knows the number of army men that Devil will send and their energy level. As poor Marut is bad in mathematics, he wants to know the minimum number of times he need to drink "CodeRas" in order to kill all army men and keep himself alive at the end of war. Help him !!!

Note: Marut cannot drink "CodeRas" in between the fight. He can only drink it before and after the fight.

Input:
First line contains an integer T, denoting the number of test cases.
Each testcase contains two lines.
First line of each testcase contains three integers N , E and V separated by single space. N denotes the size of army, E denotes the initial energy of Marut and V denotes the amount of energy which is increased after drinking "CodeRas".
Second line of each testcase contains N integers, separated by single space. ith integer of this line denotes the energy of ith army man.

Output:
For each test case, print the answer in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ E ≤ 105
1 ≤ V ≤ 105
1 ≤ Army man's energy ≤ 105
"""

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

