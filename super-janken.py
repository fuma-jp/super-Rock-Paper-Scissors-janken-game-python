import random
hands = ["グー", "チョキ", "パー","Sグー","Sチョキ","Sパー"]
cpu_normal=["グー","チョキ","パー"]
cpu_super=["Sグー","Sチョキ","Sパー"]
win=0
lose=0
draw=0
super_used=False
cpu_super_used=False
rounds=5

print("【じゃんけんゲーム】")
print("1:グー")
print("2:チョキ")
print("3:パー")
print("4:superグー")
print("5:superチョキ")
print("6:superパー")
print("※super技は1度しか使えない")
print("super技はあいこの場合でも勝てる")

for i in range(1,rounds+1):
    print(f"\n---{i}回目---")

    while True:
       player_num = input("数字を入力してね")
       if player_num not in("1","2","3","4","5","6"):
          print("正しい数字を入力してね")
          continue
    
       player=hands[int(player_num)-1]

       if player.startswith("S"):
          if super_used:
             print("1度しか使えない")
             continue

          else:
              super_used=True
              print("技を使った")
       break

    if not cpu_super_used:
        cpu= random.choice(cpu_normal+cpu_super)
        if cpu.startswith("S"):
           cpu_super_used=True
           print("ナビは技を使った")
    else:
        cpu=random.choice(cpu_normal)

    print(f"あなたは{player}を出した")
    print(f"ナビは{cpu}をだした")


    if player == cpu:
      print("あいこ")
      draw+=1
    elif (player == "グー" and cpu == "チョキ") or \
        (player == "チョキ" and cpu == "パー") or \
        (player == "パー" and cpu == "グー")or\
        (player=="Sグー"and cpu=="グー")or\
        (player=="Sチョキ"and cpu=="チョキ")or\
        (player=="Sパー"and cpu=="パー")or\
        (player=="Sグー"and cpu=="Sチョキ")or\
        (player=="Sチョキ"and cpu=="Sパー")or\
        (player=="Sパー"and cpu=="Sグー")or\
        (player=="Sグー"and cpu=="チョキ")or\
        (player=="Sチョキ"and cpu=="パー")or\
        (player=="Sパー"and cpu=="グー"):
      print("あなたの勝ち")
      win+=1
    else:
      print("あなたの負け")
      lose+=1
print("\n===結果===")
print(f"勝ち:{win}")
print(f"負け:{lose}")
print(f"引き分け:{draw}")
if win>lose:
  print("あなたの勝ち")
elif lose>win:
  print("あなたの負け")
else:
  print("引き分け")
