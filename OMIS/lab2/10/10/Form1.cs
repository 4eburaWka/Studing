using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _10
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            MessageBox.Show("X:" + e.X + "Y:" + e.Y);
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 'e')
                Application.Exit();
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            this.A++;
            this.Refresh();
        }

        private void Form1_Deactivate(object sender, EventArgs e)
        {
            this.DA++;
            this.Refresh();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            ReDrawNumber++;
            Font font = new Font("AriaL", 10);
            SolidBrush myBrush = new SolidBrush(Color.Black);
            e.Graphics.DrawString("A=" + this.A.ToString() + "\nDA=" + this.DA.ToString() + "\nReDrawNumber=" + this.ReDrawNumber.ToString(), font, myBrush, 0, 0);
        }
    }
}
