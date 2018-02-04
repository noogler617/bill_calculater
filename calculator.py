# bill_calculater

resturant_bill = float(input("What is the bill? "))

sales_tax = float(input("What was the sales tax? "))

service_level = input("Please rate your service between 1 and 10 ")

number_of_people = input("how many people came with you? ")

total_bill = resturant_bill * sales_tax

bill_split = total_bill / int(number_of_people)

print(total_bill)     #plue tax
print(bill_split)     #total bill with tax split per person 
