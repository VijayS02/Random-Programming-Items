using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium.PhantomJS;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FacebookPoster
{
    public partial class Form1 : Form
    {
        public string log;
        public List<string> PstText = new List<string>();
        public List<string> AnTxt = new List<string>();
        public int lstmax = 0;
        public int lstCur = 0;
        public Form1()
        {
            InitializeComponent();
            Console.WriteLine(DateTime.Now.ToString("ddMMMyyy"));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (AnTxt.Contains(inptTxtBx.Text) != true)
            {
                AnTxt.Add(textBox1.Text);
                PstText.Add(inptTxtBx.Text);
            }
            string tempString = "v 2.0.1.7 ----------------------------------- Days till next holiday: ~ " + textBox2.Text + " days\n\n";
            foreach (var i in PstText)
            {
                int x = PstText.IndexOf(i) + 1;
                tempString = tempString + "Announcement #" + x + ": " + AnTxt[PstText.IndexOf(i)] + "\n\n" + i + "\n----------------------------------------------------------------------------------------\n";

            }
            tempString = tempString + "Leutnant (Assistenzarzt) \n Lionel Bulletin, coded by: Vijay";
            Console.WriteLine(tempString);
            if (textBox3.Text == "7355608")
            {
                try
                {
                    FirefoxDriverService service = FirefoxDriverService.CreateDefaultService();
                    service.FirefoxBinaryPath = @"C:\Program Files (x86)\Mozilla Firefox\firefox.exe";
                    IWebDriver driver = new FirefoxDriver(service);
                    driver.Url = "https://www.facebook.com";
                    log = log+"Driver opened.\n";
                    progressBar1.Increment(10);
                    Task.Delay(1000).Wait();
                    driver.FindElement(By.XPath("//INPUT[@id='email']")).SendKeys("vikvij@hotmail.com");
                    driver.FindElement(By.XPath("//INPUT[@id='pass']")).SendKeys("vijays");
                    log = log+"Password inputted.\n";
                    progressBar1.Increment(10);
                    driver.FindElement(By.XPath("//LABEL[@id='loginbutton']")).Click();
                    log = log+"Login successful.\n";
                    WaitForLoad(driver, "//DIV[@class='_2t-a _50tj']");
                    //driver.FindElement(By.XPath("//DIV[@class='_55lr'][text()='KGV Unofficial Bulletin']")).Click();
                    driver.Url = "https://www.facebook.com/KGV-Unofficial-Bulletin-124637104764450/";
                    WaitForLoad(driver, "//DIV[@class=' _30z _4h96']");
                    driver.FindElement(By.XPath("//DIV[@class=' _30z _4h96']")).Click();
                    log = log+"Input box found.\n";
                    progressBar1.Increment(20);
                    Task.Delay(2000).Wait();
                    WaitForLoad(driver, "//DIV[@id='composer_text_input_box']");
                    IWebElement y = driver.FindElement(By.XPath("//DIV[@id='composer_text_input_box']"));
                    y.SendKeys(tempString);
                    log = log+"input sent.\n";
                    //SendKeys.SendWait(tempString);
                    progressBar1.Increment(10);
                    Task.Delay(2000).Wait();
                    WaitForLoad(driver, "//BUTTON[text()='Remove']");
                    driver.FindElement(By.XPath("//BUTTON[text()='Remove']")).Click();
                    log = log+"Removed button.\n";
                    Task.Delay(1000).Wait();
                    if (checkBox1.Checked == true)
                    {
                        Task.Delay(2000).Wait();
                        IWebDriver driver1 = new FirefoxDriver();
                        driver1.Url = "http://cn.education.sodexo.com/6.3.1.php";
                        log = log+"Loaded sodexo.\n";
                        driver1.FindElement(By.XPath("//SELECT[@id='f2']")).FindElement(By.CssSelector("option[value='17']")).Click();
                        string xp = "//select[@id='f3']/option[contains(text(),'Month')]".Replace("Month", DateTime.Now.ToString("MMMM"));
                        log = log+"Month selected.\n";
                        driver1.FindElement(By.XPath(xp)).Click();
                        driver1.FindElement(By.XPath("(//A[@href='javascript:;'])[1]")).Click();
                        WaitForLoad(driver1, "(//SPAN[text()='PREVIEW MENU'])");
                        IList<IWebElement> wblmt = driver1.FindElements(By.XPath("//A[@class='btn-s2']"));
                        string x = wblmt[wblmt.Count() - 1].GetAttribute("href");
                        log = log+"Menu found.\n";
                        driver1.Url = x;
                        progressBar1.Increment(10);
                        Task.Delay(1000).Wait();
                        Screenshot image = ((ITakesScreenshot)driver1).GetScreenshot();
                        log = log+"Menu screenshotted.\n";
                        System.IO.Directory.CreateDirectory(@"C:/temp/");
                        image.SaveAsFile(@"C:\temp\ScreenshotC.png", ScreenshotImageFormat.Png);
                        log = log+"Menu saved.\n";
                        progressBar1.Increment(10);
                        driver1.Quit();
                        Task.Delay(1000).Wait();
                        driver.Manage().Window.Maximize();
                        driver.FindElement(By.ClassName("_3jk")).Click();
                        log = log+"Upload element found.\n";
                        Task.Delay(1000).Wait();
                        SendKeys.SendWait(@"C:\temp\ScreenshotC.png");

                        System.Threading.Thread.Sleep(2000);
                        SendKeys.SendWait(@"{Enter}");
                        System.Threading.Thread.Sleep(1000);
                        SendKeys.SendWait(@"{Enter}");
                        log = log+"Upload successful.\n";
                        driver1.Quit();
                    }
                    if (checkBox2.Checked == true)
                    {
                        IWebDriver driver2 = new FirefoxDriver();
                        driver2.Url = "http://www.hko.gov.hk/wxinfo/currwx/fnd.htm#";
                        log = log+"Weather site loaded.\n";
                        IJavaScriptExecutor jse = (IJavaScriptExecutor)driver2;
                        jse.ExecuteScript("window.scrollBy(0,450)", "");
                        log = log + "Scrolled.\n";
                        Task.Delay(1000).Wait();
                        Screenshot image = ((ITakesScreenshot)driver2).GetScreenshot();
                        System.IO.Directory.CreateDirectory(@"C:/temp/");
                        log = log + "Weather screenshotted.\n";
                        image.SaveAsFile(@"C:\temp\ScreenshotW.png", ScreenshotImageFormat.Png);
                        log = log + "Weather saved.\n";
                        progressBar1.Increment(10);
                        driver.FindElement(By.ClassName("_3jk")).Click();
                        log = log + "Upload button clicked.\n";
                        Task.Delay(1000).Wait();
                        progressBar1.Increment(10);
                        SendKeys.SendWait(@"C:\temp\ScreenshotW.png");

                        System.Threading.Thread.Sleep(1000);
                        SendKeys.SendWait(@"{Enter}");
                        System.Threading.Thread.Sleep(1000);
                        SendKeys.SendWait(@"{Enter}");
                        log = log + "Weather uploaded successful.\n";
                        driver2.Quit();
                    }
                    progressBar1.Increment(10);
                   // Actions actions = new Actions(driver);
                    //actions.MoveToElement(driver.FindElement(By.XPath("//EM[text()='Publish']")));
                    //actions.ClickAndHold();
                    //Task.Delay(500).Wait();
                   // actions.Release();
                    //actions.Build().Perform();
                   // log = log + "Publish clicked.\n";
                    //Task.Delay(10000).Wait();
                    //log = log + "Post success.\n";
                    System.IO.File.Move(@"C:\temp\ScreenshotW.png", @"C:\temp\ScreenshotW" + DateTime.Now.ToString("ddMMMyyyy") + ".png");
                    System.IO.File.Move(@"C:\temp\ScreenshotC.png", @"C:\temp\ScreenshotC" + DateTime.Now.ToString("ddMMMyyyy") + ".png");


                }
                catch (Exception ex)
                {
                   throw new ApplicationException("Error: ", ex);
                }
                System.IO.File.WriteAllText(@"C:\temp\Log"+DateTime.Now.ToString("ddMMMyyy")+".txt", log);
            }
        }
        public static void WaitForLoad(IWebDriver driver, string XPATH)
        {
            try
            {
                var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(60));
                wait.Until(ExpectedConditions.VisibilityOfAllElementsLocatedBy(By.XPath(XPATH)));
            }
            catch
            {
                MessageBox.Show("Took to long to respond.");
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            if(lstmax == lstCur)
            {
                PstText.Add(inptTxtBx.Text);
                AnTxt.Add(textBox1.Text);
                inptTxtBx.Text = "";
                textBox1.Text = "";
                lstCur++;
                lstmax++;
            }
            else
            {

                PstText[lstCur] =inptTxtBx.Text;
                AnTxt[lstCur] = textBox1.Text;
                lstCur++;
                inptTxtBx.Text = PstText[lstCur];
                textBox1.Text = AnTxt[lstCur];

            }
            label1.Text = lstCur + " of " + lstmax;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (lstCur > 0)
            {
                if (lstCur == lstmax)
                {
                    PstText.Add(inptTxtBx.Text);
                    AnTxt.Add(textBox1.Text);

                }
                PstText[lstCur] = inptTxtBx.Text;
                AnTxt[lstCur] = textBox1.Text;
                lstCur--;

                inptTxtBx.Text = PstText[lstCur];
                textBox1.Text = AnTxt[lstCur];
            }
            label1.Text = lstCur + " of " + lstmax;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
            {
                e.Handled = true;
            }

            // only allow one decimal point
            if ((e.KeyChar == '.') && ((sender as TextBox).Text.IndexOf('.') > -1))
            {
                e.Handled = true;
            }
        }
    }
}
