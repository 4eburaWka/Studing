using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _20
{
    public partial class Form1 : Form
    {
        private Form3 form3 = new Form3();
        public Form1()
        {
            InitializeComponent();
            form2 = new Form2();
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                form2.ShowDialog();
            } else
            {
                form3.ShowDialog();
            }
        }
    }
}
