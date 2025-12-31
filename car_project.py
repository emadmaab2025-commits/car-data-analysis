import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مستشارك الذكي للسيارات", layout="centered")

# 2. إضافة لمسات CSS الجمالية
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق */
    .stApp {
        background-color: #f4f7f6;
    }
    
    /* تصميم بطاقة السيارة */
    .car-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1E3A5F; /* خط جانبي ملون */
    }
    
    /* تنسيق اسم السيارة */
    .car-name {
        color: #1E3A5F;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    /* تنسيق السعر */
    .price-style {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 5px 15px;
        border-radius: 10px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_input=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #1E3A5F;'>🏎️ مستشارك الذكي للسيارات</h1>", unsafe_allow_input=True)
st.write("---")

# قاعدة البيانات
cars = [
    {
        "name": "تويوتا كامري 2025",
        "img": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=500",
        "price": "131,000 ريال",
        "specs": {"المحرك": "2.5L هايبرد", "الاستهلاك": "26.2 كم/لتر", "القوة": "225 حصان"}
    },
    {
        "name": "نيسان باترول 2025",
        "img": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=500",
        "price": "350,000 ريال",
        "specs": {"المحرك": "3.5L توين توربو", "الاستهلاك": "10.2 كم/لتر", "القوة": "425 حصان"}
    }
]

# عرض السيارات باستخدام CSS
for car in cars:
    # بداية الحاوية الجمالية
    st.markdown(f"""
        <div class="car-card">
            <div class="car-name">{car['name']}</div>
            <div class="price-style">{car['price']}</div>
        </div>
    """, unsafe_allow_input=True)
    
    # عرض الصورة والزر
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(car['img'], use_container_width=True)
    
    with col2:
        # زر التفاصيل (يظهر فقط عند الضغط)
        with st.expander("🛠️ عرض المواصفات الفنية العميقة"):
            for key, value in car['specs'].items():
                st.write(f"🔹 {key}: {value}")
            st.success("هذه السيارة مطابقة لمعايير كفاءة الطاقة السعودية.")
    
    st.write("") # مسافة بين السيارات
