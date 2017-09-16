/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Menu;

import Helpers.Conexion;
import static Inicio.Login.setError;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Helpers.Conexion;
import Inicio.Login;
/**
 *
 * @author estre
 */
@WebServlet(name = "Crear", urlPatterns = {"/Crear"})
public class Crear extends HttpServlet {

   
   protected void processRequest(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      response.setContentType("text/html;charset=UTF-8");
      try (PrintWriter out = response.getWriter()) {
         /* TODO output your page here. You may use following sample code. */
         out.println("<!DOCTYPE html>");
         out.println("<html>");
         out.println("<head>");
         out.println("<title>Servlet Crear</title>");         
         out.println("</head>");
         out.println("<body>");
         out.println("<h1>Servlet Crear at " + request.getContextPath() + "</h1>");
         out.println("</body>");
         out.println("</html>");
      }
   }

   String r = "";
   public static String error="";

   public static String getError() {
      return error;
   }

   public static void setError(String error) {
      Login.error = error;
   }
    
   @Override
   protected void doPost(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
        String usuario = request.getParameter("user"); 
        String pass = request.getParameter("pass");    
        RequestBody formBody = new FormEncodingBuilder()
                .add("user",usuario)
                .add("pass", pass)
                .build();
        r = Conexion.getString("validarUsuario", formBody);
        if(r.equalsIgnoreCase("true")){
            HttpSession sesion = request.getSession(true);
            HttpSession sesion2 = request.getSession(true);
            sesion.setAttribute("sesionusuario",usuario);
            sesion2.setAttribute("sesionpass",pass);
            response.sendRedirect("Menu.jsp");
            //processRequest(request, response);
        }else{
            HttpSession sesion2 = request.getSession(true);
            setError("Usuario o Contraseña invalidos");
            response.sendRedirect("Login.jsp");  

        }       
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
