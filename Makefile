upb:
	docker compose -f docker-compose.local.yml up -d --build

down:
	docker compose -f docker-compose.local.yml down

migrate:
	docker compose -f docker-compose.local.yml exec devices python manage.py migrate

makemigrations:
	docker compose -f docker-compose.local.yml exec devices python manage.py makemigrations

logs:
	docker compose -f docker-compose.local.yml logs