class Templates:
    select = """
    SELECT {% if columns %}{{ columns }}{% else %}*{% endif %} 
    FROM {{ table_name }}
    {% if where_condition %} WHERE {{ where_condition }}{% endif %}
    """

    insert_into = """
    INSERT INTO {{ table_name }} ({{ fields }}) VALUES ({{ values }})
    """

    update = """
    UPDATE {{ table_name }}
    SET {{ data }}
    WHERE {{ where_condition }}
    """