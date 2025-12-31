import streamlit as st

# 1. إعداد الصفحة والتنسيق الجمالي
st.set_page_config(page_title="فخامة المركبات 2025", layout="centered")

# تنسيق CSS احترافي للاسم والبطاقات
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    
    .store-name {
        font-size: 50px;
        font-weight: bold;
        background: -webkit-linear-gradient(#bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
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
    {"name": "تويوتا كامري 2025", "cat": "🏙️ سيدان", "price": "131,000 ريال", "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=600", "specs": ["اعتمادية عالية", "نظام هايبرد موفر"]},
    {"name": "مرسيدس S-Class", "cat": "🏙️ سيدان", "price": "650,000 ريال", "img": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=600", "specs": ["قمة الرفاهية الألمانية", "نظام MBUX الذكي"]},
    
    # فئة SUV
    {"name": "لكزس LX 600", "cat": "🏜️ SUV", "price": "580,000 ريال", "img": "https://images.unsplash.com/photo-1635322966219-b75ed372eb01?w=600", "specs": ["فخامة يابانية مطلقة", "قدرات دفع رباعي هائلة"]},
    {"name": "مرسيدس G-Class", "cat": "🏜️ SUV", "price": "850,000 ريال", "img": "https://images.unsplash.com/photo-1520031441872-265e4ff70366?w=600", "specs": ["تصميم أيقوني خالد", "أداء جبار في الطرق الوعرة"]},
    
    # فئة الكهربائية
    {"name": "لوسيد أير (Lucid Air)", "cat": "⚡ كهربائية", "price": "320,000 ريال", "img": "https://images.unsplash.com/photo-1617788130012-05ba7feee178?w=600", "specs": ["صناعة سعودية فاخرة", "مدى شحن يصل لـ 830 كم"]},
    {"name": "تسلا موديل X", "cat": "⚡ كهربائية", "price": "410,000 ريال", "img": "https://images.unsplash.com/photo-1571127236794-81c0bbfe1ce3?w=600", "specs": ["أبواب جناح الصقر", "تسارع مذهل ونظام قيادة ذاتي"]},
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
