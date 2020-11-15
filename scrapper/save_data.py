import csv
from datetime import datetime


def save_to_file(data):
    today = str(datetime.today()).split(" ")[0].replace("-", "_")
    file = open(f"scrapper/{today}_잡코리아_파이썬_개발자_공고.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["회사명", "내용", "링크"])
    for job in data:
        writer.writerow(list(job.values()))
