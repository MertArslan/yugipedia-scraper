from dataclasses import dataclass
import re


@dataclass
class Pattern:
    table_identifier: str
    table_pattern: str
    row_pattern: str
    data_pattern: str

class Parser:
    def __init__(self, text, pattern):
        self.text = text
        self.table_identifier = pattern.table_identifier
        self.table_pattern = pattern.table_pattern
        self.row_pattern = pattern.row_pattern
        self.data_pattern = pattern.data_pattern

    def find_table(self):
        start_index = self.text.find(self.table_identifier)
        text = self.text[start_index:]

        match = re.search(self.table_pattern, text, re.DOTALL)
        if match is None:
            print("Could not find table")
            return None

        return match.group()

    def parse_table(self):
        text = self.find_table()
        rows = re.findall(self.row_pattern, text, re.DOTALL)

        return rows





