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
import Helpers.Graficador;

/**
 *
 * @author estre
 */
@WebServlet(urlPatterns = {"/login"})
public class Login extends HttpServlet {
   public static OkHttpClient webClient = new OkHttpClient();
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
        r = Conexion.postString("validarUsuario", formBody);
        if(r.equalsIgnoreCase("true")){
            String jsonArbol = Conexion.postString("obtenerRaices", formBody);
            HttpSession sesion = request.getSession(true);
            HttpSession sesion2 = request.getSession(true);
            sesion.setAttribute("sesionusuario",usuario);
            sesion2.setAttribute("sesionpass",pass);
            //Parsear json y enviar array de carpetas;
            System.out.println(jsonArbol);
            request.getSession().setAttribute("variable", new Integer(22));
            //
            ///
            ///
            ///
            ///
            ///
            // 
            //Generar graficas de las estructuras existentes
           // String grafos = Conexion.getString("graficarArboles", formBody);
            
            //Redireccionar a la pagina menu 
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
