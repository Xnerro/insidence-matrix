from js import document, console
import pandas as pd
import pyodide

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
container = document.getElementById("container")


def render():
    for key, value in korpus.items():
        h3 = document.createElement("h3")
        h3.classList.add("title")
        p = document.createElement("p")
        h3.textContent = f"{key} :"
        p.innerHTML = f"{value}"
        container.appendChild(h3)
        container.appendChild(p)


def re_render(data):
    container.innerHTML = ""
    for i, j in data.items():
        if j == True:
            h3 = document.createElement("h3")
            h3.classList.add("title")
            p = document.createElement("p")
            h3.textContent = f"{i} :"
            p.innerHTML = f"{korpus[i]}"
            container.appendChild(h3)
            container.appendChild(p)


document.addEventListener("DOMContentLoaded", render())


def get_token(x):
    data = [y.split(" ") for y in [x for temp, x in x.items()]]
    temp_data = []

    for i in data:
        for j in i:
            temp_data.append(j.lower())

    temp = []
    [temp.append(new_x) for new_x in temp_data if new_x not in temp]

    return temp


token = get_token(korpus)


def create_df(data={}, token=None):
    for key, value in korpus.items():
        data[f"{key}"] = [1 if temp in korpus[f"{key}"].lower() else 0 for temp in token]

    df = pd.DataFrame(data, index=token)
    return df


def print_element(e):
    df = create_df(token=token)
    text_search = document.getElementById("text_search").value
    for i in text_search.split(" "):
        if i.lower() in token:
            result = df.loc[f"{i.lower()}"]
        else:
            result = None
    if result is not None:
        print(result)
        re_render(result)
    else:
        container.innerHTML = "Not Found"


btn = document.getElementById("btn")
btn.addEventListener("click", pyodide.create_proxy(print_element))
