answers = {
    "как дела?" : "Хорошо!",
    "что делаешь?" : "Программирую",
    "когда домой?" : "Ну, часиков в 7",
    "устал?" : "Не, никогда не устаю",
    "пока" : "Счастливо!"
}
answer = ""
def ask_user (user, ask):
    if user == True:
        answer = input(ask).lower()
    else:
        answer = answers[ask]
    return answer
while answer != "хорошо":
    answer = ask_user(True, "Как дела? ")
print("Спроси что-нибудь")
while answer != "Счастливо!":
    answer = ask_user(False, input().lower())
    print(answer)
