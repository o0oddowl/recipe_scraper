import json
import time
import random
import re

import fake_useragent
import requests
from bs4 import BeautifulSoup

from utils import save_data, param


def get_urls():
    urls = []
    for page in range(1,8):
        soup = param(f"https://www.bbcgoodfood.com/api/editorial/posts/editorial/editorialList/recipes~collection~easy-dinner-recipes/items/true?page={page}", True)
        url_range = len(soup["items"])
        for url in range(1, url_range): 
            urls.append(soup["items"][url]["url"])
    return urls


def scraper():
    urls = get_urls()
    
    recipe_list = []
    for process, url in enumerate(urls):
        print(f" Process:{process+1}/{len(urls)}", end="\r")
        try:
            soup = param(url)
            title = soup.find("h1").text
            
            cook_details = soup.find_all("div", class_="recipe-cook-and-prep-details__item")
            if len(cook_details) > 3:
                servings = cook_details[0].text.split(" ")[1]
                prep_time = cook_details[2].text.replace("\xa0", " ").split(" ")[1]
                if cook_details[3].text.replace("\xa0", " ").split(" ")[2] in ["hr", "hrs"]:
                    cook_time = int(cook_details[3].text.replace("\xa0", " ").split(" ")[1]) * 60
                else:
                    cook_time = cook_details[3].text.replace("\xa0", " ").split(" ")[1]
            else:
                servings = cook_details[0].text.split(" ")[1]
                try:
                    prep_time = cook_details[1].text.replace("\xa0", " ").split(" ")[1]
                except:
                    prep_time = 0
                if cook_details[2].text.replace("\xa0", " ").split(" ")[1] in ["hr", "hrs"]:
                    cook_time = int(cook_details[2].text.replace("\xa0", " ").split(" ")[1]) * 60
                else:
                    cook_time = cook_details[2].text.replace("\xa0", " ").split(" ")[1]
          
            nutrition_list = soup.find_all("li", class_="nutrition-list__item")
            nutritions = {}
            for nutrition in nutrition_list:
                nutrition_key = nutrition.find("span").text
                nutrition_val = re.search (r"\D+(\d+(?:\.\d+)?)", nutrition.text).group(1)
                if nutrition_key != "kcal":
                    nutrition_key =  nutrition_key + " (g)"
                nutritions[nutrition_key] = nutrition_val
                
            ingredient_list = soup.find("section", id="ingredients-list").find_all("li", class_=["ingredients-list__item", "list-item"])
            ingredients = []
            for ingredient in ingredient_list:
                ingredients.append(ingredient.text)
            
            direction_list = soup.find_all("li", class_="method-steps__list-item")
            directions = {}
            for direction in direction_list:
                direction_key = direction.find("h3").text
                direction_val = direction.find("p").text
                directions[direction_key] = direction_val

            rating = soup.find("div", class_=["rating", "rating--inline"]).find("span", class_="rating__count-text body-copy-small").text.split(" ")[0]
            recipe_list.append({
                "title":title,
                "servings":servings,
                "prep_time": prep_time,
                "cook_time": cook_time,
                "nutritions": nutritions,
                "ingredients": ingredients,
                "directions": directions,
                "rating": rating,
                "url": url
            })
        except Exception as e:
            print("")
            print(e, url)
    save_data("../data/bbsgoodfood_data.json", data=recipe_list)
    print("")

def main():
    scraper()

if __name__ == "__main__":
    main()
