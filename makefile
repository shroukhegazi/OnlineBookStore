upbuild: build up

up:
	docker-compose -f docker-compose.yml up

build:
	docker-compose -f docker-compose.yml build

run:
	docker-compose -f docker-compose.yml run $(filter-out $@,$(MAKECMDGOALS))

restart:
	docker-compose -f docker-compose.yml restart $(filter-out $@,$(MAKECMDGOALS))

shell:
	docker-compose -f docker-compose.yml exec web python manage.py shell

makemigrations:
	docker-compose -f docker-compose.yml run --rm web python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f docker-compose.yml run --rm web python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

createsuperuser:
	docker-compose -f docker-compose.yml run --rm web python manage.py createsuperuser $(filter-out $@,$(MAKECMDGOALS))

logs:
	docker-compose -f docker-compose.yml logs -f $(filter-out $@,$(MAKECMDGOALS))
	
down:
	docker-compose -f docker-compose.yml down $(filter-out $@,$(MAKECMDGOALS))

destroy:
	docker-compose -f docker-compose.yml down -v

test_coverage:
	docker-compose -f docker-compose.yml exec -e DJANGO_SETTINGS_MODULE=OnlineBookStore.settings web coverage run -m pytest books/tests.py reviews/tests.py users/tests.py
	docker-compose -f docker-compose.yml exec -e DJANGO_SETTINGS_MODULE=OnlineBookStore.settings web coverage report
