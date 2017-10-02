/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reportesusacdrive;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import static reportesusacdrive.Reportes.dibujar;

/**
 *
 * @author estre
 */
public class ReportesUsacDrive {

   /**
    * @param args the command line arguments
    */
   public static void main(String[] args) {
      Reportes reportes = new Reportes();
      // a jframe here isn't strictly necessary, but it makes the example a little more real
      JFrame frame = new JFrame("InputDialog Example #1");
      String usuario = JOptionPane.showInputDialog(frame, "What's your name?");

//      //Caja de texto para ingresa nombre de usuario aqui
      String path = "C:\\Users\\estre\\Documents\\NetBeansProjects\\ProyectoEDD\\";
      //reportes.dibujar(path + "arbolB"+usuario+".dot", path + "arbolB"+usuario+".png", 1);
      //reportes.dibujar(path + "arbol"+usuario+".dot", path + "arbolAVL"+usuario+".png", 1);
      reportes.dibujar(path + "arbolB"+usuario+".dot", path + "arbolB"+usuario+".png", 1);
      reportes.dibujar(path + "arbol"+usuario+".dot", path + "arbolAVL"+usuario+".png", 1);
      reportes.setVisible(true);
   }
   
}
