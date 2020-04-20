def parse(query: str) -> dict:
  res = {}
  if '?' in query:
    query = query.split("?")[1]
  for i in query.split('&'):
      if '=' in i:
        p = i.split('=')
        res[p[0]] = p[1]
  return res

if __name__ == '__main__':
  assert parse('https://example.com/path/to/page?arg1=val1&arg2=val2') == {'arg1': 'val1', 'arg2': 'val2'}
  assert parse('https://example.com/path/to/page? arg1 = val1 &arg2=val2&') == {' arg1 ': ' val1 ' , 'arg2': 'val2'}
  assert parse('https://example.com/path/to/page?arg1=val1=val&arg2=val2') == {'arg1': 'val1', 'arg2': 'val2'}
  assert parse('https://example.com/path/to/page?arg1=&arg2=val2') == {'arg1': '', 'arg2': 'val2'}
  assert parse('http://example.com/?aaa=aaa') == {'aaa': 'aaa'}
  assert parse('') == {}
  assert parse('@@?aaa=aaa') == {'aaa':'aaa'}
  assert parse('aaa=aaa') == {'aaa':'aaa'}
  assert parse('=') == {'':''}
  assert parse('http://example.com/?') == {}

#I think, it`s done