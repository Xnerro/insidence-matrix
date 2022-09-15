import pandas as pd
import os

korpus = {
    "doc1": "Perkembangan yang pesat dalam dunia teknologi dan komunikasi telah menyumbang secara langsung kepada proses pengajaran dan pembelajaran bahasa",
    "doc2": "Dewasa ini, arus perkembangan teknologi semakin berkembang seiring dengan peredaran zaman.Senario ini menjadi petunjuk untuk menggerakkan Malaysia menuju negara maju yang membangun mengikut acuannya sendiri menjelang tahun 2020.",
    "doc3": "Secara umumnya, terdapat empat kemahiran yang penting dalam pengajaran bahasa iaitu kemahiran mendengar, bertutur, membaca dan menulis. Oleh itu, pengajaran bahasa Arab di Malaysia telah meletakkan matlamat membolehkan pelajar menguasai empat kemahiran bahasa tersebut",
    "doc4": "Paparan skrin menu utama mengandungi dua bingkai iaitu bingkai bawah yang menempatkan arahan, manakala bingkai tengah adalah ruangan yang memaparkan enam bebutang yang akan membawa pengguna ke menu-menu yang tertentu iaitu pembelajaran, kosa kata, nasyid, permainan, lakonan dan aktiviti",
    "doc5": "Menu pembelajaran merupakan bahagian yang utama dalam pembangunan prototaip aplikasi android",
    "doc6": "Persembahan skrin pembelajaran ini perlu ringkas, padat dan mudah difahami pengguna semasa proses pembelajaran",
    "doc7": "Susun atur kandungan dibuat dengan berhati-hati supaya tidak terlalu sesak pada halaman kandungan",
    "doc8": " Oleh itu, penyusunan atur kandungan ditumpukan kepada bebutang terlebih dahulu.",
    "doc9": "Terdapat lima bebutang utama pada skrin pembelajaran yang ditempatkan pada bahagian kiri",
    "doc10": "Pembangunan prototaip aplikasi android ini adalah bertujuan untuk membantu para guru dalam menyediakan BBM yang boleh digunakan dalam pengajaran bahasa Arab melalui pendekatan didik hibur yang berteraskan teknologi",
}

new_list = []

x = [y.split(" ") for y in [x for temp, x in korpus.items()]]
temp = []

for i in x:
    for j in i:
        temp.append(j.lower())


def get_token(x: list):
    temp = []
    [temp.append(new_x) for new_x in x if new_x not in temp]

    return temp


token = get_token(temp)
data = {}


print(len(token))

for key, value in korpus.items():
    data[f"{key}"] = [1 if temp in korpus[f"{key}"].lower() else 0 for temp in token]

df = pd.DataFrame(data, index=token)
print(token)

word = input("Masukan kata :")

searching_word = word.split(" ")
print(searching_word)
os.system("clear")


for i in searching_word:
    if i.lower() in token:
        result = df.loc[f"{i.lower()}"]
    else:
        result = None
        print(f"{i} kata tidak tersedia dalam korpus")

if result is not None:
    for i, j in result.items():
        if j == True:
            print(f"{i} :", korpus[i])
