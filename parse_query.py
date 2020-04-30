def parse_query(query: str) -> str:
    res = "SELECT * FROM Customers"
    arg_value = query.split(';')
    c = 0
    for param in arg_value:
        if ':' in param:
            p = param.split(':')
            if c == 0:
                res += f" WHERE {p[0].capitalize()} = '{p[1]}'"
            else:
                res += f" AND {p[0].capitalize()} = '{p[1]}'"
        c += 1
    return res+";"


print(parse_query('country=USA;city=Boston'))


if __name__ == '__main__':
    assert parse_query('country:USA;') == "SELECT * FROM Customers WHERE Country = 'USA';"
    assert parse_query('') == "SELECT * FROM Customers;"
    assert parse_query('f') == "SELECT * FROM Customers;"
    assert parse_query('country=USA') == "SELECT * FROM Customers;"
    assert parse_query('country:USA;city:Boston') == "SELECT * FROM Customers WHERE Country = 'USA' AND City = 'Boston';"
    assert parse_query('country=USA;city=Boston') == 'SELECT * FROM Customers;'
    

