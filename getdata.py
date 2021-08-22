from requests import get
from bs4 import BeautifulSoup
from pprint import pprint, pformat
URL = "https://smite.fandom.com/wiki/VGS_Cheat_Sheet"
page = get(URL)
soup = BeautifulSoup(page.text, "html.parser")

tables = soup.select(".wikitable")

command_values = {}
for table in tables:
    split_text = table.text.split("\n")
    good_text = [word for word in split_text if word]

    values = good_text[5:]
    command_names = [value for value in values if "-" not in value and not value.lower().startswith("v") and len(value) > 2 and "nintendo" not in value.lower()]
    command_keys = [value for value in values if value.lower().startswith("v") and "-" not in value]
    if not command_names: continue
    section_dict = dict(zip(command_keys, command_names))
    command_values.update(section_dict)

headlines = soup.select(".mw-headline")
headlines = [headline.text for headline in headlines]

with open("all_commands.py", "w") as f:
    f.write("# File containing all commands.\n")
    f.write(f"commands = {pformat(command_values)}\n\n")
    f.write(f"headlines = {pformat(headlines)}")

print("Done")