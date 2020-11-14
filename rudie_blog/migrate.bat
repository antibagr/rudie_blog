@echo off

:: ========================================
:: Easy way to make migrations on Django project

:: Made for fun by Rudolf Nemov
:: https://github.com/antibagr

echo Starting migration ...

set app_name=articles


for /F "tokens=* USEBACKQ" %%F IN (`python manage.py makemigrations %app_name%`) DO (
	SET migration_status=%%F
)

if /i "%migration_status:~0,2%"=="No" (
	echo No changes detected in "%app_name%"
	goto EOF
) else (
	echo %migration_status%
	python manage.py migrate
)


:EOF
