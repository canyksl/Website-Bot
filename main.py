from webbot import Browser
import time

result = 1
BASE_URL = "URL"
EMAIL = "E-mail"
PASS = "Password"
PAGE_QUERY = "Page query object"


def login(bot):
    bot.go_to(f"{BASE_URL}/login/")
    bot.press(bot.Key.ENTER)
    bot.type(EMAIL, into="email")
    bot.type(PASS, into="password")
    bot.press(bot.Key.ENTER)


def check_content(bot, page_query, query="/page_url"):
    bot.go_to(url=f"{BASE_URL}/-/{query}")
    xpath ="css-xpath"
    bot.exists(xpath=xpath)
    return bot.exists


def create_ad(bot):
    bot.go_to(url=f"{BASE_URL}")
    i = 1
    for i in range(3):
        bot.click('      button    ', tag='a.span')
        time.sleep(3)
        bot.click('                   button             ', tag='div')
        time.sleep(2)
        i += 1


def main():
    web = Browser()
    login(web)
    while True:
        if not check_content(web, page_query=PAGE_QUERY):
            print("Message-Error")
            create_ad(web)
        
        print(f"Message-success")
        time.sleep(10)


if __name__ == "__main__":
    main()
