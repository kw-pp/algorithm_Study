import sys
input = sys.stdin.readline


sent = input().strip().split(':')
corrected_sent = []
for i in range(len(sent)):
    if sent[i] == '':
        temp = ['0000' for _ in range(8-len(sent) + 1)]
        corrected_sent.extend(sent[:i])
        corrected_sent.extend(temp)
        corrected_sent.extend(sent[i+1:])
        break

if not corrected_sent:
    corrected_sent = sent

for i in range(len(corrected_sent)):
    if len(corrected_sent[i]) != 4:
        temp = '0' * (4 - len(corrected_sent[i]))
        corrected_sent[i] = temp + corrected_sent[i]

print(':'.join(corrected_sent))