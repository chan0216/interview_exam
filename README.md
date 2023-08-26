## 設置需求

- Python >=3.8
- pip (Python 套件管理器)

## 運行步驟

1. Clone 此專案至本地端
   ```bash
   git clone https://github.com/chan0216/interview_exam.git
   ```
2. 進入此專案資料夾

   ```bash
   cd interview_exam
   ```

3. 創建虛擬環境

   ```bash
   python -m venv venv
   ```

4. 啟動虛擬環境

- Windows

  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

5. 安裝必需的套件

   ```bash
   pip install -r requirements.txt
   ```

6. 開啟伺服器

   ```python
   python app.py
   ```

## 使用方法

此伺服器運行在 `http://localhost:3000`，可以透過 `/exchange` 進行貨幣兌換，例如:

```
GET /exchange?source=USD&target=JPY&amount=$1,525
```

## 測試

使用 pytest 對 API 進行單元測試：

```python
python -m pytest
```
