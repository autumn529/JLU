import numpy as np
import time
import requests
from bs4 import BeautifulSoup


def clean_str(p):
  return p.encode().decode("unicode-escape").encode("latin1").decode("utf-8")

def get_page_obs(page):
    # find all paragraphs
    paragraphs = page.split("\n")
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    # find all sentence
    sentences = []
    for p in paragraphs:
      sentences += p.split('. ')
    sentences = [s.strip() + '.' for s in sentences if s.strip()]
    return ' '.join(sentences[:5])

def search_step(entity):
    entity_ = entity.replace(" ", "+")
    search_url = f"https://en.wikipedia.org/w/index.php?search={entity_}"
    
    response_text = ''
    while response_text == '':
        try:
            requests.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            s_get = s.get(search_url, verify = False, timeout=(5,5))
            response_text = s_get.text
            s_get.close()
            break
        except:
            time.sleep(5)
            continue
    

    soup = BeautifulSoup(response_text, features="html.parser")
    result_divs = soup.find_all("div", {"class": "mw-search-result-heading"})
    
    if result_divs:  # mismatch
        result_titles = [clean_str(div.get_text().strip()) for div in result_divs]
        obs = f"Could not find {entity}. Similar: {result_titles[:5]}."
    else:
      page = [p.get_text().strip() for p in soup.find_all("p") + soup.find_all("ul")]
      if any("may refer to:" in p for p in page):
          obs = search_step("[" + entity + "]")
      else:
          page_re = ""
          for p in page:
            if len(p.split(" ")) > 2:
              page_re += clean_str(p)
              if not p.endswith("\n"):
                page_re += "\n"
          obs = get_page_obs(page_re)
    return obs


def clean_data(output):
    output = output.split('.')[0].strip()
    output = output.replace('\\u00e9','e')
    output = output.replace('\u00e1','a')
    output = output.replace(' and ',', ')
    output = output.replace('The ', '')
    output = output.replace('the ', '')
    output = output.replace('A ', '')
    output = output.replace(' two', '')
    output = output.replace('Two', '')
    output = output.replace('Two ', '')
    output = output.replace('Three ', '')
    output = output.replace(' a ', '')
    output = output.replace('An ', '')
    output = output.replace(' an ', '')
    output = output.replace('\"','')
    output = output.split(', ')[0]
    char_num = len(output.split(' '))
    if char_num > 5:
        output = ''
    return output.lower()



def search_wiki_knowledge(output):

    if 'Thought 2' in output:
        output = output.split('Thought 2')[0].strip()

    if 'Finish:' in output:
        entity = output.split('Finish:')[1]
        entity = clean_data(entity)

        if entity == '':
            knowledge = ''
        else:
            knowledge = search_step(entity)
            if 'Could not find' in knowledge:
                knowledge = ''
    else:
        entity = ''
        knowledge = ''
    

    return entity, knowledge

    