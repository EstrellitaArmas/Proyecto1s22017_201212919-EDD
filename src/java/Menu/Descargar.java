/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Menu;

import Helpers.Conexion;
import Helpers.FileJsonDTO;
import Helpers.ParserJson;
import static Inicio.Login.setError;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author estre
 */
@WebServlet(urlPatterns = {"/descargar"})
public class Descargar extends HttpServlet {

   /**
    * Processes requests for both HTTP <code>GET</code> and
    * <code>POST</code> methods.
    *
    * @param request servlet request
    * @param response servlet response
    * @throws ServletException if a servlet-specific error occurs
    * @throws IOException if an I/O error occurs
    */
   protected void processRequest(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      response.setContentType("text/html;charset=UTF-8");
      try (PrintWriter out = response.getWriter()) {
         /* TODO output your page here. You may use following sample code. */
         out.println("<!DOCTYPE html>");
         out.println("<html>");
         out.println("<head>");
         out.println("<title>Servlet Descargar</title>");         
         out.println("</head>");
         out.println("<body>");
         out.println("<h1>Servlet Descargar at " + request.getContextPath() + "</h1>");
         out.println("</body>");
         out.println("</html>");
      }
   }

   // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
   /**
    * Handles the HTTP <code>GET</code> method.
    *
    * @param request servlet request
    * @param response servlet response
    * @throws ServletException if a servlet-specific error occurs
    * @throws IOException if an I/O error occurs
    */
   @Override
   protected void doGet(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      processRequest(request, response);
   }

   /**
    * Handles the HTTP <code>POST</code> method.
    *
    * @param request servlet request
    * @param response servlet response
    * @throws ServletException if a servlet-specific error occurs
    * @throws IOException if an I/O error occurs
    */
   @Override
   protected void doPost(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
        String nombreArchivo = request.getParameter("descargaFile");
        HttpSession sesion = request.getSession(true);
        String user = sesion.getAttribute("sesionusuario").toString();
               
        RequestBody formBody = new FormEncodingBuilder()
                .add("user",user)
                .add("nombreArchivo", nombreArchivo)
                .build();
        String res = Conexion.postString("recuperarArchivo", formBody);
        System.out.print(res);
        try{
            // Parsea el string Json en un objeto con los atributos fileName y fileBytes
            FileJsonDTO fileObject = ParserJson.parseStrToObject(res, FileJsonDTO.class);
            //Con este código se agregan los bytes al archivo.
            FileOutputStream fileOuputStream = new FileOutputStream("C:\\Users\\estre\\Desktop\\Copia"+nombreArchivo);
            fileOuputStream.write(fileObject.getFileBytes());
            fileOuputStream.close();
        }catch(NumberFormatException | IOException e){
              System.out.println("ERROR en Descarga: "+ e);
        }
        
        response.sendRedirect("Menu.jsp");
   }

   /**
    * Returns a short description of the servlet.
    *
    * @return a String containing servlet description
    */
   @Override
   public String getServletInfo() {
      return "Short description";
   }// </editor-fold>

}
