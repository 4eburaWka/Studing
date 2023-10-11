namespace _1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void openToolStripMenuItem2_Click(object sender, EventArgs e)
        {
            try
            {
                this.openFileDialog1.ShowDialog();
                if ((this.openFileDialog1.FileName) == null) return;
                this.richTextBox1.LoadFile(this.openFileDialog1.FileName);
                this.richTextBox1.Modified = false;
            }
            catch (System.IO.FileNotFoundException S)
            {
                MessageBox.Show(S.Message);
            }
        }

        private void saveAsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.saveFileDialog1.FileName = this.openFileDialog1.FileName;
            if (this.saveFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                try
                {
                    this.richTextBox1.SaveFile(this.saveFileDialog1.FileName);
                    this.richTextBox1.Modified = false;
                }
                catch (System.IO.FileNotFoundException S)
                {
                    MessageBox.Show(S.Message);
                }

        }
    }
}