import re
from web_parser import Parser


class SecretPackParser(Parser):
    def get_data(self):
        data_list = []

        rows = self.parse_table()

        for row in rows:
            row_data = {}
            match = re.findall(self.data_pattern, row, re.DOTALL)
            if len(match) == 0:
                continue

            row_data["Name"] = self.fix_quotes(match[0])
            row_data["Rarity"] = match[1]
            row_data["Category"] = match[2:]

            data_list.append(row_data)

        return data_list

    def fix_quotes(self, card_name):
        card_name = re.sub("&#39;", '\'', card_name)
        card_name = re.sub("&quot;", '\"', card_name)
        return card_name

