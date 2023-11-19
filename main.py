# import requests
# from bs4 import BeautifulSoup
# import lxml
# import openpyxl
#
# for j in range(1,51):
#     print(f"Page - {j}")
# url = "https://kups.club/?page=1"
# user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
# headers = {"User-agent": user}
# sess = requests.Session()
#
#
# for j in range(1, 51):
#     print(f"Page - {j}")
#     url = f"https://kups.club/?page={j}"
#     response = sess.get(url, headers=headers)
#     # print(response.status_code)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "lxml")
#         # print(soup)
#         products = soup.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
#     #
#         for prod in products:
#                 price = prod.find("p", class_="card-text")
#                 title = prod.find("h3", class_="card-title")
#                 print(price.text.strip(), title.text.strip())
#                 price_prod = price.text
#                 title_prod = title.text
#                 with open("catalog.txt", "a", encoding="utf-8") as file:
#                     file.write(f"{price_prod} {title_prod}\n")

