import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from webdriver_manager import firefox, microsoft, chrome, opera

trida = ""
balik = ""

driver = None

def line(): print("="*40)

def chooseBrowser(browser):
    global driver
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        if __name__ != "__main__":
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path=chrome.ChromeDriverManager().install(), options=options)
    elif browser == "Firefox":
        options = webdriver.ChromeOptions()
        if __name__ != "__main__":
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())
    elif browser == "IE":
        options = webdriver.ChromeOptions()
        if __name__ != "__main__":
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Ie(executable_path=microsoft.IEDriverManager().install())
    elif browser == "Opera":
        options = webdriver.ChromeOptions()
        if __name__ != "__main__":
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Opera(executable_path=opera.OperaDriverManager().install(), options=options, service_log_path=os.devnull)
    elif browser == "Edge":
        options = webdriver.ChromeOptions()
        if __name__ != "__main__":
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(executable_path=microsoft.EdgeChromiumDriverManager().install())
    elif browser == "Safari":
        driver == webdriver.Safari()
    driver.get('https://wocabee.app/app/?lang=CZ')
    actions = ActionChains(driver)

def login(nickname,password):
    global driver
    #print("přihlašování...")
    login_nick = driver.find_element_by_id("login")
    login_nick.send_keys(nickname)
    login_pwd = driver.find_element_by_id("password")
    login_pwd.send_keys(password)
    login_btn = driver.find_element_by_id("submitBtn")
    login_btn.click()
    #print("přihlášeno")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logoutBtn"))
    )

def loadClasses():
    classes = []

    content_blocks = driver.find_elements_by_id("listOfClasses")

    for block in content_blocks:
        elements = block.find_elements_by_tag_name("a")
        for el in elements:
            classes.append(el)
    return classes

def loadBaliks():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "packageTableRow"))
    )
    return driver.find_elements_by_class_name("packageTableRow")

def train(baliky,balik,file): #načtení slovíček do .txt souboru
    slovicka = []
    preklad = []
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "word"))
    )
    for i in range(int(driver.find_element_by_id("wordCount").text)-1):
        slovicka.append(driver.find_element_by_id("word").text)
        preklad.append(driver.find_element_by_id("translation").text)
        driver.find_element_by_id("rightArrow").click()
        time.sleep(1)
    #přečtení posledního slovíčka
    slovicka.append(driver.find_element_by_id("word").text)
    preklad.append(driver.find_element_by_id("translation").text)
    #vypsání slovíček
    f = open(file,"w+")
    for i in range(len(slovicka)):
        f.write(f"{slovicka[i]};{preklad[i]}\n")

def translate(word,file): #přeložení slova z jednoho jazyka do druhého
    f=open(file, "r")
    words = f.read()
    words = words.split("\n")
    for i in range(len(words)):
        words[i] = words[i].split(";")

    #print(word)
    for i in words:
        if(i[0] == word): return i[1]
        if(i[1] == word): return i[0]

def do_the_hard_stuff(times,file): #řešení úkolů
    types = ["transcribe","translateWord", "chooseWord", "findPair", "completeWord", "translateFallingWord"]
    form = driver.find_element_by_id("mainForm")
    correctBtn = form.find_element_by_id("correct")
    for owo in range(times):
        while correctBtn.get_attribute("style") != "display: none;":
            pass
        type = ""
        #hledání typu ůkolu podle toho jestli mají style: display: none;, nebo ne
        for i in types:
            t = form.find_element_by_id(i)
            #print(f"type:{i} style: {t.get_attribute('style')}")
            if t.get_attribute('style') != "display: none;": 
                type = i
        #print(type)
        t = form.find_element_by_id(type)
        wait_time = 4
        #řešení jedntlivých ůkolú
        if(type == "transcribe"): #tts > přeskočení na další
            driver.find_element_by_id("transcribeSkipBtn").click()
            wait_time = 0.5
        elif(type == "translateWord"): #přeložení slova
            word = t.find_elements_by_class_name("form-group")[1].text
            word = translate(word, file)
            answer = t.find_element_by_id("translateWordAnswer")
            answer.send_keys(word)
            t.find_element_by_id("translateWordSubmitBtn").click()
        elif(type == "chooseWord"): #výbět překladu slova z nabídnutých překladů
            word = t.find_elements_by_class_name("form-group")[1].text
            word = translate(word, file)
            btns = t.find_element_by_id("chooseWords").find_elements_by_tag_name("button")
            for i in btns:
                if(word == i.text): 
                    i.click()
                    continue
        elif(type == "findPair"): #nalezení páru mezi dvěma trojicemi slovíček
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
        elif(type == "completeWord"): #doplnění chybějících písmen ve slově
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
        elif(type == "translateFallingWord"): #padající slovo (v modu x2)
            word = t.find_element_by_id("tfw_word").text
            word = translate(word,file)
            t.find_element_by_id("translateFallingWordAnswer").send_keys(word)
            t.find_element_by_id("translateFallingWordSubmitBtn").click()

def work(baliky,balik,file,how_many_times): #nahánění slovíček
    #baliky[balik].find_elements_by_tag_name('td')[3].find_element_by_tag_name("a").scrollIntoView()
    baliky[balik].find_elements_by_tag_name('td')[3].find_element_by_tag_name("a").click()
    do_the_hard_stuff(how_many_times,file)
    driver.find_element_by_id("backBtn").click()

def work_percent(baliky,balik,file): #dokončit balík, když už program umí slovíčka; (to kde jsou procenta)
    baliky[balik].find_elements_by_tag_name('td')[3].find_element_by_tag_name("a").click()
    time.sleep(1)
    while(int(driver.find_element_by_id("progressValue").text[:-1])<50):
        do_the_hard_stuff(1,file)
    time.sleep(5) #fukin upozonění že jsem za 50 procenty
    while(int(driver.find_element_by_id("progressValue").text[:-1])<100):
        do_the_hard_stuff(1,file)
    
    driver.find_element_by_id("backBtn").click()

def train_balik(baliky,balik,file): #naučit slovíčkaa z balíku (i)
    baliky[balik].find_elements_by_tag_name('td')[0].find_element_by_tag_name("a").click()#.get_attribute('href')
    train(baliky,balik,file)
    driver.find_element_by_id("backBtn").click()

def complete_balik(baliky,balik,file): #dokončit balík včetně naučení slovíček na začátku balíku (neotestováno)
    baliky[balik].find_elements_by_tag_name('td')[3].find_element_by_tag_name("a").click() #spustit balik
    driver.find_element_by_id("introRun").click() #next
    train(baliky, balik, file)
    time.sleep(1)
    while(int(driver.find_element_by_id("progressValue").text[:-1])<50):
        do_the_hard_stuff(1,file)
    time.sleep(5) #fukin upozonění že jsem za 50 procenty
    while(int(driver.find_element_by_id("progressValue").text[:-1])<100):
        do_the_hard_stuff(1,file)
    
    driver.find_element_by_id("backBtn").click()





    

if __name__ == "__main__":
    chooseBrowser(input("Jaký prohlížeč? (přesně: Chrome, Firefox, Opera, IE, Edge, Safari) "))

    nick = input("Přihlašovací jméno: ")
    pwd = getpass("Heslo: ")

    login(nick,pwd)
    line()
    time.sleep(2)

    #výběr třídy
    classes = loadClasses()
    print("nalezené třidy:")
    for i in classes:
        print(f"{classes.index(i)+1}  {i.text}")#get_attribute('href'))
    selected_class = int(input(f"vyberte třídu (1-{len(classes)}): "))
    trida = classes[selected_class-1].text
    classes[selected_class-1].find_element_by_tag_name("button").click()
    line()

    #výběr balíků
    baliky = loadBaliks()
    print("nalezené balíky: ")
    baliky = driver.find_elements_by_class_name("packageTableRow")
    for i in baliky:
        print(f"{baliky.index(i)+1}  {i.find_elements_by_tag_name('td')[0].text}")

    selected_balik = int(input(f"vyberte balík (1-{len(baliky)}): "))
    balik = baliky[selected_balik-1].find_elements_by_tag_name('td')[0].text

    akce = int(input("co si přejete s tímto balíkem udělat? (1=procvičit(vytvořit txt), 2=nahnat body, 3=vypracovat(%)): "))
    #zapsání slovíček do txt souboru
    if(akce == 1): train_balik(baliky,selected_balik-1, f"{balik}.txt")
    elif (akce == 2): 
        how_many_times = int(input("Kolik slovíček chcete vyřešit?: "))
        work(baliky, selected_balik-1, f"{balik}.txt",how_many_times)
    elif (akce == 3): work_percent(baliky, selected_balik-1, f"{balik}.txt")

