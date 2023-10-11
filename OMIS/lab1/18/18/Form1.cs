using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _18
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            rFormForDialog = new Form2();
            rFormForDialog2 = new Form3();
            this.Paint += Form1_Paint;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Click(object sender, EventArgs e)
        {
            this.rFormForDialog.ShowDialog();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.rFormForDialog.ShowDialog();
        }

        private void button2_CLick(object sender, EventArgs e)
        {
            if (this.rFormForDialog2.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                MessageBox.Show("Back with OK");
                this.Refresh();

            }
        }
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Font myFont3 = new Font("Arial", 30);
            System.Drawing.Color myColor1 = (System.Drawing.Color.Black);
            System.Drawing.SolidBrush myBrush1 = new SolidBrush(myColor1);

            e.Graphics.DrawString(this.rFormForDialog2.X, myFont3, myBrush1, 135, 135);
        }

    }
}
