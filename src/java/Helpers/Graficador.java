/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Helpers;

import java.io.File;

/**
 *
 * @author estre
 */
public class Graficador {
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
         System.out.println("\nGrafica  creada con exito");
         //String[] command = {"cmd","/c","start","Visualizador de fotos de Windows",  archivo.getAbsolutePath() };
         //Process process = Runtime.getRuntime().exec(command);

      } catch (Exception e) {
         e.printStackTrace();
      }
   }
}
