## Stuff to still SINK IN

1. MARKDOWN Tips: 
- use backlash \\ to include underscores \_ in the markdown code format

2. Testing SETUP: 
- have the run_tests.py in the main project folder
- - have it import unitest, the classes/models with the file path
- - and the: 
<code><p> if \_\_name\_\_ == '\_\_main\_\_': <br> unittest.main() </p></code>
- - within each 
- class NameConvention(unittest.TestCase):
- def setUp(self):
- def test_the_name_of_test(seld):
- expected(to fail),expected(to pass), actual, self.assertEqual(expected,actual)

3. Repositories and CRUD:
- import run_sql from the relevant dir and the class from the location
- create CRUD functions initiating them with the sql = "", values = [ This is a list] ,results = sql(sql,values)



