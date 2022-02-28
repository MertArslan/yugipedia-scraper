from network_controller import NetworkController
from master_list_parser import MasterListParser
from secret_pack_parser import SecretPackParser
from web_parser import Pattern
import re
import json

URL = 'https://yugipedia.com'
ML_PAGE = '/wiki/Secret_Pack'
ML_PATTERN = Pattern("List of Secret Packs",
                      "<table.*?</table>",
                      "<tr.*?</tr>",
                      "href=\"(.*?)\"")
SP_PATTERN = Pattern("List",
                     "<table.*?</table>",
                     "<tr.*?</tr>",
                     "title=\"(.*?)\"")


def dump_packs(count=-1):
    nc = NetworkController()
    page = nc.get_website(URL + ML_PAGE)

    ml_parser = MasterListParser(page.text, ML_PATTERN)
    master_list = ml_parser.get_master_list()
    print(master_list)

    for link in master_list:
        pack_name = link.replace("/wiki/", "")
        pack_name = pack_name.replace("_", " ")
        print(pack_name)
        pack_name = re.sub("%[0-9]*", '', pack_name)
        print(pack_name)

        page = nc.get_website(URL + link)

        secret_pack_parser = SecretPackParser(page.text, SP_PATTERN)
        data = secret_pack_parser.get_data()

        with open("packs/" + pack_name + ".json", "w") as f:
            json.dump(data, f, indent=4)

        count -= 1
        if count == 0:
            break

if __name__ == '__main__':
    dump_packs(18)

