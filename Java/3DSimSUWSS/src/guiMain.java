import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class guiMain {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					guiMain window = new guiMain();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public guiMain() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 502, 328);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel lblFile = new JLabel("File:");
		lblFile.setBounds(15, 16, 69, 20);
		frame.getContentPane().add(lblFile);
		
		JButton chooseXcel = new JButton("Select File");
		chooseXcel.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		chooseXcel.setBounds(298, 12, 115, 29);
		frame.getContentPane().add(chooseXcel);
		
		JLabel lblMinimumAmplitude = new JLabel("Minimum Amplitude:");
		lblMinimumAmplitude.setBounds(15, 81, 169, 20);
		frame.getContentPane().add(lblMinimumAmplitude);
		
		JLabel lblMaximumAmplitude = new JLabel("Maximum Amplitude:");
		lblMaximumAmplitude.setBounds(15, 117, 169, 20);
		frame.getContentPane().add(lblMaximumAmplitude);
		
		JLabel lblTransducer = new JLabel("Transducer 1 :");
		lblTransducer.setBounds(15, 154, 149, 20);
		frame.getContentPane().add(lblTransducer);
		
		JLabel lblTransducer_1 = new JLabel("Transducer 2 :");
		lblTransducer_1.setBounds(15, 194, 149, 20);
		frame.getContentPane().add(lblTransducer_1);
	}
}
