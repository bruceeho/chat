#讀取檔案將內容記錄到lines這個清單
def read_file(filename):
    lines = []
    with open('input.txt','r',encoding='UTF-8-sig') as f:#若出現\ufeff需要用uff-8-sig編碼格式
        for line in f:
            lines.append(line.strip())
    return lines
#剖析內容，呈現為需求的格式
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person +'：' + line)
    return new
#將內容寫入至檔案中
def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
		    f.write(line + '\n')
#主程式執行
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)



main()