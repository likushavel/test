# import requests
# from bs4 import BeautifulSoup
# import lxml
# import openpyxl
#
#
# user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
# headers = {"User-agent": user}
# sess = requests.Session()
# counter = 0
# space = "  "
# book = openpyxl.Workbook()
# sheet = book.active
# sheet["A1"] = "Title shop"
# sheet["B1"] = "Procent cash backer"
# count = 2
# print("Starting...")
# with open('output.txt', "a", encoding="utf-8") as file:
#     for j in range(1, 51):
#         print(f"Page - {j}")
#         url = f"https://kups.club/?page={j}"
#         response = sess.get(url, headers=headers)
#         # print(response.status_code)
#
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             # print(soup)
#             products = soup.findAll("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
#             for prod in products:
#                     counter += 1
#                     title = prod.find("div", class_="shop-title").text
#                     cashb = prod.find("div", class_="shop-rate").text
#
#                     file.write(f"Shop No {counter}  Name: {title} Cashback: {cashb}\n")
#                     sheet[f"A{count}"] = title
#                     sheet[f"B{count}"] = cashb
#                     count += 1
#                 if j == 4:
#                     print("Finishing...")
#             else:
#                 print("ERROR on start")
#                 break
#     book.save("catalog.xlsx")
#     book.close()
