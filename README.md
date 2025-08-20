# 🍽️ Dinner Recipe Scraper: Allrecipes.com & BBCGoodFood.com
This web scraper project collects dinner recipes from two websites: [allrecipes.com](https://www.allrecipes.com/recipes/17562/dinner/) and [bbcgoodfood.com](https://www.bbcgoodfood.com/recipes/collection/easy-dinner-recipes)

---

## 📄 Data Fields Collected (JSON):
- **title** – name of the dish
- **servings** – number of servings
- **prep_time** – preparation time
- **cook_time** – cooking time
- **nutritions** – nutritional information
- **ingredients** – list of ingredients
- **directions** – cooking instructions
- **rating** – recipe rating
- **url** – link to the recipe

---

## 📁 Project Structure:
```text
recipe_scraper/
│
├── src/
│   ├── scraper/
│   │   ├── allrecipes_scraper.py
│   │   └── bbcgoodfood_scraper.py
│   └── utils.py
│
├── data/
│   ├── allrecipes_data.json
│   └── bbcgoodfood_data.json
│
└── requirements.txt
```

---

## Data Output(JSON):
```bash
{
    "title": "Grilled Cheese Sandwich",
    "servings": "2",
    "prep_time": "5",
    "cook_time": "10",
    "nutritions": {
        "kcal": "400",
        "fat (g)": "28",
        "carbs (g)": "26",
        "protein (g)": "11"
    },
    "ingredients": [
        "4 slices white bread",
        "3 tablespoons butter, divided",
        "2 slices Cheddar cheese"
    ],
    "directions": {
        "step 1": "Gather all ingredients.",
        "step 2": "Preheat a nonstick skillet over medium heat. Generously butter one side of a slice of bread.",
        "step 3": "Place bread butter-side down in the hot skillet; add 1 slice of cheese.",
        "step 4": "Butter a second slice of bread on one side and place butter-side up on top of cheese.",
        "step 5": "Cook until lightly browned on one side; flip over and continue cooking until cheese is melted.",
        "step 6": "Repeat with remaining 2 slices of bread, butter, and slice of cheese. Serve and enjoy!"
    },
    "rating": "899",
    "url": "https://www.allrecipes.com/recipe/23891/grilled-cheese-sandwich/"
}
```

---

## ⚙️ Requirements:
- Python 3.11

### Python Libraries
Install dependencies using:
```bash
pip install -r requirements.txt
```
---

## 🚀 Running the Scrapers:
To run the Allrecipes scraper:
```bash
python3.11 -m src.scraper.allrecipes_scraper
```
To run the BBC Good Food scraper:
```bash
python3.11 -m src.scraper.bbcgoodfood_scraper
```
---
Note: A `main.py` file was considered for simplified execution, but the decision was made to run scrapers individually.

 
