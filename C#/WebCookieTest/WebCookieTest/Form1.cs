using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WebCookieTest
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate(new Uri("https://lionel2.kgv.edu.hk/login/index.php"));
            while (webBrowser1.ReadyState != WebBrowserReadyState.Complete)
            {
                Application.DoEvents();
            }

            while (webBrowser1.Url.ToString() != "https://lionel2.kgv.edu.hk/")
            {
                Application.DoEvents();

            }
             MessageBox.Show("Cookies!");

            var x = webBrowser1.Document.Cookie;
            WebBrowser wb = new WebBrowser();
            wb.Document.Cookie = x;
            wb.Navigate(new Uri("https://lionel2.kgv.edu.hk"));
            Console.WriteLine(wb.Document.GetElementsByTagName("div"));



        }
    }

}
