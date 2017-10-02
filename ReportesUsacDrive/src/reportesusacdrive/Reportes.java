/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reportesusacdrive;

import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import java.awt.Image;
import java.io.File;
import javax.swing.Icon;

/**
 *
 * @author estre
 */
public class Reportes extends javax.swing.JFrame {
    
   
    
    JLabel grafoPalabrasPNG = new JLabel(" ");
    JLabel grafoJugadoresPNG = new JLabel(" ");
    JLabel grafoLetrasPNG = new JLabel(" ");
    JLabel grafoManoPNG = new JLabel(" ");
    JLabel grafoTableroPNG = new JLabel(" ");
    String path = "C:\\Users\\estre\\Documents\\NetBeansProjects\\ProyectoEDD\\";
    public Reportes() { 
    
      initComponents();   
  
      imagenes();
    
    }
    public static void dibujar(String direccionDot, String direccionPng, int opcion) {
      try {
         File archivo = new File(direccionPng);
         ProcessBuilder pbuilder;

         if (opcion == 1) {
            pbuilder = new ProcessBuilder("dot", "-Tpng", "-o", direccionPng, direccionDot);

         } else {
            pbuilder = new ProcessBuilder("dot", "-Kfdp", "-n", "-Tpng", "-o", direccionPng, direccionDot);
         }

         pbuilder.redirectErrorStream(true);
         //Ejecuta el proceso
         pbuilder.start();
         System.out.println("Grafica  creada con exito");
         //String[] command = {"cmd","/c","start","Visualizador de fotos de Windows",  archivo.getAbsolutePath() };
         //Process process = Runtime.getRuntime().exec(command);

      } catch (Exception e) {
         e.printStackTrace();
      }
   }
    private void imagenes(){
        //Imagenes en el tablero
    
        ImageIcon imageTablero = new ImageIcon(path + "arbolB.png");
      //  ImageIcon iconoT = new ImageIcon(imageTablero.getImage().getScaledInstance(450,600, Image.SCALE_DEFAULT));
        grafoTableroPNG.setIcon(imageTablero);
        grafoTableroPNG.setSize(450,600);               
        grafoTableroPNG.setLocation(0,0);
        grafoTableroPNG.setVisible(true); 
        scrollTablero.setViewportView(grafoTableroPNG); 
        //panelTablero.add(grafoTableroPNG);
        
        ImageIcon imageMano = new ImageIcon(path + "arbolAVL.png");        
        grafoManoPNG.setIcon(imageMano);
        grafoManoPNG.setSize(450,600);
        grafoManoPNG.setLocation(0,0);
        grafoManoPNG.setVisible(true); 
        scrollManoJugador.setViewportView(grafoManoPNG);
        
     
        
        //añade imagen de lista de jugadores        
        ImageIcon imageJugador = new ImageIcon("grafoJugadores.png");
        grafoJugadoresPNG.setIcon(imageJugador);
        grafoJugadoresPNG.setSize(450,600);
        grafoJugadoresPNG.setLocation(0,0);
        grafoJugadoresPNG.setVisible(true); 
        panelJugadores.add(grafoJugadoresPNG); 
         
     
        
        this.repaint();
        
    }
   
    @SuppressWarnings("unchecked")
   // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
   private void initComponents() {

      jTabbedPane1 = new javax.swing.JTabbedPane();
      tabPanels = new javax.swing.JTabbedPane();
      scrollTablero = new javax.swing.JScrollPane();
      scrollManoJugador = new javax.swing.JScrollPane();
      panelJugadores = new javax.swing.JPanel();

      setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

      tabPanels.setAutoscrolls(true);
      tabPanels.addTab("Archivos", scrollTablero);
      tabPanels.addTab("Carpetas", scrollManoJugador);

      javax.swing.GroupLayout panelJugadoresLayout = new javax.swing.GroupLayout(panelJugadores);
      panelJugadores.setLayout(panelJugadoresLayout);
      panelJugadoresLayout.setHorizontalGroup(
         panelJugadoresLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 1292, Short.MAX_VALUE)
      );
      panelJugadoresLayout.setVerticalGroup(
         panelJugadoresLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 652, Short.MAX_VALUE)
      );

      tabPanels.addTab("Bitacora", panelJugadores);

      javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
      getContentPane().setLayout(layout);
      layout.setHorizontalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addComponent(tabPanels, javax.swing.GroupLayout.PREFERRED_SIZE, 1297, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addGap(0, 10, Short.MAX_VALUE))
      );
      layout.setVerticalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addComponent(tabPanels, javax.swing.GroupLayout.PREFERRED_SIZE, 680, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addGap(0, 3, Short.MAX_VALUE))
      );

      pack();
   }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Reportes().setVisible(true);
            }
        });
    }

   // Variables declaration - do not modify//GEN-BEGIN:variables
   private javax.swing.JTabbedPane jTabbedPane1;
   private javax.swing.JPanel panelJugadores;
   private javax.swing.JScrollPane scrollManoJugador;
   private javax.swing.JScrollPane scrollTablero;
   private javax.swing.JTabbedPane tabPanels;
   // End of variables declaration//GEN-END:variables
}
