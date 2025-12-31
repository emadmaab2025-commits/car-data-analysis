import streamlit as st

# 1. إعداد الصفحة والتنسيق الجمالي
st.set_page_config(page_title="فخامة المركبات 2025", layout="centered")

# تنسيق CSS احترافي للاسم والبطاقات
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    
  .store-name {
        font-family: 'Georgia', serif;
        font-size: 50px;
        color: #e63946; /* أحمر مطاعم كلاسيكي */
        text-align: center;
        border-bottom: 3px double #1d3557;
        margin-bottom: 10px;
        padding-bottom: 5px;
        font-variant: small-caps;
    }
    
    .menu-subtitle {
        text-align: center;
        font-style: italic;
        color: #457b9d;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .car-card {
        background: #fffdf5; /* ورق قديم (Creamy paper) */
        padding: 20px;
        border: 2px solid #1d3557;
        border-radius: 0px; /* زوايا حادة كأنه قائمة ورقية */
        box-shadow: 5px 5px 0px #a8dadc;
        margin-bottom: 25px;
    }

    .car-header {
        color: #1d3557;
        font-size: 26px;
        font-family: 'Times New Roman', serif;
        border-bottom: 1px dashed #e63946;
    }
    
    .car-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 10px solid #bf953f;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .car-header { color: #1E3A5F; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. اسم المتجر والسؤال
st.markdown('<div class="store-name">فخامة المركبات | Luxury Cars</div>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>أيُّ تحفةٍ هندسية سترافقك في رحلتك القادمة؟</h3>", unsafe_allow_html=True)
st.write("---")

# 3. شريط البحث
search_query = st.text_input("🔍 ابحث عن السيارة التي تليق بك:", "")

# 4. قاعدة البيانات الموسعة (سيارتان لكل تصنيف)
cars_list = [
    # فئة السيدان
   {
        "name": "تويوتا كامري 2025", 
        "cat": "🏙️ سيدان", 
        "price": "131,000 ريال", 
        "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=600", 
        "specs": [
            "محرك هايبرد 2.5 لتر بقوة 225 حصان",
            "استهلاك وقود فائق يصل لـ 26.2 كم/لتر",
            "نظام Toyota Safety Sense 3.0 للأمان",
            "شاشة لمس 12.3 بوصة مع Apple CarPlay"
        ]
    },
    {
        "name": "مرسيدس S-Class 2025", 
        "cat": "🏙️ سيدان", 
        "price": "650,000 ريال", 
        "img": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=600", 
        "specs": [
            "نظام القيادة الذاتية من المستوى الثالث",
            "شاشة OLED مركزية ونظام MBUX الذكي",
            "إضاءة محيطية تفاعلية بـ 64 لوناً",
            "مقاعد جلدية مع خاصية التدليك والتدفئة"
        ]
    },
    
    # فئة SUV
   {
        "name": "لكزس LX 600", 
        "cat": "🏜️ SUV", 
        "price": "580,000 ريال", 
        "img": "https://ymimg1.b8cdn.com/resized/car_model/12688/pictures/15980218/webp_listing_main_2022_Lexux_LX_600_Exterior_01.webp", 
        "specs": [
            "محرك V6 توين توربو سعة 3.5 لتر",
            "نظام زحف متطور للطرق الوعرة",
            "داخلية من جلد سيمي أنيلين الفاخر",
            "نظام صوتي مارك ليفينسون بـ 25 سماعة"
        ]
    },
  {
        "name": "مرسيدس G-Class", 
        "cat": "🏜️ SUV", 
        "price": "850,000 ريال", 
        "img": "https://images.unsplash.com/photo-1520031441872-265e4ff70366?w=600", 
        "specs": [
            "محرك V8 يدوي الصنع بقوة 585 حصان",
            "3 أقفال تفاضلية (Diff-Lock) لأصعب التضاريس",
            "شاشات عرض مزدوجة مقاس 12.3 بوصة",
            "تصميم كلاسيكي يجمع بين القوة والرفاهية"
        ]
    },
    
    # فئة الكهربائية
    {
        "name": "لوسيد أير (Lucid Air)", 
        "cat": "⚡ كهربائية", 
        "price": "320,000 ريال", 
        "img": "https://cdn.motor1.com/images/mgl/6ZopYG/s1/armored-lucid-air-sapphire.jpg", 
        "specs": [
            "أول سيارة كهربائية فاخرة تصنع في السعودية",
            "مدى شحن استثنائي يصل إلى 830 كم",
            "نظام شحن فائق السرعة (300 كم في 15 دقيقة)",
            "شاشة عرض زجاجية منحنية مقاس 34 بوصة بدقة 5K"
        ]
    },
    {
        "name": "تسلا موديل X", 
        "cat": "⚡ كهربائية", 
        "price": "410,000 ريال", 
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWoCd8xofzsyzbEEb84BbamoUQCjcjdKVpBQ&s", 
        "specs": [
            "أبواب (جناح الصقر) تفتح للأعلى كهربائياً",
            "تسارع مذهل من 0 إلى 100 كم/س في 2.6 ثانية",
            "نظام القيادة الذاتية الكاملة (Autopilot)",
            "أكبر زجاج أمامي بانورامي في العالم"
        ]
    },
]

# دالة العرض
def display_car_card(car):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(car['img'], use_container_width=True)
    with c2:
        st.markdown(f"<div class='car-header'>{car['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"**السعر التقديري:** :green[{car['price']}]")
        with st.expander("🛠️ التفاصيل الفنية"):
            for s in car['specs']:
                st.write(f"• {s}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. منطق العرض
if search_query:
    results = [c for c in cars_list if search_query.lower() in c['name'].lower()]
    for car in results: display_car_card(car)
else:
    t1, t2, t3 = st.tabs(["🏙️ سيدان الفخامة", "🏜️ SUV القوة", "⚡ كهربائيات المستقبل"])
    with t1:
        for car in [c for c in cars_list if "سيدان" in c['cat']]: display_car_card(car)
    with t2:
        for car in [c for c in cars_list if "SUV" in c['cat']]: display_car_card(car)
    with t3:
        for car in [c for c in cars_list if "كهربائية" in c['cat']]: display_car_card(car)




