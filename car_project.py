import streamlit as st

# 1. إعداد الصفحة والتنسيق الجمالي
st.set_page_config(page_title="مستشارك الذكي للسيارات", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f7f9fc; }
    .car-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 8px solid #1E3A5F;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .car-header { color: #1E3A5F; font-size: 22px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. الجملة الافتتاحية (مثل مطعم الأستاذ)
st.title("🚗 ماذا تريد أن تقود اليوم؟")
st.write("تصفح مجموعتنا المختارة من أفضل سيارات 2025")

# 3. إضافة محرك البحث
search_query = st.text_input("🔍 ابحث عن سيارتك المفضلة هنا:", "")

# 4. قاعدة بيانات السيارات (يمكنك تعديل الأسماء والروابط هنا بسهولة)
cars_list = [
    {"name": "تويوتا كامري 2025", "cat": "سيدان", "price": "131,000 ريال", "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=500", "specs": ["محرك هايبرد", "استهلاك ممتاز"]},
    {"name": "نيسان باترول 2025", "cat": "SUV", "price": "350,000 ريال", "img": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=500", "specs": ["قوة هائلة", "فخامة داخلية"]},
    {"name": "تسla موديل 3", "cat": "كهربائية", "price": "190,000 ريال", "img": "https://images.unsplash.com/photo-1560958089-b8a1929cea89?w=500", "specs": ["تسارع كهربائي", "هدوء تام"]},
    {"name": "لوسيد أير", "cat": "كهربائية", "price": "320,000 ريال", "img": "https://images.unsplash.com/photo-1617788130012-05ba7feee178?w=500", "specs": ["صناعة سعودية", "مدى شحن طويل"]}
]

# دالة لعرض البطاقات
def display_car_card(car):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(car['img'], use_container_width=True)
    with c2:
        st.markdown(f"<div class='car-header'>{car['name']}</div>", unsafe_allow_html=True)
        st.write(f"**السعر:** {car['price']}")
        with st.expander("🔍 عرض التفاصيل الفنية"):
            for s in car['specs']:
                st.write(f"• {s}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. منطق العرض (بحث أو تبويبات)
if search_query:
    results = [c for c in cars_list if search_query.lower() in c['name'].lower()]
    if results:
        for car in results:
            display_car_card(car)
    else:
        st.error("لم يتم العثور على نتائج للبحث.")
else:
    # عرض التبويبات إذا لم يكن هناك بحث
    t1, t2, t3 = st.tabs(["🏙️ سيدان", "🏜️ SUV", "⚡ كهربائية"])
    
    with t1:
        for car in [c for c in cars_list if c['cat'] == "سيدان"]:
            display_car_card(car)
    with t2:
        for car in [c for c in cars_list if c['cat'] == "SUV"]:
            display_car_card(car)
    with t3:
        for car in [c for c in cars_list if c['cat'] == "كهربائية"]:
            display_car_card(car)

# تم مسح النصيحة وكلمة "عميقة" كما طلبت
