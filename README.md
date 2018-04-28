# django-formset-example
example for django modelformset_factory

1. скачать содержимое репозтария django-formset-example
2. перейти в папку со скаченным проектом
3. запустить python manage.py runserver
4. для доступа к странице с формой перейти по адресу http://localhost:8000/zone/Zone01

текущие ограничения:
- редактирование ресурсов зоны, указанной в ссылке, например Zone01
- форма поддерживает добавление новых позиций ресурсов зоны без перезагрузки формы (jquery.formset.js, jquery.min.js)
- удаление ресурсов зоны не реализовано
- добавление/редактирование Zone не реализовано
