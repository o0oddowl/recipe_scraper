import json
import random
import time

import fake_useragent
import requests
from bs4 import BeautifulSoup

from utils import save_data, param


def get_url():
    soup = param("https://www.allrecipes.com/recipes/17562/dinner/")
    url_category_list = soup.find("ul", id="mntl-taxonomy-nodes__list_1-0").find_all("li")

    urls_category = []
    for url in url_category_list:
        urls_category.append(url.find("a", href=True)["href"])

    urls_recipes = []
    for url in urls_category:
        soup = param(url)
        recipes_url_list = soup.find_all("a", class_=["comp", "imntl-card-list-items", "mntl-universal-card", "mntl-document-card", "mntl-card"], href=True)
        for recipe_url in recipes_url_list:
            urls_recipes.append(recipe_url["href"])
    urls_recipes = list(dict.fromkeys(urls_recipes))
    return urls_recipes       

def scraper():
    urls = get_url()
    
    recipe_list = []
    for process, url in enumerate(urls):
        print(f" Progress:{process+1}/{len(urls)}", end="\r")
        try:
            soup = param(url)
            title = soup.find("h1").text.strip()

            cook_details = soup.find_all("div", class_="mm-recipes-details__value")
            if len(cook_details) >= 4:
                servings = cook_details[3].text.split(" ")[0]
            elif len(cook_details) == 2:
                servings = cook_details[0].text.split(" ")[0]
            else:      
                servings = cook_details[2].text.split(" ")[0]
            prep_time = cook_details[0].text.split(" ")[0]
            if cook_details[1].text.split(" ")[1] != "mins":
                cook_time = int(cook_details[1].text.strip().split(" ")[0]) * 60
            else:
                cook_time = cook_details[1].text.strip().split(" ")[0]
            
            nutrition_list = soup.find_all("tr", class_="mm-recipes-nutrition-facts-summary__table-row")
            nutritions = {}
            for nutrition in nutrition_list:
                nutrition = nutrition.text.strip().split("\n")
                nutrition_key = nutrition[1]
                nutrition_val = nutrition[0]
                if nutrition_val[-2] == "g":
                    nutrition_val = nutrition_val[:-2]
                if nutrition_key == "Calories":
                    nutritions["kcal"] = nutrition_val
                else:
                    nutrition_key = nutrition_key.lower() + " (g)"
                    nutritions[nutrition_key] = nutrition_val 
            
            ingredient_list = soup.find_all("li", class_="mm-recipes-structured-ingredients__list-item")
            ingredients = []
            for ingredient in ingredient_list:
                ingredients.append(ingredient.text.strip())
            
            try:
                direction_list = soup.find("ol", class_=["comp", "mntl-sc-block", "mntl-sc-block-startgroup", "mntl-sc-block-group--OL"]).find_all("li")
                directions = {}
                for step, direction in enumerate(direction_list):
                    direction_key = f"step {step+1}"
                    direction_val = direction.find("p").text.strip()
                    directions[direction_key] = direction_val
            except:
                direction_list = soup.find_all("ol", class_=["comp", "mntl-sc-block", "mntl-sc-block-startgroup", "mntl-sc-block-group--OL"])[1].find_all("li")
                directions = {}
                for step, direction in enumerate(direction_list):
                    direction_key = f"step {step+1}"
                    direction_val = direction.find("p").text.strip()
                    directions[direction_key] = direction_val
            try:
                rating = soup.find("div", id="mm-recipes-review-bar__rating-count_1-0").text[1:-1]
            except: 
                rating = 0
            recipe_list.append({
                "title":title,
                "servings":servings,
                "prep_time":prep_time,
                "cook_time":cook_time,
                "nutritions":nutritions,
                "ingredients":ingredients,
                "directions":directions,
                "rating":rating,
                "url":url,
            })
        except Exception as e:
            print("")
            print(url, e)

    save_data("../data/allrecipes_data.json", data=recipe_list)
    print("") 


def main():
    scraper()

if __name__ in "__main__":
    main()









