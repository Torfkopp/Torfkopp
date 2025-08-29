import random, requests

with open("../README.md", "r") as file: readme = file.readlines()

with open("chuck.txt", "r", encoding="utf8") as file: chuck_lines = file.readlines()

about_me = []
for i in range(3):
    l = random.choice(chuck_lines).strip()
    about_me.append(l.replace("Chuck Norris", "Mario"))

readme[34] = f"<li>{about_me[0]}</li>\n"
readme[35] = f"<li>{about_me[1]}</li>\n"
readme[36] = f"<li>{about_me[2]}</li>\n"

response = requests.get("https://raw.githubusercontent.com/Torfkopp/LapisDiscordBot/refs/heads/master/resources/wisdom.txt")
readme[54] = random.choice(response.text.split("\n")) + "\n"
with open("../README.md", "w", encoding="utf8") as file: file.writelines(readme)
