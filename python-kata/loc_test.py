from loc import loc
from nose_parameterized import parameterized
import unittest

class FromRomanTestCase(unittest.TestCase):
    @parameterized.expand([
        (13, 
"""// A Hello World! program in C#.
using System;
namespace HelloWorld
{
    class Hello 
    {
        static void Main() 
        {
            Console.WriteLine("Hello World!");

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
    }
}"""),
        (13, 
"""// A Hello World! program in C#.
using System;
namespace HelloWorld
{
    class Hello 
    {
        /* Multiline comment
        */
        static void Main() 
        {
            /* Single line comment */
            Console.WriteLine("Hello World!");

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
    }
}"""),
    ])
    def test_sequence(self, expected_loc, code):
        self.assertEqual(loc(code), expected_loc)