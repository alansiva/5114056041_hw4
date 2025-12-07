# AI 你畫我猜 - 操作手冊

這是一個使用 Streamlit 和 Google Gemini 模型打造的互動式網頁遊戲。使用者可以在畫布上繪圖，讓 AI 來猜測畫作的內容。

## 系統需求
- Python 3.10 或更高版本
- macOS / Linux (Windows 可能需要稍微調整指令)
- `pip` (Python 套件安裝程式)

---

## 安裝與啟動步驟

請依照以下步驟在您的本機環境中設定並啟動此專案。

### 步驟一：設定 Google API 金鑰

為了讓應用程式能順利呼叫 Google Gemini API，您需要設定您的 API 金鑰。我們有兩種推薦的方式：

#### 方法 A：使用 `secrets.toml` (Streamlit 推薦方式)

這是我們目前應用程式 (`app.py`) 採用的方式，最為推薦。

1.  在專案根目錄下，找到或建立 `.streamlit` 資料夾。
2.  在 `.streamlit` 資料夾中，建立一個名為 `secrets.toml` 的檔案。
3.  在 `secrets.toml` 檔案中，填入以下內容，並將金鑰替換成您自己的：
    ```toml
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
    ```
    Streamlit 應用程式在啟動時會自動讀取此檔案，安全又方便。

#### 方法 B：使用 `export` 環境變數 (終端機臨時設定)

這種方式適用於執行單次腳本 (例如我們先前的 `check_models.py`) 或您不想建立檔案時。

1.  打開您的終端機 (Terminal)。
2.  執行以下指令，將 `YOUR_API_KEY_HERE` 替換成您自己的金鑰：
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
3.  **重要提示**：
    *   `export` 指令設定的環境變數**只在當前的終端機視窗有效**。一旦關閉該視窗，設定就會消失。
    *   這種方式不會在任何地方留下您的金鑰紀錄，非常安全，適合臨時測試。
    *   如果您要用此方法執行 Streamlit 應用，則必須在同一個視窗中接著執行 `streamlit run app.py`。

### 步驟二：建立並啟動虛擬環境

為了避免與您系統中其他的 Python 套件產生衝突，強烈建議使用虛擬環境。

1.  打開終端機，`cd` 進入專案的根目錄。
2.  執行以下指令，建立一個名為 `venv` 的虛擬環境：
    ```bash
    python3 -m venv venv
    ```
3.  啟動這個虛擬環境：
    ```bash
    source venv/bin/activate
    ```
    成功後，您會看到終端機提示符號前面出現 `(venv)` 字樣。

### 步驟三：安裝依賴套件 (requirements.txt)

`requirements.txt` 檔案中記錄了這個專案需要的所有 Python 函式庫。

1.  確保您已經處於 `(venv)` 虛擬環境中。
2.  執行以下指令來安裝所有必要的函式庫：
    ```bash
    pip install -r requirements.txt
    ```

### 步驟四：啟動應用程式

完成以上所有設定後，您就可以啟動遊戲了！

1.  確保您已經處於 `(venv)` 虛擬環境中。
2.  (如果您選擇使用 `export` 方式設定金鑰) 確保您在設定金鑰的同一個終端機視窗中。
3.  執行以下指令：
    ```bash
    streamlit run app.py
    ```
4.  您的瀏覽器將會自動開啟一個新分頁，載入遊戲介面。現在您可以開始遊玩了！
