# 🍽️ Dinner Recipe Scraper: Allrecipes.com & BBCGoodFood.com
This web scraper project collects dinner recipes from two websites: [allrecipes.com](https://www.allrecipes.com/recipes/17562/dinner/) and [bbcgoodfood.com](https://www.bbcgoodfood.com/recipes/collection/easy-dinner-recipes)

---

## 📄 Data Fields Collected (JSON)
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

```text
## 📁 Project Structure
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
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements
- Python 3.11

### Python Libraries
Install dependencies using:
```bash
pip install -r requirements.txt
```
---

## 🚀 Running the Scrapers
To run the Allrecipes scraper:
     python3.11 -m src.scraper.allrecipes_scraper
To run the BBC Good Food scraper:
     python3.11 -m src.scraper.bbcgoodfood_scraper

Note: A `main.py` file was considered for simplified execution, but the decision was made to run scrapers individually.

 
