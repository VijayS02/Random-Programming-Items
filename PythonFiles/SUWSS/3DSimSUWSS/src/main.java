import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.Iterator;


public class main {

	public static void main(String[] args) {
		double[][] data = excelReader.dataCollection("C:\\Users\\Vijay\\Documents\\Excel\\23Jul2018_1.xlsx");
		double waveHitTime;
		double[] transducers = {139.62,133.13,119.43,67.36,36.48,19.77,14.5};
		double ClosestT = transducers[0];
		//double[] highest = highestPoint(data,29.5,30);
		//double time = highest[2][1] - highest[1][1];
		//for(double[] x : highest) {
			//System.out.println(Arrays.toString(x));
		//}
		//System.out.println((139.62-119.43)/(highest[2]-highest[1]));
		System.out.println(data(data,29.5,31.0,1000));
		
		

	}
	//36.899 - st
	//38.324 - stp
	public static double data(double[][] values, double ampStrt, double ampEnd, double freq) {
		/**
		int start = 0;
		
		double[] tmpdata = highestPoint(values,ampStrt,0);
		int zer = indx(tmpdata[0]);
		int max = indx(highestPoint(values,ampEnd,0)[tmpdata.length-1]);
		int frq = (int) freq;
		double[][] data = new double[(max-zer)*frq][tmpdata.length];
		int curMin = zer;
		double sum = 0;
		int cnt = 0;
		for(int i = zer;i<max;i+= (1/frq)) {
			double[] tmp = highestPoint(values,,curMin);
			sum+=(139.62-119.43)/(tmp[2]-tmp[1]);
			cnt++;
		}
		sum = sum/cnt;
		System.out.println(sum);
		return null;
		**/
		double sum = 0;
		double[] tmpdata = highestPoint(values,ampStrt,0);
		int zer = indx(tmpdata[0]);
		int cnt = 0;
		for(double i =ampStrt;i<ampEnd;i=i+(1/freq)){
			double[] tmp = highestPoint(values,i,zer);
			sum+=(139.62-119.43)/(tmp[2]-tmp[1]);
			cnt++;
		}
		sum = sum/cnt;
		return sum;
				
	}
	
	public static int indx(double tmval) {
		return (int) (tmval*1000 + 1);
	}
	
	public static double[] highestPoint(double[][] values,double amp,int start){
		double[] maxValues = new double[values[0].length+1];
		for(int i = 0; i < maxValues.length;i++) {
			//maxValues[i][0] = Double.MIN_VALUE;
			maxValues[i] = 0;
		}
		double lowestT = Double.MAX_VALUE;
		double highestT = Double.MIN_VALUE;
		for(int i = 0 ; i < values[0].length;i++) {
			for(int z = start; z<values.length;z++) {
				double[] row = values[z];
				if(row[i] >= amp && i != 0 && i !=  values[0].length ) {
					if(row[0] <= lowestT) {
						lowestT = row[0];
					}
					if(row[0] >= highestT) {
						highestT = row[0];
					}
					//maxValues[i][0] = amp;
					maxValues[i] = row[0];
					break;
				}
			}
		}
		maxValues[0] = lowestT;
		maxValues[values[0].length] = highestT;
		//System.out.println(Arrays.toString(maxValues));
		return maxValues;
		
		
	}
	
	
	 
}
