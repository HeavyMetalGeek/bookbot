class ReportData:
    def __init__(self, path: str):
        self.path  = path
        self.contents = self.get_text()
        self.word_count = self.get_word_count()
        self.letter_counts = self.get_letter_counts()

    def __str__(self):
        report_str = f"--- Report for {self.path} ---\n"
        report_str += f"There were {self.word_count} words found\n\n"
        report_str += "Letter Counts:\n"
        report = []
        for k,v in self.letter_counts.items():
            if k.isalpha():
                report.append({"letter": k, "count": v})
        report.sort(reverse=True, key=self.sort_on)
        for item in report:
            report_str += f"The '{item["letter"]}' character was found {item["count"]} times\n"
        report_str += f"--- End of Report ---"
        return report_str

    def sort_on(self, data: dict):
        return data["count"]

    def get_text(self):
        contents = None
        with open(self.path) as f:
            contents = f.read()
        return contents

    def get_word_count(self):
        return len(self.contents.split())

    def get_letter_counts(self):
        letter_counts = {}
        for letter in self.contents.lower():
            if letter in letter_counts.keys():
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        return letter_counts

def main():
    report_data = ReportData("books/frankenstein.txt")
    print(report_data)
    #book_path =
    #contents = get_text(book_path)
    #word_count = get_word_count(contents)
    #letter_counts = get_letter_counts(contents)
    #print_report(letter_counts)




if __name__ == '__main__':
    main()

