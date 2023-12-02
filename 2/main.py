import csv
import datetime
import time


def main():
    with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['№', 'Секунда ', 'Микросекунда'])
        for line in range(300):
            writer.writerow([line + 1, datetime.datetime.now().second, datetime.datetime.now().microsecond])
            time.sleep(0.01)


if __name__ == "__main__":
    main()
