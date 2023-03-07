points = int(input("Podaj maksymalną liczbę punktów: "))

for x in range(0, points+1):
    if(round((x/points)*100, 2) >= 0 and round((x/points)*100, 2) < 30): print(f"1 = {x}pkt")
    if(round((x/points)*100, 2) >= 30 and round((x/points)*100, 2) < 35): print(f"-2 = {x}pkt")
    if(round((x/points)*100, 2) >= 35 and round((x/points)*100, 2) < 43): print(f"2 = {x}pkt")
    if(round((x/points)*100, 2) >= 43 and round((x/points)*100, 2) < 47): print(f"+2 = {x}pkt")
    if(round((x/points)*100, 2) >= 47 and round((x/points)*100, 2) < 50): print(f"-3 = {x}pkt")
    if(round((x/points)*100, 2) >= 50 and round((x/points)*100, 2) < 63): print(f"3 = {x}pkt")
    if(round((x/points)*100, 2) >= 63 and round((x/points)*100, 2) < 69): print(f"+3 = {x}pkt")
    if(round((x/points)*100, 2) >= 69 and round((x/points)*100, 2) < 75): print(f"-4 = {x}pkt")
    if(round((x/points)*100, 2) >= 75 and round((x/points)*100, 2) < 83): print(f"4 = {x}pkt")
    if(round((x/points)*100, 2) >= 83 and round((x/points)*100, 2) < 87): print(f"+4 = {x}pkt")
    if(round((x/points)*100, 2) >= 87 and round((x/points)*100, 2) < 90): print(f"-5 = {x}pkt")
    if(round((x/points)*100, 2) >= 90 and round((x/points)*100, 2) <= 100): print(f"5 = {x}pkt")
    if(x < points):
        if(round(((x+0.5)/points)*100, 2) >= 0 and round(((x+0.5)/points)*100, 2) < 30): print(f"1 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 30 and round(((x+0.5)/points)*100, 2) < 35): print(f"-2 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 35 and round(((x+0.5)/points)*100, 2) < 43): print(f"2 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 43 and round(((x+0.5)/points)*100, 2) < 47): print(f"+2 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 47 and round(((x+0.5)/points)*100, 2) < 50): print(f"-3 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 50 and round(((x+0.5)/points)*100, 2) < 63): print(f"3 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 63 and round(((x+0.5)/points)*100, 2) < 69): print(f"+3 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 69 and round(((x+0.5)/points)*100, 2) < 75): print(f"-4 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 75 and round(((x+0.5)/points)*100, 2) < 83): print(f"4 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 83 and round(((x+0.5)/points)*100, 2) < 87): print(f"+4 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 87 and round(((x+0.5)/points)*100, 2) < 90): print(f"-5 = {x+0.5}pkt")
        if(round(((x+0.5)/points)*100, 2) >= 90 and round(((x+0.5)/points)*100, 2) <= 100): print(f"5 = {x+0.5}pkt")


while(True):
    choice = input("Wpisz 'q' zeby zamknąć program.")
    if(choice == 'q'): exit()
