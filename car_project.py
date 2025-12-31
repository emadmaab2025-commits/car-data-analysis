import streamlit as st
import pandas as pd

# 1. إعدادات الهوية البصرية (مثل تطبيق الأستاذ)
st.set_page_config(page_title="مستشارك للسيارات 2025", page_icon="🏎️", layout="wide")

# تصميم الواجهة باستخدام CSS
st.markdown("""
    <style>
    .main { background-color: #fdfdfd; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    .category-header {
        background-color: #1e3a5f;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
    }
    .price-tag { color: #e63946; font-weight: bold; font-size: 20px; }
    .spec-box {
        background-color: #f1f3f5;
        padding: 10px;
        border-radius: 10px;
        border-right: 5px solid #2e7d32;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_input=True)

# 2. العنوان وشريط البحث
st.title("🛡️ مستشارك الذكي للسيارات")
st.write("اكتشف خيارك المثالي بناءً على الميزانية، الاستهلاك، والقيمة التشغيلية.")

search_query = st.text_input("🔍 ابحث عن طراز معين أو فئة...", placeholder="مثال: هايبرد، عائلية، اقتصادية")

# 3. قاعدة البيانات العميقة (مقسمة لفئات)
car_data = {
    "سيدان اقتصادية (شعبي)": [
        {
            "name": "تويوتا كامري LE 2025",
            "price": 128000,
            "efficiency": "26.2 كم/لتر",
            "maintenance": "منخفضة جداً",
            "depreciation": "12%",
            "tags": ["هايبرد", "اعتمادية عالية"],
            "image": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=400",
            "desc": "الخيار الأول للعمل الشاق والكد، توفر في الوقود بشكل استثنائي."
        }
    ],
    "سيارات عائلية (أطباق رئيسية)": [
        {
            "name": "هيونداي باليسيد 2025",
            "price": 185000,
            "efficiency": "11.1 كم/لتر",
            "maintenance": "متوسطة",
            "depreciation": "22%",
            "tags": ["V6", "8 مقاعد"],
            "image": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=400",
            "desc": "رفاهية عائلية متكاملة مع تقنيات أمان متطورة لكل أفراد الأسرة."
        }
    ]
}

# 4. منطق العرض التفصيلي
for category, cars in car_data.items():
    st.markdown(f"<div class='category-header'><h3>{category}</h3></div>", unsafe_allow_input=True)
    
    # توزيع السيارات في أعمدة (Columns) مثل شبكة الوصفات
    cols = st.columns(2)
    for idx, car in enumerate(cars):
        with cols[idx % 2]:
            st.image(car["image"], use_container_width=True)
            st.markdown(f"### {car['name']}")
            
            # عرض التاجات (Tags)
            tag_html = "".join([f"<span style='background:#d4edda; color:#155724; padding:2px 8px; border-radius:10px; margin-left:5px; font-size:12px;'>{t}</span>" for t in car['tags']])
            st.markdown(tag_html, unsafe_allow_input=True)
            
            st.markdown(f"<p class='price-tag'>{car['price']:,} ريال</p>", unsafe_allow_input=True)
            
            # تفاصيل "عميقة" تظهر في صناديق
            st.markdown(f"""
            <div class='spec-box'>⛽ <b>كفاءة الطاقة:</b> {car['efficiency']}</div>
            <div class='spec-box'>🛠️ <b>تكلفة الصيانة:</b> {car['maintenance']}</div>
            <div class='spec-box'>📉 <b>هبوط القيمة (3 سنوات):</b> {car['depreciation']}</div>
            """, unsafe_allow_input=True)
            
            with st.expander("📝 عرض التحليل الفني"):
                st.write(car["desc"])
                st.info("توصية: هذا الخيار ممتاز لمن يقطع مسافة تزيد عن 30 ألف كم سنوياً.")

# 5. القائمة الجانبية التفاعلية (Sidebar)
with st.sidebar:
    st.header("⚙️ معايير التصفية")
    budget = st.slider("حدد ميزانيتك القصوى (ريال)", 50000, 300000, 150000)
    fuel_type = st.multiselect("نوع المحرك", ["بنزين", "هايبرد", "كهرباء"], default=["بنزين", "هايبرد"])
    
    st.markdown("---")
    st.write("📩 **هل تحتاج تقرير PDF؟**")
    if st.button("تجهيز التقرير"):
        st.toast("يتم إعداد ملف التحليل المالي...")
