/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Helpers;

/**
 *
 * @author estre
 */
public class CarpetasDTO {
   private long idNombre;

   private String nombreCarpeta;

   //private ArbolAVL raizAVL;
   public String getNombreCarpeta() {
      return nombreCarpeta;
   }

   public void setNombreCarpeta(String nombreCarpeta) {
      this.nombreCarpeta = nombreCarpeta;
   }

   public long getIdNomber() {
      return idNombre;
   }

   public void setIdNombre(long idNombre) {
      this.idNombre = idNombre;
   }
//{
   //"idNombre": 30,
   //"raizAVL": {
   //    "raiz": null,
   //    "byteFile": null
   //},
   //"nombreCarpeta": "Videos",
   //"raizB": null
//}   
}
