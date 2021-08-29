import yaml

# example profiles.yml file

json_dict = {
    "jaffle_shop": {
        "target": "dev",
        "outputs": {
            "dev": {
                "type": "postgres",
                "host": "localhost",
                "user": "alice",
                "password": "<password>",
                "port": 5432,
                "dbname": "jaffle_shop",
                "schema": "dbt_alice",
                "threads": 4,
            }
        },
    }
}

y = yaml.dump(json_dict)

print(y)

