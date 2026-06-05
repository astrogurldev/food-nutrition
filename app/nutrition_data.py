# Database nutrisi per 100g
# Format: "nama_makanan": {kalori, protein, karbo, lemak, diet_label, rekomendasi}

NUTRITION_DB = {
    "pizza": {
        "calories": 266, "protein": 11, "carbs": 33, "fat": 10,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Batasi konsumsi. Pilih topping sayuran dan kurangi keju."
    },
    "hamburger": {
        "calories": 295, "protein": 17, "carbs": 24, "fat": 14,
        "diet_label": "❌ Hindari",
        "recommendation": "Tinggi kalori dan lemak. Ganti dengan protein lean seperti ayam panggang."
    },
    "sushi": {
        "calories": 143, "protein": 6, "carbs": 28, "fat": 1,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Pilihan diet yang baik! Rendah lemak dan kaya protein."
    },
    "fried_rice": {
        "calories": 163, "protein": 3, "carbs": 22, "fat": 7,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Kurangi minyak, tambah sayuran, gunakan nasi merah untuk versi lebih sehat."
    },
    "salad": {
        "calories": 20, "protein": 1, "carbs": 3, "fat": 0,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Sangat baik untuk diet! Kaya serat dan rendah kalori."
    },
    "steak": {
        "calories": 271, "protein": 26, "carbs": 0, "fat": 18,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Kaya protein tapi tinggi lemak jenuh. Pilih potongan lean seperti sirloin."
    },
    "ice_cream": {
        "calories": 207, "protein": 3, "carbs": 24, "fat": 11,
        "diet_label": "❌ Hindari",
        "recommendation": "Tinggi gula dan lemak. Ganti dengan yogurt rendah lemak atau buah beku."
    },
    "ramen": {
        "calories": 436, "protein": 18, "carbs": 60, "fat": 14,
        "diet_label": "❌ Hindari",
        "recommendation": "Sangat tinggi sodium dan kalori. Konsumsi sesekali saja."
    },
    "grilled_salmon": {
        "calories": 208, "protein": 28, "carbs": 0, "fat": 10,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Superfood! Kaya omega-3 dan protein tinggi. Sangat direkomendasikan."
    },
    "french_fries": {
        "calories": 312, "protein": 3, "carbs": 41, "fat": 15,
        "diet_label": "❌ Hindari",
        "recommendation": "Tinggi lemak trans dan kalori. Ganti dengan ubi panggang."
    },
    "chicken_wings": {
        "calories": 203, "protein": 18, "carbs": 0, "fat": 14,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Pilih versi panggang bukan goreng untuk versi lebih sehat."
    },
    "waffles": {
        "calories": 291, "protein": 8, "carbs": 37, "fat": 12,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Kurangi sirup, tambah buah segar sebagai topping."
    },
    "pancakes": {
        "calories": 227, "protein": 6, "carbs": 28, "fat": 10,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Pilih versi whole wheat dan kurangi gula."
    },
    "omelette": {
        "calories": 154, "protein": 11, "carbs": 0, "fat": 12,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Sarapan yang sempurna! Tambah sayuran untuk nutrisi lebih lengkap."
    },
    "caesar_salad": {
        "calories": 90, "protein": 4, "carbs": 8, "fat": 5,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Pilihan sehat! Kurangi dressing untuk kalori lebih rendah."
    },
    "hot_dog": {
        "calories": 290, "protein": 10, "carbs": 24, "fat": 17,
        "diet_label": "❌ Hindari",
        "recommendation": "Tinggi sodium dan lemak jenuh. Konsumsi sesekali saja."
    },
    "tacos": {
        "calories": 226, "protein": 9, "carbs": 20, "fat": 12,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Pilih tortilla whole wheat dan topping sayuran lebih banyak."
    },
    "soup": {
        "calories": 71, "protein": 4, "carbs": 9, "fat": 2,
        "diet_label": "✅ Diet Friendly",
        "recommendation": "Pilihan diet yang baik! Kaya nutrisi dan mengenyangkan."
    },
    "chocolate_cake": {
        "calories": 371, "protein": 5, "carbs": 52, "fat": 16,
        "diet_label": "❌ Hindari",
        "recommendation": "Tinggi gula dan kalori. Nikmati dalam porsi kecil sesekali."
    },
    "apple_pie": {
        "calories": 237, "protein": 2, "carbs": 34, "fat": 11,
        "diet_label": "⚠️ Moderate",
        "recommendation": "Kurangi porsi dan nikmati sesekali sebagai dessert."
    },
}

DEFAULT_NUTRITION = {
    "calories": 150, "protein": 5, "carbs": 20, "fat": 5,
    "diet_label": "⚠️ Moderate",
    "recommendation": "Data nutrisi spesifik tidak tersedia. Konsumsi dalam porsi wajar."
}

def get_nutrition(food_name):
    # Normalize nama makanan
    food_key = food_name.lower().replace(" ", "_").replace("-", "_")
    
    # Cari di database
    for key in NUTRITION_DB:
        if key in food_key or food_key in key:
            return NUTRITION_DB[key]
    
    return DEFAULT_NUTRITION