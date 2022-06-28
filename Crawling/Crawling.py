from selenium import webdriver


class Country:
    # 지시사항 1번을 작성하세요.
    def __init__(self,name,capital,population,area):
        self.name = name
        self.capital = capital
        self.population = int(population)
        
        if 'E' in area : 
            a, b = area.split('E') # a = '1.4', b = '7'
            self.area = float(a) * (10 ** int(b))
        else:
            self.area = float(area)


with webdriver.Firefox() as driver:
    driver.get("https://www.scrapethissite.com/pages/simple/")

    # 지시사항 2번을 작성하세요.
    country_list = []
    div_list = driver.find_elements_by_class_name('country')

    for div in div_list:
        name = div.find_elements_by_tag_name('h3').text
        capital = div.find_elements_by_class_name('country-capital').text
        population = div.find_elements_by_class_name('country-population').text
        area = div.find_elements_by_class_name('country-area').text
        country = Country(name,capital,population,area)

    country_list.append(country)
    # 지시사항 3번을 작성하세요.
    capital_list = []

    for country in country_list:
        capital_list.append(country.capital)
    
    capital_list.sort()
    print(capital_list[29])


    # 지시사항 4번을 작성하세요.
    pop_list = []
    
    for country in country_list:
        pop_list.append(country.population)
    
    print(sum(pop_list))
