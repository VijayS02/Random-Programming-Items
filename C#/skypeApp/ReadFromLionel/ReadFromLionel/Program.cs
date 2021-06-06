using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Remote;
using OpenQA.Selenium.Support.UI;
using SimpleBrowser.WebDriver;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Specialized;

namespace ReadFromLionel
{
    class Program
    {

        static void Main(string[] args)
        {

            IWebDriver driver = new FirefoxDriver();
            driver.Navigate().GoToUrl("https://play.typeracer.com?");
                                            /**
                                        WaitForLoad(driver, "//EMBED[@src='sprinter.swf']");
                                        System.Threading.Thread.Sleep(12000);
                                        driver.FindElement(By.XPath("//EMBED[@src='sprinter.swf']")).Click();
                                        while (true) {
                                            
                                            driver.FindElement(By.XPath("//EMBED[@src='sprinter.swf']")).SendKeys(Keys.ArrowLeft);
                                            driver.FindElement(By.XPath("//EMBED[@src='sprinter.swf']")).SendKeys(Keys.ArrowRight);
                                            System.Threading.Thread.Sleep(0);
                                        }

                                        **/
            WaitForLoad(driver, "//SPAN[@unselectable='on']");
            string x = "";
            var element = driver.FindElements(By.XPath("//SPAN[@unselectable='on']"));
            string temps = "";
            temps = driver.FindElement(By.XPath("//SPAN[@unselectable='on'][1]")).GetAttribute("innerHTML");
            temps = temps + driver.FindElement(By.XPath("//SPAN[@unselectable='on'][2]")).GetAttribute("innerHTML");
            Console.WriteLine(x);
            foreach (var i in element)
            {
                x = i.GetAttribute("innerHTML");
                x = x + i.GetAttribute("innerHTML");
            }
            Console.WriteLine(x);
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(70));
            wait.Until(ExpectedConditions.ElementToBeClickable(By.XPath("(//INPUT[@type='text'])[1]"))).Click();
            driver.FindElement(By.XPath("(//INPUT[@type='text'])[1]")).SendKeys(temps+" ");
            string[] xy = x.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
            foreach(var i in xy)
            {
                Console.WriteLine(string.Join(",", xy));
                driver.FindElement(By.XPath("(//INPUT[@type='text'])[1]")).SendKeys(i+" ");
                System.Threading.Thread.Sleep(200);
            }
    
            Console.WriteLine(x);

            Console.ReadKey();

        }
        public static void WaitForLoad(IWebDriver driver, string XPATH)
        {
            try
            {
                var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(120));
                wait.Until(ExpectedConditions.VisibilityOfAllElementsLocatedBy(By.XPath(XPATH)));
            }
            catch
            {
                Console.WriteLine("Took to long to respond.");
            }
        }

    }
}
