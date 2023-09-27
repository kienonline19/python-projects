from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
<p>This is another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


# h1_tag = simple_soup.find('h1') # entire tag
# print(type(h1_tag))
# print(h1_tag)
#
# h1_content = h1_tag.string
# print(h1_content)
def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


find_title()


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


find_list_items()


def find_subtitle():
    # p_tag = simple_soup.find(class_='subtitle')
    p_tag = simple_soup.find('p', {'class': 'subtitle'})
    print(p_tag.string)


find_subtitle()


def find_other_paragraph():
    p_tags = [
        p for p in simple_soup.find_all('p') or []
        if 'subtitle' not in p.attrs.get('class', [])
    ]
    print(p_tags[0].string)


find_other_paragraph()
