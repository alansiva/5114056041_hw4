import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import google.generativeai as genai
import io

# ----------------
# 設定頁面
# ----------------
st.set_page_config(
    page_title="AI 你畫我猜",
    page_icon="🎨",
    layout="wide"
)

# ----------------
# Gemini API 設定
# ----------------
try:
    # 從 Streamlit secrets 讀取 API 金鑰
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

except FileNotFoundError:
    st.error("錯誤：找不到 .streamlit/secrets.toml 檔案。")
    st.info("請在專案根目錄下建立 .streamlit 資料夾，並在其中建立 secrets.toml 檔案，然後填入您的 GOOGLE_API_KEY。")
    st.stop()
except KeyError:
    st.error("錯誤：在 secrets.toml 檔案中找不到 GOOGLE_API_KEY。")
    st.info("請確保您的 secrets.toml 檔案中有 'GOOGLE_API_KEY = \"YOUR_API_KEY\"' 這樣的設定。")
    st.stop()


# 初始化 Gemini 模型
model = genai.GenerativeModel('models/gemini-2.5-flash')

# ----------------
# 主應用程式
# ----------------
st.title("🎨 AI 你畫我猜")
st.header("請在下面的畫布上畫畫，讓 AI 猜猜看是什麼！")

# 繪圖工具和畫布的佈局
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("繪圖工具")
    
    # 繪圖參數
    stroke_width = st.slider("畫筆粗細: ", 1, 25, 3)
    stroke_color = st.color_picker("畫筆顏色: ", "#000000")
    bg_color = st.color_picker("背景顏色: ", "#EEEEEE")
    drawing_mode = st.selectbox(
        "繪圖模式: ",
        ("freedraw", "line", "rect", "circle", "transform", "polygon"),
    )
    
    st.subheader("畫布")
    # 建立畫布元件
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # 填充顏色
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=400,
        width=600,
        drawing_mode=drawing_mode,
        key="canvas",
    )

# 猜測按鈕和結果顯示
with col2:
    st.subheader("AI 猜測")
    
    if st.button("讓 AI 猜猜看！"):
        if canvas_result.image_data is not None:
            # 將畫布內容轉換為圖片
            img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
            
            # 將圖片轉換為 BytesIO 物件
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            with st.spinner("AI 正在努力猜測中..."):
                try:
                    # 準備給模型的圖片
                    image_part = {
                        "mime_type": "image/png",
                        "data": img_byte_arr
                    }
                    
                    # 準備給模型的提示
                    prompt_parts = [
                        image_part,
                        "這是一張使用者畫的圖，請根據圖片內容，用繁體中文猜測這是什麼。請用輕鬆、有趣的語氣回答，就像在玩遊戲一樣。例如：『我猜這是一隻...貓咪！對嗎？』",
                    ]
                    
                    # 呼叫 API
                    response = model.generate_content(prompt_parts)
                    
                    # 顯示結果
                    st.success("AI 說：")
                    st.markdown(f"## {response.text}")

                except Exception as e:
                    st.error(f"API 呼叫失敗: {e}")
        else:
            st.warning("畫布是空的，請先畫點東西！")

st.sidebar.header("操作說明")
st.sidebar.info(
    """
    1.  在左側的畫布上開始繪圖。
    2.  您可以在「繪圖工具」區調整畫筆的粗細、顏色和繪圖模式。
    3.  完成後，點擊「讓 AI 猜猜看！」按鈕。
    4.  在右側的「AI 猜測」區查看結果。
    """
)
