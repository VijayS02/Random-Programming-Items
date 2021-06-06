import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class excelReader {

	

    public static double[][] dataCollection(String location) {
    	final String FILE_NAME = location;

        try {

            FileInputStream excelFile = new FileInputStream(new File(FILE_NAME));
            @SuppressWarnings("resource")
			Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet datatypeSheet = workbook.getSheetAt(0);
            Iterator<Row> iterator1 = datatypeSheet.iterator();
            int width = datatypeSheet.getRow(0).getLastCellNum();
            int count = 0;
            
            while (iterator1.hasNext()) {
            	 iterator1.next();
                 count+=1;

            }
            System.out.println(count + " Rows. " + width + " columns.");
            double[][] data = new double[count][width];
            Iterator<Row> iterator = datatypeSheet.iterator();
            int row = 0;
            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                Iterator<Cell> cellIterator = currentRow.iterator();
                int pos = 0;
                while (cellIterator.hasNext()) {

                    Cell currentCell = cellIterator.next();
                    //getCellTypeEnum shown as deprecated for version 3.15
                    //getCellTypeEnum ill be renamed to getCellType starting from version 4.0
                    if (currentCell.getCellTypeEnum() == CellType.STRING) {
                        //System.out.print(currentCell.getStringCellValue() + "s");
                    	
                    } else if (currentCell.getCellTypeEnum() == CellType.NUMERIC) {
                        //System.out.print(currentCell.getNumericCellValue() + " ");
                    	data[row][pos] = currentCell.getNumericCellValue();
                    }
                    pos +=1;

                }
                row+=1;
                
                //System.out.println();
                
               
            }	
            return data;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;

    }

}