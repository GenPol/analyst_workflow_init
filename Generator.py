import os

def create_analyst_project():
    structure = {
        "src/utils": ["__init__.py", "time_utils.py", "data_cleaners.py", "excel_formatters.py"],
        "scripts": ["анализ_данных.py"],
        "tests": ["test_time_utils.py"],
        "data/raw": [".gitkeep"],       # Разделил пути для надежности
        "data/processed": [".gitkeep"],
        ".": [".gitignore", "pyproject.toml", "README.md"]
    }

    for path, files in structure.items():
        # Создаем папку (нормализует слэши под Windows сама)
        os.makedirs(path, exist_ok=True)
        
        for file in files:
            full_path = os.path.join(path, file)
            
            if not os.path.exists(full_path):
                # На всякий случай еще раз проверяем наличие папки для файла
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                with open(full_path, 'w', encoding='utf-8') as f:
                    if file == ".gitignore":
                        f.write("__pycache__/\n.venv/\n.env\n*.xlsx\n*.csv\n.ipynb_checkpoints/")
                    elif file == "time_utils.py":
                        f.write("import pandas as pd\n\ndef to_datetime(df, column):\n    return pd.to_datetime(df[column], errors='coerce')")
                    elif file == "__init__.py" and "utils" in path:
                        f.write("from .time_utils import to_datetime\n")
                print(f"✅ Создан: {full_path}")

    print("\n🚀 Теперь всё заработает! Папки 'data/raw' и 'data/processed' на месте.")

if __name__ == "__main__":
    create_analyst_project()
