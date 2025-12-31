import streamlit as st

# 1. إعداد الصفحة والتنسيق الجمالي
st.set_page_config(page_title="فخامة المركبات 2025", layout="centered")

# تنسيق CSS احترافي للاسم والبطاقات
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    
    /* تنسيق اسم المتجر الذهبي */
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
        border-right: 10px solid #bf953f; /* خط ذهبي */
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .car-header { color: #1E3A5F; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. اسم المتجر والسؤال الجديد
st.markdown('<div class="store-name">فخامة المركبات | Luxury Cars</div>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>أيُّ تحفةٍ هندسية سترافقك في رحلتك القادمة؟</h3>", unsafe_allow_html=True)
st.write("---")

# 3. شريط البحث
search_query = st.text_input("🔍 ابحث عن السيارة التي تليق بك:", "")

# 4. قاعدة البيانات (تمت إضافة لوسيد وسيارات فارهة أخرى)
cars_list = [
    {"name": "لوسيد أير (Lucid Air)", "cat": "⚡ كهربائية", "price": "320,000 ريال", "img": "https://images.unsplash.com/photo-1617788130012-05ba7feee178?w=600", "specs": ["صناعة سعودية فارهة", "مدى شحن يصل لـ 830 كم", "أسرع شحن في العالم"]},
    {"name": "لكزس LX 600", "cat": "🏜️ SUV", "price": "580,000 ريال", "img": "https://images.unsplash.com/photo-1635322966219-b75ed372eb01?w=600", "specs": ["محرك V6 توين توربو", "فخامة يابانية مطلقة", "قدرات هائلة في الرمال"]},
    {"name": "مرسيدس G-Class", "cat": "🏜️ SUV", "price": "850,000 ريال", "img": "https://images.unsplash.com/photo-1520031441872-265e4ff70366?w=600", "specs": ["أيقونة الدفع الرباعي", "محرك V8 جبار", "تصميم كلاسيكي خالد"]},
    {"name": "تويوتا كامري 2025", "cat": "🏙️ سيدان", "price": "131,000 ريال", "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=600", "specs": ["اعتمادية لا تضاهى", "نظام هايبرد موفر"]},
    {"name": "بي إم دبليو i7", "cat": "⚡ كهربائية", "price": "620,000 ريال", "img": "https://images.unsplash.com/photo-1669023414166-a4cc7c0fe1f5?w=600", "specs": ["سينما خلفية 31 بوصة", "فخامة كهربائية ألمانية"]},
]

# دالة العرض
def display_car_card(car):
    st.markdown('<div class="car-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(car['img'], use_container_width=True)
    with c2:
        st.markdown(f"<div class='car-header'>{car['name']}</div>", unsafe_allow_html=True)
        st.write(f"**الفئة:** {car['cat']}")
        st.markdown(f"**السعر التقديري:** :green[{car['price']}]")
        with st.expander("🛠️ المواصفات الفنية"):
            for s in car['specs']:
                st.write(f"• {s}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. منطق العرض والتبويبات
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
