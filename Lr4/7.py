math=[100,100,100,45,59,100,100,100,100,100,100,100,21]
russian=[100,100,100,45,59,100,100,100,100,100,100,100,21]
informatika=[100,100,100,45,59,100,100,100,100,100,100,100,21]
names=["Тёама","диома","даня","дима","дора","дон","дикой","дамбер","дэбил","хусь","даблтор","шамиль","зубен"]
for i in range(len(names)):
    if math[i] == 100 and russian[i] == 100 and informatika[i] == 100:
        print("индекс",i,"Имя абитуриента", names[i])