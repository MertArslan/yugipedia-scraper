import re
from web_parser import Parser
from web_parser import Pattern


class MasterListParser(Parser):
    def get_master_list(self):
        master_list = []

        rows = self.parse_table()
        for row in rows:
            match = re.search(self.data_pattern, row, re.DOTALL)
            if match is None:
                continue
            master_list.append(match.group(1))

        return master_list
