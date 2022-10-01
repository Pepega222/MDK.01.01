sentences = ['научиться плести рыболовные сети',
            'обучать нейронные сети',
           'паук ловит в сети мух']
cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('сети')
print(cap_count) 