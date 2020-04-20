def parse(query: str) -> dict:
  res = {}
  for i in query.split(";"):
      if '=' in i:
          p=i.split('=',1)
          res[p[0]]=p[1]
  return res

if __name__ == '__main__':
  assert parse('name=Zhenya;age=20;')=={'name':'Zhenya', 'age':'20'}
  assert parse('')=={}
  assert parse(';=') == {'':''}
  assert parse('name=sasha') == {'name':'sasha'}
  assert parse ('ghegjrelgj;1=;=3') == {'1': '', '':'3'}
  assert parse('ghegjrelgj;1=;=3;') == {'1': '', '': '3'}
  assert parse('ghegjrelgj;1=;=3;=4') == {'1': '', '': '4'}
  assert parse('ghegjrelgj;1=;=3;=4 1=0') == {'1': '', '': '4 1=0'}
  assert parse('ghegjrelgj;1=;=3;=4;1=0') == {'1': '0', '': '4'}
  assert parse('ghegjrelgj;1=;=3;=4; 1=0') == {'1': '', '': '4',' 1':'0'}
  #ready