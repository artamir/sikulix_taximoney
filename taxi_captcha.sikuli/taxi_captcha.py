#import pyperclip
# сейчас это в буфере обмена так как я туда скопировал
#x = pyperclip.paste()
#print(x)

yasearch = r'https://yandex.ru/images/search?rpt=imageview'
firefox = App("c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
firefox.open()

def goToURL(url):
    fn = "goToURL"
    #o(fn)
    type(u"l",KeyModifier.CTRL)
    type(u"a",KeyModifier.CTRL)
    paste(url)
    type(Key.ENTER)
    #c(fn)

def newTab():
    fn = "newTab"
    #o(fn)
    type(r"t",KeyModifier.CTRL)    
    #c(fn)
    

while not exists("1679750694196.png"):
    sleep(2)
newTab()
goToURL(yasearch)

captcha = r"c:\Sikulix_scripts\Siculix_TaxiMoney_captcha\2022-10-21-01-26-31.jpg"
type("2",KeyModifier.CTRL)
wait(Pattern("find_picture.png").similar(0.97).targetOffset(54,2),120)
sleep(3)
click()
wait("select_file.png")
click()
wait("file_name.png",120)
click()
paste(captcha)
type(Key.ENTER)

wait(Pattern("btn_raspoznati_text.png").similar(0.96),120)
click()
wait(Pattern("copy_in_buffer.png").similar(0.97))
click()
print firefox.getClipboard()