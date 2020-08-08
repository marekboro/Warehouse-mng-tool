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
- expected , actual, seld.assertEqual(expected,actual) 


