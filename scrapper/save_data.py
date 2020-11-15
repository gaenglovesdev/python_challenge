import csv


def save_to_file(data):
    file = open("scrapper/파이썬_개발자_공고.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["회사명", "내용", "링크"])
    for job in data:
        writer.writerow(list(job.values()))
