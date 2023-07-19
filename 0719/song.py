# 2023/07/19
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morining bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
song_list = song.lower().split()
song_dict = {wd:song_list.count(wd) for wd in song_list}
song_dict = sorted(song_dict.items(), key=lambda x:x[1], reverse=True)

max_count = song_dict[0][1]  # 取得最多次出現的次數
for word, count in song_dict:
    if count == max_count:
        print(f'字串 {word} 出現最多次共出現 {count} 次')
    else:
        break