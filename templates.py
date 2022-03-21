class Templates:
    select = """
    SELECT {% if columns %}{{ columns }}{% else %}*{% endif %} 
    FROM {{ table_name }}
    {% if where_condition %} WHERE {{ where_condition }}{% endif %}
    """