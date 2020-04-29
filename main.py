import selenium
from selenium import webdriver
import time 

nick = "ahavlicek4"
pwd = "wertojenej"

driver = webdriver.Opera()
driver.get('https://wocabee.app/app/?lang=CZ')

trida = ""
balik = ""



def line(): print("="*40)

def login(nickname,password):
    
    print("přihlašování...")
    login_nick = driver.find_element_by_id("login")
    login_nick.send_keys(nickname)
    login_pwd = driver.find_element_by_id("password")
    login_pwd.send_keys(password)
    login_btn = driver.find_element_by_id("submitBtn")
    login_btn.click()
    print("přihlášeno")

def loadClasses():
    classes = []

    content_blocks = driver.find_elements_by_id("listOfClasses")

    for block in content_blocks:
        elements = block.find_elements_by_tag_name("a")
        for el in elements:
            classes.append(el)
    return classes

def loadBaliks():
    return driver.find_elements_by_class_name("packageTableRow")

def train(baliky,balik,file):
    baliky[balik].find_elements_by_tag_name('td')[0].find_element_by_tag_name("a").click()#.get_attribute('href')
    slovicka = []
    preklad = []
    time.sleep(1)
    for i in range(int(driver.find_element_by_id("wordCount").text)-1):
        slovicka.append(driver.find_element_by_id("word").text)
        preklad.append(driver.find_element_by_id("translation").text)
        driver.find_element_by_id("rightArrow").click()
        time.sleep(1)
    #přečtení posledního slovíčka
    slovicka.append(driver.find_element_by_id("word").text)
    preklad.append(driver.find_element_by_id("translation").text)
    #vypsání slovíček
    with open(file,"w+") as f:
        for i in range(len(slovicka)):
            f.write(f"{slovicka[i]};{preklad[i]}\n")
    driver.find_element_by_id("backBtn").click()

def translate(word,file):
    with open(file, "r") as f:
        words = f.read()
    words = words.split("\n")
    for i in range(len(words)):
        words[i] = words[i].split(";")

    #print(words)
    for i in words:
        if(i[0] == word): return i[1]
        if(i[1] == word): return i[0]

def do_the_hard_stuff(times,file):
    types = ["transcribe","translateWord", "chooseWord", "findPair", "completeWord", "translateFallingWord"]
    form = driver.find_element_by_id("mainForm")
    for owo in range(times):
        type = ""
        for i in types:
            t = form.find_element_by_id(i)
            #print(f"type:{i} style: {t.get_attribute('style')}")
            if t.get_attribute('style') != "display: none;": 
                type = i
        print(type)
        t = form.find_element_by_id(type)
        wait_time = 4
        if(type == "transcribe"):
            driver.find_element_by_id("transcribeSkipBtn").click()
            wait_time = 0.5
        elif(type == "translateWord"):
            word = t.find_elements_by_class_name("form-group")[1].text
            word = translate(word, file)
            answer = t.find_element_by_id("translateWordAnswer")
            answer.send_keys(word)
            t.find_element_by_id("translateWordSubmitBtn").click()
        elif(type == "chooseWord"):
            word = t.find_elements_by_class_name("form-group")[1].text
            word = translate(word, file)
            btns = t.find_element_by_id("chooseWords").find_elements_by_tag_name("button")
            for i in btns:
                if(word == i.text): 
                    i.click()
                    continue
        elif(type == "findPair"):
            q_words_list = []
            q_words = t.find_element_by_id("q_words").find_elements_by_tag_name("button")
            for i in q_words: q_words_list.append(i.text)

            a_words_list = []
            a_words = t.find_element_by_id("a_words").find_elements_by_tag_name("button")
            for i in a_words: a_words_list.append(i.text)

            for i in range(3):
                for j in range(3):
                    if(a_words_list[i] == translate(q_words_list[j],file)):
                        a_words[i].click()
                        q_words[j].click()
                        continue
        elif(type == "completeWord"):
            word = t.find_elements_by_class_name("form-group")[0].text
            word = translate(word, file)
            word_to_complete = t.find_elements_by_class_name("form-group")[1].text
            letters = []
            for i in range(len(word)):
                if word_to_complete[i] == "_":
                    letters.append(word[i])

            btns = t.find_element_by_id("characters").find_elements_by_tag_name("span")
            for i in letters: 
                wrote = False
                for b in btns:
                    if b.text == i and not wrote:
                        b.click()
                        wrote = True
            #print(i)
        elif(type == "translateFallingWord"):
            word = t.find_element_by_id("tfw_word").text
            word = translate(word,file)
            t.find_element_by_id("translateFallingWordAnswer").send_keys(word)
            t.find_element_by_id("translateFallingWordSubmitBtn").click()

        time.sleep(wait_time)

def work(baliky,balik,file, number_of_worlds):
    baliky[balik].find_elements_by_tag_name('td')[3].find_element_by_tag_name("a").click()
    how_many_times = number_of_worlds
    do_the_hard_stuff(how_many_times,file)
    driver.find_element_by_id("backBtn").click()

    

    #for i in 
"""
login(nick,pwd)
line()
time.sleep(1)

#výběr třídy
classes = loadClasses()
print("nalezené třidy:")
for i in classes:
    print(f"{classes.index(i)+1}  {i.text}")#get_attribute('href'))
selected_class = int(input(f"vyberte třídu (1-{len(classes)}): "))
trida = classes[selected_class-1].text
classes[selected_class-1].find_element_by_tag_name("button").click()
line()

#výběr bylíků
baliky = loadBaliks()
print("nalezené balíky: ")
baliky = driver.find_elements_by_class_name("packageTableRow")
for i in baliky:
    print(f"{baliky.index(i)+1}  {i.find_elements_by_tag_name('td')[0].text}")

selected_balik = int(input(f"vyberte balík (1-{len(baliky)}): "))
balik = baliky[selected_balik-1].find_elements_by_tag_name('td')[0].text

akce = int(input("co si přejete s tímto balíkem udělat? (1=procvičit(vytvořit txt), 2=vypracovat): "))
#zapsání slovíček do txt souboru
if(akce == 1): train(baliky,selected_balik-1, f"{balik}.txt")
elif (akce == 2): work(baliky, selected_balik-1, f"{balik}.txt")
"""
