"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()
import requests
import re

url = "http://www.cs.fsu.edu/department/faculty/"
keywords = {"Office": "Office", "Telephone": "Telephone", "E-Mail": "E-Mail"}

def get_info():
    links = []
    prof_data = []

    main_page = requests.get(url)
    reg_res = re.findall(r'<td style="text-align: center;"><a href=(.*?)>', main_page.text)

    for link in reg_res:
        links.append(str(link).replace('"', ''))
   
    for link in links:
        prof_page = requests.get(link)
        data = None
        data = re.search(r'<title>(.*?) | Computer Science</title>', prof_page.text, re.S)
        if data[0] is not '':
            print("Name: ", end='')
            print(data.group(1))
        else:
            print("Name: N/A")
        data = None
        data = re.search(r'<td><strong>Office:</strong></td>\n<td>(.*?)</td>', prof_page.text, re.S)
        if data[0] is not '':
            print("Office: ", end='')
            print(data.group(1))
        else:
            print("Office: N/A")
        data = None
        data = re.search(r'<td><strong>Telephone:</strong></td>\n<td>(.*?)</td>', prof_page.text, re.S)
        if data[0] is not '':
            print("Telephone: ", end='')
            print(data.group(1))
        else:
            print("Telephone: N/A")
        data = None
        data = re.search(r'<td valign="top"><strong>E-Mail:</strong></td>\n<td>(.*?)</td>', prof_page.text, re.S)
        if data[0] is not '':
            print("E-Mail: ", end='')
            print(data.group(1))
        else:
            print("E-Mail: N/A")
        data = None
	data = re.search(r'<td colspan="2"><strong> <a href=(.*?)>', prof_page.text, re.S)
        if data[0] is not '':
            print("Webpage: ", end='')
            print(data.group(1))
        else:
            print("Webpage: N/A")
        print("****************************************")

if __name__ == "__main__":
    results = get_info()
