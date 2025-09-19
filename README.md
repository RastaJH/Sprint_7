# Sprint 7

## Описание
Автотесты для учебного API сервиса Яндекс Самокат.  

## Запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите тесты:
   ```bash
   pytest -v --alluredir=allure_results
   ```
3. Сгенерируйте отчёт Allure:
   ```bash
   allure serve allure_results
   ```
