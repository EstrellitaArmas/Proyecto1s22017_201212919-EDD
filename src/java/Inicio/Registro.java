/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Inicio;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Helpers.Conexion;

/**
 *
 * @author estre
 */
@WebServlet(urlPatterns = {"/registro"})
public class Registro extends HttpServlet {
   public static OkHttpClient webClient = new OkHttpClient();
   String r = "";
   public static String error="";

    public static String getError() {
        return error;
    }

    public static void setError(String error) {
        Registro.error = error;
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
         r = Conexion.postString("insertarUsuario", formBody);
         if(r.equalsIgnoreCase("true")){
            HttpSession sesion = request.getSession(true);
            HttpSession sesion2 = request.getSession(true);
            sesion.setAttribute("sesionusuario", usuario);
            sesion2.setAttribute("sesionpass", pass);
            response.sendRedirect("Menu.jsp");
         }else{
            HttpSession sesion2 = request.getSession(true);
            setError("Usuario ya existe, ingrese un nuevo nombre de usuario");
            response.sendRedirect("Registro.jsp");  
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
