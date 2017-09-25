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
public class FileJsonDTO {
   private String fileName;
   
   private byte[] fileBytes;
   
   public byte[] getFileBytes(){
      return fileBytes;
   }
   public void setFileBytes(byte[] fileBytes){
      this.fileBytes = fileBytes;             
   }
   
   public String getFileName(){
      return fileName;
   }
   public void setFileName(String fileName){
      this.fileName = fileName;
   }
   
}
