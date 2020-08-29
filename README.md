# Аттестационный проект курса "Автоматизированное тестирование ПО на Python"
Студент: Владислав Любомский

[![Build Status](https://travis-ci.org/v-lubomski/inno_final_project.svg?branch=master)](https://travis-ci.org/v-lubomski/inno_final_project)


## Объект тестирования
Демо-версия сайта Банка Санкт-Петиербурга, располагающаяся по адресу https://idemo.bspb.ru/


## Цели
- Покрытие тестами самых важных элементов системы с учётом отведённого на проект времени
- Демонстрация усвоенных на курсе знаний


## Выбранные сценарии тестирования
<h3>Раздел 1: Карты</h3>
<ul>
<li>Заказать новую карту</li>
<li>Добавить карту другого банка</li>
<li>Создать виртуальную карту</li>
<li>Заблокировать карту</li>
</ul>

<h3>Раздел 2: Счета</h3>
<ul>
<li>Открытие счёта</li>
<li>Закрытие счёта</li>
<li>Просмотр реквизитов счёта</li>
<li>Просмотр выписки</li>
</ul>

<h3>Раздел 3: Вклады</h3>
<ul>
<li>Открытие вклада</li>
<li>Показать закрытые вклады</li>
<li>Посмотреть детали вклада</li>
<li>Переименовать вклад</li>
</ul>


## Используемые технологии
- Python
- Selenium Webdriver
- Pytest
- Travis CI
- Allure Report


## Roadmap
<ul>
<li>CI (Travis) + pre-commit (linter locally and remote)</li>
<li>Docstring's test-cases (steps + result)</li>
<li>Tests (3 sections * 4 tests for one)</li>
<li>Reports (Allure)</li>
<li>Fill README.md (installation, running test, purpose of testing)</li>
</ul>


## Разворачивание проекта
