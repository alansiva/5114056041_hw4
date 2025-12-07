import google.generativeai as genai
import os

try:
    # 這裡我們從環境變數讀取 API 金鑰
    api_key = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=api_key)

    print("成功設定 API 金鑰。正在查詢可用的模型...")
    print("="*30)

    # 迴圈遍歷並列出所有模型
    for m in genai.list_models():
        # 我們對支援 'generateContent' 方法的模型特別感興趣
        if 'generateContent' in m.supported_generation_methods:
            print(f"模型名稱: {m.name}")
            print(f"  支援的方法: {m.supported_generation_methods}")
            print("-" * 20)

except KeyError:
    print("錯誤：找不到環境變數 'GOOGLE_API_KEY'。")
    print("請依照指示在終端機中設定它。")
except Exception as e:
    print(f"發生預期外的錯誤: {e}")
