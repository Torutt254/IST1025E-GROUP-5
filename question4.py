sales_data = []
grand_total = 0

for i in range(10):
    name = input("Enter salesman name: ")
    i1 = int(input("Item 1 sales: "))
    i2 = int(input("Item 2 sales: "))
    i3 = int(input("Item 3 sales: "))
    i4 = int(input("Item 4 sales: "))
    i5 = int(input("Item 5 sales: "))
    
    total = i1 + i2 + i3 + i4 + i5
    grand_total = grand_total + total
    
    sales_data.append([name, i1, i2, i3, i4, i5, total])
    print("")

print("Name\tItem1\tItem2\tItem3\tItem4\tItem5\tTotalSales")

for s in sales_data:
    print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}")

print(f"GrandTotal\t\t\t\t\t\t{grand_total}")