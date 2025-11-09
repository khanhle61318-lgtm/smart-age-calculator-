import streamlit as st
import time

# -------------------------------
st.markdown("## 🧠 Máy tính tuổi thông minh")
st.markdown("---")

# -------------------------------
def loading(message="Đang xử lý...", t1=2, t2=1):
    st.info(message)
    time.sleep(t1)
    st.info("...")
    time.sleep(t2)

# -------------------------------
if 'age_input' not in st.session_state:
    st.session_state.age_input = ""

# -------------------------------
age = st.text_input("🤨 Nhập tuổi của bạn:", key="age_input").strip()

# -------------------------------
if st.button("Gửi", key="send"):
    if not age:
        st.warning("⚠️ Bạn không nhập gì!")
    elif age.isdigit():
        age = int(age)
        if age <= 1000000:
            loading()
            st.success(f"✅ Tuổi của bạn là: {age}")
        else:
            loading(" 😠 r u fu**ing stupid huh?", 1, 1)
            st.error("😭 Đây là tuổi loz gì thế ?!!")
    else:
        loading()
        st.warning("⚠️ Đây không phải tuổi của bạn, đúng không? ĐÚNG KHÔNG?")

# -------------------------------
# Nút Nhập lại / Thoát
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Nhập lại", key="retry"):
        st.toast("Đang làm mới...", icon="🔁")
        st.session_state.age_input = ""
        time.sleep(0.5)
        st.experimental_rerun()

with col2:
    if st.button("🚪 Thoát", key="exit"):
        st.balloons()  # Thêm animation vui nhộn
        st.write("👋🍀x36 Tạm biệt!")
        st.stop()