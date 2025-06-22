import csv
from typing import List, Union
try:
    with open('inventory.csv',mode='r', newline='') as csvfile, open('report.txt',mode='w') as reportFile: 
        spamreader = csv.reader(csvfile)
        spamwriter = csv.writer(reportFile)
        #Header csvfile: Product,Quantity,UnitPrice,SKU

        header = next(spamreader)
        newHeader = ["TotalUnits","TotalValue","MostExpensiveProduct","CheapestProduct"]
        spamwriter.writerow(newHeader)

        try:
            firstElem = next(spamreader)
            quantity = int(firstElem[1])
            totalValue = float(firstElem[2]) * quantity
            mostExpensiveProduct = firstElem[3] #Using SKU like id 
            cheapestProduct = firstElem[3]
            mostExpensiveValue = float(firstElem[2])
            cheapestValue = float(firstElem[2])

            for row in spamreader:
                quantity += int(row[1])
                totalValue += float(row[2]) * int(row[1])
                if mostExpensiveValue < float(row[2]):
                    mostExpensiveProduct = row[3]
                    mostExpensiveValue = float(row[2])
                if float(row[2]) < cheapestValue:
                    cheapestProduct = row[3]
                    cheapestValue = float(row[2])

            listOfElements: List[Union[float, str]] = [quantity, f"{totalValue:.2f}",mostExpensiveProduct,cheapestProduct]
            spamwriter.writerow(listOfElements)

        except StopIteration:
            print("Error: intentory.csv only had header")

except FileNotFoundError:
    print("Error: inventory.csv not found!")