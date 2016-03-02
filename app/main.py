import leveldb
db = leveldb.LevelDB('./db')
db.Put('hello', 'world')
print db.Get('hello')

db.Delete('hello')

for i in xrange(10):
  db.Put(str(i), 'string_%s' % i)

print list(db.RangeIter(key_from = '2', key_to = '5'))
[('2', 'string_2'), ('3', 'string_3'), ('4', 'string_4'), ('5', 'string_5')]
batch = leveldb.WriteBatch()
for i in xrange(1000):
  db.Put(str(i), 'string_%s' % i)

db.Write(batch, sync = True)

db = None
db = leveldb.LevelDB('./db')

for i in xrange(1000):
  print db.Get(str(i))

db.Put('hello', 'world')
print db.Get('hello')
