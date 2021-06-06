using OpenQA.Selenium;
using OpenQA.Selenium.PhantomJS;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            progressBar1.Hide();
            label3.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            progressBar1.Show();
            label3.Text = "Progress: ";
            var driverService = PhantomJSDriverService.CreateDefaultService(Environment.CurrentDirectory);
            driverService.HideCommandPromptWindow = true;
            progressBar1.Increment(20);
            IWebDriver driver = new PhantomJSDriver(driverService);
            driver.Url = "https://lionel2.kgv.edu.hk/login/index.php";

            progressBar1.Increment(20);
            try
            {
                driver.FindElement(By.Id("username")).SendKeys(textBox1.Text);
                driver.FindElement(By.Id("password")).SendKeys(textBox2.Text + OpenQA.Selenium.Keys.Enter);
            }
            catch (Exception)
            {
                MessageBox.Show("No connection.");
            }
            try
            {
                var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
                wait.Until(ExpectedConditions.VisibilityOfAllElementsLocatedBy(By.XPath("(//DIV[@class=' span9'])")));
            }
            catch
            {
                MessageBox.Show("Took to long to respond.");
            }
            progressBar1.Increment(20);
            IList<IWebElement> clkMr = driver.FindElements(By.XPath("//div[text()[contains(.,'[more]')]]"));

            foreach (var i in clkMr)
            {
                i.Click();
            }

            IList<IWebElement> hw = driver.FindElements(By.XPath("(//DIV[@class=' span9'])"));
            IList<IWebElement> dd = driver.FindElements(By.XPath("//div[text()[contains(.,'due on')]]|//div[text()[contains(.,'overdue')]]"));
            progressBar1.Increment(20);
            NamLbl.Text = "Hello " + driver.FindElement(By.XPath("//A[@alt='summary']")).Text + ".";
            Label[] lbls = { hwlbl1, hwlbl2, hwlbl3, hwlbl4, hwlbl5, hwlbl6 };
            Label[] lbls2 = { hwlbl7 ,hwlbl8,hwlbl9};
            foreach(var i in hw)
            {
                int c = hw.IndexOf(i);
                if (c <= 5)
                {
                    lbls[c].MaximumSize = new System.Drawing.Size(250, 6000);
                    lbls[c].Text = i.Text + "\n" + dd[hw.IndexOf(i)].Text;
                }
                if (c > 5)
                {
                        lbls2[c-6].MaximumSize = new System.Drawing.Size(250, 6000);
                        lbls2[c -6].Text = i.Text + "\n" + dd[hw.IndexOf(i)];
                }
            }
            progressBar1.Increment(20);
            driver.Close();
            progressBar1.Hide();
            label3.Hide();
            driver.Quit();
            driver.Dispose();

        }

    }
}
