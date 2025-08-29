import random, requests

with open("README.md", "r") as file: readme = file.readlines()

with open("assets/chuck.txt", "r", encoding="utf8") as file: chuck_lines = file.readlines()

about_me = [l.replace("Chuck Norris", "Mario").replace("Chuck", "Mario").strip() for l in random.sample(chuck_lines, 3)]

readme[7] = f"- {about_me[0]}\n"
readme[8] = f"- {about_me[1]}\n"
readme[9] = f"- {about_me[2]}\n"

response = requests.get("https://raw.githubusercontent.com/Torfkopp/LapisDiscordBot/refs/heads/master/resources/wisdom.txt")
readme[14] = "> " + random.choice(response.text.split('\n')) + "\n"
with open("README.md", "w", encoding="utf8") as file: file.writelines(readme)



