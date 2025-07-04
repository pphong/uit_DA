from random import choice
import unicodedata

print("="*150)
print("\t"*15,"Trò chơi")
print("\t"*15,"Kéo - Búa - Bao")
print("="*150)
gamble = ['keo', 'bua', 'bao']

Score_player = 0
Score_comp = 0
Time_play = 1
History = []

def remove_vietnamese_tones(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join([c for c in text if unicodedata.category(c) != 'Mn'])
    return text

while True:
    player = ''
    print("=" * 15, "  Lần chơi thứ ", Time_play, "  ", "=" * 20)
    print("=" * 15, "  Lưu ý nhập q/Q để thoát trò chơi và tính điểm", "=" * 15)
    while player not in gamble:
        player = input("Lượt người chơi ( chọn: kéo, búa, bao): ").lower().strip()
        if (player.lower().strip() == 'q'):
            break
        player = remove_vietnamese_tones(player)
        if player not in gamble: print("Vui lòng nhập lại, đầu vào chỉ bao gồm \"kéo\" ,\"búa\", \"bao\"!")
    if (player.lower().strip() == 'q'):
        break
    playerAsNo = (gamble.index(player) - 1)
    comp = choice([0, 1, 2]) - 1
    print("Người chơi chọn: ", gamble[playerAsNo +1])
    print("Máy chọn: ", gamble[comp +1])

    result = ''
    point_p = 0
    point_c = 0

    if playerAsNo > comp:
        if playerAsNo - comp > 1:
            print("Máy thắng")
            point_c += 1
        else:
            print("Người chơi thắng")
            point_p += 1
    elif playerAsNo < comp:
        if comp - playerAsNo > 1:
            print("Người chơi thắng")
            point_p += 1
        else:
            print("Máy thắng")
            point_c += 1
    else:
        print("Hòa nhau")
        point_p += 0.5
        point_c += 0.5



    History.append({
        "Lần": Time_play,
        "Người chọn": player,
        "Máy chọn": gamble[comp +1],
        "Kết quả": result,
        "Điểm người": point_p,
        "Điểm máy": point_c
    })

    print("-" * 30)
    Time_play += 1
    Score_player += point_p
    Score_comp += point_c
    print("==> Kết quả: ", result)
    print("Điểm người: ", Score_player, "  Điểm máy: ", Score_comp)

print("\n" * 2)
print("=" * 100)
print("|" * 41, "Kết thúc trò chơi", "|"*41)
kq = 'Người và Máy hòa nhau'
if (Score_player - Score_comp) > 0:
    kq = "Người chơi thắng"
elif (Score_player - Score_comp) < 0:
    kq = "Máy thắng"
print("Kết quả chung cuộc: ", kq)

print("=" * 100)
print("Số lần chơi: ", len(History))
print(">" * 100)
print("Lịch sử trò chơi:")
for turn in History:
    print(f"Lần {turn['Lần']}: Người - {turn['Người chọn']}, Máy - {turn['Máy chọn']}, "
          f"Kết quả: {turn['Kết quả']}, Điểm: Người {turn['Điểm người']} - Máy {turn['Điểm máy']}")
print("Tổng điểm: Người - ", Score_player, " |  ", Score_comp, " - Máy")
print("<" * 100)
print("\n" * 2)