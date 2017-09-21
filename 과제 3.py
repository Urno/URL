#텍스트 속의 단어 개수를 확인하는 프로그램
import datetime, time
import urllib.request

url = "https://namu.wiki/w/Lobotomy%20Corporation"

f = urllib.request.urlopen(url)
#data = f.read().decode('euc-kr')
data = f.read().decode('utf-8')

begin = data.find("한국의 인디 게임.")
end = data.find("느끼지 못할 수 있다")
end += len("느끼지 못할 수 있다")

print("total=", len(data))
print("begin=", begin)
print(data[begin:begin+100])
print(data[end-100:end])
print("length=", end-begin)

speech = data[begin:end]
speech = speech.split()

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
