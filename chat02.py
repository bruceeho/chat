#讀取檔案將內容記錄到lines這個清單

def read_file(filename):
    lines = []
    with open(filename,'r',encoding='UTF-8-sig') as f:#若出現\ufeff需要用uff-8-sig編碼格式
        for line in f:
            lines.append(line.strip())
    return lines

#剖析內容，呈現為需求的格式
def convert(lines):
    person = None
    allen_word_count = 0
    allen_image_count = 0
    allen_sticker_count = 0
    viki_word_count = 0
    viki_image_count = 0
    viki_sticker_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen說',allen_word_count,'個字')
    print('allen傳了',allen_sticker_count,'個貼圖')
    print('allen傳了',allen_image_count,'張圖片')

    print('viki說',viki_word_count,'個字')
    print('viki傳了',viki_sticker_count,'個貼圖')
    print('viki傳了',viki_image_count,'張圖片')

#將內容寫入至檔案中
def write_file(filename,lines):
    with open(filename,'w') as f:
        for line in lines:
            f.write(line + '\n')
#主程式執行
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)


main()