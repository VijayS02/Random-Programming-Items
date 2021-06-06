using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        public static List<int> t1= new List<int>();
        public static int Comp = 0;
        static void Main(string[] args)
        {
            var watch = System.Diagnostics.Stopwatch.StartNew();

            int x = 4;
            int count = x;
            for (int i = 0; i < x; i++)
            {
                
                
                for(int c = 1; c < x+1; c++)
                {
                    if (c >= count)
                    {
                        Comp++;
                        t1.Add(count);
                    }
                    else
                    {
                        t1.Add(c);
                    }
                }
                count--;
                Console.WriteLine(string.Join(",", t1.ToArray()));
                t1.Clear();
            }
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("Time taken: " + elapsedMs +"ms");
            Console.WriteLine("Comparisons: " + Comp );
            Console.ReadKey();
        }
    }
}
