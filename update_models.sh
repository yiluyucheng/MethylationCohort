
rm db.sqlite3
rm -rf cohort/migrations/*

python manage.py makemigrations
python manage.py migrate --run-syncd

python txt2db.py data/cohort_info.xls
python txt2db_gsm.py data/blood_age_sample.xls
