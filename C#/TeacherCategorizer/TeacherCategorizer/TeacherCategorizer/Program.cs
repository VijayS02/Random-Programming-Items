using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TeacherCategorizer
{
    class Program
    {
        static void Main(string[] args)
        {

           var profileManager = new FirefoxProfileManager();
           FirefoxProfile profile = profileManager.GetProfile("default");
            IWebDriver driver = new FirefoxDriver(profile);
            String url = "https://lionel2.kgv.edu.hk/local/mis/students/summary.php?sid=0";
            driver.Navigate().GoToUrl(url);
            Thread.Sleep(5000);
            ArrayList teachers = new ArrayList();
            for (int i = 4999; i < 6000; i++)
            {
             
                url = "https://lionel2.kgv.edu.hk/local/mis/students/summary.php?sid=" + i;
                driver.Navigate().GoToUrl(url);
                var test = "";
                try
                {
                  
                        test = driver.FindElement(By.XPath("//SPAN[@id='box2']")).GetAttribute("innerHTML");
                        int index1 = test.IndexOf("</h4>");
                        int index2 = test.IndexOf("<br>") - 5;
                        int length = index2 - index1;
                        Console.WriteLine(test.Substring(index1 + 5, length));
                        String fnal =  test.Substring(index1 + 5, length) + "," + i.ToString() ;
                        teachers.Add(fnal);
                        using (System.IO.StreamWriter file =
           new System.IO.StreamWriter(@"D:\C#\TeacherCategorizer\teachers.txt", true))
                        {
                            file.WriteLine(fnal);
                        }
                    
                }
                catch (Exception e)
                {
                    Console.WriteLine("Page number " + i + " is invalid.");
                }
            }
            Console.WriteLine("--------END END END END END-----");
                foreach(String[] x in teachers)
                {
                    Console.WriteLine(string.Join(" ", x));
                }
                //var test = "<h4 id=>Email</h4>Mr Sean Miller<br>sean.miller@kgv.edu.hk<a style=class=";
                /**temps = driver.FindElement(By.XPath("//SPAN[@unselectable='on'][1]")).GetAttribute("innerHTML");
                temps = temps + driver.FindElement(By.XPath("//SPAN[@unselectable='on'][2]")).GetAttribute("innerHTML");**/
            
    }
    }
}
