data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:  # %:求餘數
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(len(new[0]))

good = []
for d in data:
	if 'good' in d:
		good.append(d)
# 'a' in 'abc' -> True
# '1' in 'abc' -> False
print('一共有', len(good), '筆留言提到good')

# 文字計數
word_count = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1 # 新增新的key進word_count字典
for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])  # word:key; word_count[word]:value

print(len(word_count))
print(word_count['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in word_count:
		print(word, '出現過的次數為: ', word_count[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')